%global with_debug 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

# binaries and unitfiles are currently called 'docker'
# to match with upstream supplied packages
%global origname docker
%global newname moby
%global service_name %{origname}

# moby
%global git_moby https://github.com/%{newname}/%{newname}
%global commit_moby 363e9a88a11be517d9e8c65c998ff56f774eb4dc
%global shortcommit_moby %(c=%{commit_moby}; echo ${c:0:7})

# cli
%global git_cli https://github.com/%{origname}/cli
%global commit_cli 55c4c88966a912ddb365e2d73a4969e700fc458f
%global shortcommit_cli %(c=%{commit_cli}; echo ${c:0:7})

# tini
%global git_tini https://github.com/krallin/tini
%global commit_tini de40ad007797e0dcd8b7126f27bb87401d224240
%global shortcommit_tini %(c=%{commit_tini}; echo ${c:0:7})

Name: %{newname}-engine
Version: 20.10.5
Release: 1%{?dist}
Summary: The open-source application container engine
License: ASL 2.0
# no golang / go-md2man for ppc64
ExcludeArch: ppc64
Source0: %{git_moby}/archive/v%{version}.tar.gz#/moby-v%{version}.tar.gz
Source1: %{git_cli}/archive/v%{version}.tar.gz#/cli-v%{version}.tar.gz
Source2: %{git_tini}/archive/%{commit_tini}.tar.gz
Source3: %{service_name}.service
Source4: %{service_name}.sysconfig
URL: https://www.%{origname}.com

BuildRequires: golang-github-docker-devel
BuildRequires: golang-github-docker-libnetwork-devel
BuildRequires: pkgconfig(libbtrfsutil)
BuildRequires: pkgconfig(devmapper)
BuildRequires: golang
BuildRequires: go-rpm-macros
BuildRequires: go-md2man
BuildRequires: pkgconfig(libseccomp) >= 2.3.0
BuildRequires: make
BuildRequires: pkgconfig(audit)
BuildRequires: pkgconfig(systemd)
BuildRequires: firewalld-filesystem

# Build dependencies for tini
BuildRequires: cmake
BuildRequires: glibc-static

# required packages on install
Requires: container-selinux
Requires: iptables
Requires: systemd
Requires: tar
Requires: xz
Requires: pigz
Requires: runc
Requires: containerd

Requires(post): firewalld-filesystem

# Resolves: rhbz#1165615
Requires: device-mapper-libs >= 1.02.90-1

# Replace the old Docker packages
Obsoletes: %{origname} < 2:%{version}-%{release}
Obsoletes: %{origname}-latest < 2:%{version}-%{release}
Obsoletes: %{origname}-common < 2:%{version}-%{release}
Provides: %{origname} = %{version}-%{release}
Provides: %{origname}-latest = %{version}-%{release}

# conflicting packages
Conflicts: %{origname}
Conflicts: %{origname}-latest
Conflicts: %{origname}-common
Conflicts: %{origname}-io
Conflicts: %{origname}-engine-cs
Conflicts: %{origname}-ce
Conflicts: %{origname}-ce-cli
Conflicts: %{origname}-ee

