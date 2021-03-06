%global commit d012ba8216a965f81df5363c0f14d5ec6bf25627
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora} || 0%{?rhel} != 8
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           beanstalk-client
Version:        1.4.0
Release:        3%{?dist}
Summary:        C/C++ client for the beanstalkd work queue
License:        BSD
URL:            https://github.com/deepfryed/beanstalk-client
Source0:        https://github.com/deepfryed/beanstalk-client/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Not upstreamable: disables tests which require networking, they fail in mock
Patch100:       0001-tests-disable-timeout-test.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make
%if %{with tests}
BuildRequires:  beanstalkd
%endif

%description
A C/C++ client library for the beanstalkd work queue.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%set_build_flags
make %{?_smp_mflags}

%install
%make_install INCLUDEDIR=%{_includedir} LIBDIR=%{_libdir}
rm %{buildroot}%{_libdir}/libbeanstalk.a*

%check
%if %{with tests}
beanstalkd &
make test
kill %1
%endif

%files
%license debian/copyright
%doc README.md
%{_libdir}/libbeanstalk.so.1.*
%{_libdir}/libbeanstalk.so.1

%files devel
%{_includedir}/beanstalk.h
%{_includedir}/beanstalk.hpp
%{_libdir}/libbeanstalk.so
%{_libdir}/pkgconfig/libbeanstalk.pc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Nov 15 2019 Dan Callaghan <dan.callaghan@opengear.com> - 1.4.0-1
- initial version
