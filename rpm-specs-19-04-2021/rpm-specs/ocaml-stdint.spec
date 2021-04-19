%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname stdint

Name:           ocaml-%{srcname}
Version:        0.7.0
Release:        3%{?dist}
Summary:        Various signed and unsigned integers for OCaml

License:        MIT
URL:            https://github.com/andrenth/%{name}
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tbz
# Fix lognot and logxor for Int40, Int48, Int56, and Int128
# https://github.com/andrenth/ocaml-stdint/pull/60
Patch0:         %{name}-lognot.patch
# Fix or disable broken tests
# https://github.com/andrenth/ocaml-stdint/issues/59
Patch1:         %{name}-test.patch

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 1.10
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-qcheck-devel

%description
The stdint library provides signed and unsigned integer types of various
fixed widths: 8, 16, 24, 32, 40, 48, 56, 64 and 128 bits.

This interface is similar to Int32 and Int64 from the base library but
provides more functions and constants like arithmetic and bit-wise
operations, constants like maximum and minimum values, infix operators
converting to and from every other integer type (including int, float and
nativeint), parsing from and conversion to readable strings (binary,
octal, decimal, hexadecimal), and conversion to and from buffers in both
big endian and little endian byte order.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

# Skip 128-bit tests on 32-bit platforms.  The necessary functions are not
# fully implemented.
%if 0%{?__isa_bits} == 32
sed -i '/"Int128.*"/d;/"Uint128.*"/d' tests/stdint_test.ml
%endif

%build
dune build %{?_smp_mflags} --display=verbose
dune build %{?_smp_mflags} @doc

# Relink the stublib with RPM_LD_FLAGS
cd _build/default/lib
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" -o stdint_stubs $(ar t libstdint_stubs.a)
cd -

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
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*.cma
%{_libdir}/ocaml/%{srcname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllstdint_stubs.so

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
%{_libdir}/ocaml/%{srcname}/*.h

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE

%changelog
* Mon Mar  1 23:32:56 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-3
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- Version 0.7.0
- Add -lognot and -test patches

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-9
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-8
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-4
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 0.6.0-2
- OCaml 4.10.0 final

* Thu Feb  6 2020 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- Initial RPM
