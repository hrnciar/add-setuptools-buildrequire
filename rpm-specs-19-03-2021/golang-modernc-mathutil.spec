# Generated by go2rpm
%ifnarch ppc64le s390x
%bcond_without check
%endif

# https://gitlab.com/cznic/mathutil
%global goipath         modernc.org/mathutil
%global forgeurl        https://gitlab.com/cznic/mathutil
Version:                1.2.1
%global commit          c6aa83b20bd1ca367f387445176a812dd51e21b2
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Utilities supplemental to the Go standard "rand" and "math" packages.}

%global golicenses      LICENSE LICENSE-mersenne
%global godocs          example AUTHORS CONTRIBUTORS AUTHORS-mersenne\\\
                        CONTRIBUTORS-mersenne README-mersenne

Name:           %{goname}
Release:        2%{?dist}
Summary:        Utilities supplemental to the Go standard "rand" and "math" packages

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/remyoudompheng/bigfft)

%description
%{common_description}

%gopkg

%prep
%goprep
mv mersenne/LICENSE LICENSE-mersenne
mv mersenne/AUTHORS AUTHORS-mersenne
mv mersenne/CONTRIBUTORS CONTRIBUTORS-mersenne
mv mersenne/README README-mersenne

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 12:46:23 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.1-1
- Update to 1.2.1
- Close: rhbz#1909403

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 15:20:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package
