Name:           libjwt
Version:        1.12.1
Release:        7%{?dist}
Summary:        A Javascript Web Token library in C

License:        MPLv2.0
URL:            https://github.com/benmcollins/libjwt
Source0:        https://github.com/benmcollins/libjwt/archive/v%{version}.tar.gz

Patch0:         without_examples.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  jansson-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel

%description
A Javascript Web Token library in C

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
autoreconf -i

%build
%configure --disable-static --without-examples
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%doc *.md
%{_libdir}/*.so.1*

%files devel
%doc *.md
%{_includedir}/jwt.h
%{_libdir}/libjwt.so
%{_libdir}/pkgconfig/libjwt.pc

%changelog
* Sun Apr 18 2021 Philip Kovacs <pkfed@fedoraproject.org> - 1.12.1-7
- Remove examples from build

* Tue Apr 13 2021 Philip Kovacs <pkfed@fedoraproject.org> - 1.12.1-6
- Fix canonical changelog dates

* Tue Apr 13 2021 Philip Kovacs <pkfed@fedoraproject.org> - 1.12.1-5
- Build for EPEL7/8

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 7 2020 Jared K. Smith <jsmith@fedoraproject.org> - 1.12.1-3
- More minor fixes for package review

* Tue Nov 3 2020 Jared K. Smith <jsmith@fedoraproject.org> - 1.12.1-2
- Update dependencies for package review

* Thu Oct 29 2020 Jared K. Smith <jsmith@fedoraproject.org> - 1.12.1-1
- Initial packaging
