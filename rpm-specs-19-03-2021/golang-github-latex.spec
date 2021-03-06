# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/go-latex/latex
%global goipath         github.com/go-latex/latex
%global commit          94de1316b515d8ef675da793a32a761b2af97c06

%gometa

%global common_description %{expand:
Go package for LaTeX.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md mtex/README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Go package for LaTeX

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fogleman/gg)
BuildRequires:  golang(github.com/phpdave11/gofpdf)
BuildRequires:  golang(golang.org/x/image/font)
BuildRequires:  golang(golang.org/x/image/font/gofont/gobold)
BuildRequires:  golang(golang.org/x/image/font/gofont/gobolditalic)
BuildRequires:  golang(golang.org/x/image/font/gofont/goitalic)
BuildRequires:  golang(golang.org/x/image/font/gofont/goregular)
BuildRequires:  golang(golang.org/x/image/font/opentype)
BuildRequires:  golang(golang.org/x/image/font/sfnt)
BuildRequires:  golang(golang.org/x/image/math/fixed)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/go-fonts/dejavu/dejavusans)
BuildRequires:  golang(github.com/go-fonts/dejavu/dejavusansoblique)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc AUTHORS CONTRIBUTORS README.md mtex/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 12:27:45 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20201222git94de131
- Initial package

