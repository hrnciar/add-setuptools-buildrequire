# Generated by go2rpm
%bcond_without check

# https://github.com/cryptix/wav
%global goipath         github.com/cryptix/wav
%global commit          8bdace674401f0bd3b63c65479b6a6ff1f9d5e44

%gometa

%global common_description %{expand:
Golang .wav reader and writer.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        0.9%{?dist}
Summary:        Golang .wav reader and writer

License:        GPLv2
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gonum.org/v1/plot)
BuildRequires:  golang(gonum.org/v1/plot/plotter)
BuildRequires:  golang(gonum.org/v1/plot/plotutil)
BuildRequires:  golang(gonum.org/v1/plot/vg)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/cheekybits/is)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 22:14:48 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20181109git8bdace6
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git8bdace6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0-0.3.20181109git8bdace6
- Update to 8bdace6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171018git7b3d650
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Dec 21 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.20171018git7b3d650
- Initial package build
