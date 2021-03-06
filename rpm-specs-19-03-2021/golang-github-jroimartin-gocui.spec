# Generated by go2rpm 1
%bcond_without check

# https://github.com/jroimartin/gocui
%global goipath         github.com/jroimartin/gocui
Version:                0.4.0

%gometa

%global common_description %{expand:
Minimalist Go package aimed at creating Console User Interfaces.

Features:

- Minimalist API.
- Views (the "windows" in the GUI) implement the interface io.ReadWriter.
- Support for overlapping views.
- The GUI can be modified at runtime (concurrent-safe).
- Global and view-level keybindings.
- Mouse support.
- Colored text.
- Customizable edition mode.
- Easy to build reusable widgets, complex layouts...
}

%global golicenses      LICENSE
%global godocs          _examples AUTHORS README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Minimalist Go package aimed at creating Console User Interfaces

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/nsf/termbox-go)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 02:52:41 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- Initial package

