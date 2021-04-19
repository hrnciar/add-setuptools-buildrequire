%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-js-style
%global upname  ppx_js_style

Name:           ocaml-%{srcname}
Version:        0.14.0
Release:        9%{?dist}
Summary:        Code style checker for Jane Street OCaml packages

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-octavius-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.11.0
BuildRequires:  ocaml-odoc

%description
Ppx_js_style is an identity ppx rewriter that enforces Jane Street
coding styles.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-octavius-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{upname}-%{version}

%build
dune build %{?_smp_mflags} --display=verbose
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

%check
dune runtest

%files
%doc CHANGES.md README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/%{upname}/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/ppx.exe
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%endif

%files devel
%doc _build/default/_doc/_html/*
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.a
%{_libdir}/ocaml/%{upname}/*.cmx
%{_libdir}/ocaml/%{upname}/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*.cmt
%{_libdir}/ocaml/%{upname}/*.cmti
%{_libdir}/ocaml/%{upname}/*.mli

%changelog
* Tue Mar  2 10:06:37 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-9
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-8
- Rebuild for ocaml-base 0.14.1

* Wed Feb  3 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-7
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-5
- Rebuild for ocaml-ppxlib 0.15.0

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-4
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.0 rebuild

* Sat Aug 15 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-2
- Build verbosely
- Use 'with' instead of 'and' in BuildRequires

* Sat Jun 20 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
