%global common_description %{expand:
The purpose of libfixposix is to offer replacements for parts of POSIX
whose behavior is inconsistent across *NIX flavors.}

Name:           libfixposix
Summary:        Thin wrapper over POSIX syscalls
Version:        0.4.3
Release:        5%{?dist}
License:        Boost

URL:            https://github.com/sionescu/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires: make

%description %{common_description}


%package        devel
Summary:        Thin wrapper over POSIX syscalls (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains the development headers.


%prep
%autosetup -p1


%build
autoreconf -vfi

%configure
%make_build


%install
%make_install

# remove libtool archive files
find %{buildroot} -name "*.la" -print -delete


%files
%license LICENCE
%doc README.md

%{_libdir}/%{name}.so.3*


%files devel
%{_includedir}/lfp.h
%{_includedir}/lfp/

%{_libdir}/%{name}.so

%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 0.4.3-1
- Initial packaging for fedora.

