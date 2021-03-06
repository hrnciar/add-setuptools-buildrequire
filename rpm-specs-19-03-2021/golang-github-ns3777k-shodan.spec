# Generated by go2rpm 1
%bcond_without check

# https://github.com/ns3777k/go-shodan
%global goipath         github.com/ns3777k/go-shodan
Version:                4.2.0

%gometa

%global goaltipaths     github.com/ns3777k/go-shodan/v4

%global common_description %{expand:
A Shodan client written in Go.}

Name:           %{goname}
Release:        4%{?dist}
Summary:        Shodan API client

License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 12:42:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.2.0-3
- Add alternative import path

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.0-1
- Initial package

