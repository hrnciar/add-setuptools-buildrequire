# link issues on some platforms:
# https://bugzilla.redhat.com/show_bug.cgi?id=1893332
%ifarch i686 x86_64
%bcond_without static
%else
%bcond_with static
%endif

%bcond_without tests

Name:           fbzmq
Version:        2021.03.15.00
Release:        1%{?dist}
Summary:        Framework for writing services in C++ while leveraging libzmq

License:        MIT
URL:            https://github.com/facebook/fbzmq
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# this test is failing
Patch0:         %{name}-no_timeout_test.patch
# this test doesn't compile
Patch1:         %{name}-no_monitor_test.patch

# Folly is known not to work on big-endian CPUs
# https://bugzilla.redhat.com/show_bug.cgi?id=1910202
ExcludeArch:    s390x

BuildRequires:  cmake
BuildRequires:  gcc-c++
# Library dependencies
BuildRequires:  fbthrift-devel
BuildRequires:  fizz-devel
BuildRequires:  folly-devel
BuildRequires:  wangle-devel
BuildRequires:  zeromq-devel

%description
fbzmq provides a framework for writing services in C++ while leveraging the
awesomeness of libzmq (message passing semantics). At a high level it provides

- Lightweight C++ wrapper over libzmq which leverages newer C++ constructs and
  stricter type checking. Most notably it provides the ability to send/receive
  thrift objects as messages over wire without worrying about wire
  encoding/decoding protocols.
- Powerful Async Framework with EventLoop, Timeouts, SignalHandler and more to
  enable developers to write asynchronous applications efficiently.
- Suite of monitoring tools that make it easy to add logging and counters to
  your service.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if %{with static}
%global _static_builddir static_build

%package        static
Summary:        Static development libraries for %{name}
BuildRequires:  fbthrift-static
BuildRequires:  fizz-static
BuildRequires:  folly-static
BuildRequires:  wangle-static
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains static libraries for
developing applications that use %{name}.
%endif


%prep
%autosetup -p1


%build
%if %{with static}
# static build
mkdir %{_static_builddir}
pushd %{_static_builddir}
%cmake .. \
  -DBUILD_SHARED_LIBS=OFF \
  -DBUILD_TESTS=OFF \
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name}-static \
  -DFBTHRIFT_ROOT=%{_libdir}/cmake/fbthrift-static \
  -DFIZZ_ROOT=%{_libdir}/cmake/fizz-static \
  -DFOLLY_ROOT=%{_libdir}/cmake/folly-static \
  -DWANGLE_ROOT=%{_libdir}/cmake/wangle-static
%cmake_build
popd
%endif

%cmake \
  -DBUILD_SHARED_LIBS=ON \
%if %{with tests}
  -DBUILD_TESTS=ON \
%else
  -DBUILD_TESTS=OFF \
%endif
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DPACKAGE_VERSION=%{version} \
  -DSO_VERSION=%{version}
%cmake_build


%install
%if %{with static}
pushd %{_static_builddir}
%cmake_install
popd
%endif

%cmake_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%if %{with tests}
%check
# we can't use the ctest macro directly as the tests are in a subdirectory
pushd "%{__cmake_builddir}/fbzmq"
%__ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
popd
%endif


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%license LICENSE-examples
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md fbzmq/examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}

%if %{with static}
%files static
%{_libdir}/*.a
%{_libdir}/cmake/%{name}-static
%endif


%changelog
* Mon Mar 15 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2021.03.15.00-1
- Update to 2021.03.15.00

* Wed Feb 03 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2021.02.01.00-1
- Update to 2021.02.01.00

* Tue Jan 26 17:50:58 PST 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2021.01.25.00-1
- Update to 2021.01.25.00

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.28.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.12.28.00-2
- Rebuilt for Boost 1.75

* Tue Dec 29 12:16:18 PST 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2020.12.28.00-1
- Update to 2020.12.28.00

* Tue Dec 22 16:59:00 PST 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2020.12.21.00-1
- Update to 2020.12.21.00

* Mon Nov 30 10:42:58 PST 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2020.11.30.00-1
- Update to 2020.11.30.00

* Mon Nov 23 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2020.11.23.00-1
- Update to 2020.11.23.00

* Mon Nov 16 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2020.11.16.00-1
- Update to 2020.11.16.00

* Fri Nov 13 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2020.11.09.00-2
- Fix for type mismatch on 32-bit architectures
- Fix ctest invocation
- Disable failing timeout test

* Wed Nov 11 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2020.11.09.00-1
- Initial package
