# Generated by go2rpm
%bcond_without check

# https://github.com/ijc/Gotty
%global goipath         github.com/ijc/Gotty
%global commit          a8b993ba6abdb0e0c12b0125c603323a71c7790c

%gometa

%global common_description %{expand:
Gotty is a library written in Go that determines and reads termcap database
files to produce an interface for interacting with the capabilities of a
terminal.}

%global golicenses      LICENSE
%global godocs          README TODO

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Library that provides interpretation and loading of Termcap database files

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 01:05:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702gita8b993b
- Initial package
