# Do not build with tests by default
# Pass --with tests to rpmbuild to override
%bcond_with tests

%global goipath         github.com/osbuild/osbuild-composer

Version:        29

%gometa

%global common_description %{expand:
A service for building customized OS artifacts, such as VM images and OSTree
commits, that uses osbuild under the hood. Besides building images for local
usage, it can also upload images directly to cloud.

It is compatible with composer-cli and cockpit-composer clients.
}

Name:           osbuild-composer
Release:        1%{?dist}
Summary:        An image building service based on osbuild

# osbuild-composer doesn't have support for building i686 images
# and also RHEL and Fedora has now only limited support for this arch.
ExcludeArch:    i686

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}


BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  systemd
BuildRequires:  krb5-devel
BuildRequires:  python3-docutils
BuildRequires:  make
%if 0%{?fedora}
BuildRequires:  systemd-rpm-macros
BuildRequires:  git
BuildRequires:  golang(github.com/aws/aws-sdk-go)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go)
BuildRequires:  golang(github.com/Azure/azure-storage-blob-go/azblob)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/coreos/go-semver/semver)
BuildRequires:  golang(github.com/coreos/go-systemd/activation)
BuildRequires:  golang(github.com/deepmap/oapi-codegen/pkg/codegen)
BuildRequires:  golang(github.com/go-chi/chi)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/julienschmidt/httprouter)
BuildRequires:  golang(github.com/getkin/kin-openapi/openapi3)
BuildRequires:  golang(github.com/kolo/xmlrpc)
BuildRequires:  golang(github.com/labstack/echo/v4)
BuildRequires:  golang(github.com/gobwas/glob)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/gophercloud/gophercloud)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/ubccr/kerby)
BuildRequires:  golang(github.com/vmware/govmomi)
BuildRequires:  golang(cloud.google.com/go)
%endif

Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-worker = %{version}-%{release}
Requires: systemd

Provides: weldr

%if 0%{?rhel}
Obsoletes: lorax-composer <= 29
Conflicts: lorax-composer
%endif

# Remove when we stop releasing into Fedora 35
%if 0%{?fedora} >= 34
# lorax 34.3 is the first one without the composer subpackage
Obsoletes: lorax-composer < 34.3
%endif

# remove in F34
Obsoletes: golang-github-osbuild-composer < %{version}-%{release}
Provides:  golang-github-osbuild-composer = %{version}-%{release}

# remove when F34 is EOL
Obsoletes: osbuild-composer-koji <= 23

%description
%{common_description}

%prep
%if 0%{?rhel}
%forgeautosetup -p1
%else
%goprep
%endif

%if 0%{?fedora} && 0%{?fedora} <= 32
# Fedora 32 and older ships different kolo/xmlrpc and azure/azblob APIs. We
# cannot specify build tags in gobuild macro because the macro itself
# specifies build tags and -tags argument cannot be used more than once.
# Therefore, this ugly hack with build tags switcharoo is required.
# Remove when F32 is EOL.

# Remove the build constraint from the wrappers of the old APIs
sed -i "s$// +build kolo_xmlrpc_oldapi$// +build !kolo_xmlrpc_oldapi$" internal/upload/koji/xmlrpc-response-oldapi.go
sed -i "s$// +build azblob_oldapi$// +build !azblob_oldapi$" internal/upload/azure/page_blob_url_oldapi.go

# Add a build constraint to the wrappers of the new APIs
sed -i "s$// +build !kolo_xmlrpc_oldapi$// +build kolo_xmlrpc_oldapi$" internal/upload/koji/xmlrpc-response.go
sed -i "s$// +build !azblob_oldapi$// +build azblob_oldapi$" internal/upload/azure/page_blob_url.go
%endif

%build
%if 0%{?rhel}
GO_BUILD_PATH=$PWD/_build
install -m 0755 -vd $(dirname $GO_BUILD_PATH/src/%{goipath})
ln -fs $PWD $GO_BUILD_PATH/src/%{goipath}
cd $GO_BUILD_PATH/src/%{goipath}
install -m 0755 -vd _bin
export PATH=$PWD/_bin${PATH:+:$PATH}
export GOPATH=$GO_BUILD_PATH:%{gopath}
export GOFLAGS=-mod=vendor
%endif

