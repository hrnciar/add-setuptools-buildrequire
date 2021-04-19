# Generated by go2rpm
# needs a ftp server running for the tests
%bcond_with check

# https://github.com/jlaffaye/ftp
%global goipath         github.com/jlaffaye/ftp
%global commit          9aae4d1511262659fe6de69ddbbb0b1871287e18

%gometa

%global common_description %{expand:
Package Ftp implements a FTP client as described in RFC 959.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        FTP client package for Go

License:        ISC
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 11:02:54 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.15.20210110git9aae4d1
- Bump to commit 9aae4d1511262659fe6de69ddbbb0b1871287e18

* Tue Jul 28 14:50:09 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.14.20200728git13949d3
- Bump to commit 13949d38913e55cc931e1472c0054df068a7c2ac

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 16:12:44 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.11.20191224git9284a88
- Bump to commit 9284a88df536a8e9d80846c718efe1b8fdd0dcc38b910ed30a1422a5b8658a8f165aeeda5e56b898

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 22:48:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20190528git9284a88
- Bump to commit 9284a88df536a8e9d80846c718efeeda5e56b898

* Mon Feb 25 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20190225git8019e67
- Bump to commit 8019e6774408f0ef24753bccba660ae36ff4038d

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git2403248
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.6.git2403248
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git2403248
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180628git2403248
- Bump to commit 2403248fa8cc9f7909862627aa7337f13f8e0bf1

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git4274679
- Update with the new Go packaging
- Upstream GIT revision 4274679

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170927git299b7ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170927git299b7ff
- Upstream GIT revision 299b7ff

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170721git769512c
- First package for Fedora
