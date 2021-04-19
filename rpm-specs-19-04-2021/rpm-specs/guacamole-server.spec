%global username guacd

# Can be rebuilt with FFmpeg/H264 support enabled by passing "--with=ffmpeg" to
# mock/rpmbuild; or by globally setting these variable:
#global _with_ffmpeg 1

Name:           guacamole-server
Version:        1.3.0
Release:        4%{?dist}
Summary:        Server-side native components that form the Guacamole proxy
License:        ASL 2.0
URL:            https://guacamole.apache.org/

Source0:        https://github.com/apache/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
# Included in 1.4.0:
Patch0:         https://github.com/apache/guacamole-server/commit/b2ae2fdf003a6854ac42877ce0fce8e88ceb038a.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  systemd-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freerdp-client2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtelnet)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(winpr2)

%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
}

%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

%package -n libguac
Summary:        The common library used by all C components of Guacamole

%description -n libguac
libguac is the core library for guacd (the Guacamole proxy) and any protocol
support plugins for guacd. libguac provides efficient buffered I/O of text and
base64 data, as well as somewhat abstracted functions for sending Guacamole
instructions.

%package -n libguac-devel
Summary:        Development files for %{name}
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-devel
The libguac-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libguac-client-kubernetes
Summary:        Kubernetes pods terminal support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-kubernetes
libguac-client-kubernetes is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for attaching to terminals of containers running
in Kubernetes pods.

%package -n libguac-client-rdp
Summary:        RDP support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-rdp
libguac-client-rdp is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for RDP, the proprietary remote desktop protocol used by
Windows Remote Deskop / Terminal Services, via the libfreerdp library.

%package -n libguac-client-ssh
Summary:        SSH support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-ssh
libguac-client-ssh is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for SSH, the secure shell.

%package -n libguac-client-vnc
Summary:        VNC support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-vnc
libguac-client-vnc is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for VNC via the libvncclient library (part of
libvncserver).

%package -n libguac-client-telnet
Summary:        Telnet support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-telnet
libguac-client-telnet is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for Telnet via the libtelnet library.

%package -n guacd
Summary:        Proxy daemon for Guacamole
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(pre):     shadow-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description -n guacd
guacd is the Guacamole proxy daemon used by the Guacamole web application and
framework to translate between arbitrary protocols and the Guacamole protocol.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure \
  --disable-silent-rules \
  --disable-static

%make_build
cd doc/
doxygen Doxyfile

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
cp -fr doc/doxygen-output/html .

mkdir -p %{buildroot}%{_sharedstatedir}/guacd

# Systemd unit files
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/guacd.service

%pre -n guacd
getent group %username >/dev/null || groupadd -r %username &>/dev/null || :
getent passwd %username >/dev/null || useradd -r -s /sbin/nologin \
    -d %{_sharedstatedir}/guacd -M -c 'Guacamole proxy daemon' -g %username %username &>/dev/null || :
exit 0

%post -n guacd
%systemd_post guacd.service

%preun -n guacd
%systemd_preun guacd.service

%postun -n guacd
%systemd_postun_with_restart guacd.service

%ldconfig_scriptlets -n libguac

%ldconfig_scriptlets -n libguac-client-kubernetes

%ldconfig_scriptlets -n libguac-client-rdp

%ldconfig_scriptlets -n libguac-client-ssh

%ldconfig_scriptlets -n libguac-client-vnc

%ldconfig_scriptlets -n libguac-client-telnet

%files -n libguac
%license LICENSE
%doc README CONTRIBUTING
%{_libdir}/libguac.so.*

%files -n libguac-devel
%doc html
%{_includedir}/guacamole
%{_libdir}/libguac.so

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".

%files -n libguac-client-kubernetes
%{_libdir}/libguac-client-kubernetes.so
%{_libdir}/libguac-client-kubernetes.so.*

%files -n libguac-client-rdp
%{_libdir}/libguac-client-rdp.so
%{_libdir}/libguac-client-rdp.so.*
%{_libdir}/freerdp2/*.so

%files -n libguac-client-ssh
%{_libdir}/libguac-client-ssh.so
%{_libdir}/libguac-client-ssh.so.*

%files -n libguac-client-vnc
%{_libdir}/libguac-client-vnc.so
%{_libdir}/libguac-client-vnc.so.*

%files -n libguac-client-telnet
%{_libdir}/libguac-client-telnet.so
%{_libdir}/libguac-client-telnet.so.*

%files -n guacd
%{_bindir}/guaclog
%{?_with_ffmpeg:
%{_bindir}/guacenc
%{_mandir}/man1/guacenc.1.*
}
%{_mandir}/man1/guaclog.1.*
%{_mandir}/man5/guacd.conf.5.*
%{_mandir}/man8/guacd.8.*
%{_sbindir}/guacd
%{_unitdir}/guacd.service
%attr(750,%{username},%{username}) %{_sharedstatedir}/guacd

%changelog
* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 1.3.0-4
- Rebuild for updated FreeRDP.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 2021 Simone Caronni <negativo17@gmail.com> - 1.3.0-1
- Update to 1.3.0.

* Sat Dec 26 2020 Simone Caronni <negativo17@gmail.com> - 1.2.0-3
- Do not ship deprecated sysconfig file.
- Trim changelog.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Simone Caronni <negativo17@gmail.com> - 1.2.0-1
- Update to 1.2.0.

* Fri May 22 2020 Simone Caronni <negativo17@gmail.com> - 1.1.0-6
- Rebuild for updated FreeRDP.

* Sat Feb 08 2020 Simone Caronni <negativo17@gmail.com> - 1.1.0-5
- Update to final 1.1.0, switch to FreeRDP 2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4.20190711git1a9d1e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-3.20190711git1a9d1e8
- Rebuild for libwebsockets 3.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.20190711git1a9d1e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Simone Caronni <negativo17@gmail.com> - 1.1.0-1.20190711git1a9d1e8
- Update to 1.1.0 snapshot, enable Kubernetes plugin.
- Fix license.
- Drop RHEL 6 support.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- Update to version 1.0.0.
