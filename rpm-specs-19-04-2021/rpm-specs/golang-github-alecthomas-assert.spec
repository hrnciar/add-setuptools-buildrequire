# Generated by go2rpm
%bcond_without check

# https://github.com/alecthomas/assert
%global goipath         github.com/alecthomas/assert
%global commit          405dbfeb8e38effee6e723317226e93fff912d06

%gometa

%global common_description %{expand:
This is a fork of stretchr's assertion library that does two things:

 - It makes spotting differences in equality much easier. It uses repr and
   diffmatchpatch to display structural differences in colour.
 - Aborts tests on first assertion failure (the same behaviour as
   stretchr/testify/require).}

%global golicenses      LICENCE.txt
%global godocs          _example README.md

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        Fork of stretchr/testify/require that provides much nicer diffs

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/colour)
BuildRequires:  golang(github.com/alecthomas/repr)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 19:49:53 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20181111git405dbfe
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git405dbfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111git405dbfe
- Bump to commit 405dbfeb8e38effee6e723317226e93fff912d06
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git561411b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git561411b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git561411b
- Initial package build