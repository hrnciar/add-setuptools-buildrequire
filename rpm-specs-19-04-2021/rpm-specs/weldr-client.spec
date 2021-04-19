# Pass --with tests to rpmbuild to build composer-cli-tests
%bcond_with tests

%global goipath         github.com/osbuild/weldr-client

Name:      weldr-client
Version:   35.1
Release:   1%{?dist}
# Upstream license specification: Apache-2.0
License:   ASL 2.0
Summary:   Command line utility to control osbuild-composer
Url:       %{gourl}
Source0:   https://github.com/osbuild/weldr-client/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:   https://github.com/osbuild/weldr-client/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:   https://keys.openpgp.org/vks/v1/by-fingerprint/117E8C168EFE3A7F#/gpg-117E8C168EFE3A7F.key

Obsoletes: composer-cli < 34.0
Provides: composer-cli = %{version}-%{release}

%gometa

BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
%if 0%{?fedora}
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/spf13/cobra)
# Required for tests and %check
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

BuildRequires: git-core
BuildRequires: make
BuildRequires: gnupg2


%description
Command line utility to control osbuild-composer

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%if 0%{?rhel}
%forgeautosetup -p1
%else
%goprep
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
%else
export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"
export GO111MODULE=off
%endif

export LDFLAGS="-X github.com/osbuild/weldr-client/cmd/composer-cli/root.Version=%{version} "
make GOBUILDFLAGS="%{gobuildflags}" build

## TODO
##make man

%if %{with tests} || 0%{?rhel}
# Build test binaries with `go test -c`, so that they can take advantage of
# golang's testing package. The golang rpm macros don't support building them
# directly. Thus, do it manually, taking care to also include a build id.
#
# On Fedora, also turn off go modules and set the path to the one into which
# the golang-* packages install source code.
%if 0%{?fedora}
export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"
export GO111MODULE=off
%endif

export LDFLAGS="-X github.com/osbuild/weldr-client/cmd/composer-cli/root.Version=%{version} "
export BUILDTAGS="integration"
make GOBUILDFLAGS="%{gobuildflags}" integration
%endif

%install
make DESTDIR=%{buildroot} install

%if %{with tests} || 0%{?rhel}
make DESTDIR=%{buildroot} install-tests
%endif

%check
%if 0%{?fedora}
export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"
export GO111MODULE=off
%endif

export LDFLAGS="-X github.com/osbuild/weldr-client/cmd/composer-cli/root.Version=%{version} "
make GOBUILDFLAGS="%{gotestflags}" test

%files
%license LICENSE
%doc examples HACKING.md README.md
%{_bindir}/composer-cli
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/composer-cli
%{_mandir}/man1/composer-cli*

%if %{with tests} || 0%{?rhel}
%package tests
Summary:    Integration tests for composer-cli

%description tests
Integration tests to be run on a pristine-dedicated system to test the
composer-cli package.

%files tests
%license LICENSE
%{_libexecdir}/tests/composer-cli/
%endif


%changelog
* Mon Apr 12 2021 Brian C. Lane <bcl@redhat.com> - 35.1-1
- New release: 35.1 (bcl)
- spec: Change release back to 1 (bcl)
- spec: Move testify BuildRequires into fedora block (bcl)
- vendor: Add vendored dependencies for RHEL (bcl)
- tools: Add prepare-source.sh vendoring helper script (bcl)
- Makefile: skip vendor directory for check target (bcl)
- spec: Bump release to 2 (bcl)
- spec: Fix BuildRequires for tests (bcl)
- Makefile: Remove executable from bash completion (bcl)
- Makefile: Only use GOBUILDFLAGS (bcl)
- spec: Bump release to 2 (bcl)
- spec: Add doc files (bcl)
- spec: Add gpg signature verification (bcl)
- spec: Use git-core instead of git (bcl)
- spec: Set License to Apache 2.0 (bcl)
- spec: Update Source urls with new project location (bcl)