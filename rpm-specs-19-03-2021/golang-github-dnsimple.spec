# Generated by go2rpm
%bcond_without check

# https://github.com/dnsimple/dnsimple-go
%global goipath         github.com/dnsimple/dnsimple-go
Version:                0.63.0

%gometa

%global common_description %{expand:
This library is a Go client you can use to interact with the DNSimple API v2.}

%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Go client for the DNSimple API v2

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)
BuildRequires:  golang(golang.org/x/oauth2)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 06:41:32 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.63.0-1
- Update to 0.63.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 00:32:16 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.23.0-2
- Update to new macros

* Wed Apr 17 2019 Carl George <carl@george.computer> - 0.23.0-1
- Initial package