# Bundled dependencies (docker/cli is still bundled with vendored dependencies)
Provides:       bundled(tini-static)
Provides:       bundled(golang(github.com/docker/cli))
# grep -v -e '^$' -e '^#' cli/vendor.conf | sort | awk '{print "Provides:       bundled(golang("$1")) = "$2}'
Provides:       bundled(golang(cloud.google.com/go)) = ceeb313ad77b789a7fa5287b36a1d127b69b7093
Provides:       bundled(golang(github.com/agl/ed25519)) = 5312a61534124124185d41f09206b9fef1d88403
Provides:       bundled(golang(github.com/Azure/go-ansiterm)) = d6e3b3328b783f23731bc4d058875b0371ff8109
Provides:       bundled(golang(github.com/beorn7/perks)) = 37c8de3658fcb183f997c4e13e8337516ab753e6
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = d7df74196a9e781ede915320c11c378c1b2f3a1f
Provides:       bundled(golang(github.com/containerd/cgroups)) = 0b889c03f102012f1d93a97ddd3ef71cd6f4f510
Provides:       bundled(golang(github.com/containerd/console)) = 5d7e1412f07b502a01029ea20e20e0d2be31fa7c
Provides:       bundled(golang(github.com/containerd/containerd)) = 0edc412565dcc6e3d6125ff9e4b009ad4b89c638
Provides:       bundled(golang(github.com/containerd/continuity)) = efbc4488d8fe1bdc16bde3b2d2990d9b3a899165
Provides:       bundled(golang(github.com/containerd/typeurl)) = cd3ce7159eae562a4f60ceff37dada11a939d247
Provides:       bundled(golang(github.com/coreos/etcd)) = d57e8b8d97adfc4a6c224fe116714bf1a1f3beb9
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = f79a8a8ca69da163eee19ab442bedad7a35bba5a
Provides:       bundled(golang(github.com/creack/pty)) = 2a38352e8b4d7ab6c336eef107e42a55e72e7fbc
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 8991bc29aa16c548c550c7ff78260e27b9ab7c73
Provides:       bundled(golang(github.com/docker/compose-on-kubernetes)) = 78e6a00beda64ac8ccb9fec787e601fe2ce0d5bb
Provides:       bundled(golang(github.com/docker/distribution)) = 0d3efadf0154c2b8a4e7b6621fff9809655cc580
Provides:       bundled(golang(github.com/docker/docker)) = 46229ca1d815cfd4b50eb377ac75ad8300e13a85
Provides:       bundled(golang(github.com/docker/docker-credential-helpers)) = 38bea2ce277ad0c9d2a6230692b0606ca5286526
Provides:       bundled(golang(github.com/docker/go-connections)) = 7395e3f8aa162843a74ed6d48e79627d9792ac55
Provides:       bundled(golang(github.com/docker/go)) = d30aec9fd63c35133f8f79c3412ad91a3b08be06
Provides:       bundled(golang(github.com/docker/go-events)) = e31b211e4f1cd09aa76fe4ac244571fab96ae47f
Provides:       bundled(golang(github.com/docker/go-metrics)) = b619b3592b65de4f087d9f16863a7e6ff905973c
Provides:       bundled(golang(github.com/docker/go-units)) = 519db1ee28dcc9fd2474ae59fca29a810482bfb1
Provides:       bundled(golang(github.com/docker/swarmkit)) = d6592ddefd8a5319aadff74c558b816b1a0b2590
Provides:       bundled(golang(github.com/evanphx/json-patch)) = 72bf35d0ff611848c1dc9df0f976c81192392fa5
Provides:       bundled(golang(github.com/fvbommel/sortorder)) = 26fad50c6b32a3064c09ed089865c16f2f3615f6
Provides:       bundled(golang(github.com/gofrs/flock)) = 6caa7350c26b838538005fae7dbee4e69d9398db
Provides:       bundled(golang(github.com/gogo/googleapis)) = 01e0f9cca9b92166042241267ee2a5cdf5cff46c
Provides:       bundled(golang(github.com/gogo/protobuf)) = 5628607bb4c51c3157aacc3a50f0ab707582b805
Provides:       bundled(golang(github.com/golang/glog)) = 23def4e6c14b4da8ac2ed8007337bc5eb5007998
Provides:       bundled(golang(github.com/golang/groupcache)) = 869f871628b6baa9cfbc11732cdf6546b17c1298
Provides:       bundled(golang(github.com/golang/protobuf)) = 84668698ea25b64748563aa20726db66a6b8d299
Provides:       bundled(golang(github.com/googleapis/gnostic)) = 7c663266750e7d82587642f65e60bc4083f1f84e
Provides:       bundled(golang(github.com/google/go-cmp)) = 3af367b6b30c263d47e8895973edcca9a49cf029
Provides:       bundled(golang(github.com/google/gofuzz)) = 24818f796faf91cd76ec7bddd72458fbced7a6c1
Provides:       bundled(golang(github.com/google/shlex)) = e7afc7fbc51079733e9468cdfd1efcd7d196cd1d
Provides:       bundled(golang(github.com/gorilla/mux)) = 98cb6bf42e086f6af920b965c38cacc07402d51b
Provides:       bundled(golang(github.com/grpc-ecosystem/go-grpc-middleware)) = 3c51f7f332123e8be5a157c0802a228ac85bf9db
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-gateway)) = 1a03ca3bad1e1ebadaedd3abb76bc58d4ac8143b
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-opentracing)) = 8e809c8a86450a29b90dcc9efbf062d0fe6d9746
Provides:       bundled(golang(github.com/hashicorp/golang-lru)) = 7f827b33c0f158ec5dfbba01bb0b14a4541fd81d
Provides:       bundled(golang(github.com/imdario/mergo)) = 1afb36080aec31e0d1528973ebe6721b191b0369
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = 76626ae9c91c4f2a10f34cad8ce83ea42c93bb75
Provides:       bundled(golang(github.com/jaguilar/vt100)) = ad4c4a5743050fb7f88ce968dca9422f72a0e3f2
Provides:       bundled(golang(github.com/json-iterator/go)) = 0ff49de124c6f76f8494e194af75bde0f1a49a29
Provides:       bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = c12348ce28de40eed0136aa2b644d0ee0650e56c
Provides:       bundled(golang(github.com/Microsoft/go-winio)) = 5b44b70ab3ab4d291a7c1d28afe7b4afeced0ed4
Provides:       bundled(golang(github.com/Microsoft/hcsshim)) = 5bc557dd210ff2caf615e6e22d398123de77fc11
Provides:       bundled(golang(github.com/miekg/pkcs11)) = 210dc1e16747c5ba98a03bcbcf728c38086ea357
Provides:       bundled(golang(github.com/mitchellh/mapstructure)) = d16e9488127408e67948eb43b6d3fbb9f222da10
Provides:       bundled(golang(github.com/moby/buildkit)) = 8142d66b5ebde79846b869fba30d9d30633e74aa
Provides:       bundled(golang(github.com/moby/sys)) = 1bc8673b57550ddf85262eb0fed0aac651a37dab
Provides:       bundled(golang(github.com/moby/term)) = bea5bbe245bf407372d477f1361d2ff042d2f556
Provides:       bundled(golang(github.com/modern-go/concurrent)) = bacd9c7ef1dd9b15be4a9909b8ac7a4e313eec94
Provides:       bundled(golang(github.com/modern-go/reflect2)) = 4b7aa43c6742a2c18fdef89dd197aaae7dac7ccd
Provides:       bundled(golang(github.com/morikuni/aec)) = 39771216ff4c63d11f5e604076f9c45e8be1067b
Provides:       bundled(golang(github.com/opencontainers/go-digest)) = ea51bea511f75cfa3ef6098cc253c5c3609b037a
Provides:       bundled(golang(github.com/opencontainers/image-spec)) = d60099175f88c47cd379c4738d158884749ed235
Provides:       bundled(golang(github.com/opencontainers/runc)) = ff819c7e9184c13b7c2607fe6c30ae19403a7aff
Provides:       bundled(golang(github.com/opentracing/opentracing-go)) = d34af3eaa63c4d08ab54863a4bdd0daa45212e12
Provides:       bundled(golang(github.com/pkg/errors)) = 614d223910a179a466c1767a985424175c39b465
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 6edbbd9e560190e318cdc5b4d3e630b442858380
Provides:       bundled(golang(github.com/prometheus/client_model)) = 7bc5445566f0fe75b15de23e6b93886e982d7bf9
Provides:       bundled(golang(github.com/prometheus/common)) = d978bcb1309602d68bb4ba69cf3f8ed900e07308
Provides:       bundled(golang(github.com/prometheus/procfs)) = 46159f73e74d1cb8dc223deef9b2d049286f46b1
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = d3b5b032dc8e8927d31a5071b56e14c89f045135
Provides:       bundled(golang(github.com/shurcooL/sanitized_anchor_name)) = 7bfe4c7ecddb3666a94b053b422cdd8f5aaa3615
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 6699a89a232f3db797f2e280639854bbc4b89725
Provides:       bundled(golang(github.com/spf13/cobra)) = 86f8bfd7fef868a174e1b606783bd7f5c82ddf8f
Provides:       bundled(golang(github.com/spf13/pflag)) = 2e9d26c8c37aae03e3f9d4e90b7116f5accb7cab
Provides:       bundled(golang(github.com/theupdateframework/notary)) = d6e1431feb32348e0650bf7551ac5cffd01d857b
Provides:       bundled(golang(github.com/tonistiigi/fsutil)) = 0834f99b7b85462efb69b4f571a4fa3ca7da5ac9
Provides:       bundled(golang(github.com/tonistiigi/go-rosetta)) = f79598599c5d34ea253b56a1d7c89bc6a96de7db
Provides:       bundled(golang(github.com/tonistiigi/units)) = 6950e57a87eaf136bbe44ef2ec8e75b9e3569de2
Provides:       bundled(golang(github.com/xeipuuv/gojsonpointer)) = 02993c407bfbf5f6dae44c4f4b1cf6a39b5fc5bb
Provides:       bundled(golang(github.com/xeipuuv/gojsonreference)) = bd5ef7bd5415a7ac448318e64f11a24cd21e594b
Provides:       bundled(golang(github.com/xeipuuv/gojsonschema)) = 82fcdeb203eb6ab2a67d0a623d9c19e5e5a64927
Provides:       bundled(golang(golang.org/x/crypto)) = c1f2f97bffc9c53fc40a1a28a5b460094c0050d9
Provides:       bundled(golang(golang.org/x/net)) = ab34263943818b32f575efc978a3d24e80b04bd7
Provides:       bundled(golang(golang.org/x/oauth2)) = bf48bf16ab8d622ce64ec6ce98d2c98f916b6303
Provides:       bundled(golang(golang.org/x/sync)) = cd5d95a43a6e21273425c7ae415d3df9ea832eeb
Provides:       bundled(golang(golang.org/x/sys)) = b64e53b001e413bd5067f36d4e439eded3827374
Provides:       bundled(golang(golang.org/x/term)) = f5c789dd3221ff39d752ac54467d762de7cfbec6
Provides:       bundled(golang(golang.org/x/text)) = 23ae387dee1f90d29a23c0e87ee0b46038fbed0e
Provides:       bundled(golang(golang.org/x/time)) = 555d28b269f0569763d25dbe1a237ae74c6bcc82
Provides:       bundled(golang(google.golang.org/genproto)) = 3f1135a288c9a07e340ae8ba4cc6c7065a3160e8
Provides:       bundled(golang(google.golang.org/grpc)) = f495f5b15ae7ccda3b38c53a1bfcde4c1a58a2bc
Provides:       bundled(golang(go.opencensus.io)) = d835ff86be02193d324330acdb7d65546b05f814
Provides:       bundled(golang(gopkg.in/inf.v0)) = d2d2541c53f18d2a059457998ce2876cc8e67cbf
Provides:       bundled(golang(gopkg.in/yaml.v2)) = 53403b58ad1b561927d19068c655246f2db79d48
Provides:       bundled(golang(gotest.tools/v3)) = bb0d8a963040ea5048dcef1a14d8f8b58a33d4b3
Provides:       bundled(golang(k8s.io/api)) = d49a3f108dab8e8d25f22c497fb48678b124efd2
Provides:       bundled(golang(k8s.io/apimachinery)) = f336d9be0221d10a93a7d6d2ec25f6fc799f4fc6
Provides:       bundled(golang(k8s.io/client-go)) = 002560d5bf54049bf5b5ae99231cb2b591f15954
Provides:       bundled(golang(k8s.io/klog)) = 4ad0115ba9e45c096d06a31d8dfb0e5bd945ec5f
Provides:       bundled(golang(k8s.io/kube-openapi)) = 0270cf2f1c1d995d34b36019a6f65d58e6e33ad4
Provides:       bundled(golang(k8s.io/utils)) = 69764acb6e8e900b7c05296c5d3c9c19545475f9
Provides:       bundled(golang(sigs.k8s.io/yaml)) = fd68e9863619f6ec2fdd8625fe1f02e7c877e480


