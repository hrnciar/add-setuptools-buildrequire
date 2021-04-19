# vim: syntax=spec

%global libdir %{_prefix}/lib

Name: rpkg-macros
Version: 1.1
Release: 2%{?dist}
Summary: Set of preproc macros for rpkg utility
License: GPLv2+
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#98f8a437ad14a6cf93a8ea698067da0fb949ec28:macros
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util/macros
# git checkout rpkg-macros-1.1-1
# ./rpkg spec --sources
Source0: rpkg-util-macros-98f8a437.tar.gz

BuildArch: noarch

BuildRequires: bash
BuildRequires: preproc
%if 0%{?fedora}
BuildRequires: git-core
%else
BuildRequires: git
%endif
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: rpm-git-tag-sort

Requires: bash
%if 0%{?fedora}
Requires: git-core
%else
Requires: git
%endif
Requires: coreutils
Requires: findutils
Requires: rpm-git-tag-sort

%description
Set of preproc macros to be used by rpkg utilility. They
are designed to dynamically generate certain parts
of rpm spec files. You can use those macros also without
rpkg by:

   $ cat <file_with_the_macros> | preproc -s /usr/lib/rpkg.macros.d/all.bash

You can also source /usr/lib/rpkg.macros.d/all.bash into
your bash environment and then you can experiment with
them directly on your command-line. See content in
/usr/lib/rpkg.macros.d to discover available macros.

Please, see man rpkg-macros for more information.

%prep
%setup -T -b 0 -q -n rpkg-util-macros

%check
PATH=bin/:$PATH tests/run

%install
install -d %{buildroot}%{libdir}
install -d %{buildroot}%{libdir}/rpkg.macros.d
cp -ar macros.d/* %{buildroot}%{libdir}/rpkg.macros.d

install -d %{buildroot}%{_bindir}
install -p -m 755 bin/pack_sources %{buildroot}%{_bindir}/pack_sources

install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/rpkg-macros.1 %{buildroot}/%{_mandir}/man1/

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{libdir}/rpkg.macros.d
%{_bindir}/pack_sources
%{_mandir}/man1/rpkg-macros.1*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 clime <clime@fedoraproject.org> 1.1-1
- add trick in pack_sources to allow creating the archive in CWD

* Mon Oct 05 2020 clime <clime@fedoraproject.org> 1.0-1
- fix version check in git_pack
- rpm-git-tag-sort is also required during build for tests
- add man pages for rpkg-macros, redirect there from MACRO REFERENCE
  in man rpkg
- fix parameter order for rpm-git-tag-sort in git_merged_tag_refs
- fix version parsing from the latest tag, package name may contain
  dashes!
- implement support for multiple Sources at once
- use rpm-git-tag-sort for tag sorting & filtering in git_merged_tag_refs
submodules
- fix git_head for detached head state
- in git_bumped_version, lead must be numeric and greater than zero to output
follow as zero + small code tweak in git_version_generic
- remove now unused git_bumped_release, set "" as default for lead in
git_bumped_version
- make lead="" the only special case, otherwise lead is lead
- unify code and params for git_release and git_version
- code cleanup

* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.4-1
- remove shebangs in library files according to Fedora review
- changes according to review - usage of %%{_prefix} in spec, g-w for
pack_sources
- use git-core on Fedoras

* Fri Mar 06 2020 clime <clime@fedoraproject.org> 0.3-1
- fix warning about unset git indetity in test_submodule_sources
- skip test for submodule_sources on epel6
- add missing sleep in tests, add TODO
- fix changelog renderring for legacy git as there is no points-at
  option
- resolve problem in git_pack and submodules for epel7

* Wed Mar 04 2020 clime <clime@fedoraproject.org> 0.2-1
- fix bug on centos7 bash in is_physical_subpath function

* Wed Mar 04 2020 clime <clime@fedoraproject.org> 0.1-1
- initial release
