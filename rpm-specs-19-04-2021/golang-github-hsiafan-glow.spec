# Generated by go2rpm 1
# https://github.com/hsiafan/glow/issues/1
%bcond_with check

# https://github.com/hsiafan/glow
%global goipath         github.com/hsiafan/glow
Version:                1.6.0

%gometa

%global common_description %{expand:
Parsing helper for go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Parsing helper for go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/encoding/htmlindex)
BuildRequires:  golang(golang.org/x/text/encoding/unicode)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/text/encoding/charmap)
BuildRequires:  golang(golang.org/x/text/encoding/simplifiedchinese)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 17:21:56 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-1
- Initial package for Fedora
