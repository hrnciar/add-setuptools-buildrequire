# Generated by go2rpm
# https://github.com/andy-kimball/arenaskl/issues/5
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/andy-kimball/arenaskl
%global goipath         github.com/andy-kimball/arenaskl
%global commit          f701008588b9f33126c0bc1c2a47587f2aafbbef

%gometa

%global common_description %{expand:
Fast, lock-free, arena-based Skiplist implementation in Go that supports
iteration in both directions.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Fast, lock-free, arena-based Skiplist implementation in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 16:44:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200723gitf701008
- Bump to commit f701008588b9f33126c0bc1c2a47587f2aafbbef

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 00:28:35 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20200127git1243160
- Bump to commit 1243160cabf69fa4db440655008901edb7b5df2b

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 18:20:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701git6bf06cf
- Initial package
