%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname csexp

# This package is needed to build dune.  To avoid circular dependencies, this
# package cannot depend on dune, or any package that depends on dune.
# Therefore, we:
# - hack up our own build, rather than using dune to do the build
# - skip tests, which require ppx_expect, which is built with dune
# - skip building documentation, which requires odoc, which is built with dune
# If you know what you are doing, build with dune anyway using this conditional.
%bcond_with dune

Name:           ocaml-%{srcname}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Parsing and printing of S-expressions in canonical form

License:        MIT
URL:            https://github.com/ocaml-dune/csexp
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tbz

BuildRequires:  ocaml >= 4.03.0
%if %{with dune}
BuildRequires:  ocaml-dune >= 1.11
BuildRequires:  ocaml-odoc
%endif

%description
This project provides minimal support for parsing and printing
S-expressions in canonical form, which is a very simple and canonical
binary encoding of S-expressions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -N -n %{srcname}-%{version}

%build
%if %{with dune}
dune build %{?_smp_mflags} --display=verbose @install
dune build %{?_smp_mflags} @doc
%else
OFLAGS="-strict-sequence -strict-formats -short-paths -keep-locs -g"
OCFLAGS="$OFLAGS -bin-annot"
cd src
ocamlc $OCFLAGS -output-obj csexp.mli
ocamlc $OCFLAGS -a -o csexp.cma csexp.ml
%ifarch %{ocaml_native_compiler}
ocamlopt $OFLAGS -ccopt "%{build_cflags}" -cclib "%{build_ldflags}" -a \
  -o csexp.cmxa csexp.ml
ocamlopt $OFLAGS -ccopt "%{build_cflags}" -cclib "%{build_ldflags}" -shared \
  -o csexp.cmxs csexp.ml
%endif
cd -
%endif

%install
%if %{with dune}
dune install --destdir=%{buildroot}

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc
%else
# Install without dune.  See comment at the top.
mkdir -p %{buildroot}%{_libdir}/ocaml/%{srcname}
cp -p src/csexp.{cma,cmi,cmt,cmti,mli} %{buildroot}%{_libdir}/ocaml/%{srcname}
%ifarch %{ocaml_native_compiler}
cp -p src/csexp.{a,cmx,cmxa,cmxs} %{buildroot}%{_libdir}/ocaml/%{srcname}
%endif
cp -p csexp.opam %{buildroot}%{_libdir}/ocaml/%{srcname}/opam

cat >> %{buildroot}%{_libdir}/ocaml/%{srcname}/META << EOF
version = "%{version}"
description = "Parsing and printing of S-expressions in canonical form"
archive(byte) = "csexp.cma"
%ifarch %{ocaml_native_compiler}
archive(native) = "csexp.cmxa"
%endif
plugin(byte) = "csexp.cma"
%ifarch %{ocaml_native_compiler}
plugin(native) = "csexp.cmxs"
%endif
EOF

cat >> %{buildroot}%{_libdir}/ocaml/%{srcname}/dune-package << EOF
(lang dune 2.8)
(name csexp)
(version %{version})
(library
 (name csexp)
 (kind normal)
%ifarch %{ocaml_native_compiler}
 (archives (byte csexp.cma) (native csexp.cmxa))
 (plugins (byte csexp.cma) (native csexp.cmxs))
 (native_archives csexp.a)
%else
 (archives (byte csexp.cma))
 (plugins (byte csexp.cma))
%endif
 (main_module_name Csexp)
%ifarch %{ocaml_native_compiler}
 (modes byte native)
%else
 (modes byte)
%endif
 (modules
  (singleton (name Csexp) (obj_name csexp) (visibility public) (impl) (intf))))
EOF
%endif

# Cannot do this until ocaml-ppx-expect is available in Fedora.
#%%if %%{with dune}
#%%check
#dune runtest
#%%endif

%files
%doc README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*.cma
%{_libdir}/ocaml/%{srcname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.a
%{_libdir}/ocaml/%{srcname}/*.cmx
%{_libdir}/ocaml/%{srcname}/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/*.cmt
%{_libdir}/ocaml/%{srcname}/*.cmti
%{_libdir}/ocaml/%{srcname}/*.mli

%changelog
* Wed Mar 31 2021 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- Version 1.5.1
- Drop upstreamed -result patch

* Sun Feb 28 22:16:45 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-3
- Bump release and rebuild.

* Sun Feb 28 22:08:24 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-2
- OCaml 4.12.0 build

* Wed Feb 24 2021 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Version 1.4.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Version 1.3.2

* Thu Sep 10 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Initial RPM
