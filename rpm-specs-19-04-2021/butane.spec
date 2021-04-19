# Originally generated by go2rpm 1.3
%bcond_without check

# https://github.com/coreos/butane
%global goipath         github.com/coreos/butane
%global gomodulesmode   GO111MODULE=on
Version:                0.11.0

%gometa

%global common_description %{expand:
Butane translates human-readable Butane Configs into machine-readable Ignition
configs for provisioning operating systems that use Ignition.}

%global golicenses      LICENSE
%global godocs          docs README.md NEWS

Name:           butane
Release:        1%{?dist}
Summary:        Butane config transpiler

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Fix test failure on 32-bit
# https://github.com/coreos/vcontext/pull/14
Patch0:         butane-0.11.0-fix-vcontext-report-copy.patch

# Upgrade path from old FCCT package; can be dropped in Fedora 36
Provides:       fedora-coreos-config-transpiler = %{version}-%{release}
Obsoletes:      fedora-coreos-config-transpiler < 0.10.0-2
# Provided by FCCT package; can be dropped in Fedora 36
Provides:       fcct = %{version}-%{release}

# Generated by go-mods-to-bundled-provides.py
Provides: bundled(golang(github.com/clarketm/json)) = 1.14.1
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 0.3.0
Provides: bundled(golang(github.com/coreos/go-systemd/unit)) = 0.0.0-20190321100706.git95778dfbb74e
Provides: bundled(golang(github.com/coreos/go-systemd/v22/unit)) = 0.0.0-20190321100706.git95778dfbb74e
Provides: bundled(golang(github.com/coreos/ignition/v2/config/merge)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/shared/errors)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/shared/validations)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/util)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_0/types)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_1/types)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_2/types)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_3_experimental/types)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/ignition/v2/config/validate)) = 2.9.1-20210304043908.git47da4066daa8
Provides: bundled(golang(github.com/coreos/vcontext/json)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/path)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/report)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/tree)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/validate)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/yaml)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/davecgh/go-spew/spew)) = 1.1.1
Provides: bundled(golang(github.com/spf13/pflag)) = 1.0.5
Provides: bundled(golang(github.com/stretchr/testify/assert)) = 1.5.1
Provides: bundled(golang(github.com/vincent-petithory/dataurl)) = 0.0.0-20160330182126.git9a301d65acbb
Provides: bundled(golang(gopkg.in/yaml.v3)) = 3.0.0-20191010095647.gitfc94e3f71652

%description
%{common_description}

%package nonlinux
Summary:       Butane for macOS and Windows
License:       ASL 2.0
BuildArch:     noarch

%description nonlinux
%{common_description}

This package contains macOS and Windows Butane binaries built through
cross-compilation. Do not install it. It is only used for building release
binaries to be signed by Fedora release engineering and uploaded to the
Butane GitHub releases page.

%prep
%goprep -k
%autopatch -p1

%build
export LDFLAGS="-X github.com/coreos/butane/internal/version.Raw=%{version} "
export GOFLAGS="-mod=vendor"

echo "Building butane..."
%gobuild -o ./butane internal/main.go

%global gocrossbuild go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x 

echo "Building macOS Butane..."
GOARCH=amd64 GOOS=darwin %gocrossbuild -o butane-x86_64-apple-darwin internal/main.go

echo "Building Windows Butane..."
GOARCH=amd64 GOOS=windows %gocrossbuild -o butane-x86_64-pc-windows-gnu.exe internal/main.go

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./butane %{buildroot}%{_bindir}
ln -s butane %{buildroot}%{_bindir}/fcct
install -d -p %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-x86_64-apple-darwin %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-x86_64-pc-windows-gnu.exe %{buildroot}%{_datadir}/butane

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/butane
%{_bindir}/fcct

%files nonlinux
%license %{golicenses}
%dir %{_datadir}/butane
%{_datadir}/butane/butane-x86_64-apple-darwin
%{_datadir}/butane/butane-x86_64-pc-windows-gnu.exe

%changelog
* Tue Apr 06 2021 Benjamin Gilbert <bgilbert@redhat.com> - 0.11.0-1
- Initial package
