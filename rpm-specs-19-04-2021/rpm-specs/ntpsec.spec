Name:           ntpsec
Version:        1.2.0
Release:        7%{?dist}
Summary:        NTP daemon and utilities

# Primary license: MIT (NTP variant)
# attic/ntpdate: BSD
# include/{ascii,binio,ieee754io}.h: BSD
# include/{ntp_assert,isc_*.h}: ISC
# include/mbg_gps166.h: BSD
# include/ntp_{debug,endian,filegen}.h: BSD
# include/nts*.h: BSD
# include/parse*.h: BSD
# include/trimble.h: BSD
# libaes_siv: ASL 2.0
# libntp/emalloc.c: ISC
# libntp/ntp_{c,endian,random}.c: BSD
# libntp/pymodule*: BSD
# libntp/python_compatibility.h: BSD
# libntp/strl_obsd.c: ISC
# libparse: BSD
# ntpclients: BSD
# ntpd/ntp_config.c: BSD
# ntpd/ntp_dns.c: BSD
# ntpd/ntp_filegen.c: BSD
# ntpd/ntp_parser.y: BSD
# ntpd/ntp_sandbox.c: BSD
# ntpd/ntp_scanner.*: BSD
# ntpd/nts*.c: BSD
# ntpd/refclock_generic.c: BSD
# ntpd/refclock_jjy.c: BSD
# ntpd/refclock_oncore.c: Beerware (public domain)
# ntpd/refclock_trimble.c: BSD with advertising
# ntpfrob: BSD
# pylib: BSD
License:        MIT and BSD and BSD with advertising and ISC and ASL 2.0
URL:            https://www.ntpsec.org/
Source0:        https://ftp.ntpsec.org/pub/releases/ntpsec-%{version}.tar.gz
Source1:        https://ftp.ntpsec.org/pub/releases/ntpsec-%{version}.tar.gz.asc
Source2:        https://ftp.ntpsec.org/pub/releases/ntpsec.gpg.pub.asc
Source3:        ntp.conf

# Include associd in ntpq readvar output
Patch1:         ntpsec-ntpq-associd.patch
Patch2:         ntpsec-ntpq-raw.patch
# Improve ntpdate script
Patch3:         ntpsec-ntpdate.patch

BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcap-devel
BuildRequires:  m4
BuildRequires:  openssl-devel
BuildRequires:  pps-tools-devel
BuildRequires:  python3-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  systemd
BuildRequires:  waf

Requires(pre):  shadow-utils
%{?systemd_requires}

Conflicts:      ntp ntp-perl ntpdate
Obsoletes:      ntp < 4.2.10 ntp-perl < 4.2.10 ntp-doc < 4.2.10 ntpdate < 4.2.10 sntp < 4.2.10

# Set pool.ntp.org vendor zone for default configuration
%if 0%{!?vendorzone:1}
%global vendorzone %(source /etc/os-release && echo ${ID}.)
%endif

%description
NTPsec is a more secure and improved implementation of the Network Time
Protocol derived from the original NTP project.

%prep
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p1

# Fix egg info to use a shorter version which will work as an rpm provide
sed -i 's|NTPSEC_VERSION_EXTENDED|NTPSEC_VERSION|' pylib/ntp-in.egg-info

# Fix loading of the libntpc library
sed -i '/ntpc_paths = \[\]/s|\[\]|\["%{_libdir}/ntp/libntpc.so"\]|' pylib/ntpc.py

# Modify compiled-in statsdir
sed -i 's|/var/NTP|%{_localstatedir}/log/ntpstats|' \
        docs/includes/ntpd-body.adoc ntpd/ntp_util.c

%build
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"

waf configure \
        --enable-debug \
        --enable-debug-gdb \
        --disable-doc \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        ;

waf build

%install
waf --destdir=%{buildroot} install

install -p -m755 attic/ntpdate %{buildroot}%{_sbindir}/ntpdate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m644 etc/logrotate-config.ntpd \
        %{buildroot}%{_sysconfdir}/logrotate.d/ntpsec.conf

rm -rf %{buildroot}%{_docdir}

pushd %{buildroot}

sed -e 's|VENDORZONE\.|%{vendorzone}|' \
        -e 's|VARNTP|%{_localstatedir}/lib/ntp|' \
        < %{SOURCE3} > .%{_sysconfdir}/ntp.conf
