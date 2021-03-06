# Generated by go2rpm
# arm support not fully implemented: not implemented
%ifnarch %{arm}
%bcond_without check
%endif
%bcond_with bootstrap

# https://github.com/containerd/containerd
%global goipath         github.com/containerd/containerd
Version:                1.5.0~beta.4
%global tag             v1.5.0-beta.4

%gometa

%global goname          containerd
%global godevelname     containerd-devel

%global common_description %{expand:
Containerd is an industry-standard container runtime with an emphasis on
simplicity, robustness and portability. It is available as a daemon for Linux
and Windows, which can manage the complete container lifecycle of its host
system: image transfer and storage, container execution and supervision,
low-level storage and network attachments, etc.}

%global golicenses      LICENSE NOTICE
%global godocs          docs ROADMAP.md SCOPE.md code-of-conduct.md\\\
                        BUILDING.md README.md RELEASES.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Open and reliable container runtime

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        containerd.service
Source2:        containerd.toml
# Carve out code requiring github.com/Microsoft/hcsshim
Patch0:         0001-Revert-commit-for-Windows-metrics.patch
Patch1:         0002-Remove-windows-only-dep.patch

BuildRequires:  btrfs-progs-devel
BuildRequires:  go-md2man
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(github.com/BurntSushi/toml)
%if %{without bootstrap}
BuildRequires:  golang(github.com/containerd/aufs/plugin)
%endif
BuildRequires:  golang(github.com/containerd/btrfs)
BuildRequires:  golang(github.com/containerd/cgroups)
BuildRequires:  golang(github.com/containerd/cgroups/stats/v1)
BuildRequires:  golang(github.com/containerd/cgroups/v2)
BuildRequires:  golang(github.com/containerd/cgroups/v2/stats)
BuildRequires:  golang(github.com/containerd/console)
BuildRequires:  golang(github.com/containerd/continuity)
BuildRequires:  golang(github.com/containerd/continuity/fs)
BuildRequires:  golang(github.com/containerd/continuity/fs/fstest)
BuildRequires:  golang(github.com/containerd/continuity/sysx)
BuildRequires:  golang(github.com/containerd/fifo)
BuildRequires:  golang(github.com/containerd/go-cni)
BuildRequires:  golang(github.com/containerd/go-runc)
BuildRequires:  golang(github.com/containerd/imgcrypt)
BuildRequires:  golang(github.com/containerd/imgcrypt/images/encryption)
BuildRequires:  golang(github.com/containerd/nri)
BuildRequires:  golang(github.com/containerd/nri/types/v1)
BuildRequires:  golang(github.com/containerd/ttrpc)
BuildRequires:  golang(github.com/containerd/ttrpc/plugin)
BuildRequires:  golang(github.com/containerd/typeurl)
%if %{without bootstrap}
BuildRequires:  golang(github.com/containerd/zfs/plugin)
%endif
BuildRequires:  golang(github.com/containernetworking/plugins/pkg/ns)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/daemon)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/docker/go-events)
BuildRequires:  golang(github.com/docker/go-metrics)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/emicklei/go-restful)
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/gogo/googleapis/google/rpc)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/descriptor)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/generator)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/gogo/protobuf/vanity)
BuildRequires:  golang(github.com/gogo/protobuf/vanity/command)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/imdario/mergo)
BuildRequires:  golang(github.com/klauspost/compress/zstd)
# BuildRequires:  golang(github.com/Microsoft/hcsshim/cmd/containerd-shim-runhcs-v1/options)
# BuildRequires:  golang(github.com/Microsoft/hcsshim/cmd/containerd-shim-runhcs-v1/stats)
BuildRequires:  golang(github.com/moby/sys/mountinfo)
BuildRequires:  golang(github.com/moby/sys/symlink)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/opencontainers/go-digest/digestset)
BuildRequires:  golang(github.com/opencontainers/image-spec/identity)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/devices)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/user)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/selinux/go-selinux)
BuildRequires:  golang(github.com/opencontainers/selinux/go-selinux/label)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/tchap/go-patricia/patricia)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sync/semaphore)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/backoff)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/health)
BuildRequires:  golang(google.golang.org/grpc/health/grpc_health_v1)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gotest.tools/v3/assert)
BuildRequires:  golang(gotest.tools/v3/assert/cmp)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/clock)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/httpstream)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/httpstream/spdy)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/net)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/remotecommand)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apiserver/pkg/server/httplog)
BuildRequires:  golang(k8s.io/apiserver/pkg/util/wsstream)
BuildRequires:  golang(k8s.io/client-go/tools/remotecommand)
BuildRequires:  golang(k8s.io/client-go/util/cert)
BuildRequires:  golang(k8s.io/component-base/logs/logreduction)
BuildRequires:  golang(k8s.io/cri-api/pkg/apis)
BuildRequires:  golang(k8s.io/cri-api/pkg/apis/runtime/v1alpha2)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/utils/exec)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/containerd/continuity/testutil)
BuildRequires:  golang(github.com/containerd/continuity/testutil/loopback)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

Requires:       runc

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
# Used only for generation:
rm -rf cmd/protoc-gen-gogoctrd

