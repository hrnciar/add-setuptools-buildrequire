# Generated by go2rpm 1
%bcond_without check

# https://github.com/benlaurie/gds-registers
%global goipath         github.com/benlaurie/gds-registers
%global commit          6355673a9585189fadee61b5662b87b7d87b3716

%gometa

%global common_description %{expand:
Go API for GDS registers (https://registers.cloudapps.digital/).}

%global golicenses      LICENSE

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go API for GDS registers

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 03 18:10:16 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200303git6355673
- Initial package
