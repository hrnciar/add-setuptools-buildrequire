# Generated by go2rpm 1
%bcond_without check

# https://github.com/fsnotify/fsnotify
%global goipath         github.com/fsnotify/fsnotify
Version:                1.4.9

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-fsnotify-fsnotify-devel < 1.4.7-6
}

%global goaltipaths     gopkg.in/fsnotify/fsnotify.v1 gopkg.in/fsnotify/v1/fsnotify

%global common_description %{expand:
Cross-platform file system notifications for Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS CHANGELOG.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Cross-platform file system notifications for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/unix)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.9-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.7-7
- Add Obsoletes for old name

* Wed Apr 24 12:36:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.7-6
- Update to new macros

* Fri Mar 08 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.7-5
- Rewrite using new Go packaging
- Add alternate import path "gopkg.in/fsnotify/fsnotify.v1"

* Tue Feb 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.7-4
- Backport patch to fix TestInotifyOverflow

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.4.7-1
- Update version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Frederico Lima <fredlima@fedoraproject.org> - 1.4.2-1
- First package for Fedora