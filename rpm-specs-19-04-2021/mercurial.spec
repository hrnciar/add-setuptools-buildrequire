Summary: Mercurial -- a distributed SCM
Name: mercurial
Version: 5.7.1
Release: 1%{?dist}

# Release: 1.rc1%%{?dist}

#% define upstreamversion %%{version}-rc
%define upstreamversion %{version}

License: GPLv2+
URL: https://mercurial-scm.org/
Source0: https://www.mercurial-scm.org/release/%{name}-%{upstreamversion}.tar.gz
Source1: mercurial-site-start.el
BuildRequires: make
BuildRequires: bash-completion
BuildRequires: emacs-el
BuildRequires: emacs-nox
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-docutils

Provides: hg = %{version}-%{release}
Requires: python3
Requires: emacs-filesystem

# TODO: drop these obsoletes in F36
Obsoletes: %{name}-py2 < %{version}-%{release}
Obsoletes: %{name}-py3 < %{version}-%{release}
Obsoletes: %{name}-lang < %{version}-%{release}
Provides: %{name}-py3 = %{version}-%{release}
Provides: %{name}-lang = %{version}-%{release}

%description
Mercurial is a fast, lightweight source control management system designed
for efficient handling of very large distributed projects.

Quick start: http://www.selenic.com/mercurial/wiki/index.cgi/QuickStart
Tutorial: http://www.selenic.com/mercurial/wiki/index.cgi/Tutorial
Extensions: http://www.selenic.com/mercurial/wiki/index.cgi/CategoryExtension


%package hgk
Summary:    Hgk interface for mercurial
Requires:   hg = %{version}-%{release}
Requires:   tk

%description hgk
A Mercurial extension for displaying the change history graphically
using Tcl/Tk.  Displays branches and merges in an easily
understandable way and shows diffs for each revision.  Based on
gitk for the git SCM.

Adds the "hg view" command.  See
http://www.selenic.com/mercurial/wiki/index.cgi/UsingHgk for more
documentation.


%package chg
Summary:    A fast client for Mercurial command server running on Unix. It saves time of slow Python startup.
Requires:   hg = %{version}-%{release}

%description chg
chg is a C wrapper for the hg command. Typically, when you type hg, a new
Python process is created, Mercurial is loaded, and your requested command runs
and the process exits.

With chg, a Mercurial command server background process is created that runs
Mercurial. When you type chg, a C program connects to that background process
and executes Mercurial commands.


%prep
%setup -q -n %{name}-%{upstreamversion}

%build
PYTHON=%{python3} make all

# chg will invoke the 'hg' command - no direct Python dependency
pushd contrib/chg
make
popd

%install
%{python3} setup.py install -O1 --root %{buildroot} --prefix %{_prefix} --record=%{name}.files
make install-doc DESTDIR=%{buildroot} MANDIR=%{_mandir}

grep -v -e 'hgk.py*' \
        -e "%{python3_sitearch}/mercurial/" \
        -e "%{python3_sitearch}/hgext/" \
        -e "%{python3_sitearch}/hgext3rd/" \
        -e "%{python3_sitearch}/hgdemandimport/" \
        -e "%{_bindir}" \
        < %{name}.files > %{name}-base.files
grep 'hgk.py*' < %{name}.files > %{name}-hgk.files

install -D -m 755 contrib/hgk       %{buildroot}%{_libexecdir}/mercurial/hgk
install -m 755 contrib/hg-ssh       %{buildroot}%{_bindir}

bash_completion_dir=%{buildroot}$(pkg-config --variable=completionsdir bash-completion)
mkdir -p $bash_completion_dir
install -m 644 contrib/bash_completion $bash_completion_dir/hg

zsh_completion_dir=%{buildroot}%{_datadir}/zsh/site-functions
mkdir -p $zsh_completion_dir
install -m 644 contrib/zsh_completion $zsh_completion_dir/_mercurial

mkdir -p %{buildroot}%{_emacs_sitelispdir}/mercurial

