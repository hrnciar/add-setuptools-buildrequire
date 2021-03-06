# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/google/go-containerregistry
%global goipath         github.com/google/go-containerregistry
Version:                0.4.1

%gometa

%global common_description %{expand:
Go library and CLIs for working with container registries.}

%global golicenses      LICENSE
%global godocs          README.md CONTRIBUTING.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library and CLIs for working with container registries

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/containerd/stargz-snapshotter/estargz)
BuildRequires:  golang(github.com/docker/cli/cli/config)
BuildRequires:  golang(github.com/docker/cli/cli/config/types)
BuildRequires:  golang(github.com/docker/distribution/registry/client/auth/challenge)
BuildRequires:  golang(github.com/docker/docker/api/types)
BuildRequires:  golang(github.com/docker/docker/client)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/cobra/doc)
BuildRequires:  golang(k8s.io/kubernetes/pkg/credentialprovider)
BuildRequires:  golang(k8s.io/kubernetes/pkg/credentialprovider/aws)
BuildRequires:  golang(k8s.io/kubernetes/pkg/credentialprovider/azure)
BuildRequires:  golang(k8s.io/kubernetes/pkg/credentialprovider/gcp)
BuildRequires:  golang(k8s.io/kubernetes/pkg/credentialprovider/secrets)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/rest)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i "s|github.com/vdemeester/k8s-pkg-credentialprovider|k8s.io/kubernetes/pkg/credentialprovider|" $(find . -iname "*.go" -type f)

%build
for cmd in cmd/* ; do
  if [ $(basename $cmd) = "registry" ]; then
    # Binary "registry" already exists in Fedora; renaming to containerregistry
    %gobuild -o %{gobuilddir}/bin/containerregistry %{goipath}/$cmd
  elif [ $(basename $cmd) != "ko" ]; then
    # cmd/ko contains no go code
    %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
  fi
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# Exclude unit tests in pkg/v1/google because they require gcloud installed
# Exclude unit tests in pkg/v1/tarball because they require network
%gocheck -d pkg/v1/google -d pkg/v1/tarball
%endif

%files
%license LICENSE
%doc README.md CONTRIBUTING.md cmd/crane/README.md cmd/crane/doc
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Mar 16 2021 Olivier Lemasle <o.lemasle@gmail.com> - 0.4.1-1
- Update to latest upstream 0.4.1

* Wed Jan 27 22:24:20 CET 2021 Olivier Lemasle <o.lemasle@gmail.com> - 0.4.0-1
- Initial package

