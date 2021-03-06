# Generated by go2rpm
%bcond_without check

# https://github.com/go-tomb/tomb
%global goipath         gopkg.in/tomb.v1
%global forgeurl        https://github.com/go-tomb/tomb
%global commit          dd632973f1e7218eb1089048e0798ec9ae7dceb8

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-go-tomb-tomb-devel < 0-17
}

%global goaltipaths     gopkg.in/v1/tomb

%global common_description %{expand:
The Tomb package handles clean goroutine tracking and termination.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        1
Release:        6%{?dist}
Summary:        Clean goroutine termination in the Go language

# Upstream license specification: BSD-3-Clause
License:        BSD
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1-2.20190623gitdd63297
- Add Obsoletes for old name

* Tue Apr 23 23:27:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1-1.20190623gitdd63297
- Initial package
