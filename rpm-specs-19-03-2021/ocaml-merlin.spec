Name:           ocaml-merlin
Version:        4.1
Release:        1%{?dist}
Summary:        Context sensitive completion for OCaml in Vim and Emacs

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# The entire source is MIT except src/ocaml are QPL
License:        MIT and QPL
URL:            https://github.com/ocaml/%{libname}
Source0:        https://github.com/ocaml/%{libname}/archive/v%{version}.tar.gz#/%{libname}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 1.8
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-yojson-devel
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-csexp-devel
BuildRequires:  ocaml-result-devel

# For merlin-lsp
#BuildRequires:  ocaml-yojson-devel >= 1.6.0
#BuildRequires:  ocaml-menhir-devel
#BuildRequires:  ocaml-ppx-deriving-devel
#BuildRequires:  ocaml-ppx-deriving-yojson-devel
#BuildRequires:  ocaml-ppx-tools-devel
#BuildRequires:  ocaml-ppx-derivers-devel
#BuildRequires:  ocaml-migrate-parsetree-devel
#BuildRequires:  ocaml-result-devel

# Required for tests, not available in Fedora
#BuildRequires:  craml
BuildRequires:  emacs
# For byte-compile elisp
#BuildRequires:  emacs-auto-complete
#BuildRequires:  emacs-tuareg
# The following two are not yet available in Fedora.
# So byte compilation is disabled
#BuildRequires:  emacs-company
#BuildRequires:  emacs-iedit
BuildRequires:  vim-enhanced
Requires:       emacs-filesystem >= %{_emacs_version}
Requires:       vim-filesystem

%description
Merlin is an assistant for editing OCaml code. It aims to provide the features
available in modern IDEs: error reporting, auto completion, source browsing and
much more.


%prep
%setup -q -n %{libname}-%{version}


%build
dune build %{_smp_mflags} --build-dir _build_%{libname} -p %{libname}
#dune build --build-dir _build_%{libname}_lsp -p %{libname}-lsp


%install
dune install --build-dir _build_%{libname} --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir}/ocaml %{libname}
#dune install --build-dir _build_%{libname}_lsp --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir}/ocaml %{libname}-lsp

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/%{libname}/vim/* %{buildroot}%{vimfiles_root}
rmdir %{buildroot}%{_datadir}/%{libname}/vim
rmdir %{buildroot}%{_datadir}/%{libname}
# Reinstall documents using %%doc later
rm -fr %{buildroot}%{_prefix}/doc

%check
# Test requirement is not satisfied in Fedora


%files
%doc doc/* featuremap.* README.md CHANGES.md
%license LICENSE
%{_bindir}/*
%{_libdir}/ocaml/%{libname}
#%{_libdir}/ocaml/%{libname}-lsp
%{_emacs_sitelispdir}/*
%{vimfiles_root}/*/*

%changelog
* Mon Mar  1 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1-1
- New upstream version 4.1.
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-0.4.preview1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.7-0.3.preview1
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.7-0.2.preview1
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 3.3.7-0.1.preview1
- Update to 3.3.7-preview1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Robin Lee <cheeselee@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4 final

* Tue Mar  3 2020 Robin Lee <cheeselee@fedoraproject.org> - 3.3.4-0.1.preview1
- Update to 3.3.4-preview1, supports OCaml 4.10 (BZ#1799817, BZ#1809312)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.3.3-1
- Release 3.3.3 (RHBZ#1778280)
- Fix Release tag (RHBZ#1777835)

* Sat Aug  3 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1 (BZ#1703452)

* Sun Mar 31 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.2-2
- Fix ocaml library path

* Fri Mar  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.2.2-1
- Initial packaging
