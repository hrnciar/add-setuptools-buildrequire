# Generated by go2rpm
%bcond_without check

# https://github.com/unknwon/goconfig
%global goipath         github.com/unknwon/goconfig
%global commit          df7de6a44db81dd3ba39fa809f75e2063a6499d1

%gometa

%global goaltipaths     github.com/Unknwon/goconfig

%global common_description %{expand:
Package Goconfig is a fully functional and comments-support configuration file
(.ini) parser.}

%global golicenses      LICENSE
%global godocs          README.md README_ZH.md

Name:           %{goname}
Version:        0
Release:        0.14%{?dist}
Summary:        Fully functional and comments-support configuration file (.ini) parser

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 23:32:09 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.13.20210113gitdf7de6a
- Add missing alternte import path

* Wed Jan 13 17:44:56 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.12.20210113gitdf7de6a
- Bunp to commit df7de6a44db81dd3ba39fa809f75e2063a6499d1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 21:20:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20190602git3dba17d
- Bump to commit 3dba17dd7b9ec8509b3621a73a30a4b333eb28da

* Mon Feb 25 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7.20190225git56bd8ab
- Bump to upstream 56bd8ab186196b5203e3b8e17057a04a65153003

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitef1e4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.5.gitef1e4c7
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitef1e4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314gitef1e4c7
- Update with the new Go packaging
- Upstream GIT revision ef1e4c7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20161121git87a46d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20161121git87a46d9
- First package for Fedora
