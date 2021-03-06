# Generated by go2rpm 1
%bcond_without check

# https://github.com/calebcase/tmpfile
%global goipath         github.com/calebcase/tmpfile
Version:                1.0.2

%gometa

%global common_description %{expand:
This library attempts to bridge the gap between the what is provided in
ioutil.TempFile and the best practice of ensuring temporary files are always
deleted when the application exits.}

%global golicenses      LICENSE.golang LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Cross Platform Temporary Files

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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 16:49:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- Initial package
