# Copyright (c) 2012, 2014  Dave Love
# Copyright (c) 2015 James Hunt
# MIT licence, per Fedora policy

Name:           procenv
Version:        0.51
Release:        5%{?dist}
Summary:        Utility to show process environment

License:        GPLv3+
URL:            https://github.com/jamesodhunt/procenv
Source0:        https://github.com/jamesodhunt/procenv/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  expat, libcap-devel, libselinux-devel, check-devel, gcc
# Only used for testing; not in EL6.
%{!?el6:BuildRequires:  perl(JSON::PP)}
%ifnarch %{arm} s390 s390x
BuildRequires:  numactl-devel
%endif

%description
This package contains a command-line tool that displays as much
detail about itself and its environment as possible. It can be
used as a test tool, to understand the type of environment a
process runs in, and for comparing system environments.

%prep
%setup -q
# remove symlink
mv README.rst README

%build
# Pre-release GCC 10 produces a warning on s390x and fails otherwise.
sed -i -e 's/-Werror//' src/Makefile.in
%configure
%make_build

%install
%make_install

%check
make check

%files
%{_bindir}/procenv
%{_mandir}/man1/procenv.1*
# ChangeLog is empty
%doc README NEWS AUTHORS TODO
%license COPYING

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Dave love <loveshack@fedoraproject.org> - 0.51-3
- Avoid FTBFS (#1799896)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Dave love <loveshack@fedoraproject.org> - 0.51-1
- New version; drop patch

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Dave Love <loveshack@fedoraproject.org> - 0.50-4
- Patch to fix failure with gcc 9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Dave Love <loveshack@fedoraproject.org> - 0.50-1
- New version
- Remove el5-isms

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Dave Love <loveshack@fedoraproject.org> - 0.49-2
- Bump to rebuild after failed mass rebuild

* Mon Feb 13 2017 Dave Love <loveshack@fedoraproject.org> - 0.49-1
- New version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  1 2016 Dave Love <loveshack@fedoraproject.org> - 0.46-1
- New version
- Remove fedora guard in %%check
- Don't distribute ChangeLog

* Tue Mar 22 2016 Dave Love <loveshack@fedoraproject.org> - 0.45-1
- New version

* Wed Feb 17 2016 Dave Love <loveshack@fedoraproject.org> - 0.44-1
- New version

* Thu Nov  5 2015 James Hunt <jamesodhunt@gmail.com> - 0.42-1
- Simplified BuildRequires now that autoreconf is no longer needed.

* Thu Oct 29 2015 James Hunt <jamesodhunt@gmail.com> - 0.41-1
- New upstream version.
- BuildRequires: Added check-devel for new unit tests.
- This upstream version lacks a configure script, so added autoconf,
  automake and libtool to BuildRequires, plus a call to autoreconf.
- Updated URL+Source0 as project has moved to github.
- Source0 includes magic URL fragment to rename the source to be of form
  "<name>-<version>.tar.gz", rather than the bare "<tag>.tar.gz" github format.
- Add ChangeLog and TODO to package.

* Thu Oct 15 2015 Dave Love <loveshack@fedoraproject.org> - 0.40-1
- New version
- Remove %%defattr
- Use %%license
- MIT licence for packaging

* Thu Aug 28 2014 Dave Love <d.love@liverpool.ac.uk> - 0.36-1
- New upstream version

* Sat Jun 21 2014 Dave Love <d.love@liverpool.ac.uk> - 0.35-3
- BR on libselinux-devel for EPEL5
- Add doc files

* Thu Jun  5 2014 Dave Love <d.love@liverpool.ac.uk> - 0.35-2
- Only BR perl-JSON-PP and run tests on fedora
- Remove unnecessary BRs

* Fri Jan 31 2014 James Hunt <james.hunt@ubuntu.com> - 0.32-1
- Update to 0.31.

* Thu Jan 23 2014 James Hunt <james.hunt@ubuntu.com> - 0.30-1
- Update to 0.30.

* Fri Nov 15 2013 Dave Love <d.love@liverpool.ac.uk> - 0.27-1
- Update to 0.27, fix Source0

* Sun Dec  9 2012 Dave Love <fx@gnu.org> - 0.18-1
- Update to 0.18

* Tue Dec  4 2012 Dave Love <fx@gnu.org> - 0.16-2
- Re-fix locale-reporting.

* Mon Dec  3 2012 Dave Love <fx@gnu.org> - 0.16-1
- Update to 0.16

* Thu Nov 22 2012 Dave Love <fx@gnu.org> - 0.12-1
- Initial packaging
