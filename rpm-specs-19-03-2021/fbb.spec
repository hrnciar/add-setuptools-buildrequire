#%%global prerel beta

# hardened build if not overridden
%{!?_hardened_build:%global _hardened_build 1}

Name:             fbb
URL:              https://sourceforge.net/projects/linfbb/
Version:          7.0.10
Release:          %{?prerel:0.}1%{?prerel:.%{prerel}}%{?dist}.2
License:          GPLv2+
Summary:          Packet radio mailbox and utilities
BuildRequires:    gcc
BuildRequires:    automake, libax25-devel, ncurses-devel, libX11-devel
BuildRequires:    libXt-devel, libXext-devel,libXpm-devel
%if 0%{?fedora} >= 24
BuildRequires:    motif-devel
%else
BuildRequires:    lesstif-devel
%endif
BuildRequires:    desktop-file-utils
BuildRequires:    systemd
BuildRequires: make
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Source0:          http://downloads.sourceforge.net/linfbb/%{name}-%{version}%{?prerel:-%{prerel}}.tar.bz2
Source1:          epurmess.ini
Source2:          fbb.service
Source3:          fbb-icon.svg
Source4:          fbb.desktop
Source5:          org.fbb.gui.policy
Source6:          README.Fedora
# Remove real callsigns
Patch2:           fbb-7.0.8-beta-sample-conf.patch
# Use /var/lib/fbb instead of /var/ax25/fbb
# /var/ax25 is currently not allowed by FHS, but it was requested
# to be added to the FHS
Patch3:           fbb-7.0.9-var-lib.patch
# Non interactive service start
Patch4:           fbb-7.0.10-non-interactive.patch
Patch5:           fbb-7.0.9-write-port-errors.patch
Patch6:           fbb-7.0.9-stdout.patch
Patch7:           fbb-7.0.9-ncurses-fix.patch

%description
F6FBB BBS software for bulletins and messages distribution via Packet Radio
and wired networks.

%package          doc
Requires:         %{name} = %{version}-%{release}
Summary:          Documentation for fbb
BuildArch:        noarch

%description doc
Documentation for fbb.

%package          gui
Requires:         %{name}%{?_isa} = %{version}-%{release}
Summary:          GUI for fbb

%description gui
GUI for fbb.

%prep
%setup -q -n %{name}-%{version}%{?prerel:-%{prerel}}
%patch2 -p1 -b .sample-conf
%patch3 -p1 -b .var-lib
%patch4 -p1 -b .non-interactive
%patch5 -p1 -b .write-port-errors
%patch6 -p1 -b .beta-stdout
%patch7 -p1 -b .ncurses-fix

cp %{SOURCE6} README.Fedora