pushd contrib
for file in mercurial.el mq.el; do
  #emacs -batch -l mercurial.el --no-site-file -f batch-byte-compile $file
  %{_emacs_bytecompile} $file
  install -p -m 644 $file ${file}c %{buildroot}%{_emacs_sitelispdir}/mercurial
  rm ${file}c
done
popd

pushd contrib/chg
make install DESTDIR=%{buildroot} PREFIX=%{_usr} MANDIR=%{_mandir}/man1
popd


mkdir -p %{buildroot}%{_sysconfdir}/mercurial/hgrc.d

mkdir -p %{buildroot}%{_emacs_sitestartdir} && install -m644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

cat >hgk.rc <<EOF
[extensions]
# enable hgk extension ('hg help' shows 'view' as a command)
hgk=

[hgk]
path=%{_libexecdir}/mercurial/hgk
EOF
install -m 644 hgk.rc %{buildroot}%{_sysconfdir}/mercurial/hgrc.d

cat > certs.rc <<EOF
# see: http://mercurial.selenic.com/wiki/CACertificates
[web]
cacerts = /etc/pki/tls/certs/ca-bundle.crt
EOF
install -m 644 certs.rc %{buildroot}%{_sysconfdir}/mercurial/hgrc.d

mv %{buildroot}%{python3_sitearch}/mercurial/locale %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{python3_sitearch}/mercurial/locale

%find_lang hg

pathfix.py -pni "%{python3}" %{buildroot}%{_bindir}/hg-ssh