%description
Docker is an open source project to build, ship and run any application as a
lightweight container.

Docker containers are both hardware-agnostic and platform-agnostic. This means
they can run anywhere, from your laptop to the largest EC2 compute instance and
everything in between - and they don't require you to use a particular
language, framework or packaging system. That makes them great building blocks
for deploying and scaling web apps, databases, and backend services without
depending on a particular stack or provider.

%package fish-completion
Summary: Fish completion files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: fish
Conflicts: %{service_name}-fish-completion
Obsoletes: %{service_name}-fish-completion < 2:%{version}-%{release}
Provides: %{service_name}-fish-completion = %{version}-%{release}

%description fish-completion
This package installs %{summary}.

%package zsh-completion
Summary: Zsh completion files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: zsh
Conflicts: %{service_name}-zsh-completion
Obsoletes: %{service_name}-zsh-completion < 2:%{version}-%{release}
Provides: %{service_name}-zsh-completion = %{version}-%{release}

%description zsh-completion
This package installs %{summary}.

%package nano
Summary: GNU nano syntax highlighting files for Moby
Requires: %{name} = %{version}-%{release}
Requires: nano

%description nano
This package installs %{summary}.

%prep
%autosetup -n moby-%{version}

# untar cli
tar zxf %{SOURCE1}
# correct rpmlint errors for bash completion
sed -i '/env bash/d' cli-%{version}/contrib/completion/bash/docker

