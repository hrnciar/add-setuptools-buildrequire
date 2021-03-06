%bcond_with devel

%global basever 1.13.1
#%%global rcnum   0

Name:           syncthing
Summary:        Continuous File Synchronization
Version:        %{basever}%{?rcnum:~rc%{rcnum}}
Release:        2%{?dist}

%global goipath github.com/syncthing/syncthing
%global tag     v%{basever}%{?rcnum:-rc.%{rcnum}}

%gometa

# syncthing (MPLv2.0) bundles
# - angular, bootstrap, daterangepicker, fancytree, jQuery, moment (MIT),
# - ForkAwesome (MIT and OFL and CC-BY 3.0), and
# - a number of go packages (MIT and MPLv2.0 and BSD and ASL 2.0 and CC0 and ISC)
License:        MPLv2.0 and MIT and OFL and CC-BY and BSD and ASL 2.0 and CC0 and ISC

URL:            https://syncthing.net
# use official release tarball (contains vendored dependencies)
Source0:        %{gourl}/releases/download/%{tag}/%{name}-source-%{tag}.tar.gz

# rejected patch to fix tests running out of memory on 32 bit arches
# See: https://github.com/syncthing/syncthing/issues/6209
Patch0:         https://github.com/imsodin/syncthing/commit/0d64427.patch

BuildRequires:  desktop-file-utils
BuildRequires:  systemd

%{?systemd_requires}

# assets in gui/default/vendor/*
Provides:       bundled(angular) = 1.3.20
Provides:       bundled(angular-dirPagination) = 759009c
Provides:       bundled(angular-sanitize) = 1.3.20
Provides:       bundled(angular-translate) = 2.9.0.1
Provides:       bundled(angular-translate-loader-static-files) = 2.11.0
Provides:       bundled(bootstrap) = 3.3.6
Provides:       bundled(daterangepicker) = 3.0.0
Provides:       bundled(ForkAwesome) = 1.1.2
Provides:       bundled(jquery) = 2.2.2
Provides:       bundled(jquery-fancytree) = 2.28.1
Provides:       bundled(jquery-ui) = 1.12.1
Provides:       bundled(moment) = 2.19.4

# automatically generated Provides for bundled go dependencies
# manually check licenses for new deps and update License tag if necessary
# generate with "./vendor2provides.py path/to/vendor/modules.txt")

