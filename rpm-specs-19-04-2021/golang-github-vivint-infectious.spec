# Generated by go2rpm 1
%bcond_without check

# https://github.com/vivint/infectious
%global goipath         github.com/vivint/infectious
%global commit          25a574ae18a38b09019ce55e06ce2777e98ae9a0

%gometa

%global common_description %{expand:
Reed-Solomon forward error correcting library.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Reed-Solomon forward error correcting library

License:        BSD and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/cpu)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 14:32:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200702git25a574a
- Initial package