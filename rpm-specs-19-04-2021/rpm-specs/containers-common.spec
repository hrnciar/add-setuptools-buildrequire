# Below definitions are used to deliver config files from a particular branch
# of c/image, c/common, c/storage vendored in all of Buildah, Podman and Skopeo.
# These vendored components must have the same version. If it is not the case,
# pick the oldest version on c/image, c/common, c/storage vendored in
# Buildah/Podman/Skopeo.
%global skopeo_branch master
%global podman_branch master
%global image_branch  master
%global common_branch master
%global storage_branch master
%global shortnames_branch master

%global github_containers https://raw.githubusercontent.com/containers

Epoch: 4
Name: containers-common
Version: 1
Release: 17%{?dist}
Summary: Common configuration and documentation for containers
License: ASL 2.0
BuildArch: noarch
BuildRequires: go-md2man
Provides: skopeo-containers = %{epoch}:%{version}-%{release}
Requires: (container-selinux >= 2:2.160.0 if selinux-policy)
Requires: oci-runtime
Recommends: fuse-overlayfs
Recommends: slirp4netns
Source1: %{github_containers}/common/%{common_branch}/docs/containers.conf.5.md
Source2: %{github_containers}/common/%{common_branch}/pkg/config/containers.conf
Source3: %{github_containers}/common/%{common_branch}/pkg/seccomp/seccomp.json
Source4: %{github_containers}/common/%{common_branch}/pkg/subscriptions/mounts.conf
Source5: %{github_containers}/image/%{image_branch}/docs/containers-auth.json.5.md
Source6: %{github_containers}/image/%{image_branch}/docs/containers-certs.d.5.md
Source7: %{github_containers}/image/%{image_branch}/docs/containers-policy.json.5.md
Source8: %{github_containers}/image/%{image_branch}/docs/containers-registries.conf.5.md
Source9: %{github_containers}/image/%{image_branch}/docs/containers-registries.conf.d.5.md
Source10: %{github_containers}/image/%{image_branch}/docs/containers-registries.d.5.md
Source11: %{github_containers}/image/%{image_branch}/docs/containers-signature.5.md
Source12: %{github_containers}/image/%{image_branch}/docs/containers-transports.5.md
Source13: %{github_containers}/image/%{image_branch}/registries.conf
Source14: %{github_containers}/podman/%{podman_branch}/docs/source/markdown/containers-mounts.conf.5.md
Source15: %{github_containers}/shortnames/%{shortnames_branch}/shortnames.conf
Source16: %{github_containers}/skopeo/%{skopeo_branch}/default.yaml
Source17: %{github_containers}/skopeo/%{skopeo_branch}/default-policy.json
Source18: %{github_containers}/storage/%{storage_branch}/docs/containers-storage.conf.5.md
Source19: %{github_containers}/storage/%{storage_branch}/storage.conf

%description
This package contains common configuration files and documentation for container
tools ecosystem, such as Podman, Buildah and Skopeo.

It is required because the most of configuration files and docs come from projects
which are vendored into Podman, Buildah, Skopeo, etc. but they are not packaged
separately.

%prep
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .
cp %{SOURCE6} .
cp %{SOURCE7} .
cp %{SOURCE8} .
cp %{SOURCE9} .
cp %{SOURCE10} .
cp %{SOURCE11} .
cp %{SOURCE12} .
cp %{SOURCE13} .
cp %{SOURCE14} .
cp %{SOURCE15} .
cp %{SOURCE16} .
cp %{SOURCE17} .
cp %{SOURCE18} .
cp %{SOURCE19} .

%build

