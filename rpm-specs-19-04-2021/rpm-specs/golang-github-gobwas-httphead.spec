# Generated by go2rpm 1
%bcond_without check

# https://github.com/gobwas/httphead
%global goipath         github.com/gobwas/httphead
Version:                0.1.0

%gometa

%global common_description %{expand:
Tiny HTTP header value parsing library in go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        HTTP header value parsing library

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 18:19:41 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Update to 0.1.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200407git2c6c146
- Initial package