# github.com/AudriusButkevicius/pfilter : MIT
Provides:       bundled(golang(github.com/AudriusButkevicius/pfilter)) = c55ef61
# github.com/AudriusButkevicius/recli : MPLv2.0
Provides:       bundled(golang(github.com/AudriusButkevicius/recli)) = 0.0.5
# github.com/Azure/go-ntlmssp : MIT
Provides:       bundled(golang(github.com/Azure/go-ntlmssp)) = 6637195
# github.com/DataDog/zstd : BSD
Provides:       bundled(golang(github.com/DataDog/zstd)) = 1.4.1
# github.com/StackExchange/wmi : MIT
Provides:       bundled(golang(github.com/StackExchange/wmi)) = cbe6696
# github.com/beorn7/perks : MIT
Provides:       bundled(golang(github.com/beorn7/perks)) = 1.0.1
# github.com/bkaradzic/go-lz4 : BSD
Provides:       bundled(golang(github.com/bkaradzic/go-lz4)) = 7224d8d
# github.com/calmh/xdr : MIT
Provides:       bundled(golang(github.com/calmh/xdr)) = 1.1.0
# github.com/ccding/go-stun : ASL 2.0
Provides:       bundled(golang(github.com/ccding/go-stun)) = 0.1.2
# github.com/certifi/gocertifi : MPLv2.0
Provides:       bundled(golang(github.com/certifi/gocertifi)) = 2c3bb06
# github.com/cespare/xxhash : MIT
Provides:       bundled(golang(github.com/cespare/xxhash)) = 1.1.0
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = 2.1.1
# github.com/cheekybits/genny : MIT
Provides:       bundled(golang(github.com/cheekybits/genny)) = 1.0.0
# github.com/chmduquesne/rollinghash : MIT
Provides:       bundled(golang(github.com/chmduquesne/rollinghash)) = a60f8e7
# github.com/cpuguy83/go-md2man : MIT
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = f79a8a8
# github.com/d4l3k/messagediff : MIT
Provides:       bundled(golang(github.com/d4l3k/messagediff)) = 1.2.1
# github.com/dchest/siphash : CC0
Provides:       bundled(golang(github.com/dchest/siphash)) = 1.2.2
# github.com/dgraph-io/badger : ASL 2.0
Provides:       bundled(golang(github.com/dgraph-io/badger/v2)) = 2.0.3
# github.com/dgraph-io/ristretto : ASL 2.0
Provides:       bundled(golang(github.com/dgraph-io/ristretto)) = 8f368f2
# github.com/dgryski/go-farm : MIT
Provides:       bundled(golang(github.com/dgryski/go-farm)) = 6a90982
# github.com/dustin/go-humanize : MIT
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.0
# github.com/flynn-archive/go-shlex : ASL 2.0
Provides:       bundled(golang(github.com/flynn-archive/go-shlex)) = 3f9db97
# github.com/getsentry/raven-go : BSD
Provides:       bundled(golang(github.com/getsentry/raven-go)) = 0.2.0
# github.com/go-asn1-ber/asn1-ber : MIT
Provides:       bundled(golang(github.com/go-asn1-ber/asn1-ber)) = 1.5.1
# github.com/go-ldap/ldap : MIT
Provides:       bundled(golang(github.com/go-ldap/ldap/v3)) = 3.2.4
# github.com/go-ole/go-ole : MIT
Provides:       bundled(golang(github.com/go-ole/go-ole)) = 1.2.4
# github.com/gobwas/glob : MIT
Provides:       bundled(golang(github.com/gobwas/glob)) = 0.2.3
# github.com/gogo/protobuf : BSD
Provides:       bundled(golang(github.com/gogo/protobuf)) = 1.3.1
# github.com/golang/groupcache : ASL 2.0
Provides:       bundled(golang(github.com/golang/groupcache)) = 8c9f03a
# github.com/golang/protobuf : BSD
Provides:       bundled(golang(github.com/golang/protobuf)) = 1.4.3
# github.com/golang/snappy : BSD
Provides:       bundled(golang(github.com/golang/snappy)) = 0.0.1
# github.com/greatroar/blobloom : ASL 2.0
Provides:       bundled(golang(github.com/greatroar/blobloom)) = 0.5.0
# github.com/jackpal/gateway : BSD
Provides:       bundled(golang(github.com/jackpal/gateway)) = 1.0.6
# github.com/jackpal/go-nat-pmp : ASL 2.0
Provides:       bundled(golang(github.com/jackpal/go-nat-pmp)) = 1.0.2
# github.com/julienschmidt/httprouter : BSD
Provides:       bundled(golang(github.com/julienschmidt/httprouter)) = 1.3.0
# github.com/kballard/go-shellquote : MIT
Provides:       bundled(golang(github.com/kballard/go-shellquote)) = 95032a8
# github.com/lib/pq : MIT
Provides:       bundled(golang(github.com/lib/pq)) = 1.8.0
# github.com/lucas-clemente/quic-go : MIT
Provides:       bundled(golang(github.com/lucas-clemente/quic-go)) = 0.19.3
# github.com/marten-seemann/qtls : BSD
Provides:       bundled(golang(github.com/marten-seemann/qtls)) = 0.10.0
# github.com/marten-seemann/qtls-go1-15 : BSD
Provides:       bundled(golang(github.com/marten-seemann/qtls-go1-15)) = 0.1.1
# github.com/maruel/panicparse : ASL 2.0
Provides:       bundled(golang(github.com/maruel/panicparse)) = 1.5.1
# github.com/mattn/go-isatty : MIT
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.12
# github.com/matttproud/golang_protobuf_extensions : ASL 2.0
Provides:       bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = 1.0.1
# github.com/minio/sha256-simd : ASL 2.0
Provides:       bundled(golang(github.com/minio/sha256-simd)) = 0.1.1
# github.com/miscreant/miscreant.go : MIT
Provides:       bundled(golang(github.com/miscreant/miscreant.go)) = 26d3763
# github.com/oschwald/geoip2-golang : ISC
Provides:       bundled(golang(github.com/oschwald/geoip2-golang)) = 1.4.0
# github.com/oschwald/maxminddb-golang : ISC
Provides:       bundled(golang(github.com/oschwald/maxminddb-golang)) = 1.6.0
# github.com/petermattis/goid : ASL 2.0
Provides:       bundled(golang(github.com/petermattis/goid)) = b0b1615
# github.com/pkg/errors : BSD
Provides:       bundled(golang(github.com/pkg/errors)) = 0.9.1
# github.com/prometheus/client_golang : ASL 2.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 1.8.0
# github.com/prometheus/client_model : ASL 2.0
Provides:       bundled(golang(github.com/prometheus/client_model)) = 0.2.0
# github.com/prometheus/common : ASL 2.0
Provides:       bundled(golang(github.com/prometheus/common)) = 0.14.0
# github.com/prometheus/procfs : ASL 2.0
Provides:       bundled(golang(github.com/prometheus/procfs)) = 0.2.0
# github.com/rcrowley/go-metrics : BSD
Provides:       bundled(golang(github.com/rcrowley/go-metrics)) = 10cdbea
# github.com/russross/blackfriday : BSD
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = 2.0.1
# github.com/sasha-s/go-deadlock : ASL 2.0
Provides:       bundled(golang(github.com/sasha-s/go-deadlock)) = 0.2.0
# github.com/shirou/gopsutil : BSD
Provides:       bundled(golang(github.com/shirou/gopsutil/v3)) = 3.20.11
# github.com/shurcooL/sanitized_anchor_name : MIT
Provides:       bundled(golang(github.com/shurcooL/sanitized_anchor_name)) = 1.0.0
# github.com/syncthing/notify : MIT
Provides:       bundled(golang(github.com/syncthing/notify)) = 17de266
# github.com/syndtr/goleveldb : BSD
Provides:       bundled(golang(github.com/syndtr/goleveldb)) = d9e9293
# github.com/thejerf/suture : MIT
Provides:       bundled(golang(github.com/thejerf/suture/v4)) = 4.0.0
# github.com/urfave/cli : MIT
Provides:       bundled(golang(github.com/urfave/cli)) = 1.22.4
# github.com/vitrun/qart : ASL 2.0 and BSD
Provides:       bundled(golang(github.com/vitrun/qart)) = bf64b92
# golang.org/x/crypto : BSD
Provides:       bundled(golang(golang.org/x/crypto)) = 9e8e0b3
# golang.org/x/net : BSD
Provides:       bundled(golang(golang.org/x/net)) = ff519b6
# golang.org/x/sys : BSD
Provides:       bundled(golang(golang.org/x/sys)) = da20708
# golang.org/x/text: BSD
Provides:       bundled(golang(golang.org/x/text)) = 0.3.4
# golang.org/x/time : BSD
Provides:       bundled(golang(golang.org/x/time)) = 3af7569
# google.golang.org/protobuf : BSD
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.23.0

