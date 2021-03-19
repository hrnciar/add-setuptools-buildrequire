%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global libname easy-format

Name:           ocaml-%{libname}
Version:        1.3.2
Release:        14%{?dist}
Summary:        High-level and functional interface to the Format module

License:        BSD
URL:            https://github.com/ocaml-community/%{libname}
Source0:        %{url}/releases/download/%{version}/%{libname}-%{version}.tbz
# Convert from the deprecated tag functions to the stag functions
Patch0:         %{name}-stag.patch

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
This module offers a high-level and functional interface to the Format
module of the OCaml standard library. It is a pretty-printing
facility, i.e. it takes as input some code represented as a tree and
formats this code into the most visually satisfying result, breaking
and indenting lines of code where appropriate.

Input data must be first modeled and converted into a tree using 3
kinds of nodes:

    atoms
    lists
    labeled nodes

Atoms represent any text that is guaranteed to be printed as-is. Lists
can model any sequence of items such as arrays of data or lists of
definitions that are labeled with something like "int main", "let x
=" or "x:".


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -p0 -n %{libname}-%{version}


%build
dune build %{?_smp_mflags}


%install
DESTDIR=%{buildroot} dune install

# Fix permissions
chmod 755 %{buildroot}%{_libdir}/ocaml/%{libname}/*.cmxs

# Delete files we do not want or that are in the wrong place
rm -f %{buildroot}%{_libdir}/ocaml/%{libname}/*.ml
rm -fr %{buildroot}%{_prefix}/doc


%check
dune runtest


%files
%license LICENSE
%doc README.md
%dir %{_libdir}/ocaml/%{libname}/
%{_libdir}/ocaml/%{libname}/META
%{_libdir}/ocaml/%{libname}/*.cmi
%{_libdir}/ocaml/%{libname}/*.cmt
%{_libdir}/ocaml/%{libname}/*.cmti
%{_libdir}/ocaml/%{libname}/*.cmxs


%files devel
%doc CHANGES.md
%{_libdir}/ocaml/%{libname}/dune-package
%{_libdir}/ocaml/%{libname}/opam
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cma
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.cmxa
%endif
%{_libdir}/ocaml/%{libname}/*.mli


%changelog
* Mon Mar  1 12:17:35 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-14
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-12
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-11
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-8
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-7
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-3
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-2
- OCaml 4.09.0 (final) rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Update to 1.3.2 (bz 1742464)
- New URLs

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-2.20190628.76420c5
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 1.3.1-1.20190628.76420c5
- Update to 1.3.1 plus fixes from git (bz 1446352)
- Add -stag patch

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-32
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-30
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-29
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-26
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-25
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-23
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-22
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-19
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-18
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.0.2-16
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-15
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-13
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-12
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-11
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-10
- ocaml-4.02.1 rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-9
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-8
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-6
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-5
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-3
- Remove ocaml_arches (see rhbz#1087794).

* Tue Jan 21 2014 Michel Salim <salimma@fedoraproject.org> - 1.0.2-2
- Incorporate review feedback

* Mon Jan 20 2014 Michel Salim <salimma@fedoraproject.org> - 1.0.2-1
- Initial package
