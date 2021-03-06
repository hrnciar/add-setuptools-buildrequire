%ifarch %{ocaml_native_compiler}
%global camlsuffix opt
%else
%global camlsuffix byte
%endif

# .coqide-gtk2rc produces an rpmlint warning due to its name,
# however, this name is proper as per the Coq documentation

# Coq installs python files into nonstandard places
%global _python_bytecompile_extra 0

# https://bugzilla.redhat.com/show_bug.cgi?id=1874879
ExcludeArch:    s390x

Name:           coq
Version:        8.13.1
Release:        1%{?dist}
Summary:        Proof management system

License:        LGPLv2
URL:            https://coq.inria.fr/
Source0:        https://github.com/coq/coq/archive/V%{version}/%{name}-%{version}.tar.gz
Source1:        fr.inria.coqide.desktop
Source2:        coq.xml
Source3:        fr.inria.coqide.metainfo.xml

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-dune >= 2.5.0
BuildRequires:  ocaml-findlib >= 1.8.1
BuildRequires:  ocaml-lablgtk3-devel >= 3.0
BuildRequires:  ocaml-lablgtk3-sourceview3-devel >= 3.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-zarith-devel >= 1.10
BuildRequires:  csdp-tools
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libicns-utils
BuildRequires:  make
BuildRequires:  rsync
BuildRequires:  time