%if %{without bootstrap}
%build
export LDFLAGS="-X %{goipath}/version.Version=%{version} "
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mkdir _man
go-md2man -in docs/man/containerd-config.8.md -out _man/containerd-config.8
go-md2man -in docs/man/containerd-config.toml.5.md -out _man/containerd-config.toml.5
%{gobuilddir}/bin/gen-manpages containerd.8 _man
%{gobuilddir}/bin/gen-manpages ctr.8 _man
rm %{gobuilddir}/bin/gen-manpages
%else
rm -rf cmd
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -D -p -m 0644 _man/containerd.8 %{buildroot}%{_mandir}/man8/containerd.8
install -D -p -m 0644 _man/containerd-config.8 %{buildroot}%{_mandir}/man8/containerd-config.8
install -D -p -m 0644 _man/ctr.8 %{buildroot}%{_mandir}/man8/ctr.8
install -D -p -m 0644 _man/containerd-config.toml.5 %{buildroot}%{_mandir}/man5/containerd-config.toml.5
install -D -p -m 0644 %{S:1} %{buildroot}%{_unitdir}/containerd.service
install -D -p -m 0644 %{S:2} %{buildroot}%{_sysconfdir}/containerd/config.toml
%endif

%post
%systemd_post containerd.service

%preun
%systemd_preun containerd.service

%postun
%systemd_postun_with_restart containerd.service

%if %{with check}
%check
%gocheck -d . -d mount -t snapshots -d pkg/cri/server
%endif

%if %{without bootstrap}
%files
%license LICENSE NOTICE
%doc docs ROADMAP.md SCOPE.md code-of-conduct.md BUILDING.md
%doc README.md RELEASES.md
%{_bindir}/*
%{_mandir}/man8/containerd.8*
%{_mandir}/man8/containerd-config.8*
%{_mandir}/man8/ctr.8*
%{_mandir}/man5/containerd-config.toml.5*
%{_unitdir}/containerd.service
%dir %{_sysconfdir}/containerd
%config(noreplace) %{_sysconfdir}/containerd/config.toml
%endif

%gopkgfiles

%changelog
* Wed Mar 17 2021 Olivier Lemasle <o.lemasle@gmail.com> - 1.5.0~beta.4-1
- Update to upstream 1.5.0-beta.4

* Sat Mar 06 2021 Olivier Lemasle <o.lemasle@gmail.com> - 1.5.0~beta.3-1
- Update to upstream 1.5.0-beta.3

* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.0~beta.0-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Olivier Lemasle <o.lemasle@gmail.com> 1.5.0~beta.0-1
- Update to 1.5.0~beta.0 (#1918993)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Olivier Lemasle <o.lemasle@gmail.com> - 1.4.3-1
- Fix CVE-2020-15257 (#1903050)
- Update to latest upstream - 1.4.3 (#1901908)

* Mon Nov  2 23:23:57 CET 2020 Olivier Lemasle <o.lemasle@gmail.com> - 1.4.1-2
- Fix man pages

* Wed Sep 30 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 01 2020 Olivier Lemasle <o.lemasle@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Sun Mar 22 2020 Olivier Lemasle <o.lemasle@gmail.com> - 1.2.13-2
- Remove version requirement on golang-github-containerd-cri

* Sun Mar 22 2020 Olivier Lemasle <o.lemasle@gmail.com> - 1.2.13-1
- Exclude failing integration tests
- Update to containerd 1.2.13

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 15:33:19 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.2.6-1.20190501gitd68b593
- Release 1.2.6, commit d68b593de4ab10bb8b4fd64560e10d43c7156db2

* Tue Feb 26 2019 Carl George <carl@george.computer> - 1.2.4-1
- Latest upstream

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Carl George <carl@george.computer> - 1.2.1-1
- Latest upstream
- Run test suite (except on el7 or %%arm)

* Thu Oct 25 2018 Carl George <carl@george.computer> - 1.2.0-1
- Latest upstream

* Mon Aug 13 2018 Carl George <carl@george.computer> - 1.1.2-1
- Latest upstream

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Carl George <carl@george.computer> - 1.1.0-1
- Latest upstream
- Build and include man pages

* Wed Apr 04 2018 Carl George <carl@george.computer> - 1.0.3-1
- Latest upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Carl George <carl@george.computer> - 1.0.1-1
- Latest upstream

* Wed Dec 06 2017 Carl George <carl@george.computer> - 1.0.0-1
- Latest upstream

* Fri Nov 10 2017 Carl George <carl@george.computer> - 1.0.0-0.5.beta.3
- Latest upstream

* Thu Oct 19 2017 Carl George <carl@george.computer> - 1.0.0-0.4.beta.2
- Own /etc/containerd

* Thu Oct 12 2017 Carl George <carl@george.computer> - 1.0.0-0.3.beta.2
- Latest upstream
- Require runc 1.0.0 https://github.com/containerd/containerd/issues/1508#issuecomment-335566293

* Mon Oct 09 2017 Carl George <carl@george.computer> - 1.0.0-0.2.beta.1
- Add provides for vendored dependencies
- Add ctr command

* Wed Oct 04 2017 Carl George <carl@george.computer> - 1.0.0-0.1.beta.1
- Initial package