%gobuild -o _bin/osbuild-composer %{goipath}/cmd/osbuild-composer
%gobuild -o _bin/osbuild-worker %{goipath}/cmd/osbuild-worker

make man

%if %{with tests} || 0%{?rhel}

# Build test binaries with `go test -c`, so that they can take advantage of
# golang's testing package. The golang rpm macros don't support building them
# directly. Thus, do it manually, taking care to also include a build id.
#
# On Fedora, also turn off go modules and set the path to the one into which
# the golang-* packages install source code.
%if 0%{?fedora}
export GO111MODULE=off
export GOPATH=%{gobuilddir}:%{gopath}
%endif

TEST_LDFLAGS="${LDFLAGS:-} -B 0x$(od -N 20 -An -tx1 -w100 /dev/urandom | tr -d ' ')"

go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-composer-cli-tests %{goipath}/cmd/osbuild-composer-cli-tests
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-dnf-json-tests %{goipath}/cmd/osbuild-dnf-json-tests
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-weldr-tests %{goipath}/internal/client/
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-image-tests %{goipath}/cmd/osbuild-image-tests
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-auth-tests %{goipath}/cmd/osbuild-auth-tests
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-koji-tests %{goipath}/cmd/osbuild-koji-tests
go build -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/cloud-cleaner %{goipath}/cmd/cloud-cleaner

%endif

