Name:           munin
Version:        2.0.67
Release:        2%{?dist}
Summary:        Network-wide resource monitoring tool
License:        GPLv2
URL:            http://munin-monitoring.org/

Source0:        http://downloads.munin-monitoring.org/munin/stable/%{version}/%{name}-%{version}.tar.gz
Source1:        http://downloads.munin-monitoring.org/munin/stable/%{version}/%{name}-%{version}.tar.gz.asc
# fpr=910846ADEE4C5D67C19B3E6F0A24C05998BA4133
# gpg --recv-keys $fpr
# gpg -a --export-options export-minimal --export $fpr >gpgkey-$fpr.asc
Source2:        gpgkey-910846ADEE4C5D67C19B3E6F0A24C05998BA4133.asc

# Master sources
Source10:       munin.conf
Source11:       munin.logrotate
Source12:       munin.tmpfilesd
Source13:       munin.timer
Source14:       munin.service
Source15:       munin-rrdcached.service
Source16:       httpd_cgi_graphs.conf
Source17:       httpd_cron_graphs.conf
Source18:       nginx_cgi_graphs.conf

# Node sources
Source20:       munin-node.conf
Source21:       munin-node.logrotate
Source23:       munin-node.service
Source25:       munin-asyncd.service
Source26:       munin-node.xml

# CGI sources
Source32:       munin-cgi-graph.service
Source33:       munin-cgi-graph.socket
Source34:       munin-cgi-html.service
Source35:       munin-cgi-html.socket

# Patches
Patch101:       21b3d860c17d7997d64267963f91ed75ca8a3e03.patch
Patch102:       postfix-category.patch
Patch103:       munin-run_no_systemd.patch

# Use some plugins from munin 3.0 branch
Source200:      mysql_

# Plugin config
Source300:      00-default
Source301:      munin-node

BuildRequires:  firewalld-filesystem
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::SNMP)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Net::Server)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 5.8
BuildRequires:  systemd

# Munin server requires
Requires:       %{name}-common = %{version}
Requires:       %{name}-web-support
Requires:       /bin/mail
Requires:       dejavu-sans-mono-fonts
Requires:       logrotate
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(DateTime)
Requires:       perl(Digest::MD5)
Requires:       perl(FCGI)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(Getopt::Long)
Requires:       perl(HTML::Template)
Requires:       perl(IO::Socket::INET6)
Requires:       perl(Net::SNMP)
Requires:       perl(Net::SSLeay)
Requires:       perl(Net::Server)
Requires:       perl(Params::Validate)
Requires:       perl(RRDs)
Requires:       perl(Storable)
Requires:       perl(Taint::Runtime)
Requires:       perl(Text::Balanced)
Requires:       perl(Time::HiRes)
Requires:       rrdtool
Requires(pre):  shadow-utils
%{?systemd_requires}

BuildArch:      noarch


%description
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains the grapher/gatherer. You will only need one instance of
it in your network. It will periodically poll all the nodes in your network
it's aware of for data, which it in turn will use to create graphs and HTML
pages, suitable for viewing with your graphical web browser of choice.

