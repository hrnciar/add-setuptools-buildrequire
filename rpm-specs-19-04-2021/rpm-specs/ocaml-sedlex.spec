Name:           ocaml-sedlex
Version:        2.3
Release:        2%{?dist}
Summary:        Unicode-friendly lexer generator

License:        MIT
URL:            https://github.com/ocaml-community/sedlex
Source0:        https://github.com/ocaml-community/sedlex/archive/v%{version}/%{name}-%{version}.tar.gz

# Use local Unicode files instead of attempting to download them
Patch0:         %{name}-no-curl.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-gen-devel
BuildRequires:  unicode-ucd

%description
A lexer generator for OCaml, similar to ocamllex, but supporting Unicode.
Contrary to ocamllex, lexer specifications for sedlex are embedded in
regular OCaml source files.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-gen-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -p1 -n sedlex-%{version}

# Upstream's regression test is written for Unicode 6.3.0 through 12.1.0.  Our
# Unicode files are from a more recent version of the standard.  The test has a
# good chance of succeeding anyway, so we cross our fingers and give it a try.
# If the regression test fails, we'll have to try another approach.
univer=$(sed -n 's/.*PropList-\([.[:digit:]]*\)\.txt/\1/p' %{_datadir}/unicode/ucd/PropList.txt)
sed -i "s/12\\.1\\.0/$univer/" examples/regressions.ml

%build
dune build %{?_smp_mflags} -p sedlex --verbose
dune build %{?_smp_mflags} @doc

%install
dune install --destdir="$RPM_BUILD_ROOT" --verbose

# These will be installed using doc and license directives.
rm -r $RPM_BUILD_ROOT%{_prefix}/doc/sedlex/{CHANGES,README.md,LICENSE}

# Makes *.cmxs and *.opt executable such that they will be stripped.
find $RPM_BUILD_ROOT -name '*.{cmxs,opt}' -exec chmod 0755 {} \;

# uchar is a compatibility package for older OCaml version
sed -i 's/uchar//g' $RPM_BUILD_ROOT%{_libdir}/ocaml/sedlex/META
sed -i 's/uchar//g' $RPM_BUILD_ROOT%{_libdir}/ocaml/sedlex/dune-package
sed -i 's/"uchar"//g' $RPM_BUILD_ROOT%{_libdir}/ocaml/sedlex/opam


%check
dune runtest


%files
%doc README.md CHANGES
%license LICENSE
%{_libdir}/ocaml/*
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%endif


%files devel
%doc README.md CHANGES
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%endif


%changelog
* Mon Mar  1 23:50:55 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2.3-2
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 2.3-1
- Version 2.3
- Drop upstreamed -pervasives patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 2.2-1
- Version 2.2
- Add -pervasives and -no-curl patches
- Use local Unicode tables instead of downloading
- Build documentation with odoc
- Add a %%check script

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-12
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-11
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-8
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-7
- OCaml 4.11.0 pre-release attempt 2

* Sun Apr 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Andy Li <andy@onthewings.net> - 2.1-3
- Rebuild against latest ocaml package.
- Remove unneeded BuildRequires on opam-installer.

* Fri Nov 08 2019 Andy Li <andy@onthewings.net> - 2.1-2
- Remove dependency on uchar.

* Wed Oct 30 2019 Andy Li <andy@onthewings.net> - 2.1-1
- New upstream version.
- Update URL.

* Thu Aug 08 2019 Andy Li <andy@onthewings.net> - 1.99.4-7
- Add ppx_tools_versioned.diff, fix build.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Andy Li <andy@onthewings.net> - 1.99.4-5
- Do not build in parallel since the Makefile does not support it.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Andy Li <andy@onthewings.net> - 1.99.4-1
- Initial RPM release.
