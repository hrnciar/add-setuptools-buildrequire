%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-deriving-yojson
%global upname  ppx_deriving_yojson

Name:           ocaml-%{srcname}
Version:        3.6.1
Release:        4%{?dist}
Summary:        JSON codec generator for OCaml

License:        MIT
URL:            https://github.com/ocaml-ppx/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-ppx-deriving-devel >= 5.1
BuildRequires:  ocaml-ppxlib-devel >= 0.14.0
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-yojson-devel >= 1.6.0

%description
Deriving_Yojson is a ppx_deriving plugin that generates JSON serializers
and deserializers that use the Yojson library from an OCaml type
definition.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-biniou-devel%{?_isa}
Requires:       ocaml-easy-format-devel%{?_isa}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{upname}-%{version} -p1

# Work around name change for ounit
sed -i 's/oUnit/ounit2/g' src_test/dune

%build
dune build %{?_smp_mflags}
dune build %{?_smp_mflags} @doc

%install
dune install --destdir=%{buildroot}

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod a+x {} \+
%endif

# Help the debuginfo generator find the source files
ln -s ../../src/ppx_deriving_yojson.cppo.ml _build/default

%check
dune runtest

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/runtime/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/%{upname}.cma
%{_libdir}/ocaml/%{upname}/%{upname}.cmi
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cma
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.cmxs
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.a
%{_libdir}/ocaml/%{upname}/%{upname}.cmx
%{_libdir}/ocaml/%{upname}/%{upname}.cmxa
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.a
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmx
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmxa
%endif
%{_libdir}/ocaml/%{upname}/%{upname}.cmt
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmt
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmti
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.mli

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/

%changelog
* Mon Mar  1 23:31:09 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 3.6.1-4
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-3
- Rebuild for ocaml-ppx-deriving 5.2.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 3.6.1-1
- Version 3.6.1

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.3-4
- Bump release and rebuild.

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.3-3
- OCaml 4.11.1 rebuild

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.3-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 3.5.3-1
- Version 3.5.3
- Drop upstreamed ocaml-411.patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-2
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 10 2020 Jerry James <loganjerry@gmail.com> - 3.5.2-1
- Initial RPM
