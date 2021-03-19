# Generated by go2rpm 1
%bcond_without check

# https://github.com/gobuffalo/logger
%global goipath         github.com/gobuffalo/logger
Version:                1.0.3

%gometa

%global common_description %{expand:
The logger.Logger interface is used throughout Buffalo apps, and other systems,
to log a whole manner of things.}

%global golicenses      LICENSE
%global godocs          README.md SHOULDERS.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Common logging interface for the Buffalo ecosystem

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 11:56:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Initial package
