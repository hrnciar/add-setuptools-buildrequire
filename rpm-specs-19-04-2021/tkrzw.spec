%global _lto_cflags %{nil}

Name:		tkrzw
Version:	0.9.3
Release:	6%{?dist}
Summary:	A straightforward implementation of DBM
License:	ASL 2.0
URL:		https://dbmx.net/%{name}/
Source0:	https://dbmx.net/%{name}/pkg/%{name}-%{version}.tar.gz
# https://github.com/estraier/tkrzw/issues/6
# https://github.com/estraier/tkrzw/issues/7
Patch0:		tkrzw-0.9.3-do-not-override-build-flags.patch
# Developer's recomendation (https://github.com/estraier/tkrzw/issues/5)
Patch1:		tkrzw-0.9.3-skip-excessive-mlock-pages-tests.patch
BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	help2man
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
# https://bugzilla.redhat.com/show_bug.cgi?id=1920195
ExcludeArch:	%ix86

%description
Tkrzw is a C++ library implementing DBM with various algorithms. It features
high degrees of performance, concurrency and durability.

%package	libs
Summary:	Libraries for applications using Tkrzw

%description	libs
This package provides the essential shared libraries
for any Tkrzw client program or interface.

%package	devel
Summary:	Development files for Tkrzw
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
This package contains libraries and header files for
developing applications that use Tkrzw.

%package	doc
Summary:	Tkrzw API documentation
BuildArch:	noarch

%description	doc
This package contains API documentation for developing
applications that use Tkrzw.


%prep
%autosetup


%build
autoreconf -vif
%configure
%make_build apidoc all
for bin in \
  tkrzw_build_util tkrzw_str_perf tkrzw_file_perf tkrzw_dbm_perf tkrzw_dbm_util
do
  LD_LIBRARY_PATH=$PWD help2man --no-info --no-discard-stderr \
    --version-string='%{version}' --output="${bin}.1" \
    "./${bin}"
done


%install
%make_install
# Remove static .a file
rm -f %{buildroot}%{_libdir}/lib%{name}.a
# mans
install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -m 0644 -p *.1


%check
%make_build check


%if 0%{?el8}
%ldconfig_scriptlets libs
%endif


%files
%{_bindir}/%{name}_*
%{_mandir}/man1/%{name}_*.1*

%files	libs
%license COPYING
%doc CONTRIBUTING.md
%{_libdir}/lib%{name}.so.{0,0.3.0}

%files	devel
%doc example
%{_includedir}/%{name}_*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files	doc
%license COPYING
%doc doc api-doc


%changelog
* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.3-6
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Jan 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.3-5
- Link new RHBZ bug for ExcludeArch

* Thu Jan 21 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-4
- 'Required: pkgconfig' removed from -devel
- spec spaces/tabs resolved
- Added CONTRIBUTING.md to -libs
- examples/ moved from -doc to -devel
- `excludearch i686` proven

* Tue Jan 19 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-3
- Disabled only those tests that lock excessive numbers of pages (and will
  therefore fail on a system with default resource limits)
- Disabled LTO, since it causes test failures on all file-based database tests
- Added COPYING file in files section for -doc subpackage
- Installing doc/ and api-doc/ subdirectories in -doc subpackage
- Added example/ to -doc
- Changed man pages wildcard from ..._*.1.* to ..._*.1*
- Removed -lib/-libs mess
- Excluded i686 arch

* Mon Jan 18 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-2
- License fixes.
- *.so.* names fix
- make_build fix
- -doc fixes
- check fixes
- ldconfig call fix
- compiler flags fixes

* Fri Jan 08 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-1
- Initial packaging.
