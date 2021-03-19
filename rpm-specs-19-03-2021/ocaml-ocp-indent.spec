%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

%global srcname ocp-indent

Name:           ocaml-%{srcname}
Version:        1.8.2
Release:        7%{?dist}
Summary:        A simple tool to indent OCaml programs

# The entire source code is LGPLv2 with exceptions except
# src/approx_tokens.ml is QPL
License:        (LGPLv2 with exceptions) and QPL
URL:            https://www.typerex.org/ocp-indent.html
Source0:        https://github.com/OCamlPro/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Update the Emacs interface for Emacs 27.1
Patch0:         %{name}-emacs.patch

BuildRequires:  emacs
BuildRequires:  emacs-tuareg
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-findlib-devel
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif
BuildRequires:  vim-enhanced

Requires:       emacs-filesystem >= %{_emacs_version}
Requires:       vim-filesystem

%description
Ocp-indent is a simple tool and library to indent OCaml code.  It is
based on an approximate, tolerant OCaml parser and a simple stack
machine; this is much faster and more reliable than using regexps.
Presets and configuration options are available, with the possibility to
set them project-wide.  Ocp-indent supports most common syntax
extensions, and is extensible for others.

Includes:

- An indentor program, callable from the command-line or from within
  editors
- Bindings for popular editors
- A library that can be directly used by editor writers, or just for
  fault-tolerant/approximate parsing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
dune build %{?_smp_mflags} --profile=release
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

# The man page has A0 bytes for non-breaking spaces, but this is invalid UTF-8
sed -i 's/\xa0/\\ /g' %{buildroot}%{_mandir}/man1/ocp-indent.1

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/%{srcname}/vim/* %{buildroot}%{vimfiles_root}
rm -fr %{buildroot}%{_datadir}/%{srcname}

# Generate the autoload file for the Emacs interface and byte compile
cd %{buildroot}%{_emacs_sitelispdir}
emacs -batch --no-init-file --no-site-file \
  --eval "(progn (setq generated-autoload-file \"$PWD/ocp-indent-autoloads.el\" backup-inhibited t) (update-directory-autoloads \".\"))"
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv ocp-indent-autoloads.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile ocp-indent.el
cd -

%check
#Tests only run on a git checkout
# ./tests/test.sh

%files
%doc README.md CHANGELOG
%license LICENSE
%{_bindir}/ocp-indent
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/dynlink/
%dir %{_libdir}/ocaml/%{srcname}/lexer/
%dir %{_libdir}/ocaml/%{srcname}/lib/
%dir %{_libdir}/ocaml/%{srcname}/utils/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*/*.cma
%{_libdir}/ocaml/%{srcname}/*/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*/*.cmxs
%endif
%{_emacs_sitelispdir}/ocp-indent.el{,c}
%{_emacs_sitestartdir}/ocp-indent-autoloads.el
%{vimfiles_root}/indent/ocaml.vim
%{_mandir}/man1/%{srcname}.1*

%files devel
%if %{with doc}
%doc _build/default/_doc/*
%endif
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*/*.a
%{_libdir}/ocaml/%{srcname}/*/*.cmx
%{_libdir}/ocaml/%{srcname}/*/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/*/*.cmt
%{_libdir}/ocaml/%{srcname}/*/*.cmti
%{_libdir}/ocaml/%{srcname}/*/*.mli

%changelog
* Mon Mar 15 2021 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-7
- Bump and rebuild for updated ocaml-findlib.

* Mon Mar  1 16:57:58 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-6
- OCaml 4.12.0 build
- Make ocaml-odoc dependency conditional.

* Tue Feb 23 2021 Jerry James <loganjerry@gmail.com> - 1.8.2-5
- Spec file cleanup
- Add -emacs patch to adapt to Emacs 27.1
- Build documentation with odoc
- Fix non-Unicode man page
- Generate autoloads for the Emacs interface
- Byte compile the Emacs interface

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 1.8.2-5
- Rebuild for changed dynlink dependency

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-2
- OCaml 4.11.0 rebuild

* Sun Aug  9 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-10
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-8
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-6
- OCaml 4.10.0+beta1 rebuild.
- Use dune install --destdir option.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-5
- OCaml 4.09.0 (final) rebuild.

* Wed Sep 18 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-4
- Bump release and rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr  6 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.0-2
- Make cmxs files executable to properly generate debuginfo

* Fri Apr  5 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.0-1
- Initial packaging

