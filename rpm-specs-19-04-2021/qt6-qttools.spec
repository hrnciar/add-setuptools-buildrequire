%global qt_module qttools

Summary: Qt6 - QtTool components
Name:    qt6-qttools
Version: 6.0.3
Release: 1%{?dist}

License: LGPLv3 or LGPLv2
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

# help lrelease/lupdate use/prefer qmake-qt6
# https://bugzilla.redhat.com/show_bug.cgi?id=1009893
Patch1: qttools-run-qttools-with-qt6-suffix.patch

# 32-bit MIPS needs explicit -latomic
Patch2: qttools-add-libatomic.patch

## upstream patches

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/file
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtbase-static >= %{version}
BuildRequires: qt6-qtdeclarative-static >= %{version}
BuildRequires: qt6-qtdeclarative >= %{version}
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: clang-devel llvm-devel


Requires: %{name}-common = %{version}-%{release}

%description
%{summary}.

%package common
Summary: Common files for %{name}
BuildArch: noarch

%description common
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-designercomponents%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-help%{?_isa} = %{version}-%{release}
Requires: qt6-doctools = %{version}-%{release}
Requires: qt6-designer = %{version}-%{release}
Requires: qt6-linguist = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.

%package libs-designer
Summary: Qt6 Designer runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-designer
%{summary}.

%package libs-designercomponents
Summary: Qt6 Designer Components runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-designercomponents
%{summary}.

%package libs-help
Summary: Qt6 Help runtime library
Requires: %{name}-common = %{version}-%{release}
%description libs-help
%{summary}.

%package -n qt6-assistant
Summary: Documentation browser for Qt6
Requires: %{name}-common = %{version}-%{release}
%description -n qt6-assistant
%{summary}.

%package -n qt6-designer
Summary: Design GUIs for Qt6 applications
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
Requires: %{name}-libs-designercomponents%{?_isa} = %{version}-%{release}
%description -n qt6-designer
%{summary}.

%if 0%{?webkit}
%package -n qt6-designer-plugin-webkit
Summary: Qt6 designer plugin for WebKit
BuildRequires: pkgconfig(Qt6WebKitWidgets)
Requires: %{name}-libs-designer%{?_isa} = %{version}-%{release}
%description -n qt6-designer-plugin-webkit
%{summary}.
%endif

%package -n qt6-linguist
Summary: Qt6 Linguist Tools
Requires: %{name}-common = %{version}-%{release}
%description -n qt6-linguist
Tools to add translations to Qt6 applications.

%package -n qt6-qdbusviewer
Summary: D-Bus debugger and viewer
Requires: %{name}-common = %{version}-%{release}
%{?_qt6:Requires: %{_qt6}%{?_isa} >= %{_qt6_version}}
%description -n qt6-qdbusviewer
QDbusviewer can be used to inspect D-Bus objects of running programs
and invoke methods on those objects.

%package -n qt6-doctools
Summary: Qt6 doc tools package
%description -n qt6-doctools
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}-common = %{version}-%{release}
%description examples
%{summary}.


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}

%patch1 -p1 -b .run-qttools-with-qt6-suffix
%ifarch %{mips32}
%patch2 -p1 -b .libatomic
%endif


%build
%cmake_qt6

%cmake_build


%install
%cmake_install

# Add desktop files, --vendor=... helps avoid possible conflicts with qt3/qt4
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --vendor="qt6" \
  %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}

# icons
install -m644 -p -D src/assistant/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant-qt6.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant-qt6.png
install -m644 -p -D src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer-qt6.png
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/linguist-qt6.png
done

# hardlink files to {_bindir}, add -qt6 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
   assistant|designer|lconvert|linguist|lrelease|lupdate|lprodump|pixeltool| \
   qcollectiongenerator|qdbus|qdbusviewer|qhelpconverter|qhelpgenerator| \
   qtplugininfo|qtattributionsscanner|qtpaths|lrelease-pro|lupdate-pro | \
   qdistancefieldgenerator|qdoc|qtdiag)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt6
      ln -sv ${i} ${i}-qt6
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


## work-in-progress... -- rex
%check
# check icon resolutions
pushd %{buildroot}%{_datadir}/icons
for RES in $(ls hicolor); do
  for APP in designer assistant linguist qdbusviewer; do
    if [ -e hicolor/$RES/apps/${APP}*.* ]; then
      file hicolor/$RES/apps/${APP}*.* | grep "$(echo $RES | sed 's/x/ x /')"
    fi
  done
done
popd


%files
%{_bindir}/qdbus-qt6
%{_bindir}/qtpaths-qt6
%{_qt6_bindir}/qdbus
%{_qt6_bindir}/qdbus-qt6
%{_qt6_bindir}/qtpaths
%{_qt6_bindir}/qtpaths-qt6
%{_qt6_libdir}/libQt6UiTools.so.6*

