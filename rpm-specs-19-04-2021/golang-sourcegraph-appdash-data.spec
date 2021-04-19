# Generated by go2rpm
%bcond_without check

# https://github.com/sourcegraph/appdash-data
%global goipath         sourcegraph.com/sourcegraph/appdash-data
%global forgeurl        https://github.com/sourcegraph/appdash-data
%global commit          73f23eafcf67cad684fba328dd545a116ac273ff

%gometa

%global common_description %{expand:
This repository holds binary and external asset files (images, CSS, JS etc) that
Appdash relies on.}

%global golicenses      data/Caged/d3-tip/LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Binary and external asset files for Appdash

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 01:35:37 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701git73f23ea
- Initial package