# an inotify filesystem watcher is integrated with syncthing now
Provides:       syncthing-inotify = 0.8.7-5
Obsoletes:      syncthing-inotify < 0.8.7-5


%description
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing client binary and systemd services.


%if %{with devel}
%package        devel
Summary:        Continuous File Synchronization (development files)
BuildArch:      noarch

%description    devel
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing sources, which are needed as
dependency for building packages using syncthing.
%endif


%package        tools
Summary:        Continuous File Synchronization (server tools)

%description    tools
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the main syncthing server tools:

* strelaysrv / strelaypoolsrv, the syncthing relay server for indirect
  file transfers between client nodes, and
* stdiscosrv, the syncthing discovery server for discovering nodes
  to connect to indirectly over the internet.


%package        cli
Summary:        Continuous File Synchronization (CLI)

%description    cli
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the CLI program.


%prep
%autosetup -n %{name} -p1


%build
export GO111MODULE=off

# remove bundled libraries
#rm -r vendor

# prepare build environment
mkdir -p ./_build/src/github.com/syncthing

TOP=$(pwd)
pushd _build/src/github.com/syncthing
ln -s $TOP syncthing
popd

export GOPATH=$(pwd)/_build:%{gopath}
export BUILDDIR=$(pwd)/_build/src/%{goipath}

