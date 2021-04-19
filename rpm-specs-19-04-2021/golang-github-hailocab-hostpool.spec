# Generated by go2rpm
%bcond_without check

# https://github.com/hailocab/go-hostpool
%global goipath         github.com/hailocab/go-hostpool
%global commit          e80d13ce29ede4452c43dea11e79b9bc8a15b478

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-hailocab-go-hostpool-devel < 0-0.5
Obsoletes:      golang-github-hailocab-go-hostpool-unit-test-devel < 0-0.5
}

%global common_description %{expand:
A Go package to intelligently and flexibly pool among multiple hosts from your
Go application. Host selection can operate in round robin or epsilon greedy
mode, and unresponsive hosts are avoided.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.11%{?dist}
Summary:        Intelligently and flexibly pool among multiple hosts from your go application

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Fix import path
Patch0:         go-hostpool-test.patch

%if %{with check}
# Tests
BuildRequires:  golang(github.com/bmizerany/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.6.20160125gite80d13c
- Add Obsoletes for old name

* Tue Apr 30 02:12:26 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20160125gite80d13c
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20160125gite80d13c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20160125gite80d13c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160125gite80d13c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Ed Marshall <esm@logic.net> - 0-0.1.20160125gite80d13c
- First package for Fedora