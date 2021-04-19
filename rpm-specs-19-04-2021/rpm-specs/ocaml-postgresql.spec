%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Name:           ocaml-postgresql
Version:        4.0.1
Release:        34%{?dist}
Summary:        OCaml library for accessing PostgreSQL databases

License:        LGPLv2+ with exceptions
URL:            https://github.com/mmottl/postgresql-ocaml
Source0:        https://github.com/mmottl/postgresql-ocaml/releases/download/v%{version}/postgresql-ocaml-%{version}.tar.gz

BuildRequires: make
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  libpq-devel
BuildRequires:  chrpath
BuildRequires:  rpm >= 4.4.2.3-2

%global __ocaml_provides_opts -i Condition -i Event -i Mutex -i Thread -i ThreadUnix


%description
This OCaml-library provides an interface to PostgreSQL, an efficient
and reliable, open source, relational database.  Almost all
functionality available through the C-API (libpq) is replicated in a
type-safe way.  This library uses objects for representing database
connections and results of queries.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n postgresql-ocaml-%{version}
ocaml setup.ml -configure --prefix %{_prefix} --destdir $RPM_BUILD_ROOT


%build
make

chrpath --delete _build/lib/dll*.so


%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install


%files
%doc COPYING.txt
%{_libdir}/ocaml/postgresql
%if %opt
%exclude %{_libdir}/ocaml/postgresql/*.a
%exclude %{_libdir}/ocaml/postgresql/*.cmxa
%endif
%exclude %{_libdir}/ocaml/postgresql/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc COPYING.txt AUTHORS.txt CHANGES.txt README.md examples
%if %opt
%{_libdir}/ocaml/postgresql/*.a
%{_libdir}/ocaml/postgresql/*.cmxa
%endif
%{_libdir}/ocaml/postgresql/*.mli


%changelog
* Mon Mar  1 10:09:49 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-34
- OCaml 4.12.0 build

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 4.0.1-33
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-31
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-30
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-28
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-27
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-26
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-25
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-24
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-22
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-21
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-20
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-19
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-18
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-16
- OCaml 4.08.0 (final) rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-15
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-12
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-11
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-9
- OCaml 4.06.0 rebuild.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-8
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-5
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 4.0.1-2
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-1
- New upstream version 4.0.1.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-11
- OCaml 4.02.3 rebuild.

* Mon Jul 27 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-10
- Remove ExcludeArch since bytecode build should now work.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-9
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-8
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-6
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-5
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-4
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-2
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-1
- New upstream version 2.0.7.
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-1
- New upstream version 2.0.4.
- OCaml 4.01.0 rebuild.
- Enable debuginfo.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-1
- New upstream version 2.0.2.
- Fix home page and source URL.
- Clean up spec file.
- Fix build.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 1.18.0-2
- Rebuild for OCaml 4.00.0.

* Thu Jan 12 2012 Richard W.M. Jones <rjones@redhat.com> - 1.18.0-1
- New upstream version 1.18.0.
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 1.14.0-1
- New upstream version 1.14.0.

* Mon Jan 11 2010 Richard W.M. Jones <rjones@redhat.com> - 1.12.3-3
- Ignore bogus thread module Provides which the automatic dependency
  generator was giving us.
- Replace %%define with %%global.
- Use upstream RPM 4.8 OCaml internal dependency generator.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.12.3-2
- Rebuild for OCaml 3.11.2.

* Fri Oct 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.12.3-1
- New upstream version 1.12.3.
- This contains a SECURITY fix for:
  https://bugzilla.redhat.com/show_bug.cgi?id=529325
  CVE-2009-2943 ocaml-postgresql: Missing escape function (DSA-1909-1)
  HOWEVER you are not protected until you change your code to
  use the new connection#escape_string method.

* Sun Oct  4 2009 Richard W.M. Jones <rjones@redhat.com> - 1.12.1-1
- New upstream version 1.12.1.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.11.1-2
- Rebuild for OCaml 3.11.1
- New upstream version 1.11.1.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Mar 10 2009 Richard W.M. Jones <rjones@redhat.com> - 1.10.3-1
- New upstream version 1.10.3.
- Fix URL.
- Upstream Source URLs have all changed.

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-6
- Fix typo in summary (rhbz#487632).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-3
- Rebuild for OCaml 3.11.0+rc1.

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-2
- Rebuild.

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-1
- New upstream release 1.9.2.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-5
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-4
- Rebuild for OCaml 3.10.2

* Fri Apr 18 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-3
- Can't spell.  prm -> rpm.

* Fri Apr 18 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-2
- Rebuild against updated RPM (see bug 443114).

* Fri Apr  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-1
- New upstream version 1.8.2.

* Tue Mar  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-3
- Rebuild for ppc64.

* Mon Mar  3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-2
- Only include LICENSE doc in main package.
- Include extra documentation and examples in devel package.
- Check it builds in mock.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-1
- Initial RPM release.
