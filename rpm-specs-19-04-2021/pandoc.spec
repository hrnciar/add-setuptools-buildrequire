# generated by cabal-rpm-2.0.6 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name pandoc
%global pkgver %{pkg_name}-%{version}

%global hsluamodulesystem hslua-module-system-0.2.1
%global ipynb ipynb-0.1.0.1
%global emojis emojis-0.1
%global jirawikimarkup jira-wiki-markup-1.1.4
%global basenoprelude base-noprelude-4.13.0.0
%global subpkgs %{hsluamodulesystem} %{ipynb} %{emojis} %{jirawikimarkup} %{basenoprelude}

# testsuite missing deps: base-noprelude tasty-golden tasty-lua

Name:           %{pkg_name}
Version:        2.9.2.1
# can only be reset when all subpkgs bumped
Release:        9%{?dist}
Summary:        Conversion between markup formats

License:        GPLv2+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{hsluamodulesystem}/%{hsluamodulesystem}.tar.gz
Source2:        https://hackage.haskell.org/package/%{ipynb}/%{ipynb}.tar.gz
Source3:        https://hackage.haskell.org/package/%{emojis}/%{emojis}.tar.gz
Source4:        https://hackage.haskell.org/package/%{jirawikimarkup}/%{jirawikimarkup}.tar.gz
Source5:        https://hackage.haskell.org/package/%{basenoprelude}/%{basenoprelude}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-HTTP-prof
BuildRequires:  ghc-HsYAML-prof
BuildRequires:  ghc-JuicyPixels-prof
BuildRequires:  ghc-SHA-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-compat-prof
#BuildRequires:  ghc-base-noprelude-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-cmark-gfm-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-doclayout-prof
BuildRequires:  ghc-doctemplates-prof
#BuildRequires:  ghc-emojis-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-haddock-library-prof
BuildRequires:  ghc-hslua-prof
#BuildRequires:  ghc-hslua-module-system-prof
BuildRequires:  ghc-hslua-module-text-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-types-prof
#BuildRequires:  ghc-ipynb-prof
#BuildRequires:  ghc-jira-wiki-markup-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-skylighting-prof
BuildRequires:  ghc-skylighting-core-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-tagsoup-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-texmath-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-conversions-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unicode-transforms-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-prof
BuildRequires:  ghc-zip-archive-prof
BuildRequires:  ghc-zlib-prof
Requires:       %{name}-common = %{version}-%{release}
# for missing dep 'hslua-module-system':
BuildRequires:  ghc-base-prof
# for missing dep 'ipynb':
BuildRequires:  ghc-base-prof
# for missing dep 'emojis':
BuildRequires:  ghc-base-prof
# for missing dep 'jira-wiki-markup':
BuildRequires:  ghc-base-prof
# for missing dep 'base-noprelude':
BuildRequires:  ghc-base-prof
# for missing dep 'doclayout':
BuildRequires:  ghc-base-prof
# for missing dep 'text-conversions':
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-errors-prof
# End cabal-rpm deps

%description
Pandoc is a Haskell library for converting from one markup format to another,
and a command-line tool that uses this library. It can read several dialects of
Markdown and (subsets of) HTML, reStructuredText, LaTeX, DocBook, JATS,
MediaWiki markup, DokuWiki markup, TWiki markup, TikiWiki markup, Jira markup,
Creole 1.0, Haddock markup, OPML, Emacs Org-Mode, Emacs Muse, txt2tags, ipynb
(Jupyter notebooks), Vimwiki, Word Docx, ODT, EPUB, FictionBook2, roff man,
Textile, and CSV, and it can write Markdown, reStructuredText, XHTML, HTML 5,
LaTeX, ConTeXt, DocBook, JATS, OPML, TEI, OpenDocument, ODT, Word docx,
PowerPoint pptx, RTF, MediaWiki, DokuWiki, XWiki, ZimWiki, Textile, Jira, roff
man, roff ms, plain text, Emacs Org-Mode, AsciiDoc, Haddock markup, EPUB (v2
and v3), ipynb, FictionBook2, InDesign ICML, Muse, LaTeX beamer slides, and
several kinds of HTML/JavaScript slide shows (S5, Slidy, Slideous, DZSlides,
reveal.js).

