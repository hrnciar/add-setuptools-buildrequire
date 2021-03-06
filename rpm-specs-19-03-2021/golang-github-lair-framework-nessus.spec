# Generated by go2rpm 1
%bcond_without check

# https://github.com/lair-framework/go-nessus
%global goipath         github.com/lair-framework/go-nessus
%global commit          585a96dc18959b5f06044ea405e3774030a1e1d3

%gometa

%global common_description %{expand:
Nessus XML parsing library for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Nessus XML parsing library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200410git585a96d
- Initial package

