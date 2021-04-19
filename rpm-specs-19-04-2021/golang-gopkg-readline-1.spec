# Generated by go2rpm
%bcond_without check

# https://github.com/chzyer/readline
%global goipath         gopkg.in/readline.v1
%global forgeurl        https://github.com/chzyer/readline
Version:                1.4
%global commit          2972be24d48e78746da79ba8e24e8b488c9880de

%gometa

%global goaltipaths     github.com/chzyer/readline

%global common_description %{expand:
Readline is a pure Go implementation of GNU Readline like library.}

%global golicenses      LICENSE
%global godocs          example CHANGELOG.md README.md

Name:           %{goname}
Release:        13%{?dist}
Summary:        Pure Go implementation of GNU Readline-like library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/chzyer/test)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 10:40:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-9.20180628git2972be2
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8.git2972be2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.4-7.git2972be2
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6.git2972be2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-5.20180628git2972be2
- Bump to commit 2972be24d48e78746da79ba8e24e8b488c9880de

* Mon Apr 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-4.20180409gitf6d7a1f
- Upstream GIT revision f6d7a1f

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-3
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-1
- First package for Fedora
