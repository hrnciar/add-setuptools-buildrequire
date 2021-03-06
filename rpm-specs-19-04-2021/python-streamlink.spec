%global srcname streamlink
%global _description %{expand:Streamlink is a command-line utility that pipes video streams from various
services into a video player, such as VLC. The main purpose of Streamlink is to
allow the user to avoid buggy and CPU heavy flash plugins but still be able to
enjoy various streamed content. There is also an API available for developers
who want access to the video stream data. This project was forked from
Livestreamer, which is no longer maintained.}

Name:           python-%{srcname}
Version:        2.1.1
Release:        1%{?dist}
Summary:        Python library for extracting streams from various websites

# src/streamlink/packages/requests_file.py is ASL 2.0
License:        BSD and ASL 2.0
URL:            https://streamlink.github.io/
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Use pycryptodomex library instead of crypto/pycryptodome
Patch0:         %{name}-2.1.0-pycryptodomex.patch
# Use sphinx-rtd-theme to build documentation instead of furo (not available in
# Fedora, see also https://bugzilla.redhat.com/show_bug.cgi?id=1910798)
Patch1:         %{name}-2.0.0-doc.patch
# Fix dependencies version
Patch2:         %{name}-2.1.0-dependencies.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# Needed for documentation
BuildRequires:  make
BuildRequires:  %{py3_dist iso-639}
BuildRequires:  %{py3_dist iso3166}
BuildRequires:  %{py3_dist isodate}
BuildRequires:  %{py3_dist pycryptodomex}
BuildRequires:  %{py3_dist pysocks}
BuildRequires:  %{py3_dist recommonmark}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist websocket-client}
# Needed for tests
BuildRequires:  %{py3_dist freezegun}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests-mock}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       %{py3_dist setuptools}
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       %{srcname} = %{version}-%{release}

%description -n python3-%{srcname}
%{_description}


%package doc
Summary:        Documentation for %{name}
Requires:       fontawesome-fonts
Requires:       google-roboto-slab-fonts
Requires:       lato-fonts

%description doc
%{_description}

This package provides documentation for %{name}.


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove shebang
for i in $(find src/%{srcname}/ -name "*.py"); do
    sed '1{\@^#!/usr/bin/env python@d}' $i >$i.new && \
    touch -r $i $i.new && \
    mv $i.new $i
done


%build
%py3_build

# Generate documentation
%{__python3} setup.py build_sphinx -b man
%{__python3} setup.py build_sphinx -b html
rm build/sphinx/html/.buildinfo

# Drop bundled web fonts in HTML documentation
if [[ -d build/sphinx/html/_static/fonts/ ]]; then
    pushd build/sphinx/html/_static/fonts/

    for f in fontawesome-webfont.*; do
        rm "$f"
        [[ "${f##*.}" = "ttf" ]] && ln -s "%{_fontbasedir}/fontawesome/$f" .
    done

    pushd Lato/
    rm *
    for i in Bold BoldItalic Italic Regular; do
        ln -s "%{_fontbasedir}/lato/Lato-$i.ttf" "lato-${i,,}.ttf"
    done
    popd

    pushd RobotoSlab/
    rm *
    for i in Bold Regular; do
        ln -s "%{_fontbasedir}/google-roboto-slab-fonts/RobotoSlab-$i.ttf" "roboto-slab-v7-${i,,}.ttf"
    done
    popd
    popd
fi


%install
%py3_install

# Install man page
install -Dpm 0644 build/sphinx/man/%{srcname}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{srcname}.1


%check
TZ=UTC %pytest \
    --deselect=tests/test_plugins_meta.py::TestPluginMeta::test_plugin_not_in_removed_list


%files -n python3-%{srcname}
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md KNOWN_ISSUES.md README.md
%license LICENSE NOTICE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}_cli/
%{_mandir}/man1/%{srcname}.1.*


%files doc
%doc build/sphinx/html/
%license LICENSE


%changelog
* Mon Apr 12 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Tue Mar 23 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sun Oct 18 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sun Sep 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-2
- Fix dependency on pycryptodomex

* Thu Sep 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Tue Jan 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Tue Nov 26 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Use pycryptodomex library instead of crypto

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sun Mar 31 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.2-5
- Enable python dependency generator

* Fri Oct 12 2018 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.2-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.14.2-2
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.14.2-1
- Update to 0.14.2

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.7

* Thu Jun 07 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Mon May 07 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Mon May 07 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Thu Mar 08 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jan 24 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Tue Nov 14 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Tue Oct 10 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.1-3
- Fix dependecy on python-websocket-client package

* Tue Sep 19 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.1-2
- Add missing dependecy on python-websocket-client package

* Tue Sep 19 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Thu May 11 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Wed Apr 05 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Mar 10 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Feb 22 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Sat Jan 07 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-3
- Add license to doc subpackage

* Sat Jan 07 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-2
- Fix license tag
- Move documentation to a subpackage
- Enable tests

* Sun Dec 18 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Dec 16 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.0-1
- Initial RPM release
