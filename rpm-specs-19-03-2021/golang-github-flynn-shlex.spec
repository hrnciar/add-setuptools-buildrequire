# Generated by go2rpm
%bcond_without check

# https://github.com/flynn/go-shlex
%global goipath         github.com/flynn/go-shlex
%global commit          3f9db97f856818214da2e1057f8ad84803971cff

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-flynn-go-shlex-devel < 0-0.5
Obsoletes:      golang-github-flynn-go-shlex-unit-test-devel < 0-0.5
}

%global common_description %{expand:
Go-shlex is a simple lexer for Go that supports shell-style quoting, commenting,
and escaping.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        Simple lexer for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.6.20150515git3f9db97
- Add Obsoletes for old names

* Sun Apr 28 14:58:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20150515git3f9db97
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20150515git3f9db97
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20150515git3f9db97
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20150515git3f9db97
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Clément David <c.david86@gmail.com> - 0-0.1.20150515git3f9db97
- First package for Fedora
