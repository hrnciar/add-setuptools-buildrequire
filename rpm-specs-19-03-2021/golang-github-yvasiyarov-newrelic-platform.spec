# Generated by go2rpm
%bcond_without check

# https://github.com/yvasiyarov/newrelic_platform_go
%global goipath         github.com/yvasiyarov/newrelic_platform_go
%global commit          9c099fbc30e90de5bb5c5f94aa5fd08f2daeaacd

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-yvasiyarov-newrelic_platform_go-devel < 0-0.9
}

%global common_description %{expand:
This package provide very simple interface to NewRelic Platform.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        0.14%{?dist}
Summary:        Newrelic Platform SDK for Go

# Upstream license specification: BSD-2-Clause
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.10.20190626git9c099fb
- Add Obsoletes for old name

* Thu May 02 15:23:23 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20190626git9c099fb
- Bump to commit 9c099fbc30e90de5bb5c5f94aa5fd08f2daeaacd

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitb21fdbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitb21fdbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitb21fdbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitb21fdbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitb21fdbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitb21fdbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitb21fdbd
- https://fedoraproject.org/wiki/Changes/golang1.7

* Fri Mar 04 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitb21fdbd
- First package for Fedora
  resolves: #1314979
