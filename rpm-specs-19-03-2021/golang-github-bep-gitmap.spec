# Generated by go2rpm
%bcond_without check

# https://github.com/bep/gitmap
%global goipath         github.com/bep/gitmap
Version:                1.1.2

%gometa

%global godevelheader %{expand:
Requires:       git-core}

%global common_description %{expand:
A fairly fast way to create a map from all the filenames to info objects for a
given revision of a Git repo.

This library uses os/exec to talk to Git. There are faster ways to do this by
using some Go Git-lib or C bindings, but that adds dependencies I really don't
want or need.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Create map from filename to info object from revision of a repo

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Skip tests that expect gitmap to be a real clone instead of an archive
Patch0:         0001-Skip-repo-tests.patch

BuildRequires:  git-core

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 00:26:28 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Sat Feb 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 15:23:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new macros

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitdcb907b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitdcb907b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitdcb907b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitdcb907b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitdcb907b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Frederico Lima <fredlima@fedoraproject.org> - 0-0.1.gitdcb907b
- First package for Fedora
