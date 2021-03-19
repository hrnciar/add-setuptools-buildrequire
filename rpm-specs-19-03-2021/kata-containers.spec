# go-rpm-macros are not available on RHEL.
%if 0%{?fedora}
    %global have_go_rpm_macros 1
%else
    %global have_go_rpm_macros 0
%endif

%global with_debug 0

# Shamelessly copied from CRI-O spec file.
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

# https://github.com/rust-lang/rust/issues/47714
%undefine _strict_symbol_defs_build

# We want verbose builds
%global _configure_disable_silent_rules 1

# Use bundled deps as we don't ship the exact right versions for all the
# required rust libraries
%global bundled_rust_deps 1

# Release candidate version tracking
# global rcver rc0
%if 0%{?rcver:1}
%global rcrel .%{rcver}
%global rcstr -%{rcver}
%endif

# htps://github.com/kata-containers/kata-containers
Version: 2.0.1
%global tag         %{version}%{?rcstr}

%global domain      github.com
%global org         kata-containers
%global repo        kata-containers
%global download    %{domain}/%{org}/%{repo}
%global importname  %{download}


%global common_description %{expand:
Kata Containers version 2.x repository. Kata Containers is an open source
project and community working to build a standard implementation of lightweight
Virtual Machines (VMs) that feel and perform like containers, but provide the
workload isolation and security advantages of VMs. https://katacontainers.io/.}

%global golicenses  LICENSE \\\
                    src/agent/LICENSE

%global godocs      README.md \\\
                    CODE_OF_CONDUCT.md \\\
                    CONTRIBUTING.md\\\
                    src/agent/README.md

Name:       %{repo}
Release:    1%{?rcrel}%{?dist}
Summary:    Kata Containers version 2.x repository
License:    ASL 2.0
Url:        https://%{download}
Source0:    https://%{download}/archive/%{version}%{?rcstr}/%{repo}-%{version}%{?rcstr}.tar.gz
Source1:    kata-osbuilder.sh
Source2:    kata-osbuilder-generate.service
%if 0%{?fedora}
Source3:    15-dracut-fedora.conf
%else
Source3:    15-dracut-rhel.conf
%endif

Patch0001:  0001-Add-vendor-code.patch
# Keep this patch downstream as it'd be hard to justify such change upstream
Patch0999:  0999-osbuilder-Adjust-agent_version-for-our-builds.patch
Patch1000:  1000-Remove-shebang-in-non-executable-completion-script.patch


%if 0%{?have_go_rpm_macros}
BuildRequires: go-rpm-macros
%else
BuildRequires: compiler(go-compiler)
BuildRequires: golang
%endif

BuildRequires: git-core
BuildRequires: libselinux-devel
BuildRequires: make
BuildRequires: systemd
BuildRequires: gcc
BuildRequires: protobuf-compiler

%{?systemd_requires}
# %%check requirements
BuildRequires: dracut
BuildRequires: kernel

%if 0%{?fedora}
BuildRequires: busybox
%endif

%if 0%{?bundled_rust_deps}
BuildRequires: cargo
BuildRequires: rust
%else
# Generated using rust2rpm
# [dependencies]
BuildRequires: rust-packaging
BuildRequires: (crate(anyhow/default) >= 1.0.32 with crate(anyhow/default) < 2.0.0)
BuildRequires: (crate(lazy_static/default) >= 1.3.0 with crate(lazy_static/default) < 2.0.0)
BuildRequires: (crate(libc/default) >= 0.2.58 with crate(libc/default) < 0.3.0)
BuildRequires: (crate(log/default) >= 0.4.11 with crate(log/default) < 0.5.0)
BuildRequires: (crate(nix/default) >= 0.17.0 with crate(nix/default) < 0.18.0)
BuildRequires: (crate(prctl/default) >= 1.0.0 with crate(prctl/default) < 2.0.0)
BuildRequires: (crate(procfs/default) >= 0.7.9 with crate(procfs/default) < 0.8.0)
BuildRequires: (crate(prometheus/default) >= 0.9.0 with crate(prometheus/default) < 0.10.0)
BuildRequires: (crate(prometheus/process) >= 0.9.0 with crate(prometheus/process) < 0.10.0)
BuildRequires: (crate(regex/default) >= 1.0.0 with crate(regex/default) < 2.0.0)
BuildRequires: (crate(scan_fmt/default) >= 0.2.3 with crate(scan_fmt/default) < 0.3.0)
BuildRequires: (crate(scopeguard/default) >= 1.0.0 with crate(scopeguard/default) < 2.0.0)
BuildRequires: (crate(serde_json/default) >= 1.0.39 with crate(serde_json/default) < 2.0.0)
BuildRequires: (crate(signal-hook/default) >= 0.1.9 with crate(signal-hook/default) < 0.2.0)
BuildRequires: (crate(slog-scope/default) >= 4.1.2 with crate(slog-scope/default) < 5.0.0)
BuildRequires: (crate(slog-stdlog/default) >= 4.0.0 with crate(slog-stdlog/default) < 5.0.0)
BuildRequires: (crate(slog/default) >= 2.5.2 with crate(slog/default) < 3.0.0)
BuildRequires: (crate(slog/dynamic-keys) >= 2.5.2 with crate(slog/dynamic-keys) < 3.0.0)
BuildRequires: (crate(slog/max_level_trace) >= 2.5.2 with crate(slog/max_level_trace) < 3.0.0)
BuildRequires: (crate(slog/release_max_level_info) >= 2.5.2 with crate(slog/release_max_level_info) < 3.0.0)
BuildRequires: (crate(tempfile/default) >= 3.1.0 with crate(tempfile/default) < 4.0.0)
BuildRequires: crate(cgroups/default) >= 0.0.0
BuildRequires: crate(logging/default) >= 0.0.0
BuildRequires: crate(netlink/default) >= 0.0.0
BuildRequires: crate(netlink/with-agent-handler) >= 0.0.0
BuildRequires: crate(netlink/with-log) >= 0.0.0
BuildRequires: crate(oci/default) >= 0.0.0
BuildRequires: crate(protobuf/default) = 2.14.0
BuildRequires: crate(protocols/default) >= 0.0.0
BuildRequires: crate(rustjail/default) >= 0.0.0
BuildRequires: crate(ttrpc/default) >= 0.0.0
%endif

%if 0%{?fedora}
Requires: busybox
%endif

Requires: dracut
Requires: kernel
Requires: qemu-kvm-core >= 4.2.0-4

Conflicts: kata-agent
Conflicts: kata-ksm-throttler
Conflicts: kata-osbuilder
Conflicts: kata-proxy
Conflicts: kata-runtime
Conflicts: kata-shim

# The following architectures lack the required qemu support
# s390 fail to build: https://github.com/kata-containers/kata-containers/issues/1204
ExcludeArch: %{arm} %{ix86} s390 s390x


%description
%{common_description}

%gopkg


# Common variables to pass to 'make'
# The machine type uses a modern default
# The kernel parameters workaround an issue with cgroupsv2 after kernel 5.3
# To-do: add BUILDFLAGS=gobuildflags when the macro becomes available
%global qemu qemu-kvm
%if 0%{?fedora}
%global qemupath %{_bindir}/%{qemu}
%else
%global qemupath %{_libexecdir}/%{qemu}
%endif

# The machine type to be used is architecture specific:
# aarch64: virt
# ppc64le: pseries
# s390x: s390-ccw-virtio
# x86_64: q35
%ifarch aarch64
%global machinetype "virt"
%endif
%ifarch ppc64le
%global machinetype "pseries"
%endif
%ifarch s390x
%global machinetype "s390-ccw-virtio"
%endif
%ifarch x86_64
%global machinetype "q35"
%endif

%global katadatadir             %{_datadir}/kata-containers
%global katadefaults            %{katadatadir}/defaults
%global katacache               %{_localstatedir}/cache
%global katalibexecdir          %{_libexecdir}/kata-containers
%global katalocalstatecachedir  %{katacache}/kata-containers

%global kataagentdir            %{katalibexecdir}/agent
%global kataosbuilderdir        %{katalibexecdir}/osbuilder

%global runtime_make_vars       QEMUPATH=%{qemupath} \\\
                                KERNELTYPE="compressed" \\\
                                DEFSHAREDFS="virtio-fs" \\\
                                DEFVIRTIOFSDAEMON=%{_libexecdir}/"virtiofsd" \\\
                                DEFVIRTIOFSCACHESIZE=0 \\\
                                DEFSANDBOXCGROUPONLY=true \\\
                                SKIP_GO_VERSION_CHECK=y \\\
                                MACHINETYPE=%{machinetype} \\\
                                SCRIPTS_DIR=%{_bindir} \\\
                                DESTDIR=%{buildroot} \\\
                                PREFIX=/usr \\\
                                DEFAULTSDIR=%{katadefaults} \\\
                                CONFDIR=%{katadefaults} \\\
                                FEATURE_SELINUX="yes"

%global agent_make_vars         LIBC=gnu \\\
                                DESTDIR=%{buildroot}%{kataagentdir}

%prep
%autosetup -S git -p1 -n %{repo}-%{version}%{?rcstr}

# Not using gobuild here in order to stick to how upstream builds
# (This builds multiple binaries)
%build
export PATH=$PATH:"$(pwd)/go/bin"
export GOPATH="$(pwd)/go"

mkdir -p go/src/%{domain}/%{org}
ln -s $(pwd)/../%{repo}-%{version}%{?rcstr} go/src/%{importname}
cd go/src/%{importname}

pushd src/runtime
%make_build %{runtime_make_vars}
popd

pushd src/agent
%make_build %{agent_make_vars}
touch kata-agent
popd

pushd tools/osbuilder
# Manually build nsdax tool
gcc %{build_cflags} image-builder/nsdax.gpl.c -o nsdax
popd

# Not using gopkginstall here in order to stick to how upstream builds
%install
export GOPATH=$(pwd)/go
export PATH=$PATH:$GOPATH/bin

cd go/src/%{importname}

install -m 0644 -D -t %{buildroot}%{katalibexecdir} VERSION

pushd src/runtime
%make_install %{runtime_make_vars}
popd

pushd src/agent
%make_install %{agent_make_vars}
popd

pushd tools/osbuilder
rm .gitignore
rm rootfs-builder/.gitignore
mkdir -p %{buildroot}%{katalocalstatecachedir}

install -m 0644 -D -t %{buildroot}%{_unitdir} %{SOURCE2}
install -m 0755 -D -t %{buildroot}%{kataosbuilderdir} nsdax
install -m 0644 -D -t %{buildroot}%{kataosbuilderdir} %{SOURCE1}

cp -aR rootfs-builder %{buildroot}%{kataosbuilderdir}
cp -aR image-builder  %{buildroot}%{kataosbuilderdir}
cp -aR initrd-builder %{buildroot}%{kataosbuilderdir}
cp -aR scripts        %{buildroot}%{kataosbuilderdir}
cp -aR dracut         %{buildroot}%{kataosbuilderdir}

rm -f %{buildroot}%{kataosbuilderdir}/image-builder/nsdax.gpl.c
install -m 0644 -D -t %{buildroot}%{kataosbuilderdir}/dracut/dracut.conf.d/ %{SOURCE3}
chmod +x %{buildroot}%{kataosbuilderdir}/scripts/lib.sh
chmod +x %{buildroot}%{kataosbuilderdir}/kata-osbuilder.sh
popd

# Disable the image= option, so we use initrd= by default
# The kernels kata-osbuilder creates are in /var/cache now, see rhbz#1792216
sed -i -e 's|^kernel = "%{_datadir}|kernel = "%{katacache}|' \
       -e 's|^image = "%{_datadir}/kata-containers/kata-containers.img"|initrd = "%{katacache}/kata-containers/kata-containers-initrd.img"|' \
       %{buildroot}%{_datadir}/kata-containers/defaults/configuration.toml

# Enable vsock as transport instead of virtio-serial
sed -i -e 's/^#use_vsock =/use_vsock =/' %{buildroot}%{_datadir}/kata-containers/defaults/configuration.toml

# Remove non-tested / non-supported configuration files
rm %{buildroot}%{_datadir}/kata-containers/defaults/configuration-*.toml

# We could be run in a mock chroot, where uname will report
# different kernel than what we have installed in the chroot.
# So we need to determine a valid kernel version to test against.
for kernelpath in /lib/modules/*/vmlinu*; do
    KVERSION="$(echo $kernelpath | cut -d "/" -f 4)"
    break
done
TEST_MODE=1 %{buildroot}%{kataosbuilderdir}/kata-osbuilder.sh \
    -o %{buildroot}%{kataosbuilderdir} \
    -k "$KVERSION" \
    -a %{buildroot}


%preun
%systemd_preun kata-osbuilder-generate.service
%postun
%systemd_postun kata-osbuilder-generate.service
%post
# Skip running this on Fedora CoreOS / Red Hat CoreOS
if test -w %{katalocalstatecachedir}; then
    %systemd_post kata-osbuilder-generate.service

    TMPOUT="$(mktemp -t kata-rpm-post-XXXXXX.log)"
    echo "Creating kata appliance initrd..."
    %{kataosbuilderdir}/kata-osbuilder.sh > ${TMPOUT} 2>&1
    if test "$?" != "0" ; then
        echo "Building failed. Here is the log details:"
        cat ${TMPOUT}
        exit 1
    fi
fi


%files
# runtime
%{_bindir}/kata-runtime
%{_bindir}/kata-monitor
%{_bindir}/containerd-shim-kata-v2
%{_bindir}/kata-collect-data.sh
%dir %{katalibexecdir}
%{katalibexecdir}/VERSION
%{katalibexecdir}/kata-netmon
%dir %{katadatadir}
%dir %{katadefaults}
%{katadefaults}/configuration.toml
%{_datadir}/bash-completion/completions/kata-runtime
%license LICENSE
%doc README.md CONTRIBUTING.md

#agent
%dir %{kataagentdir}
%{kataagentdir}/*

#osbuilder
%dir %{kataosbuilderdir}
%dir %{katalocalstatecachedir}

%{kataosbuilderdir}/*
%{_unitdir}/kata-osbuilder-generate.service


# Remove some scripts we don't use
%exclude %{kataosbuilderdir}/rootfs-builder/alpine
%exclude %{kataosbuilderdir}/rootfs-builder/centos
%exclude %{kataosbuilderdir}/rootfs-builder/clearlinux
%exclude %{kataosbuilderdir}/rootfs-builder/debian
%exclude %{kataosbuilderdir}/rootfs-builder/fedora
%exclude %{kataosbuilderdir}/rootfs-builder/template
%exclude %{kataosbuilderdir}/rootfs-builder/suse
%exclude %{kataosbuilderdir}/rootfs-builder/ubuntu


%changelog
* Mon Mar 08 2021 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 2.0.1-1
- Kata-containers 2.0.1

* Thu Dec 17 2020 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 2.0.0-1
- Adjust package for Fedora review.

* Thu Nov 26 2020 Fabiano Fidêncio <fabiano@fidencio.org> - 2.0.0-0
- Initial packaging
