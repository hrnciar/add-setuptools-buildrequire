# Generated by go2rpm 1.1
%bcond_without check

# https://github.com/muesli/termenv
%global goipath         github.com/muesli/termenv
Version:                0.7.4

%gometa

%global common_description %{expand:
Advanced ANSI style & color support for your terminal applications.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Advanced ANSI style & color support for your terminal applications

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/lucasb-eyer/go-colorful)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(golang.org/x/sys/unix)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 18:25:20 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Tue Sep 29 20:38:35 CDT 2020 Joe Doss <joe@solidadmin.com> - 0.7.2-1
- Initial package