%files common
%license LICENSE.LGPL*

%ldconfig_scriptlets libs-designer

%files  libs-designer
%{_qt6_libdir}/libQt6Designer.so.6*
%dir %{_qt6_libdir}/cmake/Qt6Designer/

%ldconfig_scriptlets libs-designercomponents

%files  libs-designercomponents
%{_qt6_libdir}/libQt6DesignerComponents.so.6*

%ldconfig_scriptlets libs-help

%files  libs-help
%{_qt6_libdir}/libQt6Help.so.6*

%files -n qt6-assistant
%{_bindir}/assistant-qt6
%{_qt6_bindir}/assistant*
%{_datadir}/applications/*assistant.desktop
%{_datadir}/icons/hicolor/*/apps/assistant*.*


%files -n qt6-doctools
%{_bindir}/qdoc*
%{_qt6_bindir}/qdoc*
%{_bindir}/qdistancefieldgenerator*
%{_bindir}/qhelpgenerator*
%{_qt6_bindir}/qdistancefieldgenerator*
%{_qt6_bindir}/qhelpgenerator*
%{_bindir}/qtattributionsscanner-qt6
%{_qt6_bindir}/qtattributionsscanner*

%files -n qt6-designer
%{_bindir}/designer*
%{_qt6_bindir}/designer*
%{_datadir}/applications/*designer.desktop
%{_datadir}/icons/hicolor/*/apps/designer*.*

%if 0%{?webkit}
%files -n qt6-designer-plugin-webkit
%{_qt6_plugindir}/designer/libqwebview.so
%{_qt6_libdir}/cmake/Qt6Designer/Qt6Designer_QWebViewPlugin.cmake
%endif


%files -n qt6-linguist
%{_bindir}/linguist*
%{_qt6_bindir}/linguist*
# phrasebooks used by linguist
%{_datadir}/qt6/phrasebooks/*.qph
%{_datadir}/applications/*linguist.desktop
%{_datadir}/icons/hicolor/*/apps/linguist*.*
# linguist friends
%{_bindir}/lconvert*
%{_bindir}/lrelease*
%{_bindir}/lupdate*
%{_bindir}/lprodump*
%{_qt6_bindir}/lconvert*
%{_qt6_bindir}/lrelease*
%{_qt6_bindir}/lupdate*
%{_qt6_bindir}/lprodump*


%files -n qt6-qdbusviewer
%{_bindir}/qdbusviewer*
%{_qt6_bindir}/qdbusviewer*
%{_datadir}/applications/*qdbusviewer.desktop
%{_datadir}/icons/hicolor/*/apps/qdbusviewer*.*

%files devel
%{_bindir}/pixeltool*
%{_bindir}/qtdiag*
%{_bindir}/qtplugininfo*
%{_qt6_bindir}/pixeltool*
%{_qt6_bindir}/qtdiag*
%{_qt6_bindir}/qtplugininfo*
%{_qt6_headerdir}/QtDesigner/
%{_qt6_headerdir}/QtDesignerComponents/
%{_qt6_headerdir}/QtHelp/
%{_qt6_headerdir}/QtUiPlugin
%{_qt6_headerdir}/QtTools/
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/libQt6Designer*.prl
%{_qt6_libdir}/libQt6Designer*.so
%{_qt6_libdir}/libQt6Help.prl
%{_qt6_libdir}/libQt6Help.so
%{_qt6_libdir}/libQt6UiTools.so
%{_qt6_libdir}/cmake/Qt6/FindWrapLibClang.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtToolsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Designer/*.cmake
%{_qt6_libdir}/cmake/Qt6DesignerComponents/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Help/
%{_qt6_libdir}/cmake/Qt6Help/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Linguist
%{_qt6_libdir}/cmake/Qt6Linguist/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6LinguistTools
%{_qt6_libdir}/cmake/Qt6LinguistTools/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6UiPlugin/
%{_qt6_libdir}/cmake/Qt6UiPlugin/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Tools/
%{_qt6_libdir}/cmake/Qt6Tools/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ToolsTools/
%{_qt6_libdir}/cmake/Qt6ToolsTools/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6LinguistTools
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_designer.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_designer_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_designercomponents_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_help.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_help_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_linguist.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_linguist_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_tools_private.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_uiplugin.pri


%files static
%{_qt6_headerdir}/QtUiTools/
%{_qt6_libdir}/libQt6UiTools.prl
%{_qt6_libdir}/cmake/Qt6UiTools/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_uitools.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_uitools_private.pri

%if ! 0%{?no_examples:1}
%files examples
%{_qt6_examplesdir}/
%{_qt6_plugindir}/designer/*
%dir %{_qt6_libdir}/cmake/Qt6Designer
%endif


%changelog
* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-2
- Rebuild (clang)

* Wed Jan 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0
- 6.0.0
