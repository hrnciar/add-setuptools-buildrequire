# Generated by go2rpm
%bcond_without check

# https://github.com/smartystreets/gunit
%global goipath         github.com/smartystreets/gunit
Version:                1.4.2

%gometa

%global common_description %{expand:
xUnit-style test fixture adapter for Go test.}

%global golicenses      LICENSE.md
%global godocs          CONTRIBUTING.md README.md advanced_examples basic_examples

Name:           %{goname}
Release:        2%{?dist}
Summary:        xUnit-style test fixture adapter for Go test

License:        MIT
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
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 03:32:13 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.2-1
- Update to 1.4.2
- Close: rhbz#1872894

* Sun Aug 02 20:51:18 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.5-1
- Update to 1.3.5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 23:16:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Initial package
