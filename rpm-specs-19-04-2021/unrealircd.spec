%global sslcert %{_sysconfdir}/pki/%{name}/server.cert.pem
%global sslkey  %{_sysconfdir}/pki/%{name}/server.key.pem

Summary:        Open Source IRC server
Name:           unrealircd
Version:        5.0.9.1
Release:        1%{?dist}
# UnrealIRCd itself is GPLv2 but uses other source codes, breakdown:
# BSD: include/mempool.h and src/mempool.c
# ISC: src/openssl_hostname_validation.c
# MIT: include/openssl_hostname_validation.h
License:        GPLv2 and BSD and ISC and MIT
URL:            https://www.unrealircd.org/
Source0:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz
Source1:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-1D2D2B03A0B68ED11D68A24BA7A21B0A108FF4A9.gpg
Source3:        unrealircd.service
Source4:        unrealircd.tmpfilesd
Source10:       unrealircdctl
# Apply Fedora system-wide crypto policy
Patch0:         unrealircd-5.0.7-crypto-policy.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{_bindir}/openssl
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
BuildRequires:  pcre2-devel >= 10.00
BuildRequires:  libargon2-devel >= 20161029
BuildRequires:  c-ares-devel >= 1.6.0
BuildRequires:  libcurl-devel
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
Requires(pre):  shadow-utils
Requires(post): %{_bindir}/openssl

%description
UnrealIRCd is an Open Source IRC server based on the branch of IRCu called
Dreamforge, formerly used by the DALnet IRC network. Since the beginning of
development on UnrealIRCd in May of 1999, it has become a highly advanced
IRCd with a strong focus on modularity, an advanced and highly configurable
configuration file. Key features include SSL/TLS, cloaking, advanced anti-
flood and anti-spam systems, swear filtering and module support.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%if 0%{?fedora} || 0%{?rhel} >= 8
%patch0 -p1 -b .crypto-policy
touch -c -r doc/conf/examples/example.conf{.crypto-policy,}
%endif

%build
%if 0%{?rhel} == 7
sed \
  -e 's|include/openssl/|include/openssl11/openssl/|g' \
  -e 's|\(CRYPTOLIB="-lssl -lcrypto\).*|\1 -L%{_libdir}/openssl11"\nCFLAGS="$CFLAGS -I%{_includedir}/openssl11"|' \
  -i configure
%endif

# Remove pseudo check for ABI compatibility
sed -e '/do_version_check();/d' -i src/ircd.c