In contrast to most existing tools for converting Markdown to HTML, pandoc has
a modular design: it consists of a set of readers, which parse text in a given
format and produce a native representation of the document, and a set of
writers, which convert this native representation into a target format.
Thus, adding an input or output format requires only adding a reader or writer.

For pdf output please also install pandoc-pdf or weasyprint.


%package common
Summary:        %{name} common files
# templates are dual: GPLv2+ or BSD
# dzslides js and css: DWTFYWTPL
License: GPLv2+ and BSD
BuildArch:      noarch

%description common
This package provides the %{name} common data files.


%package -n ghc-%{name}
Summary:        Haskell %{name} library
Requires:       %{name}-common = %{version}-%{release}

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%package pdf
Summary:        Metapackage for pandoc pdf support
Requires:       %{name} = %{version}
Requires:       texlive-collection-latex
Requires:       texlive-ec
Obsoletes:      pandoc-markdown2pdf < %{version}-%{release}

%description pdf
This package pulls in the TeXLive latex package collection needed by
pandoc to generate pdf output using pdflatex.

To use --latex-engine=xelatex or lualatex, install texlive-collection-xetex
or texlive-collection-luatex respectively.


%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch

%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif


%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage %{hsluamodulesystem}
%ghc_lib_subpackage %{ipynb}
%ghc_lib_subpackage %{emojis}
%ghc_lib_subpackage %{jirawikimarkup}
%ghc_lib_subpackage -m %{basenoprelude}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -a1 -a2 -a3 -a4 -a5
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ifarch armv7hl
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=965121
# [101 of 166] Compiling Text.Pandoc.Writers.LaTeX
# ghc: out of memory (requested 1048576 bytes)
%define cabal_configure_options --ghc-options="-O0"
%endif
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%ghc_fix_rpath %{pkgver}
mv %{buildroot}%{_ghcdocdir}{,-common}
# End cabal-rpm install

rm %{buildroot}%{_datadir}/%{pkgver}/COPYRIGHT

ln -s pandoc %{buildroot}%{_bindir}/hsmarkdown

install -m 0644 -p -D man/pandoc.1 %{buildroot}%{_mandir}/man1/pandoc.1

echo %{_bindir}/jira-wiki-markup >> %{jirawikimarkup}/ghc-jira-wiki-markup.files
mv %{buildroot}%{_defaultlicensedir}/ghc-base-noprelude{,-devel}
echo "%%license %{basenoprelude}/LICENSE" >> %{basenoprelude}/ghc-base-noprelude-devel.files


%files
# Begin cabal-rpm files:
%{_bindir}/%{name}
# End cabal-rpm files
%{_bindir}/hsmarkdown
%{_mandir}/man1/pandoc.1*


%files common
# Begin cabal-rpm files:
%license COPYING.md
%doc AUTHORS.md BUGS CONTRIBUTING.md README.md changelog.md
%{_datadir}/%{pkgver}
# End cabal-rpm files

%files pdf


