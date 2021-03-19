Name:           ifm
Version:        5.4
Release:        3%{?dist}
Summary:        Interactive Fiction Mapper

License:        GPLv2+
URL:            http://www.sentex.net/~dchapes/ifm/
Source0:        http://www.ifarchive.org/if-archive/mapping-tools/ifm-%{version}.tar.gz
Source1:        ifm.sh
Patch1:         ifm-5.4-destdir.patch
Patch2:         0001-Fix-variable-name-clash.patch
Patch3:         0003-Rename-dumb-frotz-to-dfrotz.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  perl-generators
BuildRequires:  tk
BuildRequires:  zlib-devel
BuildRequires:  automake
BuildRequires:  vim-filesystem
BuildRequires:  emacs-common
BuildRequires: make

# For dfrotz, used by rec2scr.pl
Recommends:     frotz

%description
IFM is a language and a program for keeping track of your progress through
an Interactive Fiction game.  You can record each room you visit and its
relation to other rooms, the initial locations of useful items you find, and
the tasks you need to perform in order to solve the game.

%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}


%install
%make_install ifmdocdir=%{_pkgdocdir}
# Bash completion
install -p -D -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/bash_completion.d/ifm.sh
# Emacs mode
install -p -D -m 0644 contrib/ifm-mode.el %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
# Vim syntax file
install -p -D -m 0644 contrib/ifm.vim %{buildroot}%{vimfiles_root}/syntax/%{name}.vim
# rec2scr.pl, a transcript-building tool included in contrib/
install -p -D -m 0755 contrib/rec2scr.pl %{buildroot}%{_bindir}/%{name}-rec2scr.pl

%files
%license COPYING
%{_pkgdocdir}
%{_bindir}/*
%{_datadir}/ifm/
%{_mandir}/man1/ifm.1*
%{_sysconfdir}/bash_completion.d/ifm.sh
%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
%{vimfiles_root}/syntax/%{name}.vim

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 5.4-1
- "New" upstream release (from 2009)
- Add flex as build-req (due to patched .l file)
- Update patches; install vim, emacs files; include rec2scr.pl tool

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 5.1-15
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Robert Scheck <robert@fedoraproject.org> - 5.1-9
- Solve the ppc64-redhat-linux-gnu configure target error

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.1-7
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.1-6
- Autorebuild for GCC 4.3

* Thu Sep 14 2006 Chris Grau <chris@chrisgrau.com> 5.1-5
- Rebuild for FC-6.

* Sun Aug  6 2006 Chris Grau <chris@chrisgrau.com> 5.1-4
- Fixed file permission issue (bug #200828).

* Wed Mar 01 2006 Chris Grau <chris@chrisgrau.com> 5.1-3
- Rebuild for FC-5.

* Mon Sep 26 2005 Chris Grau <chris@chrisgrau.com> 5.1-2
- Added tk as a BR for the wish requirement in configure.
- Fixed paths in man page to point to proper documentation.
- Replaced instance of /usr with %%{_prefix}.

* Sun Sep  4 2005 Chris Grau <chris@chrisgrau.com> 5.1-1
- Initial build.
