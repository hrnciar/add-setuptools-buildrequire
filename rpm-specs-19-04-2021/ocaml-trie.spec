%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

%global srcname trie

Name:           ocaml-%{srcname}
Version:        1.0.0
Release:        7%{?dist}
Summary:        Strict impure trie tree

License:        MIT
URL:            https://github.com/kandu/trie
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-dune >= 1.0
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif

%description
This package contains an implementation of a strict impure trie tree.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

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

%files
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/%{srcname}.cma
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxs
%endif

%files devel
%if %{with doc}
%doc _build/default/_doc/*
%endif
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}.a
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmx
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmt
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmti
%{_libdir}/ocaml/%{srcname}/%{srcname}.mli

%changelog
* Mon Mar  1 15:16:08 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-7
- OCaml 4.12.0 build
- Make the ocaml-odoc dep conditional.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- Initial RPM
