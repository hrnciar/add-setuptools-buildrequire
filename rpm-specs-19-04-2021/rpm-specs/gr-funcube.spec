Name:          gr-funcube
URL:           https://github.com/dl1ksv/gr-funcube
Version:       1.0.0
Release:       1%{?dist}
License:       GPLv3+
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: hidapi-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: pybind11-devel
BuildRequires: libunwind-devel
BuildRequires: alsa-lib-devel
BuildRequires: libusbx-devel
BuildRequires: python3-devel
BuildRequires: log4cpp-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel
BuildRequires: gmp-devel
BuildRequires: orc-devel
BuildRequires: libsndfile-devel
Obsoletes:     gr-fcdproplus < 3.8.0-5.20200807git06069c2e
Summary:       GNURadio support for FUNcube Dongle Pro and FUNcube Dongle Pro+
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       10-funcube.rules
# https://github.com/dl1ksv/gr-funcube/issues/3
Patch0:        gr-funcube-1.0.0-tests-fix-path.patch

%description
GNURadio support for FUNcube Dongle Pro and FUNcube Dongle Pro+.

%package devel
Summary:       Development files for gr-funcube
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-funcube.

%package doc
Summary:       Documentation files for gr-funcube
Requires:      %{name} = %{version}-%{release}
# Workaround for rhbz#1814356
#BuildArch:    noarch

%description doc
Documentation files for gr-funcube.

%prep
%autosetup -p1

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%check
# Temporary disabled until resolved ppc64le problems
#cd %{_vpath_builddir}
#make test

%install
%cmake_install

# udev rule
install -Dpm 0644 %{S:1} %{buildroot}%{_udevrulesdir}/10-funcube.rules

%ldconfig_scriptlets

%pre
# sharing group with the rtl-sdr package not to introduce new group
# todo: consolidate also with the uhd package (usrp group) to have one generic
# group e.g. 'sdr' for this class of devices
getent group rtlsdr >/dev/null || \
  %{_sbindir}/groupadd -r rtlsdr >/dev/null 2>&1
exit 0

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%license COPYING
%doc README.md
%{_libdir}/*.so.*
%{python3_sitearch}/funcube
%{_datadir}/gnuradio/grc/blocks/*
%{_udevrulesdir}/10-funcube.rules

%files devel
%{_includedir}/funcube
%{_libdir}/*.so
%{_libdir}/cmake/funcube

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Wed Feb 17 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-1
- Initial version
  Related: rhbz#1924712
