# Generated by go2rpm 1
%bcond_without check

# https://github.com/subosito/gotenv
%global goipath         github.com/subosito/gotenv
Version:                1.2.0

%gometa

%global common_description %{expand:
Load environment variables from `.env` or `io.Reader` in Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Load environment variables from `.env` or `io.Reader` in Go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 05:06:23 EST 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Initial package
