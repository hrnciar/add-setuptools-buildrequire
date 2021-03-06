# Generated by go2rpm
%bcond_without check

# https://github.com/fortytw2/leaktest
%global goipath         github.com/fortytw2/leaktest
Version:                1.3.0

%gometa

%global common_description %{expand:
Goroutine Leak Detector.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Goroutine Leak Detector

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# Increase timeout for s390x
Patch0:         increase-timeout.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 20:45:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-2
- Update to new macros

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version
- Increase test timeout to work on s390x

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-5
- Do not run tests on aarch64 due to concurrency issues

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-1
- Update version

* Tue May 16 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-1
- Upstream now supports versions

* Wed Mar 15 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.2.git0db74e8
- Regenerate spec with new gofed version
- Remove empty conditionals
- Improve description

* Mon Nov 14 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.1.git0db74e8
- Initial package
