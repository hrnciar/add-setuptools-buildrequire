# Generated by go2rpm
%bcond_without check

# https://github.com/golang/arch
%global goipath         golang.org/x/arch
%global forgeurl        https://github.com/golang/arch
%global commit          cfa462d59626e1fd66d29ac63d6c28b4cc7f0b29

%gometa

%global common_description %{expand:
This package holds machine architecture information used by the Go toolchain.}

%global golicenses      LICENSE PATENTS
%global godocs          AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

Name:           %{goname}
Version:        0
Release:        0.9%{?dist}
Summary:        Machine architecture information used by the Go toolchain

# Upstream license specification: BSD-3-Clause
# BSD. main library
# MIT: x86/x86asm/testdata/libmach8db.c
# ASL 2.0: x86/x86avxgen/testdata/xedpath/*.txt
License:        BSD and MIT and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(rsc.io/pdf)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 01:33:56 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20210123gitcfa462d
- Bump to commit cfa462d59626e1fd66d29ac63d6c28b4cc7f0b29

* Fri Aug 07 18:20:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7.20200807gitf7c7858
- Bump to commit f7c78586839d44dc82dc2187bb3cd956bbc4446a

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 18:21:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20190523git788fe5f
- Bump to commit 788fe5ffcd8c07da9e57a7f3b134c13864be60be

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitb19384d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20181126gitb19384d
- First package for Fedora