# For documentation
BuildRequires:  antlr4
BuildRequires:  hevea
BuildRequires:  latexmk
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist antlr4-python3-runtime}
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist pexpect}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  tex(latex)
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(comment.sty)
BuildRequires:  tex(epic.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(moreverb.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(stmaryrd.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(utf8x.def)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  tex(FreeSerif.otf)
BuildRequires:  tex-cm-super
BuildRequires:  tex-courier
BuildRequires:  tex-ec
BuildRequires:  tex-helvetic
BuildRequires:  tex-symbol
BuildRequires:  tex-times
BuildRequires:  tex-xindy
BuildRequires:  tex-zapfchan
BuildRequires:  tex-zapfding

Requires:       csdp-tools
Requires:       ocaml-findlib
Requires:       texlive-base

Recommends:     emacs-proofgeneral

# Exclude private ocaml interfaces that we don't Provide
%global __requires_exclude ocamlx?\\\((Configwin_types|Interface|Richpp|Serialize|Xml_p(arser|rinter)|Xmlprotocol)\\\)

%global _desc %{expand:
Coq is a formal proof management system.  It provides a formal language
to write mathematical definitions, executable algorithms and theorems
together with an environment for semi-interactive development of
machine-checked proofs.}

%description %_desc

Typical applications include the certification of properties of
programming languages (e.g. the CompCert compiler certification project,
or the Bedrock verified low-level programming library), the formalization
of mathematics (e.g. the full formalization of the Feit-Thompson theorem
or homotopy type theory) and teaching.

%package coqide-server
Summary:        The coqidetop language server
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description coqide-server %_desc

This package provides the coqidetop language server, an implementation of
Coq's XML protocol which allows clients, such as CoqIDE, to interact with
Coq in a structured way.

%package coqide
Summary:        Coqide IDE for Coq proof management system
Requires:       %{name}-coqide-server%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       xdg-utils

%description coqide %_desc

This package provides CoqIDE, a graphical user interface for the
development of interactive proofs.

%package doc
Summary:        Documentation for Coq proof management system
License:        Open Publication and LGPLv2+
BuildArch:      noarch
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%description doc %_desc

This package provides documentation and tutorials for the system.  The
main documentation comes in two parts: the main Library documentation,
which describes all Coq.* modules, and the Reference Manual, which
gives a more complete description of the whole system. Included are
also HTML versions of both. Furthermore, there are two tutorials, the
main one, and one specifically on recursive types. The example code
for the latter is also included.

%prep
%autosetup -p1

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix a Makefile rule that causes installation to fail
sed -ri '/FULLCONFIGDIR/s/OLDROOT|COQINSTALLPREFIX/&2/g' Makefile.install

# Use Fedora compiler flags
sed -i 's|-Wall.*-O2|%{build_cflags} -Wno-unused|' configure.ml

# Use Fedora link flags
sed -i "s|-oc|-ccopt '%{build_ldflags}' -g &|" Makefile.build

# Make sure debuginfo is generated
sed -i 's,-shared,& -g,g' tools/CoqMakefile.in Makefile.build

# Do not invoke env
for f in doc/tools/coqrst/notations/fontsupport.py;
do
  sed -i.orig 's,/usr/bin/env python2,%{python3},' $f
  fixtimestamp $f
done
for f in $(grep -Frl '%{_bindir}/env'); do
  sed -r -i.orig 's,(%{_bindir}/)env[[:blank:]]+([[:alnum:]]+),\1\2,g' $f
  fixtimestamp $f
done

%build
%global coqdocdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/coq-%{version}}

# Regenerate ANTLR files
cd doc/tools/coqrst/notations
antlr4 -Dlanguage=Python3 -visitor -no-listener TacticNotations.g
cd -

%ifarch %{ocaml_native_compiler}
%global opt_option -native-compiler yes -coqide opt
%else
%global opt_option -byte-only -coqide byte
%endif
%ifarch %{ocaml_natdynlink}
%global opt_option %{opt_option} -natdynlink yes
%endif

# Set our configuration options
./configure -prefix %{_prefix}                       \
            -libdir %{_libdir}/ocaml/coq             \
            -bindir %{_bindir}                       \
            -mandir %{_mandir}                       \
            -docdir %{coqdocdir}                     \
            -configdir %{_sysconfdir}/xdg/%{name}    \
            -coqdocdir %{_texmf_main}/tex/latex/misc \
            %{opt_option}                            \
            -browser "xdg-open %s"                   \
            -with-doc yes

# Build the binary artifacts
export SPHINXWARNOPT="-w$PWD/sphinx-warn.log"
make world VERBOSE=1

%install
make COQINSTALLPREFIX="%{buildroot}%{_prefix}" OLDROOT="%{_prefix}" \
     COQINSTALLPREFIX2="%{buildroot}%{_sysconfdir}" OLDROOT2="%{_sysconfdir}" \
     install

# Fix permissions
if [ -e %{buildroot}%{_libdir}/ocaml/coq/kernel/byterun/dllcoqrun.so ]; then
  chmod 0755 %{buildroot}%{_libdir}/ocaml/coq/kernel/byterun/dllcoqrun.so
fi

# Prepare the documentation for installation
find doc/sphinx/_build/html -name .buildinfo -delete

# Use links rather than copying binaries
%ifarch %{ocaml_native_compiler}
for fil in coqtop coqidetop; do
  rm -f %{buildroot}%{_bindir}/$fil
  ln %{buildroot}%{_bindir}/$fil.%{camlsuffix} %{buildroot}%{_bindir}/$fil
done
%endif

# Install desktop and file type icons
pushd ide/coqide/MacOS
icns2png -x coqide.icns
for sz in 16 32 256 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  mv coqide_${sz}x${sz}x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/coq.png
done
icns2png -x coqfile.icns
for sz in 16 32 128 256 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes
  mv coqfile_${sz}x${sz}x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes/coqfile.png
done
popd

# Make a MIME type for .v files
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p %{SOURCE2} %{buildroot}%{_datadir}/mime/packages

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE3} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/fr.inria.coqide.metainfo.xml

# Install the language bindings
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
for fil in coq.lang coq-ssreflect.lang; do
  ln -s ../../coq/$fil %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
done

# Install the style file
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/styles
ln -s ../../coq/coq_style.xml %{buildroot}%{_datadir}/gtksourceview-3.0/styles

# We don't need both PostScript and PDF documentation
rm -fr %{buildroot}%{coqdocdir}/ps

# Install documentation not installed by install-doc in Makefile
cp -p dev/doc/changes.md CREDITS README.md %{buildroot}%{coqdocdir}

# Byte compile the tools
%py_byte_compile %{python3} %{buildroot}%{_libdir}/ocaml/coq/tools

# Install opam files
cp -p coq.opam %{buildroot}%{_libdir}/ocaml/coq/opam

mkdir -p %{buildroot}%{_libdir}/ocaml/coq-doc
cp -p coq-doc.opam %{buildroot}%{_libdir}/ocaml/coq-doc/opam

mkdir -p %{buildroot}%{_libdir}/ocaml/coqide-server
cp -p coqide-server.opam %{buildroot}%{_libdir}/ocaml/coqide-server/opam

mkdir -p %{buildroot}%{_libdir}/ocaml/coqide
cp -p coqide.opam %{buildroot}%{_libdir}/ocaml/coqide-server/opam

%files
%license LICENSE
%{_libdir}/ocaml/coq/
%{_bindir}/coqc*
%{_bindir}/coqdep
%{_bindir}/coqdoc
%{_bindir}/coq_makefile
%{_bindir}/coqpp
%{_bindir}/coqproofworker.%{camlsuffix}
%{_bindir}/coqqueryworker.%{camlsuffix}
%{_bindir}/coqtacticworker.%{camlsuffix}
%{_bindir}/coq-tex
%{_bindir}/coqtop*
%{_bindir}/coqwc
%{_bindir}/coqworkmgr
%{_bindir}/ocamllibdep
%{_bindir}/votour
%{_mandir}/man1/coqc.1*
%{_mandir}/man1/coqchk.1*
%{_mandir}/man1/coqdep.1*
%{_mandir}/man1/coqdoc.1*
%{_mandir}/man1/coq_makefile.1*
%{_mandir}/man1/coq-tex.1*
%{_mandir}/man1/coqtop.1*
%{_mandir}/man1/coqtop.byte.1*
%{_mandir}/man1/coqtop.opt.1*
%{_mandir}/man1/coqwc.1*
%{_texmf_main}/tex/latex/misc/
# This should really go in the doc subpackage, but because it is installed in
# an arch-specific path, it cannot be part of a noarch package.
%{_libdir}/ocaml/coq-doc/

%files coqide-server
%{_bindir}/coqidetop*
%{_libdir}/ocaml/coqide-server/

%files coqide
%{_bindir}/coqide
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/16x16/apps/coq.png
%{_datadir}/icons/hicolor/16x16/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/32x32/apps/coq.png
%{_datadir}/icons/hicolor/32x32/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/128x128/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/256x256/apps/coq.png
%{_datadir}/icons/hicolor/256x256/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/512x512/apps/coq.png
%{_datadir}/icons/hicolor/512x512/mimetypes/coqfile.png
%{_mandir}/man1/coqide.1*
%{_libdir}/ocaml/coqide/
%{_metainfodir}/fr.inria.coqide.metainfo.xml
%{_datadir}/applications/fr.inria.coqide.desktop
%{_datadir}/gtksourceview-3.0/language-specs/coq*.lang
%{_datadir}/gtksourceview-3.0/styles/coq_style.xml
%{_datadir}/mime/packages/coq.xml
%{_sysconfdir}/xdg/coq/

%files doc
%license doc/LICENSE
%{coqdocdir}

%changelog
* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 8.13.1-1
- Version 8.13.1

* Tue Mar  2 10:06:37 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 8.13.0-2
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 8.13.0-1
- Version 8.13.0
- Revert to make; dune is unable to build the native compilation version
- Install into the metainfo dir instead of the appdata dir

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Jerry James <loganjerry@gmail.com> - 8.12.2-1
- Version 8.12.2

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 8.12.1-1
- Version 8.12.1
- Drop upstreamed sphinx 3 support patch

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 8.12.0-3
- OCaml 4.11.1 rebuild
- ExcludeArch s390x (RHBZ#1874879).

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 8.12.0-1
- Version 8.12.0
- Build with dune
- Add coqide-server subpackage
- Unbundle fonts from the documentation

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 8.11.2-5
- OCaml 4.11.0 rebuild

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 8.11.2-4
- Rebuild to fix ocamlx(Dynlink) dependency

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.11.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 8.11.2-1
- Version 8.11.2

* Tue May 19 2020 Jerry James <loganjerry@gmail.com> - 8.11.1-1
- Version 8.11.1
- Drop upstreamed 0001-Add-support-for-OCaml-4.10.patch

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 8.11.0-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 8.11.0-4
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 8.11.0-3
- Add 0002-Sphinx-3-support.patch for sphinx 3 support (bz 1823529)

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 8.11.0-3
- Update all OCaml dependencies for RPM 4.16.

* Fri Mar 27 2020 Jerry James <loganjerry@gmail.com> - 8.11.0-2
- Update the ocaml 4.10 patch to upstream's version

* Wed Mar 25 2020 Jerry James <loganjerry@gmail.com> - 8.11.0-1
- Version 8.11.0
- Drop upstreamed 0002-fix-signal-polling-for-OCaml-4.10.patch
- Stop bundling the python3 runtime for antlr4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jerry James <loganjerry@gmail.com> - 8.9.1-12
- Add 0002-fix-signal-polling-for-OCaml-4.10.patch

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 8.9.1-12
- OCaml 4.10.0+beta1 rebuild.

* Wed Jan 15 2020 Jerry James <loganjerry@gmail.com> - 8.9.1-11
- Move coqidetop into the main package (bz 1791377)

* Fri Jan 10 2020 Richard W.M. Jones <rjones@redhat.com> - 8.9.1-10
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 8.9.1-9
- OCaml 4.09.0 (final) rebuild.
- Bump antlr4rel.

* Tue Sep  3 2019 Jerry James <loganjerry@gmail.com> - 8.9.1-6
- Fix the release numbers

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 8.9.1-5
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 8.9.1-3
- OCaml 4.08.1 (rc2) rebuild.

* Mon Jul 29 2019 Jerry James <loganjerry@gmail.com> - 8.9.1-2
- Bump Epoch on antlr4-python3-runtime due to decrease in version number
- Work around pr_dump.cmo snafu with new ocaml-camlp5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 8.9.1-1
- New upstream release
- Emacs support has been dropped upstream; obsolete the -emacs subpackage
- Recommend ProofGeneral
- Install more icon sizes
- Bring the config dir back for system-wide configuration
- Fix the antlr4-python3-runtime version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 8.8.2-1
- New upstream release
- Bundle the python3 runtime for antlr4 4.7.2 due to inaction on bz 1595974 and
  bz 1599015

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 8.7.1-6
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 8.7.1-5
- Bump release and rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 8.7.1-4
- Bump release and rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 8.7.1-3
- OCaml 4.07.0-rc1 rebuild.

* Mon Feb 19 2018 Jerry James <loganjerry@gmail.com> - 8.7.1-2
- Also filter out ocaml(Configwin_types) since the Provides is not generated

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 8.7.1-1
- New upstream release
- All patches have been upstreamed; drop them
- Switch back to camlp5, now required

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 8.6.1-3
- Bump and rebuild against new ocaml-num package.

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 8.6.1-2
- OCaml 4.06.0 rebuild.
- Backport various fixes to make Coq compile with OCaml 4.06.
- BR the "new" legacy ocaml-num library.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 8.6.1-1
- New upstream version 8.6.1.
- Remove patch now upstream.
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 8.6-5
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 8.6-4
- Bump release and rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 8.6-3
- OCaml 4.04.1 rebuild.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 8.6-1
- New upstream release

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 8.5pl3-2
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 8.5pl3-1
- New upstream release
- Remove obsolete scriptlets
- Fix install path for coqdoc.sty

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 8.5pl2-1
- New upstream release

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 8.5pl1-1
- New upstream release

* Sat Feb 13 2016 Jerry James <loganjerry@gmail.com> - 8.5-2
- Workaround ocaml dep generator failure with ocaml-lablgtk

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 8.5-1
- New upstream release
- Use camlp4 in preference to camlp5
- Absorb -emacs-el into -emacs according to current guidelines
- Update appdata for latest specification

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.4pl6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 Richard W.M. Jones <rjones@redhat.com> - 8.4pl6-5
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 8.4pl6-4
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 8.4pl6-3
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4pl6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 8.4pl6-1
- New upstream release
- Drop upstreamed -fix-ints patch
- Update appdata URLs

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 8.4pl5-4
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 8.4pl5-3
- ocaml-4.02.1 rebuild.

* Thu Nov  6 2014 Jerry James <loganjerry@gmail.com> - 8.4pl5-2
- Rebuild for ocaml-camlp5 6.12

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 8.4pl5-1
- New upstream release
- Drop upstreamed comment patch
- Drop aarch64 bug workaround, fixed in ocaml 4.02.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 8.4pl4-19
- fix/update mime scriptlet

* Wed Sep 17 2014 Jerry James <loganjerry@gmail.com> - 8.4pl4-18
- Rebuild due to ocaml update
- Fix license handling

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-17
- Bump release and rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-16
- Bump release and rebuild.
- Fix to int types in OCaml > 4.02.0 and Fedora.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-14
- ocaml-4.02.0 final rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-13
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4pl4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-11
- Add stublibs to library path to make coqide build.

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-10
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.
- Add workaround for build failure on aarch64.
- BR emacs since emacs-nox no longer provides this binary (RHBZ#1123573).

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-6
- Add patch to fix build failure with OCaml 4.02.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl4-4
- Rebuild for OCaml 4.02.0 beta.

* Wed Jul 16 2014 Richard Hughes <richard@hughsie.com> - 8.4pl4-3
- Install the coq application icon in a standard location to fix display in
  gnome-software and Apper.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4pl4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 8.4pl4-1
- New upstream release

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 8.4pl3-3
- Remove ocaml_arches macro (RHBZ#1087794).

* Thu Jan 23 2014 Jerry James <loganjerry@gmail.com> - 8.4pl3-2
- Rebuild with fixed hevea package to get good HTML docs
- Hevea is now available on all architectures that support ocaml
- Drop Fedora 18 compatibility now that F-18 has reached EOL
- Add AppData file

* Mon Dec 16 2013 Jerry James <loganjerry@gmail.com> - 8.4pl3-1
- New upstream release

* Wed Oct 02 2013 Richard W.M. Jones <rjones@redhat.com> - 8.4pl2-4
- Rebuild for ocaml-lablgtk 2.18.

* Mon Sep 16 2013 Jerry James <loganjerry@gmail.com> - 8.4pl2-3
- Rebuild for OCaml 4.01.0
- Enable debuginfo

* Fri Jul 26 2013 Ville Skytt?? <ville.skytta@iki.fi> - 8.4pl2-2
- Install docs to %%{_pkgdocdir} where available.

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 8.4pl2-1
- New upstream release
- Harden the build due to network use

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 8.4pl1-3
- Remove --vendor from desktop-file-install in F19+  https://fedorahosted.org/fesco/ticket/1077

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4pl1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 8.4pl1-1
- New upstream release
- Drop upstreamed GDK patch
- Adapt configure arguments to new version
- Add csdp-tools requirement to get csdp binary

* Thu Dec 13 2012 Jerry James <loganjerry@gmail.com> - 8.4-3
- Use minimal TeXLive BRs

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 8.4-2
- Rebuild for OCaml 4.00.1
- Support more GDK key modifiers in the IDE (hyper, meta, release, super)
- New BRs due to the new texlive package layout
- Substitute the geometry package for fullpage.sty, which is not included in
  the latest Fedora TeXLive packages.

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 8.4-1
- New upstream release
- Drop patch; merged upstream
- Drop workaround for install bug; fixed in 8.4

* Fri Jul 27 2012 Jerry James <loganjerry@gmail.com> - 8.3pl4-3
- ProofGeneral dropped support for XEmacs, so we have to drop it too

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3pl4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 8.3pl4-2
- Rebuild for OCaml 4.00.0.

* Sat Jun  9 2012 Jerry James <loganjerry@gmail.com> - 8.3pl4-1
- New upstream release

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 8.3pl3-2
- Rebuild for Ocaml 3.12.1

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 8.3pl3-1
- New upstream release

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 8.3pl2-4
- Rebuild for new libpng

* Thu Oct 27 2011 Jerry James <loganjerry@gmail.com> - 8.3pl2-3
- Rebuild for new ocaml-camlp5; patch for bz 691913 no longer needed
- Drop tar_base_name, no longer necessary
- Drop versioned dependencies for packages that meet the dep in F14
- Build without HTML documentation on arches lacking hevea
- Change ExclusiveArch to %%{ocaml_arches}
- Fix a broken conditional and a typo

* Wed Jun 15 2011 Jerry James <loganjerry@gmail.com> - 8.3pl2-2
- Remove workaround for bad documentation link in 8.3pl1, fixed in 8.3pl2
- Revert change in 8.3pl1-1 to split arch-specific stuff from noarch stuff.
  Coq tactics are written in ocaml, which compiles to arch-specific files,
  and those files are stored in the same place as the noarch proof files.
- Move tutorial code into main package; it is small and we can then leave
  all the rest of the documentation as noarch

* Tue Apr 26 2011 Jerry James <loganjerry@gmail.com> - 8.3pl2-1
- New upstream release
- Change the list of supported arches to match the ocaml list, except for
  ppc64, which is missing hevea

* Mon Apr  4 2011 Jerry James <loganjerry@gmail.com> - 8.3pl1-2
- Change the mime type to application/x-coq, and inherit from text/plain
  (bz 530254)

* Thu Mar 31 2011 Jerry James <loganjerry@gmail.com> - 8.3pl1-1
- New upstream release
- Drop BuildRoot tag and clean section
- Drop all patches (all merged or otherwise fixed upstream)
- Comply with latest Ocaml packaging specs
- Identify xdg-open as the default web browser
- Comply with the emacs packaging guidelines, and build an XEmacs package
- The -doc and -emacs* subpackages are now noarch
- Workaround bug 691913
- Drop PostScript documentation; it's identical to PDF documentation
- Deal with arch-specific files in /usr/share; install everything to libdir,
  then move the noarch stuff to datadir, but leave symlinks behind
- Add a new mime type application/x-coqide and use it in the desktop file
- Add post and postun scripts

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2pl1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 05 2009 Alan Dunn <amdunn@gmail.com> - 8.2pl1-1
- New upstream release
- Eliminated modification of tar_base_name that occurred for only version 8.2
- Added reference to bugzilla bug for ppc64 ExcludeArch
- HTML form of documentation seems to no longer be distributed -> must generate
  Decided for consistency to generate all documentation
- Additional file for iconv - documentation license file
- Changed tutorial directory name, now also using bundled version
  of tutorial

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Alan Dunn <amdunn@gmail.com> - 8.2-1
- New upstream release
- Seems documentation license has changed or wasn't explicitly stated
  before, fixed (is ok Fedora license)
- Added versioning to documentation
- Removed special OCaml, TeX logic for Fedora < 9 (no longer relevant)
- Dropped makefile patch for compiling grammar.cma (fixed in Coq 8.2)
- Dropped cmxa-install patch (fixed in Coq 8.2)
- Changed makefile-strip patch and name (not yet fixed upstream...)
- Changed check.patch -> coq-check-(version).patch, slightly changed
  for 8.2 (not yet fixed upstream...)
- Dropped parser-renaming makefile-parser.patch, parser-man.patch
  (fixed in Coq 8.2)
- Dropped coq-lablgtk-2.12.patch (fixed in Coq 8.2)
- Changed way source (.v) files are installed
- Stopped addition of other icon file (icon fixed in Coq 8.2)
- Bytecode executables are now "clean" (not build with custom -> don't
  need to configure prelink around these)
- define -> global
- Added ExcludeArch sparc64

* Wed Jun 17 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org> 8.1pl4-3.1
- ExcludeArch s390, s390x as we don't have OCaml on those archs

* Wed Mar 04 2009 Alan Dunn <amdunn@gmail.com> - 8.1pl4-3
- Minor change to cmxa-install patch instruction
- Fixed to work with lablgtk 2.12

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1pl4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild 

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 8.1pl4-1
- New upstream version 8.1pl4.
- Attempt to rebuild against OCaml 3.11.0.
- Run make with VERBOSE=1 so we can see the actual commands.
- Pass -camlp5dir to configure so it uses camlp5 (overriding existence
  of camlp4 if it happens to be installed).

* Wed Oct 22 2008 Alan Dunn <amdunn@gmail.com> 8.1pl3-5
- Added Coq .v files into the main package at user request.

* Tue Sep 09 2008 Alan Dunn <amdunn@gmail.com> 8.1pl3-4
- Added creation of prelink blacklist for any bytecode files.
- Fixed execstack status for binaries.

* Tue Aug 05 2008 Alan Dunn <amdunn@gmail.com> 8.1pl3-3
- Changed parser to coq-parser to avoid name conflict with
  coda-client.
- Made make process noisy again.

* Sun Jul 20 2008 Alan Dunn <amdunn@gmail.com> 8.1pl3-2.1
- Minor bump for Fedora 8 to bring it into line with the rest.

* Thu Jul 17 2008 Alan Dunn <amdunn@gmail.com> 8.1pl3-2
- Added check for Fedora distribution number to allow for Fedora 8 release.

* Wed Jun 11 2008 Alan Dunn <amdunn@gmail.com> 8.1pl3-1
- Initial Fedora RPM version.