# Mention unrealircdctl compatibility shim rather script
for file in src/{conf,misc,modulemanager,modules,tls}.c doc/conf/examples/*.conf; do
  sed -e 's|./unrealircd |unrealircdctl |g' ${file} > ${file}.tmp
  touch -c -r ${file} ${file}.tmp && mv -f ${file}.tmp ${file}
done

%configure \
  --enable-ssl \
  --enable-libcurl \
  --with-bindir=%{_bindir} \
  --with-scriptdir=unused \
  --with-confdir=%{_sysconfdir}/%{name} \
  --with-modulesdir=%{_libdir}/%{name} \
  --with-logdir=%{_localstatedir}/log/%{name} \
  --with-cachedir=%{_localstatedir}/cache/%{name} \
  --with-tmpdir=%{_localstatedir}/lib/%{name}/tmp \
  --with-datadir=%{_localstatedir}/lib/%{name} \
  --with-docdir=unused \
  --with-pidfile=%{_rundir}/%{name}/%{name}.pid \
  --with-permissions=0640 \
  --enable-dynamic-linking \
  --with-privatelibdir=no
%make_build

%install
%make_install

# Fix strange default permissions
chmod -R g+rX,o+rX $RPM_BUILD_ROOT

# Provide default configuration based on default example
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{examples/example.conf,%{name}.conf}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/examples/

# Remove module repository configuration (for module manager)
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/modules.sources.list

# Remove upgrade script intended only for source code users
rm -f $RPM_BUILD_ROOT%{_bindir}/unrealircd-upgrade-script

# Move tls directory and symlink it
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/{%{name}/tls,pki/%{name}}/
ln -s ../pki/%{name}/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tls
ln -sf ../tls/certs/ca-bundle.crt $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}/curl-ca-bundle.crt

# Install systemd and tmpfiles files
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}/%{name}/

# Install compatibility shim for unrealircd script
install -D -p -m 0755 %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}/unrealircdctl

%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "UnrealIRCd" %{name}
exit 0

%post
%systemd_post %{name}.service

if [ ! -f %{sslkey} ]; then
  umask 077
  %{_bindir}/openssl genrsa 4096 > %{sslkey} 2> /dev/null
  chown root:%{name} %{sslkey}
  chmod 640 %{sslkey}
fi

if [ ! -f %{sslcert} ]; then
  FQDN=`hostname 2> /dev/null`
  if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
  fi

  %{_bindir}/openssl req -new -key %{sslkey} -x509 -sha256 -days 365 -set_serial $RANDOM -out %{sslcert} \
    -subj "/C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=${FQDN}/emailAddress=root@${FQDN}"
  chmod 644 %{sslcert}
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc doc/Authors doc/coding-guidelines doc/tao.of.irc
%doc README.md doc/RELEASE-NOTES.md
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%{_sysconfdir}/pki/%{name}/curl-ca-bundle.crt
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/*.conf
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/aliases/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/aliases/*.conf
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/help/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/help/*.conf
%{_sysconfdir}/%{name}/tls
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/unrealircdctl
%{_libdir}/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/cache/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/tmp/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%dir %attr(0755,%{name},%{name}) %{_rundir}/%{name}/

%changelog
* Fri Mar 26 2021 Robert Scheck <robert@fedoraproject.org> 5.0.9.1-1
- Upgrade to 5.0.9.1 (#1943492)

* Sun Mar 21 2021 Robert Scheck <robert@fedoraproject.org> 5.0.9-1
- Upgrade to 5.0.9 (#1938404)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.8-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Robert Scheck <robert@fedoraproject.org> 5.0.8-1
- Upgrade to 5.0.8 (#1911652)

* Sat Nov 07 2020 Robert Scheck <robert@fedoraproject.org> 5.0.7-2
- Remove build-time path from rpath (#1891370 #c1)
- Apply Fedora system-wide crypto policy (#1891370 #c1)
- License breakdown in spec file (#1891370 #c1)

* Sun Oct 18 2020 Robert Scheck <robert@fedoraproject.org> 5.0.7-1
- Upgrade to 5.0.7 (#1891370)

* Wed Apr 16 2008 Robert Scheck <robert@fedoraproject.org> 3.2.7-2
- Rebuild for openssl 0.9.8g and curl 7.18.0

* Thu Sep 06 2007 Robert Scheck <robert@fedoraproject.org> 3.2.7-1
- Upgrade to 3.2.7

* Sun Jun 10 2007 Robert Scheck <robert@fedoraproject.org> 3.2.6-2
- Rebuild for curl 7.16.2

* Sat Dec 23 2006 Robert Scheck <robert@fedoraproject.org> 3.2.6-1
- Upgrade to 3.2.6

* Sun Nov 05 2006 Robert Scheck <robert@fedoraproject.org> 3.2.5-2
- Enabled ziplinks and remote includes by linking zlib and curl

* Wed Nov 01 2006 Robert Scheck <robert@fedoraproject.org> 3.2.5-1
- Upgrade to 3.2.5 and rebuilt against glibc 2.5

* Sun May 07 2006 Robert Scheck <robert@fedoraproject.org> 3.2.4-3
- Added proxyscan 1.1 module for scanning open proxy servers (DNSBL,
  HTTP-CONNECT and -POST, Socks 4 and 5, Wingate and Cisco routers)

* Mon Mar 20 2006 Robert Scheck <robert@fedoraproject.org> 3.2.4-2
- Install Anope IRC Services aliases configuration files

* Thu Mar 16 2006 Robert Scheck <robert@fedoraproject.org> 3.2.4-1
- Upgrade to 3.2.4 and rebuilt against gcc 4.1 and glibc 2.4
- Re-added nocodes, privdeaf, ircops, sanick and timedbans modules
- Backported native cgiirc support from latest UnrealIRCd CVS

* Sat Oct 22 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-5
- Added timedbans 1.0 module to provide timebased channel bans
- Added cgiirc 1.7 module for hostname rewriting at CGI:IRC webchats
- Added cmdflood 1.8 module to limit the use of IRC commands
- Added chgswhois 1.3 module for easy changing SWHOIS information

* Sat Aug 27 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-4
- Added uline 1.13 module for allowing u:lined network admins
- Added netadmins 1.8 module for having unkillable netadmins
- Fixed IPv6 problem with gcc 4.0 in a sane way from UnrealIRCd CVS
- Added clones 1.8 module for displaying users with the same IP

* Sun Aug 21 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-3
- Added sanick 1.2 module for changing as IRC op a user's nickname
- Show nick!user@host of the person who set the topic, rather nick
- Added privdeaf 0.0.6 module for avoiding private messages/notices
- Added ircops 3.6 module for displaying a list of all IRC operators

* Tue Aug 09 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-2
- Added the nocodes 0.1 module for striping bold, underlined etc.
- Show the modes a channel has set in the /list output
- Rebuilt against gcc 4.0.1 and glibc 2.3.90

* Mon Mar 21 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-1
- Upgrade to 3.2.3 and rebuilt against gcc 4.0

* Sun Feb 06 2005 Robert Scheck <robert@fedoraproject.org> 3.2.2b-3
- Fixed system user creation and logging behaviour
- Adapted unrealircd.conf default configuration file

* Sun Jan 30 2005 Robert Scheck <robert@fedoraproject.org> 3.2.2b-2
- Fixed initscript

* Sun Jan 16 2005 Robert Scheck <robert@fedoraproject.org> 3.2.2b-1
- Upgrade to 3.2.2b

* Mon Nov 29 2004 Robert Scheck <robert@fedoraproject.org> 3.2.2-1
- Upgrade to 3.2.2
- Initial spec file for Red Hat Linux and Fedora Core
