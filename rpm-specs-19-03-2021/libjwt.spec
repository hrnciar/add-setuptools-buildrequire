Name:           libjwt
Version:        1.12.1
Release:        4%{?dist}
Summary:        A Javascript Web Token library in C

License:        MPLv2.0
URL:            https://github.com/benmcollins/libjwt
Source0:        https://github.com/benmcollins/libjwt/archive/v%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  jansson-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires: make

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
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc *.md
%{_libdir}/*.so.1*
%{_bindir}/jwtauth
%{_bindir}/jwtgen

%files devel
%doc *.md
%{_includedir}/jwt.h
%{_libdir}/libjwt.so
%{_libdir}/pkgconfig/libjwt.pc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov  7 10:50:01 EST 2020 Jared K. Smith <jsmith@fedoraproject.org> - 1.12.1-3
- More minor fixes for package review

* Tue Nov  3 04:59:39 EST 2020 Jared K. Smith <jsmith@fedoraproject.org> - 1.12.1-2
- Update dependencies for package review

* Thu Oct 29 09:45:39 EDT 2020 Jared K. Smith <jsmith@fedoraproject.org> - 1.12.1-1
- Initial packaging
