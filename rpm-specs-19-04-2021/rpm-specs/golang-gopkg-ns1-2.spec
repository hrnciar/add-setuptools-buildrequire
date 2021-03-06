# Generated by go2rpm
%bcond_without check

# https://github.com/ns1/ns1-go
%global goipath         gopkg.in/ns1/ns1-go.v2
%global forgeurl        https://github.com/ns1/ns1-go
Version:                2.4.3

%gometa

%global common_description %{expand:
Golang API client for NS1.}

%global golicenses      LICENSE.txt
%global godocs          README.md _examples

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang API client for NS1

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/stretchr/testify/assert)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/mock)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 13:38:40 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.3-1
- Update to 2.4.3
- Close: rhbz#1868998

* Wed Aug 05 18:24:07 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 02:09:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190503git6c599e5
- Bump to commit 6c599e5e57901a8e58e1729f444de1edeb77bf97

* Mon Feb 11 2019 Carl George <carl@george.computer> - 0-0.1.20190211gita57b2a1
- Initial package
