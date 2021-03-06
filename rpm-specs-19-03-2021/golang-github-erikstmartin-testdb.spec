# Generated by go2rpm
%bcond_without check

# https://github.com/erikstmartin/go-testdb
%global goipath         github.com/erikstmartin/go-testdb
%global commit          8d10e4a1bae52cd8b81ffdec3445890d6dccab3d

%gometa

%global common_description %{expand:
Framework for stubbing responses from Go's driver.Driver interface.

This can be used to sit in place of your sql.Db so that you can stub responses
for sql calls, and remove database dependencies for your test suite.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Framework for stubbing responses from Go's driver.Driver interface

# Upstream license specification: BSD-2-Clause
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 19:24:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190630git8d10e4a
- Initial package
