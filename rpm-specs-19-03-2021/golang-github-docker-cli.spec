# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap

# https://github.com/docker/cli
%global goipath         github.com/docker/cli
Version:                20.10.5

%gometa

%global goipaths0       github.com/docker/cli
%global goipathsex0     github.com/docker/cli/cli/command/image

%if %{without bootstrap}
%global goipaths1       github.com/docker/cli/cli/command/image
%endif

%global common_description %{expand:
The docker CLI.}

%global golicenses      LICENSE NOTICE
%global godocs          docs CONTRIBUTING.md README.md TESTING.md AUTHORS

Name:           %{goname}
Release:        1%{?dist}
Summary:        The docker CLI

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         0001-Adapt-to-k8s-client-go-v1.18.patch

BuildRequires:  golang(github.com/containerd/console)
BuildRequires:  golang(github.com/containerd/containerd/platforms)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/clientset)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/clientset/scheme)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/clientset/typed/compose/v1alpha3)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/clientset/typed/compose/v1beta1)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/clientset/typed/compose/v1beta2)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/informers)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/informers/compose)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/informers/compose/v1beta2)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/informers/internalinterfaces)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/client/listers/compose/v1beta2)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/compose/clone)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/compose/impersonation)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/compose/v1alpha3)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/compose/v1beta1)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/compose/v1beta2)
BuildRequires:  golang(github.com/docker/compose-on-kubernetes/api/labels)
BuildRequires:  golang(github.com/docker/distribution)
BuildRequires:  golang(github.com/docker/distribution/manifest/manifestlist)
BuildRequires:  golang(github.com/docker/distribution/manifest/schema2)
BuildRequires:  golang(github.com/docker/distribution/reference)
BuildRequires:  golang(github.com/docker/distribution/registry/api/errcode)
BuildRequires:  golang(github.com/docker/distribution/registry/api/v2)
BuildRequires:  golang(github.com/docker/distribution/registry/client)
BuildRequires:  golang(github.com/docker/distribution/registry/client/auth)
BuildRequires:  golang(github.com/docker/distribution/registry/client/auth/challenge)
BuildRequires:  golang(github.com/docker/distribution/registry/client/transport)
BuildRequires:  golang(github.com/docker/docker-credential-helpers/client)
BuildRequires:  golang(github.com/docker/docker-credential-helpers/credentials)
BuildRequires:  golang(github.com/docker/docker/api)
BuildRequires:  golang(github.com/docker/docker/api/types)
BuildRequires:  golang(github.com/docker/docker/api/types/blkiodev)
BuildRequires:  golang(github.com/docker/docker/api/types/container)
BuildRequires:  golang(github.com/docker/docker/api/types/events)
BuildRequires:  golang(github.com/docker/docker/api/types/filters)
BuildRequires:  golang(github.com/docker/docker/api/types/image)
BuildRequires:  golang(github.com/docker/docker/api/types/mount)
BuildRequires:  golang(github.com/docker/docker/api/types/network)
BuildRequires:  golang(github.com/docker/docker/api/types/registry)
BuildRequires:  golang(github.com/docker/docker/api/types/strslice)
BuildRequires:  golang(github.com/docker/docker/api/types/swarm)
BuildRequires:  golang(github.com/docker/docker/api/types/versions)
BuildRequires:  golang(github.com/docker/docker/api/types/volume)
BuildRequires:  golang(github.com/docker/docker/builder/remotecontext/git)
BuildRequires:  golang(github.com/docker/docker/client)
BuildRequires:  golang(github.com/docker/docker/errdefs)
BuildRequires:  golang(github.com/docker/docker/pkg/archive)
BuildRequires:  golang(github.com/docker/docker/pkg/fileutils)
BuildRequires:  golang(github.com/docker/docker/pkg/homedir)
BuildRequires:  golang(github.com/docker/docker/pkg/idtools)
BuildRequires:  golang(github.com/docker/docker/pkg/ioutils)
BuildRequires:  golang(github.com/docker/docker/pkg/jsonmessage)
BuildRequires:  golang(github.com/docker/docker/pkg/pools)
BuildRequires:  golang(github.com/docker/docker/pkg/progress)
BuildRequires:  golang(github.com/docker/docker/pkg/signal)
BuildRequires:  golang(github.com/docker/docker/pkg/stdcopy)
BuildRequires:  golang(github.com/docker/docker/pkg/streamformatter)
BuildRequires:  golang(github.com/docker/docker/pkg/stringid)
BuildRequires:  golang(github.com/docker/docker/pkg/system)
BuildRequires:  golang(github.com/docker/docker/pkg/urlutil)
BuildRequires:  golang(github.com/docker/docker/registry)
BuildRequires:  golang(github.com/docker/go-connections/nat)
BuildRequires:  golang(github.com/docker/go-connections/tlsconfig)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/docker/swarmkit/api)
BuildRequires:  golang(github.com/docker/swarmkit/api/defaults)
BuildRequires:  golang(github.com/docker/swarmkit/api/genericresource)
BuildRequires:  golang(github.com/fvbommel/sortorder)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/google/shlex)
BuildRequires:  golang(github.com/imdario/mergo)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/moby/buildkit/api/services/control)
BuildRequires:  golang(github.com/moby/buildkit/client)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/dockerignore)
BuildRequires:  golang(github.com/moby/buildkit/session)
%if %{without bootstrap}
BuildRequires:  golang(github.com/moby/buildkit/session/auth/authprovider)
%endif
BuildRequires:  golang(github.com/moby/buildkit/session/filesync)
BuildRequires:  golang(github.com/moby/buildkit/session/secrets/secretsprovider)
BuildRequires:  golang(github.com/moby/buildkit/session/sshforward/sshprovider)
BuildRequires:  golang(github.com/moby/buildkit/util/appcontext)
BuildRequires:  golang(github.com/moby/buildkit/util/progress/progressui)
BuildRequires:  golang(github.com/moby/buildkit/util/progress/progresswriter)
BuildRequires:  golang(github.com/moby/term)
BuildRequires:  golang(github.com/morikuni/aec)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/cobra/doc)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/theupdateframework/notary)
BuildRequires:  golang(github.com/theupdateframework/notary/client)
BuildRequires:  golang(github.com/theupdateframework/notary/client/changelist)
BuildRequires:  golang(github.com/theupdateframework/notary/cryptoservice)
BuildRequires:  golang(github.com/theupdateframework/notary/passphrase)
BuildRequires:  golang(github.com/theupdateframework/notary/storage)
BuildRequires:  golang(github.com/theupdateframework/notary/trustmanager)
BuildRequires:  golang(github.com/theupdateframework/notary/trustpinning)
BuildRequires:  golang(github.com/theupdateframework/notary/tuf/data)
BuildRequires:  golang(github.com/theupdateframework/notary/tuf/signed)
BuildRequires:  golang(github.com/theupdateframework/notary/tuf/utils)
BuildRequires:  golang(github.com/tonistiigi/fsutil/types)
BuildRequires:  golang(github.com/tonistiigi/go-rosetta)
BuildRequires:  golang(github.com/xeipuuv/gojsonschema)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/execabs)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(golang.org/x/text/width)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(gotest.tools/v3/assert)
BuildRequires:  golang(gotest.tools/v3/assert/cmp)
BuildRequires:  golang(gotest.tools/v3/fs)
BuildRequires:  golang(gotest.tools/v3/icmd)
BuildRequires:  golang(gotest.tools/v3/poll)
BuildRequires:  golang(gotest.tools/v3/skip)
BuildRequires:  golang(k8s.io/api/apps/v1beta2)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/apps/v1beta2)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(gotest.tools/v3/env)
BuildRequires:  golang(gotest.tools/v3/golden)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
BuildRequires:  golang(k8s.io/client-go/testing)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

# %%build
# for cmd in cmd/* ; do
#   %%gobuild -o %%{gobuilddir}/bin/$(basename $cmd) %%{goipath}/$cmd
# done

%install
%gopkginstall
# install -m 0755 -vd                     %%{buildroot}%%{_bindir}
# install -m 0755 -vp %%{gobuilddir}/bin/* %%{buildroot}%%{_bindir}/

%%if %{with check}
%check
%gocheck -t cmd \
         -t cli/command \
         -t cli/context \
         -d internal/containerizedengine \
         -t kubernetes
%endif

# %%files
# %%license LICENSE NOTICE
# %%doc docs CONTRIBUTING.md README.md TESTING.md AUTHORS
# %%{_bindir}/*

%gopkgfiles

%changelog
* Sun Mar 14 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.5-1
- Update to 20.10.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jul 25 22:24:04 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.03.12-1
- Update to 19.03.12

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 14:46:13 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.03.5-1
- Update to 19.03.5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.0-1.rc3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.0-1.rc3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 20:37:45 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.03.0-1.rc3
- Release 19.03.0-rc3

* Wed May 01 15:26:24 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 18.09.6-1
- Initial package
