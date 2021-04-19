%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname bigarray-compat

Name:           ocaml-%{srcname}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Compatibility library to use Stdlib.Bigarray when possible

License:        ISC
URL:            https://github.com/mirage/bigarray-compat
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/mirage/bigarray-compat/pull/5
Source1:        https://raw.githubusercontent.com/mirage/bigarray-compat/master/LICENSE.md

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 1.0

%description
Bigarray-compat is an OCaml library that exposes `Stdlib.Bigarray` when
possible (OCaml >= 4.07) but can fallback to `Bigarray`.  The compability
bigarray module is exposed under `Bigarray_compat`.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}
cp -p %{SOURCE1} .

%build
dune build %{?_smp_mflags}

%install
dune install --destdir=%{buildroot}

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
%doc README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/bigarray-compat/
%{_libdir}/ocaml/bigarray-compat/META
%{_libdir}/ocaml/bigarray-compat/*.cma
%{_libdir}/ocaml/bigarray-compat/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/bigarray-compat/*.cmxs
%endif

%files devel
%{_libdir}/ocaml/bigarray-compat/dune-package
%{_libdir}/ocaml/bigarray-compat/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/bigarray-compat/*.a
%{_libdir}/ocaml/bigarray-compat/*.cmx
%{_libdir}/ocaml/bigarray-compat/*.cmxa
%endif
%{_libdir}/ocaml/bigarray-compat/*.cmt

%changelog
* Mon Mar  1 12:17:30 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-2
- OCaml 4.12.0 build

* Tue Feb 09 2021 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- Initial package
