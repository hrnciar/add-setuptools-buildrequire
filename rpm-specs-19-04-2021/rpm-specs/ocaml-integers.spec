# Debuginfo generation is broken, so disable it.  We should work out
# how to add -g option instead XXX.
%global debug_package %{nil}

# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

Name:           ocaml-integers
Version:        0.4.0
Release:        4%{?dist}
Summary:        Various signed and unsigned integer types for OCaml

License:        MIT
URL:            https://github.com/ocamllabs/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-dune
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif

%description
The ocaml-integers library provides a number of 8-, 16-, 32- and 64-bit
signed and unsigned integer types, together with aliases such as `long`
and `size_t` whose sizes depend on the host platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%if %{with doc}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains developer documentation for
%{name}.
%endif

%prep
%autosetup

%build
dune build %{?_smp_mflags}
%if %{with doc}
dune build %{?_smp_mflags} @doc
%endif

# Relink the stublib with Fedora flags
cd _build/default/src
ocamlmklib -g -ldopt "%{build_ldflags}" -o integers_stubs \
  $(ar t libintegers_stubs.a)
cd -

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
%license LICENSE.md
%doc CHANGES.md README.md
%dir %{_libdir}/ocaml/integers/
%dir %{_libdir}/ocaml/integers/top/
%{_libdir}/ocaml/integers/META
%{_libdir}/ocaml/integers/*.cma
%{_libdir}/ocaml/integers/*.cmi
%{_libdir}/ocaml/integers/top/*.cma
%{_libdir}/ocaml/integers/top/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/integers/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllintegers_stubs.so

%files devel
%{_libdir}/ocaml/integers/dune-package
%{_libdir}/ocaml/integers/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/integers/*.a
%{_libdir}/ocaml/integers/*.cmx
%{_libdir}/ocaml/integers/*.cmxa
%endif
%{_libdir}/ocaml/integers/*.cmt
%{_libdir}/ocaml/integers/*.cmti
%{_libdir}/ocaml/integers/*.h
%{_libdir}/ocaml/integers/*.mli
%{_libdir}/ocaml/integers/top/*.cmt
%{_libdir}/ocaml/integers/top/*.cmti
%{_libdir}/ocaml/integers/top/*.mli

%if %{with doc}
%files doc
%doc _build/default/_doc/*
%endif

%changelog
* Mon Mar  1 11:02:39 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-4
- Disable the debuginfo subpackages.
- Make the -doc subpackage conditional.

* Mon Mar  1 11:02:39 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-2
- OCaml 4.12.0 build

* Tue Feb 09 2021 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- Initial package
