%global debug_package %{nil}

Name:           ocamlmod
Version:        0.0.9
Release:        23%{?dist}
Summary:        Generate OCaml modules from source files

License:        LGPLv2+ with exceptions
URL:            https://forge.ocamlcore.org/projects/ocamlmod/
Source0:        https://github.com/gildor478/ocamlmod/archive/%{version}/%{name}-%{version}.tar.gz

# Use a setup.ml generated by `oasis setup`,
# such that the package doesn't depend on oasis,
# to avoid circular dependency.
# Also set CompiledObject to "best" (RHBZ#1600596).
Patch0:         ocamlmod-setupml.patch

# Use ounit2 instead of oUnit.
Patch1:         ocamlmod-0.0.9-ounit2.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit
BuildRequires:  help2man

%description
ocamlmod allows to create OCaml modules from source files.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1


%build
ocaml setup.ml -configure \
    --destdir $RPM_BUILD_ROOT \
    --prefix %{_prefix} \
    --enable-tests
ocaml setup.ml -build


%install
ocaml setup.ml -install

# generate manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
help2man $RPM_BUILD_ROOT%{_bindir}/ocamlmod \
    --output $RPM_BUILD_ROOT%{_mandir}/man1/ocamlmod.1 \
    --name "Generate OCaml modules from source files" \
    --version-string %{version} \
    --no-info

%check
ocaml setup.ml -test

# check that ocamlmod is compiled as native executable if possible
%ifarch %{ocaml_native_compiler}
file $RPM_BUILD_ROOT%{_bindir}/ocamlmod | grep -vq "script executable"
%endif

%files
%doc README.txt
%{_bindir}/ocamlmod
%{_mandir}/man1/ocamlmod.1*


%changelog
* Mon Mar  1 21:30:58 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-23
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-21
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-20
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-18
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-17
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-16
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-15
- Bump release and rebuild.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-14
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-12
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-11
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-10
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-9
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-8
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-6
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.0.9-5
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Andy Li <andy@onthewings.net> - 0.0.9-3
- Update ocamlmod-setupml.patch with _oasis CompiledObject set to "best" (RHBZ#1600596).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Andy Li <andy@onthewings.net> - 0.0.9-1
- Initial RPM release.