%files -n ghc-%{name} -f ghc-%{name}.files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license COPYING.md
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 21:12:58 +08 2020 Jens Petersen <petersen@redhat.com> - 2.9.2.1-8
- rebuild for cmark-gfm-0.2.2: fixes exponential parse (#1854329)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Jens Petersen <petersen@redhat.com> - 2.9.2.1-5
- https://hackage.haskell.org/package/pandoc-2.9.2.1/changelog
- subpackage base-noprelude
- bitarray and unicode-transforms were packaged

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 2.9.1.1-4
- https://hackage.haskell.org/package/pandoc-2.9.1.1/changelog
- new deps: doclayout, emojis, jira-wiki-markup, text-conversions

* Sun Feb 23 2020 Jens Petersen <petersen@redhat.com> - 2.7.3-3
- https://pandoc.org/releases.html#pandoc-2.7.3-2019-06-11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Jens Petersen <petersen@redhat.com> - 2.5-1
- update to 2.5
- subpackage HsYAML, unicode-transforms, bitarray

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 2.2.1-1
- update to 2.2.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Jens Petersen <petersen@redhat.com> - 2.1.2-2
- rebuild for static executable
- resurrect common subpackage

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 2.1.2-1
- update to 2.1.2

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-7
- Enable annotated build again

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-6
- Rebuilt for #1607054

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun  1 2018 Jens Petersen <petersen@redhat.com> - 2.0.6-4
- rebuild

* Thu May 31 2018 Jens Petersen <petersen@redhat.com> - 2.0.6-3
- no longer subpackage cmark-gfm and hslua-module-text

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 2.0.6-1
- update to 2.0.6
- subpackage 2 new deps

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 1.19.2.4-2
- refresh to cabal-rpm-0.12

* Thu Nov 16 2017 Jens Petersen <petersen@redhat.com> - 1.19.2.4-1
- update to 1.19.2.4
- uses skylighting instead of highlighting-kate

* Sun Oct 22 2017 Jens Petersen <petersen@fedoraproject.org> - 1.19.1-5
- doc-templates is now packaged in Fedora

* Tue Oct 10 2017 Jens Petersen <petersen@redhat.com> - 1.19.1-4
- enable https (#1497456)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 1.19.1-1
- update to 1.19.1

* Wed Feb 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.17.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
  to get back in sync with Haskell so-names

* Wed Feb  8 2017 Jens Petersen <petersen@redhat.com> - 1.17.0.3-4
- drop the static and common subpackages

* Sat Jan 07 2017 Adam Williamson <awilliam@redhat.com> - 1.17.0.3-3
- Rebuild for new ghc

* Thu Sep  8 2016 Jens Petersen <petersen@redhat.com> - 1.17.0.3-2
- bump release

* Mon Jun 27 2016 Jens Petersen <petersen@redhat.com> - 1.17.0.3-1
- update to 1.17.0.3

* Thu Jun 16 2016 Jens Petersen <petersen@redhat.com> - 1.16.0.2-4
- build with network-uri

* Mon May 02 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.16.0.2-3
- Rebuild for cmark 0.25

* Tue Apr 26 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.16.0.2-2
- Rebuild for ghc(tagsoup)

* Sat Mar 05 2016 Jens Petersen <petersen@redhat.com> - 1.16.0.2-1
- update to 1.16.0.2
- patches no longer needed
- move hsmarkdown and pandoc.1 to base package

* Thu Mar 03 2016 Adam Williamson <awilliam@redhat.com> - 1.13.2-6
- backport patches to allow build with newer haddock
- rebuild for new ghc-haddock

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.13.2-4
- Rebuild (aarch64 vector hashes)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Jens Petersen <petersen@fedoraproject.org> - 1.13.2-2
- rebuild

* Mon Jan 26 2015 Jens Petersen <petersen@redhat.com> - 1.13.2-1
- update to 1.13.2

* Thu Dec 11 2014 Jens Petersen <petersen@redhat.com> - 1.12.3.3-6
- add a static alternative subpackage and a common subpackage

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Adam Williamson <awilliam@redhat.com> - 1.12.3.3-3
- rebuild for new ghc-scientific

* Tue May 13 2014 Jens Petersen <petersen@redhat.com> - 1.12.3.3-2
- fix building on ARM (llvm) by using -O1 (#992430)

* Thu May 08 2014 Jens Petersen <petersen@redhat.com> - 1.12.3.3-1
- update to 1.12.3.3

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 1.12.3.1-1
- update to 1.12.3.1
- disable http-conduit

* Wed Aug 28 2013 Jens Petersen <petersen@redhat.com> - 1.11.1-6
- temporarily exclude armv7hl since build with ghc-7.6.3 and llvm-3.3 hanging
  mysteriously (#992430)

* Tue Aug 06 2013 Adam Williamson <awilliam@redhat.com> - 1.11.1-5
- rebuild for new libbibutils

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jens Petersen <petersen@redhat.com>
- update to new simplified Haskell Packaging Guidelines

* Wed May  1 2013 Jens Petersen <petersen@redhat.com> - 1.11.1-2
- pandoc-pdf now requires texlive-collection-latex and texlive-ec (#957876)

* Fri Mar 22 2013 Jens Petersen <petersen@redhat.com> - 1.11.1-1
- update to 1.11.1

* Sun Mar 10 2013 Jens Petersen <petersen@redhat.com> - 1.10.1-1
- update to 1.10.1
- allow blaze-html-0.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-4
- rebuild

* Mon Nov 19 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-3
- rebuild

* Wed Oct 31 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-2
- drop the latex template patch for old TeXLive

* Fri Oct 26 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-1
- update to 1.9.4.5
- refresh with cabal-rpm

* Fri Oct 26 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-6
- disable threaded rts with upstream patch copied from Debian (#862543)

* Tue Oct  2 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-5
- add a files section for the pdf subpackage so it is actually created

* Tue Oct  2 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-4
- add a pdf meta-subpackage for the texlive packages needed for pdf output

* Fri Sep 28 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-3
- also disable luatex in the default.beamer template (#861300)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-1
- update to 1.9.4.2
- add hsmarkdown symlink
- change prof BRs to devel

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.1-2
- rebuild

* Sun Jun 10 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.1-1
- update to 1.9.4.1

* Wed Apr 25 2012 Jens Petersen <petersen@redhat.com> - 1.9.2-1
- update to 1.9.2

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 1.9.1.2-1
- update to 1.9.1.2

* Wed Mar  7 2012 Jens Petersen <petersen@redhat.com> - 1.9.1.1-2
- rebuild

* Mon Feb 13 2012 Jens Petersen <petersen@redhat.com> - 1.9.1.1-1
- update to 1.9.1.1
  http://johnmacfarlane.net/pandoc/releases.html#pandoc-1.9-2012-02-05
- new depends on blaze-html, temporary, zlib
- markdown2pdf is now handled by pandoc itself:
  add README.fedora file documenting required texlive packages
- add changelog file

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.8.2.1-9
- Rebuild against PCRE 8.30

* Tue Feb  7 2012 Jens Petersen <petersen@redhat.com> - 1.8.2.1-8
- rebuild

* Thu Jan 26 2012 Jens Petersen <petersen@redhat.com> - 1.8.2.1-7
- set highlighting build flag by patching instead to help dependency tracking

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 1.8.2.1-6
- update to cabal2spec-0.25.2

* Thu Dec 22 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-5
- workaround texlive-2007 xelatex outputting to current dir

* Wed Nov 30 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-4
- add missing requires for pdflatex

* Thu Nov 17 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-3
- disable ifluatex in default.latex for texlive-2007 (Luis Villa, #752621)
- subpackage markdown2pdf and make it require texlive-xetex

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.8.2.1-2.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.8.2.1-2.1
- rebuild with new gmp

* Mon Oct  3 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-2
- rebuild against newer dependencies

* Thu Aug  4 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-1
- update to 1.8.2.1
- depends on base64-bytestring

* Wed Jul 27 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.2-3
- rebuild for xml-1.3.9

* Fri Jul 22 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.2-2
- rebuild for highlighting-kate-0.2.10

* Thu Jul 21 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.2-1
- update to 1.8.1.2

* Wed Jul 13 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.1-3
- build with code highlighting support using highlighting-kate

* Wed Jun 22 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.1-2
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Sat May 28 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.1-1
- update to 1.8.1.1
- update to cabal2spec-0.23: add ppc64
- new depends on citeproc-hs, dlist, json, pandoc-types, tagsoup
- new pandoc_markdown.5 manpage

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.6.0.1-5
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 1.6.0.1-4
- rebuild for latest zip-archive and haskell-platform-2011.1 updates

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Jens Petersen <petersen@redhat.com> - 1.6.0.1-2
- fix manpage perms (narasim)
- improve the summary (#652582)

* Fri Jan 14 2011 Jens Petersen <petersen@redhat.com> - 1.6.0.1-1
- 1.6.0.1
- add description
- update to cabal2spec-0.22.4

* Fri Nov 12 2010 Jens Petersen <petersen@redhat.com> - 1.6-1
- GPLv2+
- take care of docdir files
- add dependencies

* Thu Nov 11 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 1.6-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2