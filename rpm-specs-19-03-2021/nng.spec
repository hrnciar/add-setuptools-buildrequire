Name:     nng
Version:  1.4.0
Release:  1%{?dist}
Summary:  nanomsg next generation: light-weight brokerless messaging

License:  MIT
URL:      https://nanomsg.github.io/nng/
Source0:  https://github.com/nanomsg/nng/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libnsl2-devel
BuildRequires: mbedtls-devel
BuildRequires: rubygem-asciidoctor

%description
nng (nanomsg next generation) is a socket library that provides several 
common communication patterns. It aims to make the networking layer fast, 
scalable, and easy to use. Implemented in C, it works on a wide range 
of operating systems with no further dependencies.

The communication patterns, also called "scalability protocols", are
basic blocks for building distributed systems. By combining them you can
create a vast array of distributed applications.

%package  devel
Summary:  Development files for the nng socket library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files needed to develop applications using nanomsg,
a socket library that provides several common communication patterns.

%package  utils
Summary:  Command line interface for communicating with nng

%description utils
Includes nngcat, a simple utility for reading and writing to nanomsg
sockets and bindings, which can include local and remote connections.

%prep
%autosetup

%build
%cmake -DCMAKE_CXX_FLAGS="%optflags -fPIC" -DBUILD_SHARED_LIBS=ON \
       -DNNG_SUPP_TLS=ON -DNNG_SUPP_WEBSOCKET=ON -DNNG_ENABLE_NNGCAT=ON \
       -DNNG_TESTS=ON -DNNG_ENABLE_DOC=ON .

%cmake_build

%install
%cmake_install
# No need to ship dev docs as both html and man format
rm -rf %{buildroot}/%{_mandir}/man[3-7]*

%ldconfig_scriptlets

%files
%license LICENSE.txt
%{_libdir}/libnng.so.1*

%files devel
%{_docdir}/nng/
%{_includedir}/nng/
%{_libdir}/libnng.so
%{_libdir}/cmake/nng/

%files utils
%{_bindir}/nngcat
%{_mandir}/man1/nngcat.1.gz

%changelog
* Sun Feb 14 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0 (rhbz#1808813)

* Thu Feb 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6-1
- Update to latest upstream release 1.2.6 (rhbz#1798888)

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.5-1
- Update to latest upstream release 1.2.5 (rhbz#1795639)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.4-1
- Update to 1.2.4

* Mon Jan 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-1
- Update to 1.2.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-1
- Update to 1.1.1

* Mon Nov 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-1
- Update to 1.1.0

* Sat Oct 06 2018 Morten Stevens <mstevens@fedoraproject.org> 1.0.1-2
- Rebuilt for mbed TLS 2.13.0

* Wed Aug  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- Update to 1.0.1

* Sun Jun 17 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.0-1
- Initial package
