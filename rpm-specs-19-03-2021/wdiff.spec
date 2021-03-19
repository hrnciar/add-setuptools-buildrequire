%bcond_without rebuild_mans

Name:           wdiff
Version:        1.2.2
Release:        19%{?dist}
Summary:        Compare files on a word per word basis

# Entire source is GPLv3+, except wdiff.texi and the documentation built from
# it, including info, HTML, and PDF documentation, which is Latex2e.
License:        GPLv3+ and Latex2e
URL:            https://www.gnu.org/software/%{name}/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool  

BuildRequires:  gettext-devel
BuildRequires:  ncurses-devel

BuildRequires:  help2man
BuildRequires:  texinfo  
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)

BuildRequires:  gnupg2

#https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = 30.5.2012

%description
The GNU wdiff program is a front end to diff for comparing files on a word per
word basis. A word is anything between whitespace. This is useful for comparing
two texts in which a few words have been changed and for which paragraphs have
been refilled. It works by creating two temporary files, one word per line, and
then executes diff on these files. It collects the diff output and uses it to
produce a nicer display of word differences between the original files.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

# Fix ISO-8859-1-encoded files
tmp="$(mktemp)"
for fn in BACKLOG ChangeLog
do
  iconv --from=ISO-8859-1 --to=UTF-8 "${fn}" > "${tmp}"
  touch -r "${fn}" "${tmp}"
  cp -p "${tmp}" "${fn}"
done
rm "${tmp}"


%build
autoreconf -fiv
%configure --enable-experimental="mdiff wdiff2 unify" 
%make_build all

%if %{with rebuild_mans}
rm -v man/mdiff.1 man/%{name}.1 man/%{name}2.1 man/unify.1
%make_build -C man mdiff.1 %{name}.1 %{name}2.1 unify.1
%endif

# Make sure we rebuild the info page too.
rm -v doc/%{name}.info
%make_build -C doc info html pdf


%install
%make_install
find '%{buildroot}' -type f -name '*gnulib.mo' -print -delete
rm '%{buildroot}%{_infodir}/dir'
install -d '%{buildroot}%{_pkgdocdir}'
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 \
    ABOUT-NLS \
    AUTHORS \
    BACKLOG \
    ChangeLog \
    NEWS \
    README \
    THANKS \
    TODO
cp -rp doc/%{name}.html %{buildroot}%{_pkgdocdir}/html

%find_lang %{name}


%check
%make_build check


%files -f %{name}.lang
%license COPYING

%{_bindir}/mdiff
%{_bindir}/%{name}
%{_bindir}/%{name}2
%{_bindir}/unify

%{_mandir}/man1/mdiff.1*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}2.1*
%{_mandir}/man1/unify.1*

%{_infodir}/%{name}.info.*

%{_pkgdocdir}


%changelog
* Mon Feb 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.2-19
- Work around no “install -D” support in EPEL7

* Mon Feb 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.2-18
- Improve summary and description text
- Build HTML and PDF versions of the documentation
- Add Latex2e to License field

* Sun Feb 07 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.2-17
- Change URLs from HTTP to HTTPS
- Add source file signature verification
- Use %%make_build and %%make_install macros
- Reformatting and minor changes for personal style preference
- Fix man page glob
- Use less broad globs
- Add ABOUT-NLS, BACKLOG, and THANKS as %%doc files
- Rebuild configure script at build time
- Add a %%check section and run the tests
- Add ncurses-devel BR for termcap/curses support
- Add missing BR on gcc
- Rebuild man pages in RPM build
- Properly install license file (COPYING)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.2-12
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.2.2-1
- New release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.2.1-1
- New release 

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.1.2-1
- New release and fixed no bundled library issue

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.1.0-1
- New release

* Thu Oct 20 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-1
- New release

* Thu Sep 8 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.0-1
- New release

* Fri Mar 4 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-5
- Fix change log issue 

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-4
- Add find language tag

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-3
- Removed unnecessary -gnulib translation files.
- Rpmlint warning fixed for ChangeLog not utf8 file.
- Adding %%doc files

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-2
- Fix license,buildroot issue. Add find language tag.

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-1
- Initial version of the package