%install
# install config and policy files for registries
install -dp %{buildroot}%{_sysconfdir}/containers/{certs.d,oci/hooks.d,registries.conf.d,registries.d}
install -dp %{buildroot}%{_sharedstatedir}/containers/sigstore
install -m0644 default.yaml %{buildroot}%{_sysconfdir}/containers/registries.d/default.yaml
install -m0644 storage.conf %{buildroot}%{_sysconfdir}/containers/storage.conf
install -m0644 registries.conf %{buildroot}%{_sysconfdir}/containers/registries.conf
install -m0644 shortnames.conf %{buildroot}%{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
install -m0644 default-policy.json %{buildroot}%{_sysconfdir}/containers/policy.json

# install manpages
install -dp %{buildroot}%{_mandir}/man5
go-md2man -in containers-storage.conf.5.md -out %{buildroot}%{_mandir}/man5/containers-storage.conf.5
go-md2man -in containers-registries.conf.5.md -out %{buildroot}%{_mandir}/man5/containers-registries.conf.5
go-md2man -in containers-policy.json.5.md -out %{buildroot}%{_mandir}/man5/containers-policy.json.5
go-md2man -in containers-mounts.conf.5.md -out %{buildroot}%{_mandir}/man5/containers-mounts.conf.5
go-md2man -in containers-signature.5.md -out %{buildroot}%{_mandir}/man5/containers-signature.5
go-md2man -in containers-transports.5.md -out %{buildroot}%{_mandir}/man5/containers-transports.5
go-md2man -in containers-certs.d.5.md -out %{buildroot}%{_mandir}/man5/containers-certs.d.5
go-md2man -in containers-registries.d.5.md -out %{buildroot}%{_mandir}/man5/containers-registries.d.5
go-md2man -in containers.conf.5.md -out %{buildroot}%{_mandir}/man5/containers.conf.5
go-md2man -in containers-auth.json.5.md -out %{buildroot}%{_mandir}/man5/containers-auth.json.5
go-md2man -in containers-registries.conf.d.5.md -out %{buildroot}%{_mandir}/man5/containers-registries.conf.d.5

# install config files for mounts, containers and seccomp
install -dp %{buildroot}%{_datadir}/containers
install -m0644 mounts.conf %{buildroot}%{_datadir}/containers/mounts.conf
install -m0644 seccomp.json %{buildroot}%{_datadir}/containers/seccomp.json
install -m0644 containers.conf %{buildroot}%{_datadir}/containers/containers.conf

# install secrets patch directory
install -d -p -m 755 %{buildroot}/%{_datadir}/rhel/secrets
# rhbz#1110876 - update symlinks for subscription management
ln -s %{_sysconfdir}/pki/entitlement %{buildroot}%{_datadir}/rhel/secrets/etc-pki-entitlement
ln -s %{_sysconfdir}/rhsm %{buildroot}%{_datadir}/rhel/secrets/rhsm
ln -s %{_sysconfdir}/yum.repos.d/redhat.repo %{buildroot}%{_datadir}/rhel/secrets/redhat.repo

%files
%dir %{_sysconfdir}/containers
%dir %{_sysconfdir}/containers/certs.d
%dir %{_sysconfdir}/containers/oci
%dir %{_sysconfdir}/containers/oci/hooks.d
%dir %{_sysconfdir}/containers/registries.conf.d
%dir %{_sysconfdir}/containers/registries.d
%config(noreplace) %{_sysconfdir}/containers/policy.json
%config(noreplace) %{_sysconfdir}/containers/registries.conf
%config(noreplace) %{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
%config(noreplace) %{_sysconfdir}/containers/registries.d/default.yaml
%config(noreplace) %{_sysconfdir}/containers/storage.conf
%ghost %{_sysconfdir}/containers/containers.conf
%dir %{_sharedstatedir}/containers/sigstore
%{_mandir}/man5/*
%dir %{_datadir}/containers
%{_datadir}/containers/containers.conf
%{_datadir}/containers/mounts.conf
%{_datadir}/containers/seccomp.json
%dir %{_datadir}/rhel/secrets
%{_datadir}/rhel/secrets/*

%changelog
* Thu Apr 15 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-17
- add common dependencies like oci-runtime and container-selinux
- will pull in crun by default, runc users should install runc separately first
 or explicitly require runc

* Mon Apr 12 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-16
- use latest configs from upstream

* Fri Apr 09 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-15
- pull latest files from upstream

* Fri Mar 19 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-14
- also provide skopeo-containers
- bump release tag for smooth upgrade from f34
- use latest upstream files

* Thu Feb 18 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-10
- install shortnames.conf as 000-shrotnames.conf

* Mon Feb 15 2021 Dan Walsh <dwalsh@fedoraproject.org> - 4:1-9
- Remove registry.centos.org and add quay.io from registries.conf

* Mon Feb 15 2021 Dan Walsh <dwalsh@fedoraproject.org> - 4:1-8
- Update content

* Mon Feb 01 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-7
- use the correct policy.json file

* Thu Jan 28 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-6
- short-name-mode="enforcing" in registries.conf

* Thu Jan 28 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-5
- number sources in order

* Thu Jan 28 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-4
- Resolves: #1916922 - do not depend on subscription-manager
- reorder sources in alphabetical order

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4:1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:1-2
- bump version to random number
- no connection of package to github.com/containers/common
- add conf files to dist-git repo
- bring back update.sh

* Wed Jan 13 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:0.33.0-3
- copy source files into builddir and change them there before installation

* Tue Jan 12 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:0.33.0-2
- move update.sh code to spec file itself

* Tue Jan 12 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 4:0.33.0-1
- update registries.conf and other files
- source urls in update.sh

* Tue Dec 08 2020 Jindrich Novy <jnovy@redhat.com> - 3:1-1
- initial build
