# Generated by go2rpm
%bcond_without check

# https://github.com/golang/freetype
%global goipath         github.com/golang/freetype
%global commit          e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-BurntSushi-freetype-go-devel < 0-0.8
}

%global goaltipaths     github.com/BurntSushi/freetype-go

%global common_description %{expand:
The Freetype font rasterizer in the Go programming language.}

%global golicenses      LICENSE licenses/gpl.txt licenses/ftl.txt
%global godocs          example AUTHORS CONTRIBUTORS README

Name:           %{goname}
Version:        0
Release:        0.13%{?dist}
Summary:        Freetype font rasterizer in the Go programming language

License:        GPLv2 or FTL
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/image/font)
BuildRequires:  golang(golang.org/x/image/math/fixed)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.9.20190701gite2365df
- Add Obsoletes for old name

* Thu May 16 23:40:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20190701gite2365df
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gite2365df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 mosquito <sensor.wen@gmail.com> - 0-0.6.20181119gite2365df
- Fix go import path

* Wed Nov 14 2018 mosquito <sensor.wen@gmail.com> - 0-0.5.20181114gite2365df
- Change upstream to github.com/golang/freetype

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181113gitb763ddb
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitb763ddb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitb763ddb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitb763ddb
- Initial package build
