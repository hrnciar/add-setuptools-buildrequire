%global _hardened_build 1

%if 0%{?rhel} == 6
%global _rundir %{_localstatedir}/run
%endif

Name:       pgbouncer
Version:    1.14.0
Release:    7%{?dist}
Summary:    Lightweight connection pooler for PostgreSQL
License:    MIT and BSD
URL:        https://www.pgbouncer.org

Source0:    %{url}/downloads/files/%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}.init
Source2:    %{name}.sysconfig
Source3:    %{name}.logrotate
Source4:    %{name}.service
Source5:    %{name}.service.el7
Source6:    %{name}.pam

Patch0:     %{name}-ini.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libevent)

%if 0%{?fedora} || 0%{?rhel} >= 7

# For Fedora systemd-rpm-macros would be enough:
BuildRequires:      systemd-devel
Requires:           systemd

%else

Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts
Requires(postun):   initscripts

%endif

Requires(pre):      shadow-utils
Requires:           logrotate

%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:           python3-psycopg2
%else
Requires:           python-psycopg2
%endif

%description
pgbouncer is a lightweight connection pooler for PostgreSQL and uses libevent
for low-level socket handling.

%prep
%autosetup -p0

%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i -e 's|/usr/bin/env python|%__python3|g' etc/mkauth.py
%else
sed -i -e 's|/usr/bin/env python|%__python2|g' etc/mkauth.py
%endif


%build
# Building with systemd flag tries to enable notify support which is not
# available on RHEL/CentOS 7.
%configure \
    --enable-debug \
    --with-pam \
%if 0%{?fedora} || 0%{?rhel} >= 8
    --with-systemd
%endif

%make_build V=1

%install
%make_install

# Configuration
install -p -d %{buildroot}%{_sysconfdir}/%{name}/
install -p -d %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 640 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -p -m 640 etc/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}
install -p -m 600 etc/userlist.txt %{buildroot}%{_sysconfdir}/%{name}
install -p -m 700 etc/mkauth.py %{buildroot}%{_sysconfdir}/%{name}/

# Install pam configuration file
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -p -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/%{name}

# Temporary folder
mkdir -p %{buildroot}%{_rundir}/%{name}

# Log folder
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

%if 0%{?fedora} || 0%{?rhel} >= 7

# systemd unit
install -d %{buildroot}%{_unitdir}
%if 0%{?rhel} == 7
install -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
%else
install -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
%endif

# tmpfiles.d configuration
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d %{_rundir}/%{name} 0755 %{name} %{name} -
EOF

%else

# SysV script
install -p -d %{buildroot}%{_initrddir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%endif

# logrotate file
install -p -d %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%pre
getent group %{name} >/dev/null || groupadd -r %{name} &>/dev/null || :
getent passwd %{name} >/dev/null || useradd -r -s /sbin/nologin \
    -d / -M -c "PgBouncer Server" -g %{name} %{name} &>/dev/null || :
exit 0

%if 0%{?fedora} || 0%{?rhel} >= 7

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%else

%post
/sbin/chkconfig --add %{name}

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service %{name} condstop >/dev/null 2>&1
    chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ] ; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi

%endif

%files
%license COPYRIGHT
%doc NEWS.md README.md doc/*.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/mkauth.py*
%config(noreplace) %attr(600,%{name},%{name}) %{_sysconfdir}/%{name}/%{name}.ini
%config(noreplace) %attr(600,%{name},%{name}) %{_sysconfdir}/%{name}/userlist.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}.*
%attr(700,%{name},%{name}) %{_localstatedir}/log/%{name}

%if 0%{?fedora} || 0%{?rhel} >= 7
%attr(755,%{name},%{name}) %dir %{_rundir}/%{name}
%ghost %{_rundir}/%{name}/%{name}.pid
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif

%changelog
* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.14.0-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 20:42:50 CEST 2020 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.14.0-5
- Rebuilt for libevent 2.1.12

* Tue Sep 15 2020 Devrim G??nd??z <devrim@gunduz.org> - 1.14.0-4
- Rebuild against new libevent

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Simone Caronni <negativo17@gmail.com> - 1.14.0-2
- Do not enable notify support on RHEL/CentOS 7.

* Wed Jul 22 2020 Simone Caronni <negativo17@gmail.com> - 1.14.0-1
- Update to 1.14.0.
- Update URL.
- Enable systemd support at compile time so notify/socket support is built in.

* Thu Jul 02 2020 Simone Caronni <negativo17@gmail.com> - 1.13.0-2
- Enable notify in systemd unit.

* Fri May 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.13.0-1
- Update to new upstream version 1.13.0

* Thu Apr 23 2020 Simone Caronni <negativo17@gmail.com> - 1.12.0-5
- Change configuration file permissions and also add a template user list.

* Wed Apr 15 2020 Simone Caronni <negativo17@gmail.com> - 1.12.0-4
- Update SPEC file (build & runtime requirements, macros, rpmlint fixes, etc.).
- Fix build on RHEL/CentOS 6/7/8.
- Do not use a normal home folder and shell for the user.
- Do not remove/change files in the scriptlets.
- Do not start in daemon mode in systemd units.
- Trim changelog.

* Wed Mar 04 2020 Aaron Burnett <golanv@adelie.io> - 1.12.0-3
- Fixes bug #1810267
- Fixes bug #1801301

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 3 2019 Devrim G??nd??z <devrim@gunduz.org> - 1.12.0-1
- Update to 1.12.0
- Fix bz #1736426

* Fri Aug 9 2019 Devrim G??nd??z <devrim@gunduz.org> - 1.10.0-1
- Update to 1.10.0
- Use more macros.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 4 2019 Devrim G??nd??z <devrim@gunduz.org> - 1.9.0-1
- Update to 1.9.0
* Mon Feb 4 2019 Devrim G??nd??z <devrim@gunduz.org> - 1.9.0-1
- Update to 1.9.0
- Add patch for Python3 compatibility.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