# compile assets used by the build process
pushd _build/src/%{goipath}
go run build.go assets
rm build.go
popd

# set variables expected by syncthing binaries as additional FOOFLAGS
export BUILD_HOST=fedora-koji
export COMMON_LDFLAGS="-X %{goipath}/lib/build.Version=%{tag} -X %{goipath}/lib/build.Stamp=$SOURCE_DATE_EPOCH -X %{goipath}/lib/build.User=$USER -X %{goipath}/lib/build.Host=$BUILD_HOST"
export BUILDTAGS="noupgrade"

export LDFLAGS="-X %{goipath}/lib/build.Program=syncthing $COMMON_LDFLAGS"
%gobuild -o _bin/syncthing %{goipath}/cmd/syncthing

export LDFLAGS="-X %{goipath}/lib/build.Program=stdiscosrv $COMMON_LDFLAGS"
%gobuild -o _bin/stdiscosrv %{goipath}/cmd/stdiscosrv

export LDFLAGS="-X %{goipath}/lib/build.Program=strelaysrv $COMMON_LDFLAGS"
%gobuild -o _bin/strelaysrv %{goipath}/cmd/strelaysrv

export LDFLAGS="-X %{goipath}/lib/build.Program=strelaypoolsrv $COMMON_LDFLAGS"
%gobuild -o _bin/strelaypoolsrv %{goipath}/cmd/strelaypoolsrv

export LDFLAGS="-X %{goipath}/lib/build.Program=stcli $COMMON_LDFLAGS"
%gobuild -o _bin/stcli %{goipath}/cmd/stcli


%install
export GO111MODULE=off

# install binaries
mkdir -p %{buildroot}/%{_bindir}

cp -pav _bin/syncthing %{buildroot}/%{_bindir}/
cp -pav _bin/stdiscosrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaysrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaypoolsrv %{buildroot}/%{_bindir}/
cp -pav _bin/stcli %{buildroot}/%{_bindir}/

# install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man5
mkdir -p %{buildroot}/%{_mandir}/man7

