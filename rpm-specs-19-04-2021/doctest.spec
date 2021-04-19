%undefine __cmake3_in_source_build
%global debug_package %{nil}

Name: doctest
Version: 2.4.5
Release: 2%{?dist}
Summary: Feature-rich header-only C++ testing framework
License: MIT
URL: https://github.com/onqtam/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1: 0001-linux-always-include-signal.h.patch

BuildRequires: gcc-c++
BuildRequires: cmake3
BuildRequires: git

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake3 \
  -DCMAKE_BUILD_TYPE=Release \
  -DDOCTEST_WITH_MAIN_IN_STATIC_LIB:BOOL=OFF \
  -DDOCTEST_WITH_TESTS:BOOL=ON \
  %{nil}
%cmake3_build

%check
%ctest3

%install
%cmake3_install

%files devel
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
* Thu Feb 18 2021 Nick Black <dankamongmen@gmail.com> - 2.4.5-2
- Add my patch to work around recent libc blues

* Tue Feb 02 2021 Nick Black <dankamongmen@gmail.com> - 2.4.5-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Nick Black <dankamongmen@gmail.com> - 2.4.4-1
- New upstream release

* Wed Dec 16 2020 Nick Black <dankamongmen@gmail.com> - 2.4.3-1
- New upstream release

* Wed Nov 04 2020 Nick Black <dankamongmen@gmail.com> - 2.4.1-1
- New upstream release
- Trivial patch from upstream to fix unit tests

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Nick Black <dankamongmen@gmail.com> - 2.4.0-1
- New upstream release

* Sun May 24 2020 Nick Black <dankamongmen@gmail.com> - 2.3.8-1
- New upstream release

* Thu Apr 30 2020 Nick Black <dankamongmen@gmail.com> - 2.3.7-1
- Initial RPM release
