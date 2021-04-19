# Generated by go2rpm
# Dead upstream
%ifnarch aarch64 ppc64le s390x
%bcond_without check
%endif

# https://github.com/BurntSushi/graphics-go
%global goipath         github.com/BurntSushi/graphics-go
%global commit          b43f31a4a96688fba0b612e25e22648b9267e498

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-BurntSushi-graphics-go-devel < 0-0.7
}

%global common_description %{expand:
This is a Graphics library for the Go programming language.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README

Name:           %{goname}
Version:        0
Release:        0.12%{?dist}
Summary:        Graphics library for the Go programming language

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.8.20190702gitb43f31a
- Add Obsoletes for old name

* Thu May 23 22:39:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7.20190702gitb43f31a
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitb43f31a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20181113gitb43f31a
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitb43f31a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitb43f31a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 mosquito <sensor.wen@gmail.com> - 0-0.2.gitb43f31a
- ignore test error for ppc64le

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitb43f31a
- Initial package build