You must also install munin-nginx or munin-apache sub-package to generate
web graphs. See /usr/share/doc/munin-*/*.conf for example nginx/apache config
files and installation instructions.


%package node
Summary:        Network-wide resource monitoring tool (node)
Requires:       %{name}-common = %{version}
Requires:       /usr/bin/which
Requires:       bc
Requires:       conntrack-tools
Requires:       firewalld-filesystem
Requires:       hdparm
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Cache::Cache)
Requires:       perl(IO::Socket::INET6)
Requires:       perl(Net::CIDR)
Requires:       perl(Net::SSLeay)
Requires:       perl(Net::Server)
Requires:       procps
Requires:       sysstat
Requires(pre):  shadow-utils
%{?systemd_requires}
BuildArch:      noarch


%description node
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains node software. You should install it on all the nodes
in your network. It will know how to extract all sorts of data from the
node it runs on, and will wait for the gatherer to request this data for
further processing.

It includes a range of plugins capable of extracting common values such as
cpu usage, network usage, load average, and so on. Creating your own plugins
which are capable of extracting other system-specific values is very easy,
and is often done in a matter of minutes. You can also create plugins which
relay information from other devices in your network that can't run Munin,
such as a switch or a server running another operating system, by using
SNMP or similar technology.


%package common
Summary:        Network-wide resource monitoring tool (common files)
Requires:       acl
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires(pre):  shadow-utils
%{?systemd_requires}
BuildArch:      noarch


%description common
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains common files that are used by both the server (munin)
and node (munin-node) packages.


%package plugins-ruby
Summary:        Ruby plugins for Munin resource monitoring
Requires:       %{name}-node = %{version}
BuildArch:      noarch


%description plugins-ruby
Additional Ruby plugins for munin-node.


%package nginx
Summary:        NGINX support for Munin resource monitoring
Requires:       %{name} = %{version}
Requires:       munin-cgi
Requires:       nginx-filesystem
Provides:       munin-web-support = %{version}-%{release}
BuildArch:      noarch


%description nginx
NGINX support for Munin resource monitoring.


%package apache
Summary:        Apache support for Munin resource monitoring
Requires:       %{name} = %{version}
Requires:       httpd
Requires:       mod_fcgid
Provides:       munin-web-support = %{version}-%{release}
BuildArch:      noarch


%description apache
Apache support for Munin resource monitoring.


%package cgi
Summary:        FastCGI startup scripts for Munin resource monitoring
Requires:       %{name} = %{version}
Requires:       nginx-filesystem
%{?systemd_requires}
BuildArch:      noarch


%description cgi
FastCGI startup scripts for Munin resource monitoring. Use these with
NGINX to generate graphs on demand. Apache has built in support for
FastCGI so you don't need this package.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

sed -i -e '
  s,^PREFIX     = \(.*\),PREFIX     = $(DESTDIR)%{_prefix},;
  s,^CONFDIR    = \(.*\),CONFDIR    = $(DESTDIR)%{_sysconfdir}/munin,;
  s,^DOCDIR     = \(.*\),DOCDIR     = $(DESTDIR)%{_docdir}/%{name}-%{version},;
  s,^MANDIR     = \(.*\),MANDIR     = $(DESTDIR)%{_mandir},;
  s,^LIBDIR     = \(.*\),LIBDIR     = $(DESTDIR)%{_datadir}/munin,;
  s,^HTMLDIR    = \(.*\),HTMLDIR    = $(DESTDIR)%{_localstatedir}/www/html/munin,;
  s,^CGIDIR     = \(.*\),CGIDIR     = $(HTMLDIR)/cgi,;
  s,^DBDIR      = \(.*\),DBDIR      = $(DESTDIR)%{_sharedstatedir}/munin,;
  s,^DBDIRNODE  = \(.*\),DBDIRNODE  = $(DESTDIR)%{_sharedstatedir}/munin,;
  s,^LOGDIR     = \(.*\),LOGDIR     = $(DESTDIR)%{_localstatedir}/log/munin,;
%if 0%{?rhel} >= 8 || 0%{?fedora}
  s,^PYTHON     := \(.*\),PYTHON     := /usr/bin/python3,;
%else
  s,^PYTHON     := \(.*\),PYTHON     := /usr/bin/python2,;
%endif
  s,^RUBY       := \(.*\),RUBY       := /usr/bin/ruby,;
  s,^PERLLIB    = \(.*\),PERLLIB    = $(DESTDIR)%{perl_vendorlib},;
  s,^HOSTNAME   := \(.*\),HOSTNAME   := localhost.localdomain,;
  s,^PLUGINUSER := \(.*\),PLUGINUSER := munin,;
  s,^CGIUSER := \(.*\),CGIUSER    := munin,;
  s,^CHECKUSER  := \(.*\),CHECKUSER  := /bin/true,;
  s,^CHECKGROUP := \(.*\),CHECKGROUP := /bin/true,;
  s,^CHOWN      := \(.*\),CHOWN      := echo Not done: chown,;
  s,^CHMOD      := \(.*\),CHMOD      := echo Not done: chmod,;
  s,^CHGRP      := \(.*\),CHGRP      := echo Not done: chgrp,;
  s,^JC         := \(.*\),JC         := /bin/false,;
  ' Makefile.config

%patch101 -p1
%patch102 -p1
%patch103 -p1

cp %SOURCE16 .
cp %SOURCE17 .
cp %SOURCE18 .


%build
make CONFIG=Makefile.config


%install
make CONFIG=Makefile.config DESTDIR=%{buildroot} install

# Remove bundled fonts
rm -f %{buildroot}%{_datadir}/munin/DejaVuSans*.ttf


### Node ###

# Overwrite default config file
cp %{SOURCE20} %{buildroot}%{_sysconfdir}/munin/

# Install logrotate script
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp %{SOURCE21} %{buildroot}%{_sysconfdir}/logrotate.d/munin-node

# Add services
mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE23} %{buildroot}%{_unitdir}
cp %{SOURCE25} %{buildroot}%{_unitdir}

# Move munin-asyncd to /usr/sbin/ (FHS)
mv %{buildroot}%{_datadir}/munin/munin-asyncd %{buildroot}%{_sbindir}/munin-asyncd

# Remove the Sybase plugin for now, as they need perl modules that are not available
rm -f %{buildroot}%{_datadir}/munin/plugins/sybase_space

# Update some plugins from 3.0 branch
cp %{SOURCE200} %{buildroot}%{_datadir}/munin/plugins/

# Install plugin config
cp %{SOURCE300} %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/
cp %{SOURCE301} %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/

# Create plugin state dirs
mkdir -p %{buildroot}%{_sharedstatedir}/munin/plugin-state
mkdir -p %{buildroot}%{_sharedstatedir}/munin/plugin-state/munin
mkdir -p %{buildroot}%{_sharedstatedir}/munin/plugin-state/root

# firewalld config
mkdir -p %{buildroot}/%{_prefix}/lib/firewalld/services
cp %{SOURCE26} %{buildroot}/%{_prefix}/lib/firewalld/services/


# Disable some plugins from autoconfig
for i in if_err_ bonding_err_ yum ntp_ ntp_kernel_err ntp_kernel_pll_freq ntp_kernel_pll_off ntp_states nfsd; do
    sed -i -e 's/family=auto/family=manual/' %{buildroot}%{_datadir}/munin/plugins/$i
done

# Fix plugin charsets
for i in courier_mta_mailqueue courier_mta_mailstats courier_mta_mailvolume \
         dhcpd3 mysql_isam_space_ snmp__print_pages snmp__print_supplies \
         snmp__rdp_users tomcat_jvm; do
    fname="%{buildroot}%{_datadir}/munin/plugins/$i"
    iconv -f iso8859-1 -t UTF-8 $fname > $fname.tmp
    chmod --reference=$fname $fname.tmp
    mv -f $fname.tmp $fname
done


### Server ###

# Rename server's config directory
mv %{buildroot}%{_sysconfdir}/munin/munin-conf.d %{buildroot}%{_sysconfdir}/munin/conf.d

# Overwrite default config file
cp %{SOURCE10} %{buildroot}%{_sysconfdir}/munin/

# Install logrotate script
cp %{SOURCE11} %{buildroot}%{_sysconfdir}/logrotate.d/munin

# Install tmpfiles config
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_rundir}/munin
cp %{SOURCE12} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Add timer and service
cp %{SOURCE13} %{buildroot}%{_unitdir}
cp %{SOURCE14} %{buildroot}%{_unitdir}

# ssh for asyncd
mkdir -p %{buildroot}%{_sharedstatedir}/munin/.ssh

# rrdcached
mkdir -p %{buildroot}%{_sharedstatedir}/munin/rrdcached
cp %{SOURCE15} %{buildroot}%{_unitdir}

# Use UTF-8 in XML templates
for i in static/definitions.html templates/partial/head.tmpl; do
    sed -i -e 's/iso-8859-1/utf-8/g' %{buildroot}%{_sysconfdir}/munin/$i
done


### CGI ###

cp %{SOURCE32} %{buildroot}%{_unitdir}
cp %{SOURCE33} %{buildroot}%{_unitdir}
cp %{SOURCE34} %{buildroot}%{_unitdir}
cp %{SOURCE35} %{buildroot}%{_unitdir}


### Log files (ghost) ###

touch %{buildroot}%{_localstatedir}/log/munin/munin-cgi-graph.log
touch %{buildroot}%{_localstatedir}/log/munin/munin-cgi-html.log
touch %{buildroot}%{_localstatedir}/log/munin/munin-graph.log
touch %{buildroot}%{_localstatedir}/log/munin/munin-html.log
touch %{buildroot}%{_localstatedir}/log/munin/munin-limits.log
touch %{buildroot}%{_localstatedir}/log/munin/munin-update.log
mkdir -p %{buildroot}%{_localstatedir}/log/munin-node
touch %{buildroot}%{_localstatedir}/log/munin-node/munin-node.log


### Keep old apache munin.conf files (ghost) ###

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
touch %{buildroot}%{_sysconfdir}/httpd/conf.d/munin.conf
touch %{buildroot}%{_sysconfdir}/httpd/conf.d/munin-cgi.conf
touch %{buildroot}%{_sysconfdir}/munin/munin-htpasswd


%pre
getent group munin >/dev/null || groupadd -r munin
getent passwd munin >/dev/null || useradd -r -g munin -d %{_sharedstatedir}/munin -s /bin/sh -c "Munin user" munin
exit 0


%post
# Create log files
[ -f %{_localstatedir}/log/munin/munin-html.log ] || \
    /usr/bin/install -m 0640 -o munin -g adm /dev/null %{_localstatedir}/log/munin/munin-html.log
[ -f %{_localstatedir}/log/munin/munin-limits.log ] || \
    /usr/bin/install -m 0640 -o munin -g adm /dev/null %{_localstatedir}/log/munin/munin-limits.log
[ -f %{_localstatedir}/log/munin/munin-update.log ] || \
    /usr/bin/install -m 0640 -o munin -g adm /dev/null %{_localstatedir}/log/munin/munin-update.log
# On new install only: create simple localhost config.
if [ "$1" = "1" ]; then
    if [ ! -f %{_sysconfdir}/munin/conf.d/local.conf ]; then
        cat - >> %{_sysconfdir}/munin/conf.d/local.conf <<EOF
# Example host tree with localhost node. Configure your nodes here.

[localhost]
    address 127.0.0.1
    use_node_name yes
EOF
    fi
fi
%systemd_post munin-rrdcached.service munin.timer


%preun
%systemd_preun munin-rrdcached.service munin.timer


%postun
%systemd_postun_with_restart munin-rrdcached.service munin.timer


%pre node
getent group munin >/dev/null || groupadd -r munin
getent passwd munin >/dev/null || useradd -r -g munin -d %{_sharedstatedir}/munin -s /bin/sh -c "Munin user" munin
exit 0


%post node
# Create log file
[ -f %{_localstatedir}/log/munin-node/munin-node.log ] || \
    /usr/bin/install -m 0640 -o root -g adm /dev/null %{_localstatedir}/log/munin-node/munin-node.log
# Run configure only on a new install, not an upgrade.
if [ "$1" = "1" ]; then
    %{_sbindir}/munin-node-configure --shell 2> /dev/null | sh >& /dev/null || :
    # Clean up munin mysql_ plugin shmems and semaphores to fix selinux issue
    if [ -x %{_bindir}/ipcs -a -x %{_bindir}/ipcrm ]; then
        for mem in $(%{_bindir}/ipcs --shmems | grep munin | cut --delimiter=' ' --fields=1); do
            %{_bindir}/ipcrm --shmem-key ${mem} 2>/dev/null || :
        done
        for sem in $(%{_bindir}/ipcs --semaphores | grep munin | cut --delimiter=' ' --fields=1); do
            %{_bindir}/ipcrm --semaphore-key ${sem} 2>/dev/null || :
        done
    fi
fi
%firewalld_reload
%systemd_post munin-node.service munin-asyncd.service


%preun node
%systemd_preun munin-node.service munin-asyncd.service


%postun node
%systemd_postun_with_restart munin-node.service munin-asyncd.service


%pre common
getent group munin >/dev/null || groupadd -r munin
getent passwd munin >/dev/null || useradd -r -g munin -d %{_sharedstatedir}/munin -s /bin/sh -c "Munin user" munin
exit 0


%post nginx
# Create log files
[ -f %{_localstatedir}/log/munin/munin-cgi-graph.log ] || \
    /usr/bin/install -m 0660 -o munin -g munin /dev/null %{_localstatedir}/log/munin/munin-cgi-graph.log
[ -f %{_localstatedir}/log/munin/munin-cgi-html.log ] || \
    /usr/bin/install -m 0660 -o munin -g munin /dev/null %{_localstatedir}/log/munin/munin-cgi-html.log
[ -f %{_localstatedir}/log/munin/munin-graph.log ] || \
    /usr/bin/install -m 0660 -o munin -g munin /dev/null %{_localstatedir}/log/munin/munin-graph.log


%post apache
# Create log files
[ -f %{_localstatedir}/log/munin/munin-cgi-graph.log ] || \
    /usr/bin/install -m 0660 -o munin -g apache /dev/null %{_localstatedir}/log/munin/munin-cgi-graph.log
[ -f %{_localstatedir}/log/munin/munin-cgi-html.log ] || \
    /usr/bin/install -m 0660 -o munin -g apache /dev/null %{_localstatedir}/log/munin/munin-cgi-html.log
[ -f %{_localstatedir}/log/munin/munin-graph.log ] || \
    /usr/bin/install -m 0660 -o munin -g apache /dev/null %{_localstatedir}/log/munin/munin-graph.log


%post cgi
%systemd_post munin-cgi-graph.socket munin-cgi-graph.service
%systemd_post munin-cgi-html.socket munin-cgi-html.service


%preun cgi
%systemd_preun munin-cgi-graph.socket munin-cgi-graph.service
%systemd_preun munin-cgi-html.socket munin-cgi-html.service


%postun cgi
%systemd_postun_with_restart munin-cgi-graph.socket munin-cgi-graph.service
%systemd_postun_with_restart munin-cgi-html.socket munin-cgi-html.service


%files
%doc %{_mandir}/man5/munin.conf*
%doc %{_mandir}/man8/munin*
%dir %{_sysconfdir}/munin
%dir %{_sysconfdir}/munin/conf.d
%dir %{_sysconfdir}/munin/templates
%dir %{_sysconfdir}/munin/static
%{_unitdir}/munin.timer
%{_unitdir}/munin.service
%config(noreplace) %{_sysconfdir}/logrotate.d/munin
%config(noreplace) %{_sysconfdir}/munin/munin.conf
%config(noreplace) %{_sysconfdir}/munin/templates/*
%config(noreplace) %{_sysconfdir}/munin/static/*
%{_bindir}/munin-check
%{_bindir}/munin-cron
%dir %{_datadir}/munin
%{_datadir}/munin/munin-datafile2storable
%{_datadir}/munin/munin-graph
%{_datadir}/munin/munin-html
%{_datadir}/munin/munin-limits
%{_datadir}/munin/munin-storable2datafile
%{_datadir}/munin/munin-update
%{perl_vendorlib}/Munin/Master
%attr(-, munin, munin) %dir %{_sharedstatedir}/munin
%attr(0700, munin, munin) %dir %{_sharedstatedir}/munin/.ssh
%attr(0750, munin, adm) %dir %{_localstatedir}/log/munin
%attr(-, munin, munin) %dir %{_localstatedir}/www/html/munin
%attr(-, munin, munin) %{_localstatedir}/www/html/munin/cgi
%attr(0640, munin, adm) %ghost %{_localstatedir}/log/munin/munin-html.log
%attr(0640, munin, adm) %ghost %{_localstatedir}/log/munin/munin-limits.log
%attr(0640, munin, adm) %ghost %{_localstatedir}/log/munin/munin-update.log
%attr(-, munin, munin) %dir %{_sharedstatedir}/munin/rrdcached
%{_unitdir}/munin-rrdcached.service
%dir %{_datadir}/munin/plugins
%{_datadir}/munin/plugins/munin_stats
%config(noreplace) %ghost %{_sysconfdir}/munin/munin-htpasswd
%config(noreplace) %ghost %{_sysconfdir}/httpd/conf.d/munin.conf
%config(noreplace) %ghost %{_sysconfdir}/httpd/conf.d/munin-cgi.conf
%config(noreplace) %ghost %{_localstatedir}/www/html/munin/.htaccess


%files node
%doc %{_mandir}/man1/munin*
%doc %{_mandir}/man3/Munin*
%doc %{_mandir}/man5/munin-node.conf*
%dir %{_sysconfdir}/munin
%dir %{_sysconfdir}/munin/plugin-conf.d
%dir %{_sysconfdir}/munin/plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/munin-node
%config(noreplace) %{_sysconfdir}/munin/munin-node.conf
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/*
%{_unitdir}/munin-node.service
%{_unitdir}/munin-asyncd.service
%{_bindir}/munindoc
%{_bindir}/munin-get
%{_sbindir}/munin-node
%{_sbindir}/munin-node-configure
%{_sbindir}/munin-run
%{_sbindir}/munin-asyncd
%dir %{_datadir}/munin
%{_datadir}/munin/munin-async
%{_datadir}/munin/plugins/
%exclude %{_datadir}/munin/plugins/tomcat_
%exclude %{_datadir}/munin/plugins/munin_stats
%{perl_vendorlib}/Munin/Node
%{perl_vendorlib}/Munin/Plugin*
%{_prefix}/lib/firewalld/services/munin-node.xml
%attr(-, munin, munin) %dir %{_sharedstatedir}/munin
%attr(-, root, root) %dir %{_sharedstatedir}/munin/plugin-state
%attr(-, munin, root) %dir %{_sharedstatedir}/munin/plugin-state/munin
%attr(-, root, root) %dir %{_sharedstatedir}/munin/plugin-state/root
%attr(-, munin, munin) %dir %{_sharedstatedir}/munin/spool
%attr(0700, munin, munin) %dir %{_sharedstatedir}/munin/.ssh
%attr(0750, root, adm) %dir %{_localstatedir}/log/munin-node
%attr(0640, root, adm) %ghost %{_localstatedir}/log/munin-node/munin-node.log


%files common
%license COPYING
%doc ChangeLog HACKING.pod perltidyrc
%doc httpd_cgi_graphs.conf httpd_cron_graphs.conf nginx_cgi_graphs.conf
%dir %{perl_vendorlib}/Munin
%{perl_vendorlib}/Munin/Common
%{_tmpfilesdir}/%{name}.conf
%attr(0775, root, munin) %dir %{_rundir}/munin


%files plugins-ruby
%{_datadir}/munin/plugins/tomcat_


%files nginx
%attr(0775, munin, munin) %dir %{_sharedstatedir}/munin/cgi-tmp
%attr(0660, munin, munin) %ghost %{_localstatedir}/log/munin/munin-cgi-graph.log
%attr(0660, munin, munin) %ghost %{_localstatedir}/log/munin/munin-cgi-html.log
%attr(0660, munin, munin) %ghost %{_localstatedir}/log/munin/munin-graph.log


%files apache
%attr(0775, munin, apache) %dir %{_sharedstatedir}/munin/cgi-tmp
%attr(0660, munin, apache) %ghost %{_localstatedir}/log/munin/munin-cgi-graph.log
%attr(0660, munin, apache) %ghost %{_localstatedir}/log/munin/munin-cgi-html.log
%attr(0660, munin, apache) %ghost %{_localstatedir}/log/munin/munin-graph.log


%files cgi
%{_unitdir}/munin-cgi-graph.service
%{_unitdir}/munin-cgi-graph.socket
%{_unitdir}/munin-cgi-html.service
%{_unitdir}/munin-cgi-html.socket


%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.67-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 24 2021 Kim B. Heino <b@bbbs.net> - 2.0.67-1
- Upgrade to 2.0.67

* Fri Feb 05 2021 Todd Zullinger <tmz@pobox.com> - 2.0.66-1
- Upgrade to 2.0.66
- Verify upstream signature

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Kim B. Heino <b@bbbs.net> - 2.0.65-2
- Add plugin-state subdirs for munin and root

* Tue Nov 17 2020 Kim B. Heino <b@bbbs.net> - 2.0.65-1
- Upgrade to 2.0.65
- Improve plugin-state directory owners
- Don't require tmpwatch
- Change log file owner to root:adm or munin:adm

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 Kim B. Heino <b@bbbs.net> - 2.0.63-1
- Upgrade to 2.0.63
- Don't use systemd-run in munin-run, rhbz #1852345
- Use "Type=notify" for munin-node and munin-asyncd

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.54-5
- Perl 5.32 rebuild

* Tue Mar 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.54-4
- Specify all perl's dependencies for build

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Kim B. Heino <b@bbbs.net> - 2.0.54-2
- Convert cronjob to systemd timer and tmpfiles

* Tue Jan 21 2020 Kim B. Heino <b@bbbs.net> - 2.0.54-1
- Upgrade to 2.0.54
- Improve df's ignore list
- Use systemd hardening options for node and asyncd

* Sat Oct 19 2019 Kim B. Heino <b@bbbs.net> - 2.0.51-1
- Upgrade to 2.0.51

* Thu Oct 17 2019 Kim B. Heino <b@bbbs.net> - 2.0.50-2
- Revert 290650ee2c as it breaks munin-limits on rhel

* Thu Oct 17 2019 Kim B. Heino <b@bbbs.net> - 2.0.50-1
- Upgrade to 2.0.50

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Kim B. Heino <b@bbbs.net> - 2.0.49-3
- rhbz#1721384: Mark .htaccess as ghost, include it to example config files

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.49-2
- Perl 5.30 rebuild

* Thu May 16 2019 Kim B. Heino <b@bbbs.net> - 2.0.49-1
- Upgrade to 2.0.49

* Mon Mar 18 2019 Kim B. Heino <b@bbbs.net> - 2.0.45-2
- Drop munin-plugins-java subpackage

* Fri Feb  8 2019 Kim B. Heino <b@bbbs.net> - 2.0.45-1
- Upgrade to 2.0.45

* Mon Jan 28 2019 Kim B. Heino <b@bbbs.net> - 2.0.44-2
- Add smart_ plugin config to 00-default

* Thu Dec 20 2018 Kim B. Heino <b@bbbs.net> - 2.0.44-1
- Upgrade to 2.0.44

* Mon Nov 19 2018 Kim B. Heino <b@bbbs.net> - 2.0.43-1
- Upgrade to 2.0.43

* Sun Sep 30 2018 Kim B. Heino <b@bbbs.net> - 2.0.42-3
- Fix postfix and nginx categories

* Sat Sep 22 2018 Kim B. Heino <b@bbbs.net> - 2.0.42-2
- Change /run/munin owner to root:munin for clean update without dac override

* Fri Sep 21 2018 Kim B. Heino <b@bbbs.net> - 2.0.42-1
- Upgrade to 2.0.42

* Thu Sep 20 2018 Kim B. Heino <b@bbbs.net> - 2.0.41-1
- Upgrade to 2.0.41

* Mon Sep 17 2018 Kim B. Heino <b@bbbs.net> - 2.0.40-4
- rhbz#1327512: munin-limits not reporting actual state of variable to NSCA
- rhbz#1629438: Create localhost-config on first install
- rhbz#1629438: Include old httpd config files as ghost

* Fri Sep 14 2018 Kim B. Heino <b@bbbs.net> - 2.0.40-3
- rhbz#1628390: Fix missing Perl dependencies in Fedora
- Obsolete munin-netip-plugins for epel upgrade path

* Sat Aug 25 2018 Kim B. Heino <b@bbbs.net> - 2.0.40-2
- Fix upgrade path for munin-asyncd and force restart on first upgrade

* Fri Aug 24 2018 Kim B. Heino <b@bbbs.net> - 2.0.40-1
- Upgrade to 2.0.40
- This is major update with rpm package reorganize and directory changes

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.33-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.0.33-4
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.33-3
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.33-2
- Fix building on Perl without '.' in @INC

* Fri Mar 03 2017 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.33-1
- Upstream released 2.0.33

* Wed Mar 01 2017 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.32-1
- Upstream released 2.0.32

* Mon Feb 27 2017 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.30-5
- CVE-2017-6188: Upstream PR 797: Fix wrong parameter expansion in CGI
- RHBZ#: 1425855,1425857,1425858

* Fri Feb 10 2017 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.30-4
- added Pablo Chamorro packaging suggestions for helping CGI scripts

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.30-2
- RHBZ#: 1416199 - Munin-node is unable to determine FQDN hostname at boot

* Thu Jan 19 2017 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.30-1
- Upstream released 2.0.30

* Mon Jan 02 2017 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.29-1
- Upstream released 2.0.29
- RHBZ#: 1408492 - Munin 2.0.28 update breaks dynazoom

* Sat Dec 10 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.28-2
- RHBZ#: 1392279 - munin-node.rpm requires munin.rpm

* Mon Dec 05 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.28-1
- Upstream released 2.0.28

* Tue Nov 01 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.27-1
- Upstream released 2.0.27

* Tue Oct 11 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.26-4
- BZ# 1383219 - user nginx is not required for cgi

* Mon Oct 10 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.26-3
- BZ# 1339122 - Include PR-737 to fix hddtemp_smartctl until 2.0.27 is official
- BZ# 1383219 - user nginx is not required for cgi

* Mon Oct 10 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.26-2
- cgi subpackage requires spawn-fcgi

* Sun Sep 25 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.26-1
- Upstream released 2.0.26

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.25-12
- Perl 5.24 rebuild

* Sat Mar 12 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-11
- Moved /sbin/service to pre-systemd as well
- BZ# 1312121 - Munin dynamic graph zoom (dynazoom) failing due to Apache config.
- BZ# 1210767 - At least one file seems corrupt in version 2.0.25-2 and earlier
- BZ# 1269230 - hddtemp_smartctl fails to parse temperature from output

* Fri Mar 11 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-10
- EL5/6 do not need to install firewalld files
- BZ# 1315810 - postgresql plugin default configuration (contrib)

* Fri Mar 11 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-9
- BZ# 1315990 - Please remove unnecessary requirements for munin-node
- BZ# 1315951 - move /etc/tmpfiles.d/munin.conf to /usr/lib/tmpfiles.d

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-7
- Remove firewalld Require and associated script. EPEL7 does not have them.

* Thu Jan 21 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-6
- BZ# 1300379 - Please include firewalld service file for munin-node in RPM
  package

* Wed Sep 16 2015 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-5
- BZ# 1262751 - munin-common should be requires(pre) shadow-utils package
- munin-2.0.26-406c67e

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.25-3
- Perl 5.22 rebuild

* Sat Mar 07 2015 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-2
- Merge 2.1 patches back to 2.0
- BZ# 1149949 - munin-async init script to override defaults (PR-274 backport)
- BZ# 1049262 - munin ntp_ plugin uses perl features from perl 5.10.0 but can only use perl 5.8.8
- BZ# 1140015 - Munin mysql plugin fails to parse MariaDB status

* Tue Nov 25 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.25-1
- Upstream released 2.0.25

* Sun Oct 26 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.24-1
- Upstream released 2.0.24

* Sat Oct 18 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.23-1
- Upstream released 2.0.23

* Fri Oct 17 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.22-1
- Upstream released 2.0.22

* Tue Oct 07 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.21-8
- BZ# 1149948 - munin-async pid file in /var/run rather than /var/run/munin

* Mon Sep 15 2014 Petr Pisar <ppisar@redhat.com> - 2.0.21-6
- Build against perl 5.20

* Sun Sep 14 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.21-6
- Add amavis plugin config defaults

* Sun Sep 07 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.21-5
- BZ# 1114857 - munin-2.0.21-2.fc21 FTBFS: No Package found for java-1.7.0-devel
- re-merge earlier commit for epel7

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.21-4
- Perl 5.20 rebuild

* Fri Aug 01 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.21-3
- Default to a localhost name to prevent munin-node from complaining

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.0.21-1.1
- mx4j is not a build time dependency
- RHEL 7 Actually uses systemd too
- No Net::CIDR in el7
- No Cache::Memcached in el7
- Carp::Always is not actually required

* Fri Apr 25 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.21-1
- Upstream released 2.0.21

* Fri Mar 28 2014 "D. Johnson" <fenris02@fedoraproject.org> - 2.0.20-1
- Upstream released 2.0.20
- BZ# 1082162: munin-asyncd doesn't get added to chkconfig

* Wed Mar 26 2014 D. Johnson <fenris02@fedoraproject.org> - 2.0.19-2
- BZ# 1081254: Start asyncd after node
- BZ# 1028075: munin-node doesn't get added to chkconfig

* Sun Dec 08 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.19-1
- Upstream to 2.0.19

* Sun Dec 08 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.18-2
- Modifying hostname require for f21

* Sat Dec 07 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.18-1
- BZ# 1037890,1037889,1037888: CVE-2013-6359

* Tue Sep 24 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.17-6
- Move Net::IP plugins to a subpackage for dep handling

* Fri Aug 16 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.17-5
- BZ# 993985: munin possibly affected by F-20 unversioned docdir change

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 2.0.17-3
- Perl 5.18 rebuild

* Sat Jul 27 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 2.0.17-2
- BZ# 989080 Add a missing requirement on crontabs to spec file

* Sat Jul 20 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.17-1
- Upstream release 2.0.17

* Tue Jun 04 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.16-1
- Upstream released 2.0.16

* Sat Jun 01 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.15-1
- Upstream released 2.0.15

* Wed May 22 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.14-2
- Corrected bugid 905241 references

* Sat May 11 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.14-1
- Upstream released 2.0.14

* Fri Apr 26 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.13-1
- Upstream released 2.0.13

* Thu Apr 4 2013 Viljo Viitanen <viljo.viitanen@iki.fi> - 2.0.12-4
- BZ #905241 add nginx cgi package, removed unnecessary services from apache
  cgi package

* Mon Apr 01 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.12-3
- Add fw_ default config

* Sun Mar 24 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.12-2
- BZ# 917002 minor edits for asyncd

* Fri Mar 22 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.12-1
- Upstream release 2.0.12

* Sat Mar 09 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.11.1-3
- Update systemd scriptlets

* Fri Feb 22 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.11.1-2
- BZ# 913111 Removed R:webserver because it pulls boa .. and no clean way to
  prefer apache.
- BZ# 917002 munin-asyncd should wait for munin-node

* Sat Feb 09 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.11.1-1
- Upstream version 2.0.11.1

* Thu Feb 07 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.11-4
- BZ# 908711 munin-async: wrong path in init script

* Wed Feb 06 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.11-3
- Split out tomcat plugin to remove ruby dep from node.

* Mon Feb 04 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.11-2
- BZ# 907369 revert HTMLOld.pm patch

* Sun Feb 03 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.11-1
- Upstream release 2.0.11

* Mon Jan 21 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.10-2
- BZ# 896644 Wrong path to munin jar in jmx plugin

* Wed Jan 09 2013 D. Johnson <fenris02@fedoraproject.org> - 2.0.10-1
- Update to 2.0.10
- BZ# 891940,892377 Only stop/restart services provided by sub-package, not deps.
- BZ# 881689 Fix config file so that it no longer references the build host
- BZ# 877116 Patch using '&' in the URLs instead of '&amp;' in HTMLConfig

* Fri Dec 21 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.9-4
- Use Makefile.config-dist instead of sed.
- BZ# 890246,890247 "su" directive is not used in epel5/6 logrotate

* Sun Dec 09 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.9-3
- Add documentation links for async
- BZ# 885422 Move munin-node logs to /var/log/munin-node/
- BZ# 877166 Convert '&' to '&amp;' in HTMLConfig.pm for validation

* Thu Dec 06 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.9-2
- Require: LWP::UserAgent for plugins
- BZ# 861816 Add simplified files for switching to FCGI
- BZ# 880505 Change logrotate files to include su directive

* Thu Dec 06 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9

* Fri Nov 30 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.8-3
- BZ# 880505 munin logrotate permissions fix.

* Tue Nov 13 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.8-2
- Added cgitmp patch c/o Diego Elio Pettenò <flameeyes@flameeyes.eu>
- BZ# 861816 Add sample files for switching to FCGI

* Sun Nov 11 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.8-1
- Upstream to 2.0.8

* Sun Nov 04 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.7-6
- minor CGI permission fixes

* Sun Nov 04 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.7-5
- BZ# 872891 Re-add config file option to use conf.d/ instead of munin-conf.d/

* Fri Oct 26 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.7-4
- more CGI files to correct cgi-bin/
- BZ# 871967 Upstream 1235, Munin: unknown states on services for LimitsOld.pm
- BZ# 861816 Create CGI sub-package for dynamic graphing

* Fri Oct 19 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.7-3
- BZ# 859956 Minor fedora/rhel build macro fixes
- BZ# 861148 Upstream 1213, Incorrect child count in worker threads for GraphOld.pm and HTMLOld.pm

* Sun Oct 14 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.7-2
- Do not use 'env' for #! lines.
- Require: perl-Taint-Runtime to prevent warnings

* Sun Oct 07 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.7-1
- Upstream to 2.0.7
- BZ# 850401 Use systemd_preun when available (f18)
- BZ# 863490 [patch] http_load plugin uses wrong time command
- BZ# 862469 Move asyncd init files to asyncd subpackage

* Tue Sep 11 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.6-3
- Upstream removed dists/redhat/

* Sat Sep 08 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.6-2
- node: remove File::Path as it is no longer needed.
- added DBDIRNODE for munin-node.

* Fri Aug 31 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.6-1
- BZ# 851375 Replace @@GOODSH@@ in epel init scripts
- BZ# 849831,849834 CVE-2012-3512 munin: insecure state file handling, munin->root privilege [fedora-all]

* Mon Aug 20 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.5-3
- rebuilt for epel

* Tue Aug 14 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.5-2
- Added munin-asyncd init files

* Tue Aug 14 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.5-1
- Updated to 2.0.5
- BZ# 603344 / upstream 1180, ACPI thermal information changed with 3.x kernels

* Tue Aug 07 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.4-3
- BZ# 823533 "hddtemp_smartctl plugin has a bug" - upstream patched
- BZ# 825820 Munin memcache plugin requires "perl(Cache::Memcached)"
- BZ# 834055 Munin updates changing permissions, conflicts with what munin-check does
- BZ# 812893,812894,839786,840496 - updated to munin2

* Sun Aug 05 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.4-2
- Changing permissions on html directories to minimize cron messages.

* Sat Aug 04 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.4-1
- updated to 2.0.4
- backported el6 packaging items

* Tue Jul 24 2012 fenris02@fedoraproject.org - 2.0.3-1
- Adjust default conf.d entry.
- updated to 2.0.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 19 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.2-2
- fixed conflicts

* Sat Jul 14 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.2-1
- updated to 2.0.2

* Thu Jun 07 2012 D. Johnson <fenris02@fedoraproject.org> - 2.0.0-1
- initial 2.0 release

* Fri May 18 2012 D. Johnson <fenris02@fedoraproject.org> - 1.4.7-5
- BZ# 822992 Including GCTime.java.patch
- BZ# 747663 Include older cpuspeed.in for older kernels
- BZ# 822894 Requires: perl-Net-CIDR
- BZ# 746083 Append user=munin for munin-node plugins
- BZ# 821912 Move htaccess to httpd/conf.d/munin.conf for easier administration

* Sun May 13 2012 Kevin Fenzi <kevin@scrye.com> - 1.4.7-4
- Fix ownership on /var/run/munin. Fixes bug #821204

* Tue Apr 24 2012 Kevin Fenzi <kevin@scrye.com> - 1.4.7-3
- A better for for 811867 with triggers.
- Fix directory conflict. Fixes bug #816340
- Fix path in java plugin. Fixes bug #816570

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.4.7-2
- Fix node postun from messing up plugins on upgrade. Works around bug #811867

* Wed Mar 14 2012 D. Johnson <fenris02@fedoraproject.org> - 1.4.7-1
- updated for 1.4.7 release

* Wed Feb 22 2012 Kevin Fenzi <kevin@scrye.com> 1.4.6-8
- Build against java-1.7.0 now. Fixes bug #796345

* Tue Jan 31 2012 D. Johnson <fenris02@fedoraproject.org> - 1.4.6-7
- Create state file for yum-plugin. Fixes BZ #786030.

* Fri Jan 20 2012 Kevin Fenzi <kevin@scrye.com> - 1.4.6-6
- Add PrivateTmp=true to systemd unit file. Fixes bug #782512
- Change logrotate to use munin user. Fixes bug #771017

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-5.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.6-4.3
- Rebuild for java 1.6.0 downgrade (fesco ticket 663)

* Sat Aug 27 2011 Kevin Fenzi <kevin@scrye.com> - 1.4.6-4.1
- Add patch to run restorecon in the sysvinit script.
- This doesn't matter on f16+

* Sat Aug 20 2011 D. Johnson <fenris02@fedoraproject.org> - 1.4.6-4
- fix tmpfiles.d file for f15 (BZ# 731181)

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.4.6-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.4.6-2
- Perl mass rebuild

* Fri Jul 08 2011 D. Johnson <fenris02@fedoraproject.org> - 1.4.6-1
- update to 1.4.6

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.5-13
- Perl mass rebuild

* Wed Jun 15 2011 D. Johnson <fenris02@fedoraproject.org> - 1.4.5-12
- Use tmpfiles.d instead of ExecStartPre
- Add patch for noSuchObject errors (BZ# 712245)

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.5-11
- Perl 5.14 mass rebuild

* Wed Jun  1 2011 D. Johnson <fenris02@fedoraproject.org> - 1.4.5-10
- Fixes http://munin-monitoring.org/ticket/887

* Mon May 30 2011 D. Johnson <fenris02@fedoraproject.org> - 1.4.5-9
- Native systemd service file for munin-node (BZ# 699275)

* Tue Feb 08 2011 Kevin Fenzi <kevin@tummy.com> - 1.4.5-8
- Fix issue with uppercase node names returning no data. Fixes #673263

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 05 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-6
- Adjust the df fix to include all the right fses

* Thu Nov 25 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-5
- Exclude some fses from df plugin. fixes #601410

* Wed Aug 11 2010 Todd Zullinger <tmz@pobox.com> - 1.4.5-4.1
- Move jmx_ plugin to java-plugins package

* Wed Jul 07 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-4
- Move docs to common subpackage to make sure COPYING is installed.

* Sat Jul 03 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-3
- Add /etc/munin/node.d dir

* Sat Jun 12 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-2
- Add /etc/munin/conf.d/ dir

* Sat Jun 05 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-1
- Update to 1.4.5

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.4.4-2
- Mass rebuild with perl-5.12.0

* Mon Mar 01 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.4-1
- Update to 1.4.4
- Add more doc files. Fixes bug #563824
- fw_forwarded_local fixed upstream in 1.4.4. Fixes bug #568500

* Sun Jan 17 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.3-2
- Fix owner on state files.
- Add some BuildRequires.
- Make munin-node-configure only run on install, not upgrade. bug 540687

* Thu Dec 31 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.3-1
- Update to 1.4.3

* Thu Dec 17 2009 Ingvar Hagelund <ingvar@linpro.no> - 1.4.2-1
- New upstream release
- Removed upstream packaged fonts
- Added a patch that makes rrdtool use the system bitstream vera fonts on
  rhel < 6 and fedora < 11

* Fri Dec 11 2009 Ingvar Hagelund <ingvar@linpro.no> - 1.4.1-3
- More correct fedora and el versions for previous font path fix
- Added a patch that fixes a quoting bug in GraphOld.pm, fixing fonts on el4

* Wed Dec 09 2009 Ingvar Hagelund <ingvar@linpro.no> - 1.4.1-2
- Remove jmx plugins when not supported (like on el4 and older fedora)
- Correct font path on older distros like el5, el4 and fedora<11

* Fri Dec 04 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.1-1
- Update to 1.4.1

* Sat Nov 28 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.0-1
- Update to final 1.4.0 version

* Sat Nov 21 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.0-0.1.beta
- Update to beta 1.4.0 version.
- Add common subpackage for common files.

* Sun Nov 08 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.0-0.1.alpha
- Initial alpha version of 1.4.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Andreas Thienemann <andreas@bawue.net> - 1.2.6-8
- Updated dependencies to better reflect plugin requirements
- Added hddtemp_smartctl patch to only scan for standby state on /dev/[sh]d? devices.

* Sat Jan 17 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-7
- Adjust font requires for new dejavu-sans-mono-fonts name (fixes #480463)

* Mon Jan 12 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-6
- Fix to require the correct font

* Sun Jan 11 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-5
- Switch to using dejavu-fonts instead of bitstream-vera

* Sun Jan 04 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-4
- Require bitstream-vera-fonts-sans-mono for Font (fixes #477428)

* Mon Aug 11 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.6-3
- Move Munin/Plugin.pm to the node subpackage (fixes #457403)

* Sat Jul 12 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.6-2
- Apply postfix patch (fixes #454159)
- Add perl version dep and remove unneeded perl-HTML-Template (fixes #453923)

* Fri Jun 20 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.6-1
- Upgrade to 1.2.6

* Tue May 20 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.5-5
- Rebuild for new perl

* Wed Dec 26 2007 Kevin Fenzi <kevin@tummy.com> - 1.2.5-4
- Add patch to fix ampersand and degrees in plugins (fixes #376441)

* Fri Nov 30 2007 Kevin Fenzi <kevin@tummy.com> - 1.2.5-3
- Removed unnneeded plugins.conf file (fixes #288541)
- Fix license tag.
- Fix ip_conntrack monitoring (fixes #253192)
- Switch to new useradd guidelines.

* Tue Mar 27 2007 Kevin Fenzi <kevin@tummy.com> - 1.2.5-2
- Fix directory ownership (fixes #233886)

* Tue Oct 17 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.5-1
- Update to 1.2.5
- Fix HD stats (fixes #205042)
- Add in logrotate scripts that seem to have been dropped upstream

* Sun Aug 27 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-10
- Rebuild for fc6

* Tue Jun 27 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-9
- Re-enable snmp plugins now that perl-Net-SNMP is available (fixes 196588)
- Thanks to Herbert Straub <herbert@linuxhacker.at> for patch.
- Fix sendmail plugins to look in the right place for the queue

* Sat Apr 22 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-8
- add patch to remove unneeded munin-nagios in cron.
- add patch to remove buildhostname in munin.conf (fixes #188928)
- clean up prep section of spec.

* Fri Feb 24 2006 Kevin Fenzi <kevin@scrye.com> - 1.2.4-7
- Remove bogus Provides for perl RRDs (fixes #182702)

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-6
- Readded old changelog entries per request
- Rebuilt for fc5

* Sat Dec 24 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-5
- Fixed ownership for /var/log/munin in node subpackage (fixes 176529)

* Wed Dec 14 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-4
- Fixed ownership for /var/lib/munin in node subpackage

* Wed Dec 14 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-3
- Fixed libdir messup to allow builds on x86_64

* Mon Dec 12 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-2
- Removed plugins that require Net-SNMP and Sybase

* Tue Dec  6 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-1
- Inital cleanup for fedora-extras

* Thu Apr 21 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-4
- Fixed a bug in the iostat plugin

* Wed Apr 20 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-3
- Added the missing /var/run/munin

* Tue Apr 19 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-2
- Removed a lot of unecessary perl dependencies

* Mon Apr 18 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-1
- Sync with svn

* Tue Mar 22 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.2-5
- Sync with release of 1.2.2
- Add some nice text from the suse specfile
- Minimal changes in the header
- Some cosmetic changes
- Added logrotate scripts (stolen from debian package)

* Sun Feb 01 2004 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS. Version 1.0.0pre2

* Sun Jan 18 2004 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS. Change names to munin.

* Fri Oct 31 2003 Ingvar Hagelund <ingvar@linpro.no>
- Lot of small fixes. Now builds on more RPM distros

* Wed May 21 2003 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS
- 0.9.5-1

* Tue Apr  1 2003 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS
- Makefile-based install of core files
- Build doc (only pod2man)

* Thu Jan  9 2003 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS, auto rpmbuild

* Thu Jan  2 2003 Ingvar Hagelund <ingvar@linpro.no>
- Fix spec file for RedHat 8.0 and new version of lrrd

* Wed Sep  4 2002 Ingvar Hagelund <ingvar@linpro.no>
- Small bugfixes in the rpm package

* Tue Jun 18 2002 Kjetil Torgrim Homme <kjetilho@linpro.no>
- new package
