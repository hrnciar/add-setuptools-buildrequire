%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

%global srcname ptmap

Name:           ocaml-%{srcname}
Version:        2.0.5
Release:        3%{?dist}
Summary:        Maps over integers implemented as Patricia trees

License:        LGPLv2 with exceptions
URL:            https://github.com/backtracking/ptmap
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tbz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.0.0
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif
BuildRequires:  ocaml-seq-devel

%description
OCaml implementation of an efficient maps over integers,
from a paper by Chris Okasaki.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-seq-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Fedora does not have stdlib-shims, which is only needed for older versions
# of OCaml.  Remove references to it.
sed -i 's/ stdlib-shims//' dune
sed -i '/stdlib-shims/d' ptmap.opam


%build
dune build %{?_smp_mflags} --display=verbose
%if %{with doc}
dune build %{?_smp_mflags} @doc
%endif


%install
dune install --destdir=%{buildroot}

%if %{with doc}
# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete
%endif

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod a+x {} \+
%endif


%check
dune runtest


%files
%doc CHANGES.md README.md
%license COPYING LICENSE
%{_libdir}/ocaml/ptmap
%{_libdir}/ocaml/ptmap/META
%{_libdir}/ocaml/ptmap/*.cma
%{_libdir}/ocaml/ptmap/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/ptmap/*.cmxs
%endif


%files devel
%if %{with doc}
%doc _build/default/_doc/*
%endif
%{_libdir}/ocaml/ptmap/dune-package
%{_libdir}/ocaml/ptmap/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/ptmap/*.a
%{_libdir}/ocaml/ptmap/*.cmxa
%{_libdir}/ocaml/ptmap/*.cmx
%endif
%{_libdir}/ocaml/ptmap/*.cmt
%{_libdir}/ocaml/ptmap/*.cmti
%{_libdir}/ocaml/ptmap/*.mli


%changelog
* Mon Mar  1 16:57:55 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2.0.5-3
- OCaml 4.12.0 build
- Make ocaml-odoc dependency conditional.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Jerry James <loganjerry@gmail.com> - 2.0.5-1
- Version 2.0.5
- License is LGPLv2, not LGPLv2+
- Drop upstreamed filter_map patch
- Building and testing are now done with dune
- Documentation is now generated with odoc

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-15
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-14
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-10
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-8
- OCaml 4.10.0 final.

* Wed Feb 19 2020 Jerry James <loganjerry@gmail.com> - 2.0.4-7
- Rebuild for ocaml-qcheck 0.13.
- Remove unnecessary ounit BR.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Andy Li <andy@onthewings.net> - 2.0.4-5
- Rebuild against the latest ocaml package.

* Fri Aug 09 2019 Andy Li <andy@onthewings.net> - 2.0.4-4
- Disabled testing due to obuild incompatible with recent qcheck changes.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Andy Li <andy@onthewings.net> - 2.0.4-1
- New upstream version (RHBZ#1610325).
- Fix OCaml 4.07 compatibility (RHBZ#1605283).
- Remove patch, which was merged in upstream.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Andy Li <andy@onthewings.net> - 2.0.3-1
- Initial RPM release.