cp -pav ./man/syncthing.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/*.5 %{buildroot}/%{_mandir}/man5/
cp -pav ./man/*.7 %{buildroot}/%{_mandir}/man7/
cp -pav ./man/stdiscosrv.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/strelaysrv.1 %{buildroot}/%{_mandir}/man1/

# install systemd units
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_userunitdir}

cp -pav etc/linux-systemd/system/syncthing@.service %{buildroot}/%{_unitdir}/
cp -pav etc/linux-systemd/system/syncthing-resume.service %{buildroot}/%{_unitdir}/
cp -pav etc/linux-systemd/user/syncthing.service %{buildroot}/%{_userunitdir}/

# Unmark source files as executable
for i in $(find -name "*.go" -executable -print); do
    chmod a-x $i;
done

%if %{with devel}
%goinstall
%endif


%check
# restore executable bit on a folder ending in .go
# (likely caused by a bug in a brp script)
chmod +x vendor/github.com/miscreant/miscreant.go

export LANG=C.utf8
export GOPATH=$(pwd)/_build:%{gopath}
export GO111MODULE=off

%gotest %{goipath}/cmd/stdiscosrv
%gotest %{goipath}/cmd/strelaypoolsrv
%gotest %{goipath}/cmd/syncthing

%gotest %{goipath}/lib/api
%gotest %{goipath}/lib/beacon
%gotest %{goipath}/lib/config
%gotest %{goipath}/lib/connections
%gotest %{goipath}/lib/db
%gotest %{goipath}/lib/dialer
%gotest %{goipath}/lib/discover
%gotest %{goipath}/lib/events
%gotest %{goipath}/lib/fs
%gotest %{goipath}/lib/ignore
%gotest %{goipath}/lib/logger

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4370
%gotest %{goipath}/lib/model || :

%gotest %{goipath}/lib/nat
%gotest %{goipath}/lib/osutil
%gotest %{goipath}/lib/pmp
%gotest %{goipath}/lib/protocol
%gotest %{goipath}/lib/rand
%gotest %{goipath}/lib/relay/client
%gotest %{goipath}/lib/relay/protocol
%gotest %{goipath}/lib/scanner
%gotest %{goipath}/lib/signature
%gotest %{goipath}/lib/stats
%gotest %{goipath}/lib/sync
%gotest %{goipath}/lib/syncthing
%gotest %{goipath}/lib/tlsutil
%gotest %{goipath}/lib/upgrade
%gotest %{goipath}/lib/upnp
%gotest %{goipath}/lib/util

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4351
%gotest %{goipath}/lib/versioner || :

%gotest %{goipath}/lib/watchaggregator
%gotest %{goipath}/lib/weakhash


%post
%systemd_post 'syncthing@.service'
%systemd_user_post syncthing.service

%preun
%systemd_preun 'syncthing@*.service'
%systemd_user_preun syncthing.service

%postun
%systemd_postun_with_restart 'syncthing@*.service'
%systemd_user_postun_with_restart syncthing.service


%files
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/syncthing

%{_mandir}/*/syncthing*

%{_unitdir}/syncthing@.service
%{_unitdir}/syncthing-resume.service
%{_userunitdir}/syncthing.service


%files tools
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/stdiscosrv
%{_bindir}/strelaysrv
%{_bindir}/strelaypoolsrv

%{_mandir}/man1/stdiscosrv*
%{_mandir}/man1/strelaysrv*


%files cli
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/stcli