# untar tini
tar zxf %{SOURCE2}

%build
export GOPATH="/usr/share/gocode"
mkdir -p _build

# build docker-proxy / libnetwork
(
        export LDFLAGS="-linkmode=external"
        %gobuild -o _build/%{service_name}-proxy github.com/%{service_name}/libnetwork/cmd/proxy
)

# build tini
(
        cd tini-%{commit_tini}
        %cmake .
        make tini-static -C "%{__cmake_builddir}"
)

# build engine
(
        export LDFLAGS="-w"
        export LDFLAGS+=" -X github.com/docker/docker/dockerversion.Version=%{version}"
        export LDFLAGS+=" -X github.com/docker/docker/dockerversion.GitCommit=%{shortcommit_moby}"
        export LDFLAGS+=" -X github.com/docker/docker/dockerversion.IAmStatic=false"
        export LDFLAGS+=" -X 'github.com/docker/docker/dockerversion.BuildTime=$(date -u --rfc-3339 ns)'"
        export BUILDTAGS="seccomp selinux journald"
        %gobuild -o _build/%{service_name}d github.com/%{service_name}/%{service_name}/cmd/dockerd
)

# build cli
(
        cd cli-%{version}
        mkdir -p src/github.com/%{service_name}
        ln -fns ../../.. src/github.com/%{service_name}/cli
        export DISABLE_WARN_OUTSIDE_CONTAINER=1
        export GOPATH="${PWD}"
        export GO111MODULE=off
        make VERSION=%{version} GITCOMMIT=%{shortcommit_cli} dynbinary
        man/md2man-all.sh
)

