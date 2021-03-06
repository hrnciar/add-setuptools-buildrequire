# Generated by go2rpm
%bcond_without check

# https://github.com/martini-contrib/render
%global goipath         github.com/martini-contrib/render
%global commit          ec18f8345a1181146728238980606fb1d6f40e8c

%gometa

%global common_description %{expand:
Martini middleware/handler for easily rendering serialized JSON, XML, and HTML
template responses.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Martini middleware/handler for easily rendering serialized template responses

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-martini/martini)
BuildRequires:  golang(github.com/oxtoacart/bpool)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 17:55:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190628gitec18f83
- Initial package
