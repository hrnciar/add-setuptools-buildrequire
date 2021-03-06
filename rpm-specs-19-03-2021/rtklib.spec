%global gitcommit_full c6e6c03143c5b397a9217fae2f6423ccf9c03fb7
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})

%global tools_build convbin pos2kml str2str rnx2rtkp rtkrcv

Name:           rtklib
Version:        2.4.3.b33
Release:        6%{?dist}
Summary:        Program Package for GNSS Positioning

License:        BSD
URL:            http://www.rtklib.com
Source0:        https://github.com/tomojitakasu/RTKLIB/tarball/%{gitcommit_full}/%{name}-%{gitcommit}.tar.gz
# Full readme from master branch
Source1:        https://raw.githubusercontent.com/tomojitakasu/RTKLIB/master/readme.txt
# https://github.com/JensReimann/RTKLIB/tree/rtklib_2.4.3
# ceb8106d53afa44cad6c45ae7873ba85ca458dc5
# All 69 commits ahead of tomojitakasu:rtklib_2.4.3
Patch0:         rtklib-qt.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  chrpath


%description
RTKLIB is an open source program package for standard and precise
positioning with GNSS (global navigation satellite system). RTKLIB
consists of a portable program library and several APs (application
programs) utilizing the library.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Include files and mandatory libraries for development.

%package        doc
Summary:        RTKLIB manual
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
Manual for RTKLIB tools.

%package        libs
Summary:        RTKLIB shared library

%description    libs
RTKLIB Shared library.

%package        qt
Summary:        RTKLIB GUI tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    qt
GUI part of RTKLIB tools.

%prep
%setup -q -n tomojitakasu-RTKLIB-%{gitcommit}
# License text not in separate file and not in packaged branch
# https://github.com/tomojitakasu/RTKLIB/issues/540
cp %{SOURCE1} readme_orig.txt
%patch0 -p1

sed -e "s|target.path = /usr/lib|target.path = %{buildroot}%{_libdir}|" \
    -e "s|staticlib|sharedlib|" -i src/src.pro
sed -i "s|LDLIBS  = ../../../lib/iers/gcc/iers.a|LDLIBS  = ../../../lib/libiers.a|" app/rnx2rtkp/gcc/makefile
# Correct CLI tools build flags
for i in %{tools_build}; do
    pushd app/$i/gcc
        sed -i "s|-O3|%{optflags}|" makefile
    popd
done


%build
# Build GUI tools
%{qmake_qt5}
%make_build
# Build lib
pushd lib
    %{qmake_qt5}
    %make_build
popd
# Build cli tools
for i in %{tools_build}; do
    pushd app/$i/gcc
        %make_build
    popd
done

%install
%make_install
mkdir -p %{buildroot}/%{_bindir}
install -pm 755 app/rtknavi_qt/rtknavi_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkget_qt/rtkget_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkplot_qt/rtkplot_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkpost_qt/rtkpost_qt %{buildroot}%{_bindir}
install -pm 755 app/rtklaunch_qt/rtklaunch_qt %{buildroot}%{_bindir}
install -pm 755 app/srctblbrows_qt/srctblbrows_qt %{buildroot}%{_bindir}
install -pm 755 app/strsvr_qt/strsvr_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkconv_qt/rtkconv_qt %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm 755 app/convbin/gcc/convbin %{buildroot}%{_bindir}
install -pm 755 app/pos2kml/gcc/pos2kml %{buildroot}%{_bindir}
install -pm 755 app/str2str/gcc/str2str %{buildroot}%{_bindir}
install -pm 755 app/rnx2rtkp/gcc/rnx2rtkp %{buildroot}%{_bindir}
install -pm 755 app/rtkrcv/gcc/rtkrcv %{buildroot}%{_bindir}
install -pm 755 app/rtkrcv/gcc/rtk*.sh %{buildroot}%{_bindir}

install -pm 644 data/P1C1_ALL.DCB %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/P1P2_ALL.DCB %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/P2C2.DCB %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_GSI.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS08.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS_H.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS_HR.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS_MGEX.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/TLE_GNSS_SATNO.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/TLE_GNSS_SIM.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/URL_LIST.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/elmask_sample.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/gnssdatasrc.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/igs10P1565_wocov.snx %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/ngs_abs.pcv %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/stations.pos %{buildroot}%{_datadir}/%{name}/

chrpath --delete %{buildroot}%{_bindir}/*_qt


%files
# %license add-license-file-here
%doc readme.txt readme_orig.txt
%{_bindir}/convbin
%{_bindir}/pos2kml
%{_bindir}/str2str
%{_bindir}/rnx2rtkp
%{_bindir}/rtkrcv
%{_bindir}/rtkstart.sh
%{_bindir}/rtkshut.sh
%{_datadir}/%{name}/

%files devel
%{_libdir}/libRTKLib.so

%files doc
%doc doc

%files libs
# %license add-license-file-here
%doc readme.txt readme_orig.txt
%{_libdir}/libRTKLib.so.1*

%files qt
%{_bindir}/rtknavi_qt
%{_bindir}/rtkget_qt
%{_bindir}/rtkplot_qt
%{_bindir}/rtkpost_qt
%{_bindir}/rtklaunch_qt
%{_bindir}/srctblbrows_qt
%{_bindir}/strsvr_qt
%{_bindir}/rtkconv_qt


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.b33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 I??aki ??car <iucar@fedoraproject.org> - 2.4.3.b33-5
- Drop unneeded dependencies

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.b33-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.b33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul  5 2020 Vasiliy Glazov <vascom2@gmail.com> - 2.4.3.b33-2
- Split to subpackages
- Clean spec

* Wed Jul  1 2020 Vasiliy Glazov <vascom2@gmail.com> - 2.4.3.b33-1
- Initial packaging
