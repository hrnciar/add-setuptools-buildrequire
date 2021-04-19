# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

%global srcname graphics

Name:           ocaml-%{srcname}
Version:        5.1.1
Release:        2%{?dist}
Summary:        Portable drawing primitives for OCaml

License:        LGPLv2 with exceptions
URL:            https://github.com/ocaml/graphics
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tbz

BuildRequires:  ocaml >= 4.09.0
BuildRequires:  ocaml-dune-devel >= 2.1
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif
BuildRequires:  pkgconfig(x11)

%description
The graphics library provides a set of portable drawing primitives.
Drawing takes place in a separate window that is created when
Graphics.open_graph is called.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%build
dune build %{?_smp_mflags} --display=verbose
%if %{with doc}
dune build %{?_smp_mflags} @doc
%endif

# Relink the stublibs with $RPM_LD_FLAGS.
cd _build/default/src
ocamlmklib -g -ldopt '%{build_ldflags}' -o graphics_stubs \
  $(ar t libgraphics_stubs.a)
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
%doc CHANGES.md README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*.cma
%{_libdir}/ocaml/%{srcname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllgraphics_stubs.so

%files devel
%if %{with doc}
%doc _build/default/_doc/_html/* examples
%endif
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
* Mon Mar  1 17:17:56 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 5.1.1-2
- OCaml 4.12.0 build
- Make ocaml-odoc build dependency conditional.

* Tue Feb  2 2021 Jerry James <loganjerry@gmail.com> - 5.1.1-1
- Version 5.1.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 Jerry James <loganjerry@gmail.com> - 5.1.0-1
- Initial RPM