touch -r %{SOURCE3} .%{_sysconfdir}/ntp.conf

for f in .%{_bindir}/*; do
        head -c 30 "$f" | grep -q python || continue
        %py3_shebang_fix "$f"
done

# Move ntpq to sbin for better compatibility with ntp package
mv .%{_bindir}/ntpq .%{_sbindir}/ntpq

mkdir -p .%{_localstatedir}/{lib/ntp,log/ntpstats}
touch .%{_localstatedir}/lib/ntp/ntp.drift

mkdir -p .%{_prefix}/lib/systemd/ntp-units.d
echo 'ntpd.service' > .%{_prefix}/lib/systemd/ntp-units.d/60-ntpd.list

popd

%check
waf check

%pre
# UID/GID inherited from the ntp package
/usr/sbin/groupadd -g 38 ntp 2> /dev/null || :
/usr/sbin/useradd -u 38 -g 38 -s /sbin/nologin -M -r \
        -d %{_localstatedir}/lib/ntp ntp 2>/dev/null || :

%post
%systemd_post ntpd.service ntp-wait.service
systemctl daemon-reload 2> /dev/null || :

%preun
%systemd_preun ntpd.service ntp-wait.service

%postun
%systemd_postun_with_restart ntpd.service

%global service_save_file /run/ntp-ntpsec.upgrade.services

%triggerprein -- ntp < 4.2.10
[ $1 = 0 ] || exit 0
# Save enabled ntp services and configuration (before our post)
for s in ntpd ntp-wait; do
        systemctl is-enabled -q "$s".service 2> /dev/null &&
                echo "$s" 2> /dev/null >> %{service_save_file}
done
rm -rf %{_sysconfdir}/ntp.ntpsec
cp -r --preserve=all %{_sysconfdir}/ntp %{_sysconfdir}/ntp.ntpsec 2> /dev/null
:

%triggerpostun -- ntp < 4.2.10
[ $2 = 0 ] || exit 0
# Restore the services and configuration from ntp (after its preun)
for s in ntpd ntp-wait; do
        grep -q "^$s$" %{service_save_file} 2> /dev/null &&
                systemctl enable -q "$s".service 2> /dev/null
done
rm -f %{service_save_file}
mv -f -T --backup=numbered %{_sysconfdir}/ntp.ntpsec %{_sysconfdir}/ntp
# Remove unsupported restrictions
sed -i.bak -E '/^restrict/s/no(e?peer|trap)//g' %{_sysconfdir}/ntp.conf
:

%files
%license LICENSE.adoc
%doc NEWS.adoc README.adoc
%config(noreplace) %{_sysconfdir}/ntp.conf
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/ntpsec.conf
%{_bindir}/ntp*
%{_sbindir}/ntp*
%dir %{_libdir}/ntp
%{_libdir}/ntp/libntpc.so*
%{_mandir}/man1/ntp*.1*
%{_mandir}/man5/ntp*.5*
%{_mandir}/man8/ntp*.8*
%{_unitdir}/ntp*.service
%{_unitdir}/ntp*.timer
%{_prefix}/lib/systemd/ntp-units.d/*ntpd.list
%dir %attr(-,ntp,ntp) %{_localstatedir}/lib/ntp
%ghost %attr(644,ntp,ntp) %{_localstatedir}/lib/ntp/ntp.drift
%dir %attr(-,ntp,ntp) %{_localstatedir}/log/ntpstats
%{python3_sitearch}/ntp-*.egg-info
%{python3_sitearch}/ntp

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 01 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-6
- change ntpdate defaults to follow classic ntpdate (#1917884)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-4
- include associd in ntpq readvar output (#1914901)
- fix ntpq crash in raw mode (#1914901)

* Wed Jan 06 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-3
- switch to flat default configuration
- save enabled services and configuration when replacing ntp
- move ntpdate and ntpq to /usr/sbin for better compatibility
- extend ntp conflicts and obsoletes

* Tue Dec 01 2020 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-2
- address issues found in package review (#1896368)

* Tue Nov 10 2020 Miroslav Lichvar <mlichvar@redhat.com> 1.2.0-1
- package ntpsec