%install
install -dp %{buildroot}%{_bindir}
install -dp %{buildroot}%{_libexecdir}/%{service_name}

# install binary
install -p -m 755 cli-%{version}/build/%{service_name} %{buildroot}%{_bindir}/%{service_name}
install -p -m 755 _build/%{service_name}d %{buildroot}%{_bindir}/%{service_name}d

# install proxy
install -p -m 755 _build/%{service_name}-proxy %{buildroot}%{_libexecdir}/%{service_name}/%{service_name}-proxy

# install tini
install -p -m 755 tini-%{commit_tini}/%{__cmake_builddir}/tini-static %{buildroot}%{_libexecdir}/%{service_name}/%{service_name}-init

# install udev rules
install -dp %{buildroot}%{_prefix}/lib/udev/rules.d
install -p -m 644 contrib/udev/80-%{service_name}.rules %{buildroot}%{_usr}/lib/udev/rules.d/80-%{service_name}.rules

# add init scripts
install -dp %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}
install -p -m 644 contrib/init/systemd/docker.socket %{buildroot}%{_unitdir}

# for additional args
install -dp %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/%{service_name}

# add bash, zsh, and fish completions
install -dp %{buildroot}%{_datadir}/bash-completion/completions
install -dp %{buildroot}%{_datadir}/zsh/vendor-completions
install -dp %{buildroot}%{_datadir}/fish/vendor_completions.d
install -p -m 644 cli-%{version}/contrib/completion/bash/%{service_name} %{buildroot}%{_datadir}/bash-completion/completions/%{service_name}
install -p -m 644 cli-%{version}/contrib/completion/zsh/_%{service_name} %{buildroot}%{_datadir}/zsh/vendor-completions/_%{service_name}
install -p -m 644 cli-%{version}/contrib/completion/fish/%{service_name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{service_name}.fish

# install manpages
install -dp %{buildroot}%{_mandir}/man{1,5,8}
install -p -m 644 cli-%{version}/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -p -m 644 cli-%{version}/man/man5/*.5 %{buildroot}%{_mandir}/man5
install -p -m 644 cli-%{version}/man/man8/*.8 %{buildroot}%{_mandir}/man8

# add nano files
install -dp %{buildroot}%{_datadir}/nano
install -p -m 644 contrib/syntax/nano/Dockerfile.nanorc %{buildroot}%{_datadir}/nano/Dockerfile.nanorc

for cli_file in LICENSE MAINTAINERS NOTICE README.md; do
    cp "cli-%{version}/$cli_file" "cli-$cli_file"
done

%pre
getent group %{service_name} >/dev/null || groupadd -r %{service_name} || :

%post
%systemd_post %{service_name}.service %{service_name}.socket
%firewalld_reload

%preun
%systemd_preun %{service_name}.service %{service_name}.socket

%postun
%systemd_postun_with_restart %{service_name}.service

%files
%license LICENSE cli-LICENSE
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md MAINTAINERS NOTICE README.md
%doc cli-MAINTAINERS cli-NOTICE cli-README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{service_name}
%{_bindir}/%{service_name}
%{_bindir}/%{service_name}d
%dir %{_libexecdir}/%{service_name}/
%{_libexecdir}/%{service_name}/%{service_name}-proxy
%{_libexecdir}/%{service_name}/%{service_name}-init
%{_usr}/lib/udev/rules.d/80-%{service_name}.rules
%{_unitdir}/%{service_name}.service
%{_unitdir}/%{service_name}.socket
%{_datadir}/bash-completion/completions/%{service_name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files zsh-completion
%dir %{_datadir}/zsh/vendor-completions/
%{_datadir}/zsh/vendor-completions/_%{service_name}

%files fish-completion
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{service_name}.fish

%files nano
%dir %{_datadir}/nano
%{_datadir}/nano/Dockerfile.nanorc

%changelog
* Sun Mar 14 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.5-1
- Update to latest upstream 20.10.5 - fixes #1903426
- Upstream brings compatibility with cgroups v2 - fixes #1746355
- Remove package moby-engine-vim (dockerfile.vim has been merged in upstream vim)
- Remove firewalld docker zone, since dockerd can now communicate with firewalld - fixes #1852680
- Build dockerd and docker-proxy from unbundled source packages
- Remove fixed storage-driver (cf. https://src.fedoraproject.org/rpms/moby-engine/pull-request/6)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 19.03.13-3.ce.git4484c46
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.13-2.ce.git4484c46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 02 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.13-1.ce.git4484c46
- Update to upstream 19.03.13 (#1837641)

* Fri Oct 02 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.11-4.ce.git42e35e6
- Fix FTBFS: adapt to change to CMake builds (#1864160)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.11-3.ce.git42e35e6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.11-2.ce.git42e35e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.11-1.ce.git42e35e6
- Update to upstream 19.03.11 to prevent CVE-2020-13401

* Thu May 07 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.8-2.ce.gitafacb8b
- Configure storage-driver explicitely (fixes #1832301)
- Add firewalld zone: trust interface docker0, as firewalld now uses nftables
  by default and docker communicates with iptables (fixes #1817022)

* Mon Mar 16 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.8-1.ce.gitafacb8b
- Update to latest upstream release - Docker CE 19.03.8
- Prune unused BuildRequires

* Sun Mar 8 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.7-2.ce.git7141c19
- Add Conflicts with docker-ce-cli and Obsoletes docker-common

* Sat Mar 7 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.7-1.ce.git7141c19
- Update to latest upstream release - Docker CE 19.03.7
- Add Epoch: 2 to Obsoletes for docker and docker-latest

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.09.8-3.ce.git0dd43dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09.8-2.ce.git0dd43dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.8-1.ce.git0dd43dd
- Update to latest upstream release - Docker CE 18.09.8

* Sat Jul 13 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-5.ce.git2d0083d
- Move docker-init and docker-proxy to /usr/libexec/docker
- Update moby-engine-nano summary to follow guidelines

* Sat Jul 13 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-4.ce.git2d0083d
- Add nofile ulimit to default docker daemon options (#1715254, #1708115)

* Fri Jul 12 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-3.ce.git2d0083d
- rebuilt

* Fri Jul 12 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-2.ce.git2d0083d
- Depend on packaged versions "runc" and "containerd" instead of building them.

* Thu Jun 27 2019 David Michael <dm0@redhat.com> - 18.09.7-1.ce.git2d0083d
- Update docker-ce to commit 2d0083d (version 18.09.7).
- Update runc to commit 425e105.
- Update containerd to commit 894b81a (1.2.6).
- Update docker-proxy to commit e7933d4.

* Tue May 14 2019 David Michael <dm0@redhat.com> - 18.09.6-1.ce.git481bc77
- Update docker-ce to commit 481bc77 (version 18.09.6).
- Update docker-proxy to commit 872f0a8.
- Obsolete and provide the docker and docker-latest packages. (#1700006)

* Thu Apr 11 2019 David Michael <dm0@redhat.com> - 18.09.5-1.ce.gite8ff056
- Update docker-ce to commit e8ff056 (version 18.09.5).
- Update docker-runc to commit 2b18fe1.
- Update docker-containerd to commit bb71b10 (version 1.2.5).
- Update docker-proxy to commit 4725f21.
- Report the correct engine version.
- Install symlinks to unprefixed runc/containerd program names.

* Thu Mar 28 2019 David Michael <dm0@redhat.com> - 18.06.3-2.ce.gitd7080c1
- Conflict with docker-common. (#1693397)

* Thu Feb 21 2019 David Michael <dm0@redhat.com> - 18.06.3-1.ce.gitd7080c1
- Update docker-ce to commit d7080c1 (version 18.06.3).

* Tue Feb 12 2019 David Michael <dm0@redhat.com> - 18.06.2-1.ce.git6d37f41
- Update docker-ce to commit 6d37f41 (version 18.06.2).
- Update docker-runc to commit a592beb.

* Mon Feb 11 2019 David Michael <dm0@redhat.com> - 18.06.1-3.ce.gite68fc7a
- Apply a runc patch for CVE-2019-5736.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.06.1-2.ce.gite68fc7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 David Michael <dm0@redhat.com> - 18.06.1-1.ce.gite68fc7a
- Update docker-ce to commit e68fc7a (version 18.06.1).
- Update docker-runc to commit 69663f0.
- Update docker-containerd to commit 468a545 (version 1.1.2).
- Update docker-proxy to commit 3ac297b.
- Backport a fix for mounting named volumes.
- Create a "docker" group for non-root Docker access.
- Support systemd socket-activation.
- Make runc and containerd commit IDs match their expected values.
- Preserve containerd debuginfo.

* Mon Nov 12 2018 Marcin Skarbek <rpm@skarbek.name> - 18.06.0-2.ce.git0ffa825
- add configuration file
- update service file

* Sat Aug 18 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 18.06.0-1.ce.git0ffa825
- Resolves: #1539161 - first upload to Fedora
- built docker-ce commit 0ffa825
- built docker-runc commit ad0f5255
- built docker-containerd commit a88b631
- built docker-proxy commit a79d368
- built docker-init commit fec3683

* Tue Mar 20 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-4.ce.gitf5ec1e2
- correct some rpmlint errors

* Wed Feb 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-3.ce
- docker-* symlinks to moby-* (RE: gh PR 34226)

* Wed Feb 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-2.ce
- rename binaries as per upstream gh PR 34226

* Fri Jan 26 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-1
- initial build
- built moby commit f5ec1e2
- built cli commit 4b61f56
- built docker-runc commit 2d41c047
- built docker-containerd commit 3addd84
- built docker-proxy commit 7b2b1fe
