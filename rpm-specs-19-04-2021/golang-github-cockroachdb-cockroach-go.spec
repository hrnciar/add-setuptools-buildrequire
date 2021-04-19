# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/cockroachdb/cockroach-go
%global goipath         github.com/cockroachdb/cockroach-go
Version:                2.1.0

%gometa

%global goname          golang-github-cockroachdb-cockroach-go
%global godevelname     golang-github-cockroachdb-cockroach-go-devel
%global goaltipaths     github.com/cockroachdb/cockroach-go/v2

%global common_description %{expand:
Testing helpers for cockroach clients.}

%global golicenses      LICENSE
%global godocs          README.md crdb/README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Testing helpers for cockroach clients.

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jackc/pgx/v4)
BuildRequires:  golang(github.com/jmoiron/sqlx)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(gorm.io/gorm)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 18:56:43 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Wed Sep 09 12:46:30 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 21:54:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20190626gite0a95df
- Bump to commit e0a95dfd547cc9c3ebaaba1a12c2afe4bf621ac5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git59c0560
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181114git59c0560
- Bump to commit 59c0560478b705bf9bd12f9252224a0fad7c87df
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170809gitc806b48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170809gitc806b48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170809gitc806b48
- First package for Fedora