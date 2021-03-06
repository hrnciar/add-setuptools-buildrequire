# Generated by go2rpm
%bcond_without check

# https://github.com/anacrolix/envpprof
%global goipath         github.com/anacrolix/envpprof
Version:                1.1.1

%gometa

%global common_description %{expand:
Allows run time configuration of Go's pprof features and default HTTP mux using
environment variables.}

%global golicenses      LICENSE

Name:           %{goname}
Release:        3%{?dist}
Summary:        Run time configuration of Go's pprof features

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/anacrolix/log)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 15:02:09 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sun Jan 26 23:14:24 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 00:00:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new macros

* Tue Mar 26 18:07:19 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> -1.0.0-1
- Release 1.0.0 (#1692635)

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190307git323002c
- First package for Fedora
