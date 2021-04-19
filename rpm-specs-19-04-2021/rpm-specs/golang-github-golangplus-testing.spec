# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap

# https://github.com/golangplus/testing
%global goipath         github.com/golangplus/testing
Version:                1.0.0

%gometa

%global common_description %{expand:
Package Testingp is a plus to standard "testing" package..}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Plus to the standard testing package

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golangplus/fmt)

%if %{without bootstrap}
%if %{with check}
# Tests
BuildRequires:  golang(github.com/golangplus/bytes)
%endif
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 21:04:56 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 22:18:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190629gitaf21d9c
- Initial package