%install
install -m 0755 -vd                                             %{buildroot}%{_libexecdir}/osbuild-composer
install -m 0755 -vp _bin/osbuild-composer                       %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp _bin/osbuild-worker                         %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp dnf-json                                    %{buildroot}%{_libexecdir}/osbuild-composer/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/osbuild-composer/repositories
install -m 0644 -vp repositories/*                              %{buildroot}%{_datadir}/osbuild-composer/repositories/

install -m 0755 -vd                                             %{buildroot}%{_unitdir}
install -m 0644 -vp distribution/*.{service,socket}             %{buildroot}%{_unitdir}/

install -m 0755 -vd                                             %{buildroot}%{_sysusersdir}
install -m 0644 -vp distribution/osbuild-composer.conf          %{buildroot}%{_sysusersdir}/

install -m 0755 -vd                                             %{buildroot}%{_localstatedir}/cache/osbuild-composer/dnf-cache

install -m 0755 -vd                                             %{buildroot}%{_mandir}/man7
install -m 0644 -vp docs/*.7                                    %{buildroot}%{_mandir}/man7/

%if %{with tests} || 0%{?rhel}

install -m 0755 -vd                                             %{buildroot}%{_libexecdir}/osbuild-composer-test
install -m 0755 -vp _bin/osbuild-composer-cli-tests             %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-weldr-tests                    %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-dnf-json-tests                 %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-image-tests                    %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-auth-tests                     %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-koji-tests                     %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/cloud-cleaner                          %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/provision.sh                          %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/gen-certs.sh                          %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/image-info                            %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/run-koji-container.sh                 %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/koji-compose.py                       %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/libvirt_test.sh                       %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vd                                             %{buildroot}%{_libexecdir}/tests/osbuild-composer
install -m 0755 -vp test/cases/*                                %{buildroot}%{_libexecdir}/tests/osbuild-composer/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/ansible
install -m 0644 -vp test/data/ansible/*                         %{buildroot}%{_datadir}/tests/osbuild-composer/ansible/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/azure
install -m 0644 -vp test/data/azure/*                           %{buildroot}%{_datadir}/tests/osbuild-composer/azure/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/manifests
install -m 0644 -vp test/data/manifests/*                       %{buildroot}%{_datadir}/tests/osbuild-composer/manifests/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/cloud-init
install -m 0644 -vp test/data/cloud-init/*                      %{buildroot}%{_datadir}/tests/osbuild-composer/cloud-init/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/composer
install -m 0644 -vp test/data/composer/*                        %{buildroot}%{_datadir}/tests/osbuild-composer/composer/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/worker
install -m 0644 -vp test/data/worker/*                          %{buildroot}%{_datadir}/tests/osbuild-composer/worker/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/repositories
install -m 0644 -vp test/data/repositories/*                    %{buildroot}%{_datadir}/tests/osbuild-composer/repositories/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/kerberos
install -m 0644 -vp test/data/kerberos/*                        %{buildroot}%{_datadir}/tests/osbuild-composer/kerberos/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/keyring
install -m 0644 -vp test/data/keyring/id_rsa.pub                %{buildroot}%{_datadir}/tests/osbuild-composer/keyring/
install -m 0600 -vp test/data/keyring/id_rsa                    %{buildroot}%{_datadir}/tests/osbuild-composer/keyring/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/koji
install -m 0644 -vp test/data/koji/*                            %{buildroot}%{_datadir}/tests/osbuild-composer/koji/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/x509
install -m 0644 -vp test/data/x509/*                            %{buildroot}%{_datadir}/tests/osbuild-composer/x509/

%endif

%check
%if 0%{?rhel}
export GOFLAGS=-mod=vendor
export GOPATH=$PWD/_build:%{gopath}
# cd inside GOPATH, otherwise go with GO111MODULE=off ignores vendor directory
cd $PWD/_build/src/%{goipath}
%gotest ./...
%else
%gocheck
%endif

%post
%systemd_post osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-remote-worker.socket

%preun
%systemd_preun osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-remote-worker.socket

%postun
%systemd_postun_with_restart osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-remote-worker.socket

%files
%license LICENSE
%doc README.md
%{_mandir}/man7/%{name}.7*
%{_unitdir}/osbuild-composer.service
%{_unitdir}/osbuild-composer.socket
%{_unitdir}/osbuild-composer-api.socket
%{_unitdir}/osbuild-local-worker.socket
%{_unitdir}/osbuild-remote-worker.socket
%{_sysusersdir}/osbuild-composer.conf

%package core
Summary:    The core osbuild-composer binary

%description core
The core osbuild-composer binary. This is suitable both for spawning in containers and by systemd.

%files core
%{_libexecdir}/osbuild-composer/osbuild-composer
%{_libexecdir}/osbuild-composer/dnf-json
%{_datadir}/osbuild-composer/

%package worker
Summary:    The worker for osbuild-composer
Requires:   systemd
Requires:   qemu-img
Requires:   osbuild >= 26
Requires:   osbuild-ostree >= 26

# remove in F34
Obsoletes: golang-github-osbuild-composer-worker < %{version}-%{release}
Provides:  golang-github-osbuild-composer-worker = %{version}-%{release}

%description worker
The worker for osbuild-composer

%files worker
%{_libexecdir}/osbuild-composer/osbuild-worker
%{_unitdir}/osbuild-worker@.service
%{_unitdir}/osbuild-remote-worker@.service

%post worker
%systemd_post osbuild-worker@.service osbuild-remote-worker@.service

%preun worker
# systemd_preun uses systemctl disable --now which doesn't work well with template services.
# See https://github.com/systemd/systemd/issues/15620
# The following lines mimicks its behaviour by running two commands:

# disable and stop all the worker services
systemctl --no-reload disable osbuild-worker@.service osbuild-remote-worker@.service
systemctl stop "osbuild-worker@*.service" "osbuild-remote-worker@*.service"

%postun worker
# restart all the worker services
%systemd_postun_with_restart "osbuild-worker@*.service" "osbuild-remote-worker@*.service"

%if %{with tests} || 0%{?rhel}

%package tests
Summary:    Integration tests
Requires:   %{name} = %{version}-%{release}
Requires:   composer-cli
Requires:   createrepo_c
Requires:   genisoimage
Requires:   qemu-kvm-core
Requires:   systemd-container
Requires:   jq
Requires:   unzip
Requires:   container-selinux
Requires:   dnsmasq
Requires:   krb5-workstation
Requires:   podman
Requires:   python3
Requires:   sssd-krb5
Requires:   libvirt-client libvirt-daemon
Requires:   libvirt-daemon-config-network
Requires:   libvirt-daemon-config-nwfilter
Requires:   libvirt-daemon-driver-interface
Requires:   libvirt-daemon-driver-network
Requires:   libvirt-daemon-driver-nodedev
Requires:   libvirt-daemon-driver-nwfilter
Requires:   libvirt-daemon-driver-qemu
Requires:   libvirt-daemon-driver-secret
Requires:   libvirt-daemon-driver-storage
Requires:   libvirt-daemon-driver-storage-disk
Requires:   libvirt-daemon-kvm
Requires:   qemu-img
Requires:   qemu-kvm
Requires:   virt-install
Requires:   expect
Requires:   python3-lxml
Requires:   httpd
Requires:   openssl
Requires:   podman-plugins
%if 0%{?fedora}
# koji and ansible are not in RHEL repositories. Depending on them breaks RHEL
# gating (see OSCI-1541). The test script must enable EPEL and install those
# packages manually.
Requires:   koji
Requires:   ansible
%endif
%ifarch %{arm}
Requires:   edk2-aarch64
%endif

%description tests
Integration tests to be run on a pristine-dedicated system to test the osbuild-composer package.

%files tests
%{_libexecdir}/osbuild-composer-test/
%{_libexecdir}/tests/osbuild-composer/
%{_datadir}/tests/osbuild-composer/

%endif

%changelog
* Fri Mar 05 2021 Martin Sehnoutka <msehnout@redhat.com> - 29-1
- New upstream release

* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 28-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sat Feb 20 2021 Martin Sehnoutka <msehnout@redhat.com> - 28-1
- New upstream release

* Thu Feb 04 2021 Ondrej Budai <obudai@redhat.com> - 27-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Ondrej Budai <obudai@redhat.com> - 26-2
- Fix the compatibility with a new golang-github-azure-storage-blob 0.12

* Thu Dec 17 2020 Ondrej Budai <obudai@redhat.com> - 26-1
- New upstream release

* Thu Nov 19 2020 Ondrej Budai <obudai@redhat.com> - 25-1
- New upstream release

* Thu Nov 12 2020 Ondrej Budai <obudai@redhat.com> - 24-1
- New upstream release

* Fri Nov 06 2020 Ondrej Budai <obudai@redhat.com> - 23-1
- New upstream release

* Fri Oct 16 2020 Ondrej Budai <obudai@redhat.com> - 22-1
- New upstream release

* Sun Aug 23 2020 Tom Gundersen <teg@jklm.no> - 20-1
- New upstream release

* Tue Aug 11 2020 Tom Gundersen <teg@jklm.no> - 19-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Ondrej Budai <obudai@redhat.com> - 18-1
- New upstream release

* Wed Jul 08 2020 Ondrej Budai <obudai@redhat.com> - 17-1
- New upstream release

* Mon Jun 29 2020 Ondrej Budai <obudai@redhat.com> - 16-1
- New upstream release

* Fri Jun 12 2020 Ondrej Budai <obudai@redhat.com> - 15-1
- New upstream release

* Thu Jun 04 2020 Ondrej Budai <obudai@redhat.com> - 14-1
- New upstream release

* Fri May 29 2020 Ondrej Budai <obudai@redhat.com> - 13-2
- Add missing osbuild-ostree dependency

* Thu May 28 2020 Ondrej Budai <obudai@redhat.com> - 13-1
- New upstream release

* Thu May 14 2020 Ondrej Budai <obudai@redhat.com> - 12-1
- New upstream release

* Wed Apr 29 2020 Ondrej Budai <obudai@redhat.com> - 11-1
- New upstream release

* Wed Apr 15 2020 Ondrej Budai <obudai@redhat.com> - 10-1
- New upstream release

* Wed Apr 01 2020 Ondrej Budai <obudai@redhat.com> - 9-1
- New upstream release

* Mon Mar 23 2020 Ondrej Budai <obudai@redhat.com> - 8-1
- Initial package (renamed from golang-github-osbuild-composer)
