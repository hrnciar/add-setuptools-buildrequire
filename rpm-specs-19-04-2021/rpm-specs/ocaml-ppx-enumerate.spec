%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

%global srcname ppx-enumerate
%global upname  ppx_enumerate

Name:           ocaml-%{srcname}
Version:        0.14.0
Release:        8%{?dist}
Summary:        Generate a list containing all values of a finite type

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-ppxlib-devel >= 0.11.0
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif

%description
Ppx_enumerate is a ppx rewriter which generates a definition for the
list of all values of a type (for a type which has only finitely many
values).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{upname}-%{version}

%build
dune build %{?_smp_mflags}
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
%license LICENSE.md
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/runtime-lib/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%{_libdir}/ocaml/%{upname}/runtime-lib/*.cma
%{_libdir}/ocaml/%{upname}/runtime-lib/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%{_libdir}/ocaml/%{upname}/runtime-lib/*.cmxs
%endif

%files devel
%if %{with doc}
%doc _build/default/_doc/_html/*
%endif
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.a
%{_libdir}/ocaml/%{upname}/*.cmx
%{_libdir}/ocaml/%{upname}/*.cmxa
%{_libdir}/ocaml/%{upname}/runtime-lib/*.a
%{_libdir}/ocaml/%{upname}/runtime-lib/*.cmx
%{_libdir}/ocaml/%{upname}/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*.cmt
%{_libdir}/ocaml/%{upname}/*.cmti
%{_libdir}/ocaml/%{upname}/*.mli
%{_libdir}/ocaml/%{upname}/runtime-lib/*.cmt

%changelog
* Mon Mar  1 17:34:16 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-8
- OCaml 4.12.0 build
- Make ocaml-odoc dependency conditional.

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-7
- Rebuild for ocaml-base 0.14.1

* Wed Feb  3 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-6
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-4
- Rebuild for ocaml-ppxlib 0.15.0

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Sat Jun 20 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
