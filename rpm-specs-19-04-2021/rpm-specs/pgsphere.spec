Summary: Spherical data types, functions, and operators for PostgreSQL
Name: pgsphere
Version: 1.1.1
Release: 31%{?dist}
License: BSD

# https://github.com/akorotkov/pgsphere/issues/15
Source0: http://pgfoundry.org/frs/download.php/2558/%{name}-%{version}.tar.gz
Patch0: pgsphere-pgsl93.patch
# The changes are upstream already, fixed via a number of different commits.
# Most of the changes seem to be in this one 2d97f1652afb4ef5405e0e1e5988c.
Patch1: pgsphere-pgsl11.patch
Patch2: pgsphere-pgsl12.patch
URL: http://pgfoundry.org/projects/pgsphere

BuildRequires: make
BuildRequires: gcc
BuildRequires: postgresql-server-devel
BuildRequires: clang-devel
BuildRequires: llvm-devel
%{?postgresql_module_requires}

%description
pgSphere is a server side module for PostgreSQL. It contains methods for 
working with spherical coordinates and objects. It also supports indexing of 
spherical objects.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build USE_PGXS=1 PG_CONFIG=%_bindir/pg_server_config

%install
install -d %{buildroot}%{_libdir}/pgsql/
install -d %{buildroot}%{_datadir}/%{name}

install -m 755 pg_sphere.so %{buildroot}%{_libdir}/pgsql/pg_sphere.so
install -m 644 pg_sphere.sql %{buildroot}%{_datadir}/%{name}/

%ldconfig_scriptlets

%files
%doc README.pg_sphere
%license COPYRIGHT.pg_sphere
%{_datadir}/%{name}
%{_libdir}/pgsql/pg_sphere.so

%changelog
* Thu Jan 14 2021 Patrik Novotný <panovotn@redhat.com> - 1.1.1-31
- Add compatibility for llvm enabled postgresql

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-28
- Rebuild for PostgreSQL 12 (rhbz#1813525)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Petr Kubat <pkubat@redhat.com> - 1.1.1-24
- rebuild for PostgreSQL 11

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-23
- rebuild against postgresql-server-devel (rhbz#1618698)

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.1.1-22
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-19
- rebuild for PostgreSQL 10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-15
- bump: build in rawhide done too early

* Mon Oct 10 2016 Petr Kubat <pkubat@redhat.com> - 1.1.1-14
- Rebuild for PostgreSQL 9.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Pavel Kajaba <pkajaba@redhat.com> - 1.1.1-12
- Rebuild for PostgreSQL 9.5 (rhbz#1296584)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-10
- rebuild for PostgreSQL 9.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-7
- Patch to build with psql 9.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-2
- Fix source url
- Directory in datadir included

* Tue Jan 11 2011 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-1
- Initial spec file
