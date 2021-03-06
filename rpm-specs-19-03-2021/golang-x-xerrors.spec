# Generated by go2rpm 1
%bcond_without check

# https://github.com/golang/xerrors
%global goipath         golang.org/x/xerrors
%global forgeurl        https://github.com/golang/xerrors
%global commit          5ec99f83aff198f5fbd629d6c8d8eb38a04218ca

%gometa

%global common_description %{expand:
This package holds the transition packages for the new Go 1.13 error values.
See golang.org/design/29934-error-values.}

%global golicenses      LICENSE PATENTS
%global godocs          README

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Transition packages for the new Go 1.13 error values

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 21:40:52 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20200807git5ec99f8
- Bump to commit 5ec99f83aff198f5fbd629d6c8d8eb38a04218ca

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20200218git9bdfabe
- Update to 9bdfabe68543c54f90421aeb9a60ef8061b5b544

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190917gita985d34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 15:42:55 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190917gita985d34
- Initial package
