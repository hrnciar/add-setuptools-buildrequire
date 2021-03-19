%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

# This package is required by ocaml-time-now, which is required by
# ocaml-ppx-inline-test.  This package requires ocaml-ppx-inline-test to run
# its tests.  We break the circular dependency here.
%bcond_with test

%global srcname ppx-optcomp
%global upname  ppx_optcomp

Name:           ocaml-%{srcname}
Version:        0.14.1
Release:        2%{?dist}
Summary:        Optional compilation for OCaml

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14
BuildRequires:  ocaml-dune >= 2.0.0
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif
BuildRequires:  ocaml-ppxlib-devel >= 0.18.0
BuildRequires:  ocaml-stdio-devel >= 0.14
%if %{with test}
BuildRequires:  ocaml-ppx-inline-test-devel
%endif

%description
Ppx_optcomp provides optional compilation for OCaml.  It is a tool used
to handle optional compilations of pieces of code depending of the word
size, the version of the compiler, etc.  The syntax is based on OCaml
item extension nodes, with keywords similar to cpp.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}

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

%if %{with test}
%check
dune runtest
%endif

%files
%doc CHANGES.md README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/%{upname}/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
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
%endif
%{_libdir}/ocaml/%{upname}/*.cmt

%changelog
* Mon Mar  1 17:29:48 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-2
- OCaml 4.12.0 build
- Make ocaml-odoc dependency conditional.

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- Version 0.14.1

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-6
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-4
- Rebuild for ocaml-ppxlib 0.15.0

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Fri Jun 19 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