# recode ISO-8859-15 (French) to UTF-8, reported upstream
for f in doc/satdoc-f.doc src/*.c include/*.h;
do
  iconv -f ISO8859-15 -t UTF8 -o $f.utf-8 $f
  mv $f.utf-8 $f
done

%build
autoreconf -fi
%configure
# -fcommon is workaround for gcc-10
make %{?_smp_mflags} CFLAGS="%{optflags} %{?_hardened_build:-pie} -fcommon" \
  LDFLAGS="%{?__global_ldflags} %{?_hardened_build:-pie -Wl,-z,relro,-z,now}"

%install
make install DESTDIR=%{buildroot}
make installconf DESTDIR=%{buildroot}

# Directories
mkdir -p %{buildroot}%{_var}/lib/fbb/{binmail/mail{0..9},docs,fbbdos/{readonly,yapp},\
log,mail/mail{0..9},oldmail,sat,wp}

# Install sample configuration files
mv %{buildroot}%{_docdir}/fbb/fbb.conf.sample %{buildroot}%{_sysconfdir}/ax25/fbb/fbb.conf
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/ax25/fbb/epurmess.ini
pushd %{buildroot}%{_sysconfdir}/ax25/fbb
mv port.sys.sample port.sys
cd lang
mv english.ent.sample english.ent
mv francais.ent.sample francais.ent
popd

# Systemd
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/fbb.service

# Icon
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/fbb.svg

# Desktop file
install -dD %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}

# Polkit policy
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_datadir}/polkit-1/actions/org.fbb.gui.policy

# Ghosts
touch %{buildroot}%{_var}/lib/fbb/{ERROR.SYS,dirmes.sys,etat.sys,heard.bin,inf.sys,\
statis.dat,themes.dat,tpstat.sys,wfbid.sys,sat/satel.dat,wp/wp.sys}

%post
%systemd_post fbb.service

%preun
%systemd_preun fbb.service

%postun
%systemd_postun_with_restart fbb.service

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_docdir}/%{name}/fbb.conf.min.sample
%{_docdir}/%{name}/fbb.sh
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/*.doc
%dir %{_sysconfdir}/ax25/fbb/
%dir %{_sysconfdir}/ax25/fbb/lang
%dir %{_sysconfdir}/ax25/fbb/fwd
%dir %{_var}/lib/fbb
%dir %{_var}/lib/fbb/docs
%dir %{_var}/lib/fbb/sat
%dir %{_var}/lib/fbb/wp
%{_var}/lib/fbb/binmail
%{_var}/lib/fbb/oldmail
%{_var}/lib/fbb/fbbdos
%{_var}/lib/fbb/mail
%{_var}/lib/fbb/log
%{_sbindir}/ajoursat
%{_sbindir}/fbbgetconf
%{_sbindir}/satupdat
%{_sbindir}/xfbbC
%{_sbindir}/fbb
%{_sbindir}/satdoc
%{_sbindir}/xfbbd
%{_mandir}/man1/*
%{_mandir}/man8/*
%config(noreplace) %{_sysconfdir}/ax25/fbb/fbb.conf
%config(noreplace) %{_sysconfdir}/ax25/fbb/port.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/epurmess.ini
%config(noreplace) %{_sysconfdir}/ax25/fbb/bbs.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/cron.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/fbbopt.conf
%config(noreplace) %{_sysconfdir}/ax25/fbb/forward.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/fwd/amsat.fwd
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/english.ent
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/english.hlp
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/english.inf
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/english.txt
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/francais.ent
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/francais.hlp
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/francais.inf
%config(noreplace) %{_sysconfdir}/ax25/fbb/lang/francais.txt
%config(noreplace) %{_sysconfdir}/ax25/fbb/langue.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/passwd.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/protect.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/redist.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/reject.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/swapp.sys
%config(noreplace) %{_sysconfdir}/ax25/fbb/themes.sys
%{_libdir}/fbb
%{_unitdir}/fbb.service
%ghost %{_var}/lib/fbb/sat/satel.dat
%ghost %{_var}/lib/fbb/wp/wp.sys
%ghost %{_var}/lib/fbb/ERROR.SYS
%ghost %{_var}/lib/fbb/dirmes.sys
%ghost %{_var}/lib/fbb/etat.sys
%ghost %{_var}/lib/fbb/heard.bin
%ghost %{_var}/lib/fbb/inf.sys
%ghost %{_var}/lib/fbb/statis.dat
%ghost %{_var}/lib/fbb/themes.dat
%ghost %{_var}/lib/fbb/tpstat.sys
%ghost %{_var}/lib/fbb/wfbid.sys

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/*.doc

%files gui
%doc README.Fedora
%{_sbindir}/xfbb
%{_sbindir}/xfbbX
%{_sbindir}/xfbbX_cl
%{_datadir}/icons/hicolor/scalable/apps/fbb.svg
%{_datadir}/applications/fbb.desktop
%{_datadir}/polkit-1/actions/org.fbb.gui.policy

%changelog
* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.10-1.2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.10-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.10-1
- New version
  Resolves: rhbz#1795008

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.9-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar  9 2020 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.9-2
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1799334

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.9-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.9-1
- New version
  Resolves: rhbz#1791020

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.7.beta.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.7.beta.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.7.beta.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.7.beta.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.8-0.7.beta.4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.7.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.7.beta.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.7.beta.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 22 2016 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.8-0.7.beta
- Preserve icon timestamp during installation and minor spec simplification

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-0.6.beta.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Richard Shaw <hobbes1069@gmail.com> - 7.0.8-0.6.beta
- Rebuild for new libax25.

* Wed Oct 14 2015 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.8-0.5.beta
- Replaced png icon by new scalable icon

* Thu Oct 08 2015 Ralf Cors??pius <corsepiu@fedoraproject.org> - 7.0.8-0.4.beta
- Build against motif on fedora >= 24.
- Reflect upstream having added fbb.conf.min.sample, fbb.sh to */doc (Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.8-0.3.beta.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.8-0.3.beta
- Added /var/lib/fbb/oldmail directory
- Added policykit policy for xfbb
- Other minor fixes according to fedora review

* Wed May 13 2015 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.8-0.2.beta
- Added icon and desktop files
- Other minor fixes according to fedora review

* Thu Apr 23 2015 Jaroslav ??karvada <jskarvad@redhat.com> - 7.0.8-0.1.beta
- Initial version
