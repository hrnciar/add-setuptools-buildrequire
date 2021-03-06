%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name: scitokens-cpp
Version: 0.5.1
Release: 3%{?dist}
Summary: C++ Implementation of the SciTokens Library
License: ASL 2.0
URL: https://github.com/scitokens/scitokens-cpp

# Directions to generate a proper release:
# git archive --prefix "scitokens-cpp-0.3.3/" -o "scitokens-cpp-0.3.3.tar" v0.3.3
# git submodule update --init
# git submodule foreach --recursive "git archive --prefix=scitokens-cpp-0.3.3/\$path/ --output=\$sha1.tar HEAD && tar --concatenate --file=$(pwd)/scitokens-cpp-0.3.3.tar \$sha1.tar && rm \$sha1.tar"
# gzip "scitokens-cpp-0.3.3.tar"
Source0: https://github.com/scitokens/scitokens-cpp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Fix build failure with GCC10.1 and Werror (upstream pull request)
# https://github.com/kazuho/picojson/pull/131
Patch0: %{name}-paren.patch
# Fix compilation error with gcc 11
# https://github.com/scitokens/scitokens-cpp/pull/34
Patch1: %{name}-fix-compilation-error-with-gcc-11.patch

# Scitokens-cpp bundles jwt-cpp, a header only dependency
# Since it doesn't create a library that can be used by others, it seems
# inappropriate to include a "Provides", as jwt-cpp is not provided
# by this package.

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake3
BuildRequires: sqlite-devel
BuildRequires: openssl-devel
BuildRequires: libcurl-devel
BuildRequires: libuuid-devel

# Needed for C++11
%if 0%{?el6}
BuildRequires: devtoolset-8-toolchain
BuildRequires: scl-utils
%endif

%description
%{summary}

%package devel
Summary: Header files for the scitokens-cpp public interfaces

Requires: %{name}%{?_isa} = %{version}

%description devel
%{summary}

%prep
%setup -q
cd vendor/jwt-cpp/include/jwt-cpp
%patch0 -p1
cd -
%patch1 -p1

%build
%cmake3
%cmake3_build

%install
%cmake3_install

# Run the ldconfig
%ldconfig_scriptlets

%files
%{_libdir}/libSciTokens.so.0*
%license LICENSE
%doc README.md

%files devel
%{_libdir}/libSciTokens.so
%{_includedir}/scitokens/scitokens.h
%dir %{_includedir}/scitokens

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.1-2
- Fix build failure with GCC10.1 and Werror (upstream pull request)
- Adapt specfile to new cmake macros (out of tree build)
- Drop EPEL 6 conditionals (EOL)
- Fix compilation error with gcc 11

* Wed Jun 24 2020 Derek Weitzel <dweitzel@unl.edu> - 0.5.1-1
- Add storage.modify as write permission

* Fri Feb 28 2020 Derek Weitzel <dweitzel@unl.edu> - 0.5.0-1
- Add API for retrieving string list attributes

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Derek Weitzel <dweitzel@unl.edu> - 0.4.0-1
- Add support for WLCG profile

* Fri Nov 08 2019 Derek Weitzel <dweitzel@unl.edu> - 0.3.5-1
- Fix EC public key handling

* Wed Sep 18 2019 Derek Weitzel <dweitzel@unl.edu> - 0.3.4-1
- Fix bugs for support with IAM

* Thu Aug 01 2019 Derek Weitzel <dweitzel@unl.edu> - 0.3.3-3
- Update the packaging to bring it line with EPEL (fedora) guidelines

* Tue Jul 30 2019 Derek Weitzel <dweitzel@unl.edu> - 0.3.3-2
- Change the Source URL
- Use make_build in the packaging

* Thu Jul 25 2019 Derek Weitzel <dweitzel@unl.edu> - 0.3.3-1
- Merge OSG changes
- Use a newer, still supported version of devtoolset
- Fix bug in verifying EC signed tokens #13

* Thu Jul 25 2019 Derek Weitzel <dweitzel@unl.edu> - 0.3.2-1
- Update RPM to v0.3.2 of the packaging.
- Fix downloading public key bug #12

* Thu Jun 20 2019 Brian Bockelman <brian.bockelman@cern.ch> - 0.3.1-1
- Update RPM to v0.3.1 of the packaging.

* Wed May 29 2019 M??ty??s Selmeci <matyas@cs.wisc.edu> - 0.3.0-4
- Use double layer of const for deserialize
  (patch from https://github.com/scitokens/scitokens-cpp/commit/ac0b2f0679488fa91c14ed781268efbcdb69ed3c)

* Mon May 13 2019 M??ty??s Selmeci <matyas@cs.wisc.edu> - 0.3.0-3
- Add Force-aud-test-in-the-validator.patch from
  https://github.com/scitokens/scitokens-cpp/pull/8

* Fri May 03 2019 M??ty??s Selmeci <matyas@cs.wisc.edu> - 0.3.0-2
- Fix requirements

* Thu May 02 2019 M??ty??s Selmeci <matyas@cs.wisc.edu> - 0.3.0-1
- Update to v0.3.0
- Add dependencies on libcurl-devel, libuuid-devel

* Thu Jan 03 2019 Brian Bockelman <bbockelm@cse.unl.edu> - 0.1.0-1
- Initial version of the SciTokens C++ RPM.