%files -f %{name}-base.files -f hg.lang
%doc CONTRIBUTORS COPYING doc/README doc/hg*.txt doc/hg*.html *.cgi contrib/*.fcgi contrib/*.wsgi
%doc %attr(644,root,root) %{_mandir}/man?/hg*.gz
%doc %attr(644,root,root) contrib/*.svg
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%{_datadir}/bash-completion/
%{_datadir}/zsh/site-functions/_mercurial
%{python3_sitearch}/mercurial/
%{python3_sitearch}/hgext/
%{python3_sitearch}/hgext3rd/
%{python3_sitearch}/hgdemandimport/
%{_emacs_sitelispdir}/mercurial
%{_emacs_sitestartdir}/*.el
%{_bindir}/hg
%{_bindir}/hg-ssh

%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/certs.rc

%files hgk -f %{name}-hgk.files
%{_libexecdir}/mercurial/
%{_sysconfdir}/mercurial/hgrc.d/hgk.rc

%files chg
%{_bindir}/chg
%doc %attr(644,root,root) %{_mandir}/man?/chg.*.gz


#%%check
# This will now fail everytime. Mercurial is not ported properly for Python3
# and current split of mercurial for Py2 and Py3 brings additional problems
# for extensions then pure Python3 packaging.
#cd tests && HGPYTHON3=1 %%{python3} run-tests.py


%changelog
* Tue Mar 09 2021 Mads Kiilerich <mads@kiilerich.com> - 5.7.1-1
- mercurial 5.7.1

* Wed Feb 03 2021 Mads Kiilerich <mads@kiilerich.com> - 5.7-1
- mercurial 5.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Petr Stodulka <pstodulk@redhat.com> - 5.6.1-6
- Set Provides for the obsoleted mercurial-py3 and mercurial-lang rpms
- Relates: #1917946

* Sun Jan  3 03:39:35 CET 2021 Mads Kiilerich <mads@kiilerich.com> - 5.6.1-5
- Stop providing hg3 - that is the only hg we have
- Drop alternatives - there is no alternative
- Move main package back to mercurial without py3 suffix
- Drop the -lang package

* Tue Dec  8 17:14:14 CET 2020 Mads Kiilerich <mads@kiilerich.com> - 5.6.1-4
- Change mercurial-hgk to use py3
- Use py3 for locales - py2 is going away
- Clarify in comment that chg has no py2/py3 concerns
- Drop comment left over from 53899096 when it introduced use of PYTHON=
- Let mercurial-py3 obsolete mercurial-py2 - it is going away soon
- Trivial removal of py2 package - no cleanup

* Sat Dec  5 14:50:30 CET 2020 Mads Kiilerich <mads@kiilerich.com> - 5.6.1-3
- Fix ownership of hgext3rd and hgdemandimport (#1897681)

* Thu Dec  3 21:24:26 CET 2020 Mads Kiilerich <mads@kiilerich.com> - 5.6.1-2
- Drop hgdemandimport_ast.patch - it has been fixed both in Mercurial 5.5.2 and
  Python 3.9.0rc2

* Thu Dec  3 20:39:41 CET 2020 Mads Kiilerich <mads@kiilerich.com> - 5.6.1-1
- mercurial 5.6.1

* Mon Nov 30 2020 Miro Hrončok <mhroncok@redhat.com> - 5.4-5
- Install Python 3 based mercurial by default

* Wed Sep 02 2020 Petr Viktorin <pviktori@redhat.com> - 5.4-4
- Add _ast to hgdemandimport ignore list
  Works around: BZ#1871992

* Mon Aug 10 2020 Petr Stodulka <pstodulk@redhat.com> - 5.4-3
- Fix upgrade from previous mercurial 4.9 causing broken alternatives for
  mercurial
- Resolves: #1831562

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Neal Becker <ndbecker2@gmail.com> - 5.4-1
- Update to 5.4

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2-3
- Remove stray Python 2 files from the Python 3 package

* Tue Nov 26 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2-2
- Use alternatives for /usr/bin/hg

* Mon Nov 25 2019 Petr Stodulka <pstodulk@redhat.com> - 5.2-1
- Update to 5.2
- Mercurial port is now much more stable on Python3 than before;
  still some issues can be discovered regarding the Python3
- Relates: #1737931

* Sat Oct 19 2019 Petr Stodulka <pstodulk@redhat.com> - 5.1.2-2
- first attempt to create builds for py2 & py3 version
- separate lang into the own subpackage as files are shared between
  mercurial for both pythons
- extensions are now prepared and working only under Python2
- the core mercurial is prepared in mercurial-python3 subpackage providing
  the hg3 executable
- Relates: #1737931

* Sat Oct 19 2019 Petr Stodulka <pstodulk@redhat.com> - 5.1.2-1
- Update to 5.1.2
- fix patching of Makefiles

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr  8 2019 Neal Becker <ndbecker2@gmail.com> - 4.9-1
- Update to 4.9

* Tue Mar  5 2019 Neal Becker <ndbecker2@gmail.com> - 4.7-3
- Fix shebang for python2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Petr Stodulka <pstodulk@redhat.com> - 4.7-1
- Update to 4.7

* Sat Aug 11 2018 Tom Prince <tom.prince@ualberta.net> - 4.5.3-1
- Package chg extension.

* Sat Aug 11 2018 Petr Stodulka <pstodulk@redhat.com> - 4.5.3-1
- Update to 4.5.3
- Resolves: CVE-2018-1000132

* Tue Jul 24 2018 Sebastian Kisela <skisela@redhat.com> - 4.4.2-6
- Stop using deprecated python macros: https://fedoraproject.org/wiki/Packaging:Python
- Add gcc build time dependency, as gcc was removed from default buildroot package set.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.4.2-4
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.4.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Dec 29 2017 Neal Becker <nbecker@nbecker2> - 4.4.2-1
- Update to 4.4.2

* Fri Aug 11 2017 Petr Stodulka <pstodulk@redhat.com> - 4.2.3-1
- Update to 4.2.3
- Resolves: CVE-2017-1000115 CVE-2017-1000116

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Neal Becker <nbecker@nbecker2> - 4.2.1-1
- Update to 4.2.1

* Mon Feb 27 2017 Neal Becker <nbecker@nbecker2> - 4.1-1
- Update to 4.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Neal Becker <nbecker@nbecker2> - 4.0.1-1
- Update to 4.0.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 03 2016 Neal Becker <ndbecker2@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 29 2016 Neal Becker <ndbecker2@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Thu Feb 25 2016 Neal Becker <ndbecker2@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Neal Becker <ndbecker2@gmail.com> - 3.6.3-1
- Update to 3.6.3

* Thu Dec 24 2015 Neal Becker <ndbecker2@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Fri Sep 11 2015 Neal Becker <ndbecker2@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Wed Aug 12 2015 Neal Becker <ndbecker2@gmail.com> - 3.5-1
- Update to 3.5

* Tue Jun 23 2015 Neal Becker <ndbecker2@gmail.com> - 3.4.1-1
- Update to 3.4.1
- Obsolete emacs-mercurial{-el}
- own _emacs_sitelispdir/mercurial
- use standard emacs macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr  3 2015 Neal Becker <ndbecker2@gmail.com> - 3.3.3-1
- update to 3.3.3

* Mon Mar 16 2015 Neal Becker <ndbecker2@gmail.com> - 3.3.2-1
- Update to 3.3.2
- upstream dropped mergetools.rc

* Sat Jan 24 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.2.3-2
- Install bash completion to %%{_datadir}/bash-completion/completions

* Sun Dec 21 2014 nbecker <ndbecker2@gmail.com> - 3.2.3-1
- Fixes CVE-2014-9390

* Tue Dec 16 2014 nbecker <ndbecker2@gmail.com> - 3.2-1
- Update to 3.2.2

* Sun Oct 19 2014 nbecker <ndbecker2@gmail.com> - 3.2-1.rc
- Patch0 no longer needed?
- Drop sample.hgrc (from upstream)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 nbecker <ndbecker2@gmail.com> - 3.0-1
- fix Release

* Fri May 30 2014 nbecker <ndbecker2@gmail.com> - 3.0-
- Update to 3.0

* Wed Feb  5 2014 nbecker <ndbecker2@gmail.com> - 2.9-1
- Update to 2.9

* Fri Nov  8 2013 nbecker <ndbecker2@gmail.com> - 2.8-1
- Update to 2.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  8 2013 nbecker <ndbecker2@gmail.com> - 2.6.3-1
- Update to 2.6.3


* Thu Jun 6 2013 nbecker <ndbecker2@gmail.com> - 2.6.2-1
- Update to 2.6.2

* Wed May  8 2013 nbecker <ndbecker2@gmail.com> - 2.6-1
- Update to 2.6

* Mon Mar 18 2013 nbecker <ndbecker2@gmail.com> - 2.5.2-2
- Add hgweb.wsgi

* Sat Mar  2 2013 nbecker <ndbecker2@gmail.com> - 2.5.2-1
- Update to 2.5.2

* Sat Feb  9 2013 Neal Becker <ndbecker2@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Tue Feb  5 2013 Neal Becker <ndbecker2@gmail.com> - 2.5-1
- Update to 2.5

* Sun Dec 16 2012 Neal Becker <ndbecker2@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Sun Nov  4 2012 Neal Becker <ndbecker2@gmail.com> - 2.4-1
- Update to 2.4

* Wed Sep  5 2012 Neal Becker <ndbecker2@gmail.com> - 2.3.1-1
- Update to 2.3.1

* Mon Aug 13 2012 Neal Becker <ndbecker2@gmail.com> - 2.3-1
- Update to 2.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  9 2012 Neal Becker <ndbecker2@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Sun Jun  3 2012 Neal Becker <ndbecker2@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Fri May 25 2012 Neal Becker <ndbecker2@gmail.com> - 2.2.1-2
- Add certs.rc

* Fri May  4 2012 Neal Becker <ndbecker2@gmail.com> - 2.2.1-1
- update to 2.2.1

* Wed May  2 2012 Neal Becker <ndbecker2@gmail.com> - 2.2-1
- Update to 2.2

* Fri Apr  6 2012 Neal Becker <ndbecker2@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Sat Mar 10 2012 Neal Becker <ndbecker2@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan  1 2012 Neal Becker <ndbecker2@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Wed Nov 16 2011 Neal Becker <ndbecker2@gmail.com> - 2.0-1
- Update to 2.0

* Tue Oct 11 2011 Neal Becker <ndbecker2@gmail.com> - 1.9.3-2
- Fix br 744931 (unowned dir)

* Sun Oct  2 2011 Neal Becker <ndbecker2@gmail.com> - 1.9.3-1
- update to 1.9.3

* Sat Aug 27 2011 Neal Becker <ndbecker2@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Wed Aug  3 2011 Neal Becker <ndbecker2@gmail.com> - 1.9.1-1
- Update to 1.9.1

* Fri Jul  1 2011 Neal Becker <ndbecker2@gmail.com> - 1.9-2
- Remove docutils patch

* Fri Jul  1 2011 Neal Becker <ndbecker2@gmail.com> - 1.9-1
- Update to 1.9

* Thu Jun  2 2011 Neal Becker <ndbecker2@gmail.com> - 1.8.4-2
- Add docutils-0.8 patch

* Wed Jun  1 2011 Neal Becker <ndbecker2@gmail.com> - 1.8.4-1
- Update to 1.8.4

* Sat Apr  2 2011 Neal Becker <ndbecker2@gmail.com> - 1.8.2-1
- update to 1.8.2

* Mon Mar 14 2011 Neal Becker <ndbecker2@gmail.com> - 1.8.1-2
- Try BR emacs-nox

* Mon Mar 14 2011 Neal Becker <ndbecker2@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Wed Mar  2 2011 Neal Becker <ndbecker2@gmail.com> - 1.8-1
- Update to 1.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb  5 2011 Neal Becker <ndbecker2@gmail.com> - 1.7.5-1
- Update to 1.7.5

* Sun Jan  2 2011 Neal Becker <ndbecker2@gmail.com> - 1.7.3-1
- Update to 1.7.3

* Thu Dec  2 2010 Neal Becker <ndbecker2@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Mon Nov 15 2010 Neal Becker <ndbecker2@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Mon Nov  1 2010 Neal Becker <ndbecker2@gmail.com> - 1.7-3
- BR python-docutils

* Mon Nov  1 2010 Neal Becker <ndbecker2@gmail.com> - 1.7-2
- Make that 1.7

* Mon Nov  1 2010 Neal Becker <ndbecker2@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Thu Oct 21 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.4-4
- Try another way to own directories

* Wed Oct 20 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.4-3
- Fixup unowned directories

* Wed Oct  6 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.4-3
- patch i18n.py so hg will find moved locale files

* Fri Oct  1 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.4-1
- Update to 1.6.4

* Fri Aug 27 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.3-1
- Fix some rpmlint issues

* Thu Aug 26 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.3-1
- Update to 1.6.3

* Mon Aug  2 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul  4 2010 Neal Becker <ndbecker2@gmail.com> - 1.6-2
- Remove hg-viz, git-rev-tree

* Sun Jul  4 2010 Neal Becker <ndbecker2@gmail.com> - 1.6-1
- Update to 1.6
- git-viz is removed

* Fri Jun 25 2010 Neal Becker <ndbecker2@gmail.com> - 1.5.4-1
- Don't install mercurial-convert-repo (use hg convert instead)

* Wed Jun  2 2010 Neal Becker <ndbecker2@gmail.com> - 1.5.4-1
- Update to 1.5.4

* Fri May 14 2010 Neal Becker <ndbecker2@gmail.com> - 1.5.3-1
- Update to 1.5.3

* Mon May  3 2010 Neal Becker <ndbecker2@gmail.com> - 1.5.2-1
- update to 1.5.2

* Mon Apr  5 2010 Neal Becker <ndbecker2@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Sat Mar  6 2010 Neal Becker <ndbecker2@gmail.com> - 1.5-2
- doc/ja seems to be gone

* Sat Mar  6 2010 Neal Becker <ndbecker2@gmail.com> - 1.5-1
- Update to 1.5

* Fri Feb  5 2010 Neal Becker <ndbecker2@gmail.com> - 1.4.3-2
- License changed to gplv2+

* Mon Feb  1 2010 Neal Becker <ndbecker2@gmail.com> - 1.4.3-1
- Update to 1.4.3

* Sat Jan  2 2010 Neal Becker <ndbecker2@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Wed Dec  2 2009 Neal Becker <ndbecker2@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Mon Nov 16 2009 Neal Becker <ndbecker2@gmail.com> - 1.4-1.1
- Bump to 1.4-1.1

* Mon Nov 16 2009 Neal Becker <ndbecker2@gmail.com> - 1.4-1
- Update to 1.4

* Fri Jul 24 2009 Neal Becker <ndbecker2@gmail.com> - 1.3.1-3
- Disable self-tests

* Fri Jul 24 2009 Neal Becker <ndbecker2@gmail.com> - 1.3.1-2
- Update to 1.3.1

* Wed Jul  1 2009 Neal Becker <ndbecker2@gmail.com> - 1.3-2
- Re-enable tests since they now pass

* Wed Jul  1 2009 Neal Becker <ndbecker2@gmail.com> - 1.3-1
- Update to 1.3

* Sat Mar 21 2009 Neal Becker <ndbecker2@gmail.com> - 1.2.1-1
- Update to 1.2.1
- Tests remain disabled due to failures

* Wed Mar  4 2009 Neal Becker <ndbecker2@gmail.com> - 1.2-2
- patch0 for filemerge bug should not be needed

* Wed Mar  4 2009 Neal Becker <ndbecker2@gmail.com> - 1.2-1
- Update to 1.2

* Tue Feb 24 2009 Neal Becker <ndbecker2@gmail.com> - 1.1.2-7
- Use noreplace option on config

* Mon Feb 23 2009 Neal Becker <ndbecker2@gmail.com> - 1.1.2-6
- Fix typo

* Mon Feb 23 2009 Neal Becker <ndbecker2@gmail.com> - 1.1.2-5
- Own directories bash_completion.d and zsh/site-functions
  https://bugzilla.redhat.com/show_bug.cgi?id=487015

* Mon Feb  9 2009 Neal Becker <ndbecker2@gmail.com> - 1.1.2-4
- Mark mergetools.rc as config

* Sat Feb  7 2009 Neal Becker <ndbecker2@gmail.com> - 1.1.2-3
- Patch mergetools.rc to fix filemerge bug

* Thu Jan  1 2009 Neal Becker <ndbecker2@gmail.com> - 1.1.2-2
- Rename mergetools.rc -> mergetools.rc.sample

* Thu Jan  1 2009 Neal Becker <ndbecker2@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Wed Dec 24 2008 Neal Becker <ndbecker2@gmail.com> - 1.1.1-3
- Install mergetools.rc as mergetools.rc.sample

* Sun Dec 21 2008 Neal Becker <ndbecker2@gmail.com> - 1.1.1-2
- Fix typo

* Sun Dec 21 2008 Neal Becker <ndbecker2@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-2
- Rebuild for Python 2.6

* Tue Dec  2 2008 Neal Becker <ndbecker2@gmail.com> - 1.1-1
- Update to 1.1

* Mon Dec  1 2008 Neal Becker <ndbecker2@gmail.com> - 1.0.2-4
- Bump tag

* Mon Dec  1 2008 Neal Becker <ndbecker2@gmail.com> - 1.0.2-3
- Remove BR asciidoc
- Use macro for python executable

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.2-2
- Rebuild for Python 2.6

* Fri Aug 15 2008 Neal Becker <ndbecker2@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Sun Jun 15 2008 Neal Becker <ndbecker2@gmail.com> - 1.0.1-4
- Bitten by expansion of commented out macro (again)

* Sun Jun 15 2008 Neal Becker <ndbecker2@gmail.com> - 1.0.1-3
- Add BR pkgconfig

* Sun Jun 15 2008 Neal Becker <ndbecker2@gmail.com> - 1.0.1-2
- Update to 1.0.1
- Fix emacs_version, etc macros (need expand)
- Remove patch0

* Mon Jun  2 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-15
- Bump release tag

* Thu Apr 17 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-14
- Oops, fix %%files due to last change

* Wed Apr 16 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-13
- install mergetools.hgrc as mergetools.rc

* Sat Apr 12 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-12
- Remove xemacs pkg - this is moved to xemacs-extras
- Own %%{python_sitearch}/{mercurial,hgext} dirs

* Thu Apr 10 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-11
- Use install -p to install .el{c} files
- Don't (load mercurial) by default.

* Wed Apr  9 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-10
- Patch to hgk from Mads Kiilerich <mads@kiilerich.com>

* Tue Apr  8 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-9
- Add '-l mercurial.el' for emacs also

* Tue Apr  8 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-8
- BR xemacs-packages-extra

* Tue Apr  8 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-7
- Various fixes

* Tue Apr  8 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-6
- fix to comply with emacs packaging guidelines

* Thu Mar 27 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-5
- Move hgk-related py files to hgk
- Put mergetools.hgrc in /etc/mercurial/hgrc.d
- Add hgk.rc and put in /etc/mercurial/hgrc.d

* Wed Mar 26 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-4
- Rename mercurial-site-start -> mercurial-site-start.el

* Wed Mar 26 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-3
- Incorprate suggestions from hopper@omnifarious.org

* Wed Mar 26 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-2
- Add site-start

* Tue Mar 25 2008 Neal Becker <ndbecker2@gmail.com> - 1.0-1
- Update to 1.0
- Disable check for now - 1 test fails
- Move emacs to separate package
- Add check

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.5-7
- Autorebuild for GCC 4.3

* Fri Nov  9 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.5-6
- rpmlint fixes

* Fri Nov  9 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.5-5
- /etc/mercurial/hgrc.d missing

* Fri Nov  9 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.5-3
- Fix to last change

* Fri Nov  9 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.5-2
- mkdir /etc/mercurial/hgrc.d for plugins

* Tue Oct 23 2007  <ndbecker2@gmail.com> - 0.9.5-2
- Bump tag to fix confusion

* Mon Oct 15 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.5-1
- Sync with spec file from mercurial

* Sat Sep 22 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.4-8
- Just cp contrib tree.
- Revert install -O2

* Thu Sep 20 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.4-7
- Change setup.py install to -O2 to get bytecompile on EL-4

* Thu Sep 20 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.4-6
- Revert last change.

* Thu Sep 20 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.4-5
- Use {ghost} on contrib, otherwise EL-4 build fails

* Thu Sep 20 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.4-4
- remove {_datadir}/contrib stuff for now

* Thu Sep 20 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.4-3
- Fix mercurial-install-contrib.patch (/usr/share/mercurial->/usr/share/mercurial/contrib)

* Wed Aug 29 2007 Jonathan Shapiro <shap@eros-os.com> - 0.9.4-2
- update to 0.9.4-2
- install contrib directory
- set up required path for hgk
- install man5 man pages

* Thu Aug 23 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.4-1
- update to 0.9.4

* Wed Jan  3 2007 Jeremy Katz <katzj@redhat.com> - 0.9.3-1
- update to 0.9.3
- remove asciidoc files now that we have them as manpages

* Mon Dec 11 2006 Jeremy Katz <katzj@redhat.com> - 0.9.2-1
- update to 0.9.2

* Mon Aug 28 2006 Jeremy Katz <katzj@redhat.com> - 0.9.1-2
- rebuild

* Tue Jul 25 2006 Jeremy Katz <katzj@redhat.com> - 0.9.1-1
- update to 0.9.1

* Fri May 12 2006 Mihai Ibanescu <misa@redhat.com> - 0.9-1
- update to 0.9

* Mon Apr 10 2006 Jeremy Katz <katzj@redhat.com> - 0.8.1-1
- update to 0.8.1
- add man pages (#188144)

* Fri Mar 17 2006 Jeremy Katz <katzj@redhat.com> - 0.8-3
- rebuild

* Fri Feb 17 2006 Jeremy Katz <katzj@redhat.com> - 0.8-2
- rebuild

* Mon Jan 30 2006 Jeremy Katz <katzj@redhat.com> - 0.8-1
- update to 0.8

* Thu Sep 22 2005 Jeremy Katz <katzj@redhat.com> 
- add contributors to %%doc

* Tue Sep 20 2005 Jeremy Katz <katzj@redhat.com> - 0.7
- update to 0.7

* Mon Aug 22 2005 Jeremy Katz <katzj@redhat.com> - 0.6c
- update to 0.6c

* Tue Jul 12 2005 Jeremy Katz <katzj@redhat.com> - 0.6b
- update to new upstream 0.6b

* Fri Jul  1 2005 Jeremy Katz <katzj@redhat.com> - 0.6-1
- Initial build.

