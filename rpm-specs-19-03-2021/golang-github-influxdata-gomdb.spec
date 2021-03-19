# Generated by go2rpm 1
%bcond_without check

# https://github.com/influxdata/gomdb
%global goipath         github.com/influxdata/gomdb
%global commit          29fe330c5ab33c4e48470bd4b980bf522471190a

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-influxdb-gomdb-devel < 0-0.18
}

%global common_description %{expand:
Go wrapper for LMDB - OpenLDAP Lightning Memory-Mapped Database.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.19%{?dist}
Summary:        Go wrapper for LMDB

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
# .: https://github.com/szferi/gomdb/issues/40
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 11:15:44 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.18.20200909git29fe330
- Renamed to golang-github-influxdata-gomdb

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 18:48:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.14.20140925git29fe330
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.12.git29fe330
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git29fe330
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git29fe330
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git29fe330
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git29fe330
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git29fe330
- First package for Fedora
