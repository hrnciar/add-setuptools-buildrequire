# Generated by go2rpm
%bcond_without check

# https://github.com/pkg/xattr
%global goipath         github.com/pkg/xattr
Version:                0.4.3

%gometa

%global common_description %{expand:
Extended attribute support for Go (linux + darwin + freebsd + netbsd).

"Extended attributes are name:value pairs associated permanently with files and
directories, similar to the environment strings associated with a process. An
attribute may be defined or undefined. If it is defined, its value may be empty
or non-empty."}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Extended attribute support for Go

# Upstream license specification: BSD-2-Clause
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 18:22:49 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.3-1
- Update to 0.4.3
- Close: rhbz#1895706

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 20:05:28 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Release 0.4.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.3.1-2
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Sun Oct 14 2018 Steve Miller (copart) <code@rellims.com> - 0.3.1-1
- Bumped upstream version, bug fix release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Steve Miller (copart) <code@rellims.com> - 0.3.0-1
- First package for Fedora
