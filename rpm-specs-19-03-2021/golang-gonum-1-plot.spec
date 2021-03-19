# Generated by go2rpm
%bcond_without check

# https://github.com/gonum/plot
%global goipath         gonum.org/v1/plot
%global forgeurl        https://github.com/gonum/plot
Version:                0.8.1
%global commit          a02d161f61a31cb69eb421e6c8063ccc8986a4b9

%gometa

%global common_description %{expand:
Plot provides an API for building and drawing plots in Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Package for plotting and visualizing dataZ

License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gioui.org/app/headless)
BuildRequires:  golang(gioui.org/f32)
BuildRequires:  golang(gioui.org/font/gofont)
BuildRequires:  golang(gioui.org/font/opentype)
BuildRequires:  golang(gioui.org/layout)
BuildRequires:  golang(gioui.org/op)
BuildRequires:  golang(gioui.org/op/clip)
BuildRequires:  golang(gioui.org/op/paint)
BuildRequires:  golang(gioui.org/text)
BuildRequires:  golang(gioui.org/unit)
BuildRequires:  golang(gioui.org/widget/material)
BuildRequires:  golang(github.com/ajstarks/svgo)
BuildRequires:  golang(github.com/fogleman/gg)
BuildRequires:  golang(github.com/go-latex/latex/drawtex)
BuildRequires:  golang(github.com/go-latex/latex/font/ttf)
BuildRequires:  golang(github.com/go-latex/latex/mtex)
BuildRequires:  golang(github.com/go-latex/latex/tex)
BuildRequires:  golang(github.com/phpdave11/gofpdf)
BuildRequires:  golang(golang.org/x/image/font)
BuildRequires:  golang(golang.org/x/image/font/opentype)
BuildRequires:  golang(golang.org/x/image/font/sfnt)
BuildRequires:  golang(golang.org/x/image/math/fixed)
BuildRequires:  golang(golang.org/x/image/tiff)

%if %{with check}
# Tests
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  golang(golang.org/x/exp/rand)
BuildRequires:  golang(gonum.org/v1/gonum/floats/scalar)
BuildRequires:  golang(gonum.org/v1/gonum/mat)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d. -d palette	-d palette/moreland -d plotter -d vg/vggio
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 02:40:38 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.1-2.20210125gita02d161
- Bump to commit a02d161f61a31cb69eb421e6c8063ccc8986a4b9

* Tue Dec 22 07:20:45 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.1-1.20201223gitf888cdb
- Update to 0.8.1, commit f888cdb60200a6291af8763d83eda6c866a6f53d6
- Close: rhbz#1875875

* Wed Aug 05 14:35:18 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 22:30:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190703gite2840ee
- Initial package
