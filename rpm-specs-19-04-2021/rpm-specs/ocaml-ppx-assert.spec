%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-assert
%global upname  ppx_assert
%global upstream_version 0.14.0

Name:           ocaml-%{srcname}
Version:        0.15.0
Release:        0.git78f9989.1%{?dist}
Summary:        Assert-like extension nodes that raise useful errors on failure

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{upstream_version}/%{upname}-%{upstream_version}.tar.gz

# Include all changes from upstream since 0.14 was released.
# Upstream doesn't apparently believe in commit messages, and
# the individual patches don't make any sense, so bundle this
# as a single diff.
# git diff 3993004 > ppx_assert_0.14_0.15.patch
Patch1:         ppx_assert_0.14_0.15.patch

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ppx-cold-devel >= 0.14
BuildRequires:  ocaml-ppx-compare-devel >= 0.14
BuildRequires:  ocaml-ppx-here-devel >= 0.14
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.14
BuildRequires:  ocaml-ppxlib-devel >= 0.11.0

%description
Ppx_assert is a ppx rewriter that defines assert-like extension nodes
that raise useful errors on failure.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-cold-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-here-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{upname}-%{upstream_version} -p1

%build
dune build %{?_smp_mflags} --display=verbose --profile release
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
%dir %{_libdir}/ocaml/%{upname}/runtime-lib/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/ppx.exe
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%{_libdir}/ocaml/%{upname}/*/*.cma
%{_libdir}/ocaml/%{upname}/*/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%{_libdir}/ocaml/%{upname}/*/*.cmxs
%endif

%files devel
%doc _build/default/_doc/_html/*
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.a
%{_libdir}/ocaml/%{upname}/*.cmx
%{_libdir}/ocaml/%{upname}/*.cmxa
%{_libdir}/ocaml/%{upname}/*/*.a
%{_libdir}/ocaml/%{upname}/*/*.cmx
%{_libdir}/ocaml/%{upname}/*/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*.cmt
%{_libdir}/ocaml/%{upname}/*.cmti
%{_libdir}/ocaml/%{upname}/*.mli
%{_libdir}/ocaml/%{upname}/*/*.cmt
%{_libdir}/ocaml/%{upname}/*/*.cmti
%{_libdir}/ocaml/%{upname}/*/*.mli

%changelog
* Tue Mar  2 23:22:54 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-0.git78f9989.1
- Package latest upstream for OCaml 4.12.

* Mon Mar  1 23:22:54 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-8
- OCaml 4.12.0 build

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

* Fri Jun 19 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