%if %{with devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS
%endif


%changelog
* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.13.1-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Feb 04 2021 Fabio Valentini <decathorpe@gmail.com> - 1.13.1-1
- Update to version 1.13.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Fabio Valentini <decathorpe@gmail.com> - 1.12.1-1
- Update to version 1.12.1.

* Mon Dec 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.12.0-1
- Update to version 1.12.0.

* Wed Nov 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.11.1-1
- Update to version 1.11.1.

* Tue Nov 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.11.0-1
- Update to version 1.11.0.

* Fri Oct 09 2020 Fabio Valentini <decathorpe@gmail.com> - 1.10.0-1
- Update to version 1.10.0.

* Tue Sep 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.9.0-1
- Update to version 1.9.0.

* Mon Sep 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.9.0~rc5-2
- Use correct version format for build flags.

* Sat Sep 05 2020 Carl George <carl@george.computer> - 1.9.0~rc5-1
- Update to version 1.9.0-rc.5

* Thu Aug 20 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.0-2
- Include upstream patch to fix issues on ppc64le.

* Sun Aug 16 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.0-1
- Update to version 1.8.0.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fabio Valentini <decathorpe@gmail.com> - 1.7.1-1
- Update to version 1.7.1.

* Tue Jul 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.7.0-1
- Update to version 1.7.0.

* Tue Jun 02 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6.1-1
- Update to version 1.6.1.

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-1
- Update to version 1.5.0.

* Wed Apr 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.2-1
- Update to version 1.4.2.

* Tue Mar 17 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.0-1
- Update to version 1.4.0.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3.4-2
- Drop custom systemd user session preset file.
  See: https://bugzilla.redhat.com/show_bug.cgi?id=1708297

* Tue Feb 04 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3.4-1
- Update to version 1.3.4.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3.3-1
- Update to version 1.3.3.

* Tue Dec 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.2-2
- Add proposed patch to fix tests running out of memory on 32 bit arches.

* Tue Dec 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.2-1
- Update to version 1.3.2.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.1-1
- Update to version 1.3.1.
- Update build scriptlet to match upstream build system changes.
- Fix broken systemd_post scriptlet.

* Thu Oct 10 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Update to version 1.3.0.

* Thu Sep 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.2.2-1
- Update to version 1.2.2.

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-1
- Update to version 1.2.1.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-1
- Update to version 1.2.0.

* Sun Jun 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.4-2
- Disable building -devel package by default.

* Tue Jun 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.4-1
- Update to version 1.1.4.

* Tue May 21 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.3-1
- Update to version 1.1.3.

* Fri Apr 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-1
- Update to version 1.1.1.

* Thu Mar 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-2
- Fix build tags for changed variable names.

* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Update to version 1.0.0.

* Wed Dec 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.54-1
- Update to version 0.14.54.
- Switch back to using bundled dependencies.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.53-1
- Update to version 0.14.53.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.52-1
- Update to version 0.14.52.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.51-1
- Update to version 0.14.51.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.50-2
- Adapt to rollinghash v4.0.0 changes.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.50-1
- Update to version 0.14.50.
- Clean up .spec file and use new macros.
- Drop upstreamed go1.11 patch.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.49-1
- Update to version 0.14.49.
- Drop upstreamed osext patch.
- Add upstream patch to fix building tests with go 1.11.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.48-1
- Update to version 0.14.48.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.47-1
- Update to version 0.14.47.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.46-1
- Update to version 0.14.46.
- Simplify .spec file and build process, and drop build system patches.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.45-1
- Update to version 0.14.45.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.44-1
- Update to version 0.14.44.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.43-1
- Update to version 0.14.43.

* Tue Dec 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.42-1
- Update to version 0.14.42.

* Tue Dec 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.41-1
- Update to version 0.14.41.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.40-1
- Update to version 0.14.40.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.39-1
- Update to version 0.14.39.

* Wed Sep 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.38-1
- Update to version 0.14.38.
- Add patch to use internal luhn version again.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.37-2
- Rebuild for updated dependencies, fixing crashes.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.37-1
- Update to version 0.14.37.

* Tue Aug 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.36-2
- Adapt patch to work on ppc64, where PIE isn't supported.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.36-1
- Update to version 0.14.36.

* Wed Aug 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.35-2
- Add Provides for bundled JS libraries and adapt License tag.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.35-1
- Update to version 0.14.35.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.34-1
- Update to version 0.14.34.

* Sat Aug 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.33-3
- Add another missing ldflags argument.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.33-2
- Adapt patched build script to use the correct LDFLAGS.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.33-1
- Update to version 0.14.33.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.32-1
- Update to version 0.14.32.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.31-1
- Update to version 0.14.31.

* Tue Jun 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.30-1
- Update to version 0.14.30.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.29-1
- Update to version 0.14.29.

* Tue May 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.28-1
- Update to version 0.14.28.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.27-1
- Update to version 0.14.27.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.26-1
- Update to version 0.14.26.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.25-1
- Update to version 0.14.25.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.24-1
- Update to version 0.14.24.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.23-2
- Clean up spec file, remove bundled libs on fedora, add man pages.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.23-1
- First package for fedora.

