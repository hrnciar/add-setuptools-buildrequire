%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname merlin
%global ocamlver 412

Name:           ocaml-%{srcname}
Version:        4.2
Release:        1%{?dist}
Summary:        Context sensitive completion for OCaml

# The entire source is MIT except:
# - QPL: src/ocaml/driver/pparse.ml{,i}
# - QPL: src/ocaml/preprocess/lexer_ident.mll
# - QPL: src/ocaml/preprocess/lexer_raw.ml{i,l}
# - LGPLv2 with exceptions: src/ocaml/preprocess/parser_raw.mly
# - LGPLv2 with exceptions: upstream/ocaml_411/parsing/parser.mly
# - LGPLv2 with exceptions: upstream/ocaml_412/parsing/parser.mly
#
# The final license is due to the linking exception on the LGPLv2 files.
License:        MIT and QPL
URL:            https://ocaml.github.io/%{srcname}/
Source0:        https://github.com/ocaml/%{srcname}/releases/download/v%{version}-%{ocamlver}/%{srcname}-v%{version}-%{ocamlver}.tbz
# Fix the tests to work with /usr/lib64 as well as /usr/lib
Patch0:         %{name}-test-lib64.patch
# Fix various issues in the Emacs interface
Patch1:         %{name}-emacs.patch
# On i386, we get extra output about text relocations
# See https://github.com/ocaml/ocaml/issues/9800
Patch2:         %{name}-textrel.patch

BuildRequires:  emacs
BuildRequires:  emacs-auto-complete
BuildRequires:  emacs-company-mode
BuildRequires:  emacs-iedit
BuildRequires:  emacs-tuareg
BuildRequires:  jq
BuildRequires:  ocaml >= 4.11.1
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-caml-mode
BuildRequires:  ocaml-csexp-devel >= 1.2.3
BuildRequires:  ocaml-dune >= 2.7.0
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-findlib-devel >= 1.6.0
BuildRequires:  ocaml-menhir-devel
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-result-devel >= 1.5
BuildRequires:  ocaml-source
BuildRequires:  ocaml-yojson-devel >= 1.6.0
BuildRequires:  vim-enhanced

Requires:       dot-merlin-reader%{?_isa} = %{version}-%{release}

%global _desc %{expand:
Merlin is an assistant for editing OCaml code.  It aims to provide the
features available in modern IDEs: error reporting, auto completion,
source browsing and much more.}

%description %_desc

You should also install a package that integrates with your editor of
choice, such as emacs-merlin or vim-merlin.

%package     -n dot-merlin-reader
Summary:        Merlin configuration file reader

%description -n dot-merlin-reader
This package contains a helper process that reads .merlin files and gives
the normalized content to merlin.

%package     -n emacs-merlin
Summary:        Context sensitive completion for OCaml in Emacs
BuildArch:      noarch
Requires:       ocaml-merlin = %{version}-%{release}
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       emacs-caml-mode

Recommends:     emacs-auto-complete
Recommends:     emacs-company-mode
Recommends:     emacs-iedit
Recommends:     emacs-tuareg

%description -n emacs-merlin %_desc

This package contains the Emacs interface to merlin.

%package     -n vim-merlin
Summary:        Context sensitive completion for OCaml in Vim
BuildArch:      noarch
Requires:       ocaml-merlin = %{version}-%{release}
Requires:       vim-filesystem

%description -n vim-merlin %_desc

This package contains the Vim interface to merlin.

%prep
%autosetup -n %{srcname}-v%{version}-%{ocamlver} -N
%patch0 -p1
%patch1 -p1
%ifarch %{ix86}
%patch2 -p1
%endif

%build
dune build %{_smp_mflags}
dune build %{_smp_mflags} @doc

%install
dune install --destdir=%{buildroot}

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/%{srcname}/vim/* %{buildroot}%{vimfiles_root}
rm -fr %{buildroot}%{_datadir}/%{srcname}

# Generate the autoload file for the Emacs interface and byte compile
cd %{buildroot}%{_emacs_sitelispdir}
emacs -batch --no-init-file --no-site-file \
  --eval "(progn (setq generated-autoload-file \"$PWD/merlin-autoloads.el\" backup-inhibited t) (update-directory-autoloads \".\"))"
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv merlin-autoloads.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile *.el
cd -

%check
dune runtest

%files
%doc featuremap.* CHANGES.md README.md
%license LICENSE
%{_bindir}/ocamlmerlin
%{_bindir}/ocamlmerlin-server
%{_libdir}/ocaml/%{srcname}/

%files -n dot-merlin-reader
%license LICENSE
%{_bindir}/dot-merlin-reader
%{_libdir}/ocaml/dot-merlin-reader/

%files -n emacs-merlin
%{_emacs_sitelispdir}/merlin*
%{_emacs_sitestartdir}/merlin-autoloads.el

%files -n vim-merlin
%{vimfiles_root}/*/*

%changelog
* Tue Apr 13 2021 Jerry James <loganjerry@gmail.com> - 4.2-1
- Version 4.2
- Drop upstreamed -iedit patch
- Add -emacs patch to fix various Emacs issues
- Add -textrel patch to fix FTBFS on i386

* Fri Mar 26 2021 Jerry James <loganjerry@gmail.com> - 4.1-2
- Fix tests on 64-bit systems with the -test-lib64 patch
- Add -emacs-iedit patch to adapt to recent iedit changes
- Build with auto-complete, company-mode, and caml-mode support
- Add subpackages: dot-merlin-reader, emacs-merlin, and vim-merlin
- Generate autoloads for the Emacs interface

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
