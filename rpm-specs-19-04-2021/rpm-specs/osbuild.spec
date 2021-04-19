%global         forgeurl https://github.com/osbuild/osbuild
%global         selinuxtype targeted

Version:        28

%forgemeta

%global         pypi_name osbuild
%global         pkgdir %{_prefix}/lib/%{pypi_name}

Name:           %{pypi_name}
Release:        1%{?dist}
License:        ASL 2.0

URL:            %{forgeurl}

Source0:        %{forgesource}
BuildArch:      noarch
Summary:        A build system for OS images

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docutils

Requires:       bash
Requires:       bubblewrap
Requires:       coreutils
Requires:       curl
Requires:       dnf
Requires:       e2fsprogs
Requires:       glibc
Requires:       policycoreutils
Requires:       qemu-img
Requires:       systemd
Requires:       tar
Requires:       util-linux
Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})

# Turn off dependency generators for runners. The reason is that runners are
# tailored to the platform, e.g. on RHEL they are using platform-python. We
# don't want to pick up those dependencies on other platform.
%global __requires_exclude_from ^%{pkgdir}/(runners)/.*$

# Turn off shebang mangling on RHEL. brp-mangle-shebangs (from package
# redhat-rpm-config) is run on all executables in a package after the `install`
# section runs. The below macro turns this behavior off for:
#   - runners, because they already have the correct shebang for the platform
#     they're meant for, and
#   - stages and assemblers, because they are run within osbuild build roots,
#     which are not required to contain the same OS as the host and might thus
#     have a different notion of "platform-python".
# RHEL NB: Since assemblers and stages are not excluded from the dependency
# generator, this also means that an additional dependency on /usr/bin/python3
# will be added. This is intended and needed, so that in the host build root
# /usr/bin/python3 is present so stages and assemblers can be run.
%global __brp_mangle_shebangs_exclude_from ^%{pkgdir}/(assemblers|runners|stages)/.*$

%{?python_enable_dependency_generator}

%description
A build system for OS images

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A build system for OS images

%package        ostree
Summary:        OSTree support
Requires:       %{name} = %{version}-%{release}
Requires:       ostree
Requires:       rpm-ostree

%description ostree
Contains the necessary stages, assembler and source
to build OSTree based images.

%package        selinux
Summary:        SELinux policies
Requires:       %{name} = %{version}-%{release}
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description    selinux
Contains the necessary SELinux policies that allows
osbuild to use labels unknown to the host inside the
containers it uses to build OS artifacts.

%prep
%forgesetup

%build
%py3_build
make man

# SELinux
make -f /usr/share/selinux/devel/Makefile osbuild.pp
bzip2 -9 osbuild.pp

%pre
%selinux_relabel_pre -s %{selinuxtype}

%install
%py3_install

mkdir -p %{buildroot}%{pkgdir}/stages
install -p -m 0755 $(find stages -type f) %{buildroot}%{pkgdir}/stages/

mkdir -p %{buildroot}%{pkgdir}/assemblers
install -p -m 0755 $(find assemblers -type f) %{buildroot}%{pkgdir}/assemblers/

mkdir -p %{buildroot}%{pkgdir}/runners
install -p -m 0755 $(find runners -type f -or -type l) %{buildroot}%{pkgdir}/runners

mkdir -p %{buildroot}%{pkgdir}/sources
install -p -m 0755 $(find sources -type f) %{buildroot}%{pkgdir}/sources

mkdir -p %{buildroot}%{pkgdir}/inputs
install -p -m 0755 $(find inputs -type f) %{buildroot}%{pkgdir}/inputs

# mount point for bind mounting the osbuild library
mkdir -p %{buildroot}%{pkgdir}/osbuild

# schemata
mkdir -p %{buildroot}%{_datadir}/osbuild/schemas
install -p -m 0755 $(find schemas/*.json) %{buildroot}%{_datadir}/osbuild/schemas
ln -s %{_datadir}/osbuild/schemas %{buildroot}%{pkgdir}/schemas

# documentation
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
install -p -m 0644 -t %{buildroot}%{_mandir}/man1/ docs/*.1
install -p -m 0644 -t %{buildroot}%{_mandir}/man5/ docs/*.5

# SELinux
install -D -m 644 -t %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype} %{name}.pp.bz2
install -D -m 644 -t %{buildroot}%{_mandir}/man8 selinux/%{name}_selinux.8

%check
exit 0
# We have some integration tests, but those require running a VM, so that would
# be an overkill for RPM check script.

%files
%license LICENSE
%{_bindir}/osbuild
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}-manifest.5*
%{_datadir}/osbuild/schemas
%{pkgdir}
# the following files are in the ostree sub-package
%exclude %{pkgdir}/assemblers/org.osbuild.ostree.commit
%exclude %{pkgdir}/sources/org.osbuild.ostree
%exclude %{pkgdir}/stages/org.osbuild.ostree
%exclude %{pkgdir}/stages/org.osbuild.rpm-ostree

%files -n       python3-%{pypi_name}
%license LICENSE
%doc README.md NEWS.md
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%files ostree
%{pkgdir}/assemblers/org.osbuild.ostree.commit
%{pkgdir}/sources/org.osbuild.ostree
%{pkgdir}/stages/org.osbuild.ostree
%{pkgdir}/stages/org.osbuild.rpm-ostree

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%{_mandir}/man8/%{name}_selinux.8.*
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%changelog
* Thu Apr  8 2021 Christian Kellner <ckellner@redhat.com> - 28-1
- Upstream release 28
- Drop Fedora 35 runner patch incldued in release 28.

* Wed Mar 17 2021 Christian Kellner <ckellner@redhat.com> - 27-2
- Include Fedora 35 runner (upstream commit 337e0f0)

* Tue Mar 16 2021 Christian Kellner <ckellner@redhat.com> - 27-1
- Upstream release 27
- Various bug fixes related to the new container and installer
  stages introdcued in version 25 and 26.

* Sat Feb 20 2021 Christian Kellner <ckellner@redhat.com> - 26-1
- Upstream release 26
- Support for building boot isos
- Grub stage gained support for 'saved_entry' to fix grub tooling

* Fri Feb 12 2021 Christian Kellner <ckellner@redhat.com> - 25-1
- Upstream release 25
- First tech preview of the new manifest format. Includes
  various new stages and inputs to be able to build ostree
  commits contained in a oci archive.

* Thu Jan 28 2021 Christian Kellner <ckellner@redhat.com> - 24-1
- Upstream release 24
- Turn on dependency generator for everything but runners
- Include new 'input' binaries

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Christian Kellner <ckellner@redhat.com> - 23-1
- Upstream release 23
- Do not mangle shebangs for assemblers, runners & stages.

* Mon Oct 12 2020 Christian Kellner <ckellner@redhat.com> - 22-1
- Upstream release 22

* Thu Sep 10 2020 Christian Kellner <ckellner@redhat.com> - 21-1
- Upstream reelase 21

* Thu Aug 13 2020 Christian Kellner <ckellner@redhat.com> - 20-1
- Upstream reelase 20

* Fri Aug  7 2020 Christian Kellner <ckellner@redhat.com> - 19-1
- Upstream release 19
- Drop no-floats-in-sources.patch included in release 19
- bubblewrap replaced systemd-nspawn for sandboxing; change the
  requirements accordingly.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Christian Kellner <ckellner@redhat.com> - 18-2
- Add patch to not pass floats to curl in the files source
  https://github.com/osbuild/osbuild/pull/459

* Tue Jun 23 2020 Christian Kellner <ckellner@redhat.com> - 18-1
- Upstream release 18
- All RHEL runners now use platform-python.

* Wed Jun 10 2020 Christian Kellner <ckellner@redhat.com> - 17-1
- new upstream relaese 17
- Add custom SELinux policy that lets osbuild set labels inside
  the build root that are unknown to the host.

* Thu Jun  4 2020 Christian Kellner <ckellner@redhat.com> - 16-1
- new upstream release 16
- Drop sources-fix-break-when-secrets-is-None.patch included in
  the new upstream reelase.

* Wed May 27 2020 Miro Hrončok <mhroncok@redhat.com> - 15-4
- Rebuilt for Python 3.9

* Tue May 26 2020 Christian Kellner <ckellner@redhat.com> - 15-3
- Add a patch to allow org.osbuild.files source in the new format
  but without actually containing the secrets key.
  Taken from merged PR: https://github.com/osbuild/osbuild/pull/416

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 15-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Christian Kellner <ckellner@redhat.com> - 15-1
- new upstream release 15

* Wed May  6 2020 Christian Kellner <christian@kellner.me> - 14-2
- Install schemata to <datadir>/osbuild/schemas and include a
  symlink to it in /usr/lib/osbuild/schemas

* Wed May  6 2020 Christian Kellner <christian@kellner.me> - 14-1
- new upstream release 14
- The directories /usr/lib/osbuild/{assemblers, stages}/osbuild
  got removed. Changes to osbuild made them obsolete.

* Wed Apr 15 2020 Christian Kellner <ckellner@redhat.com> - 12-1
- new upstream release 12
- Specify the exact version in the 'python3-osbuild' requirement
  to avoid the library and the main binary being out of sync.
- osbuild-ostree sub-package with the necessary bits to create
  OSTree based images

* Thu Apr  2 2020 Christian Kellner <ckellner@redhat.com> - 11-1
- new upstream release 11
- Turn of dependency generator for internal components

* Thu Mar 19 2020 Christian Kellner <ckellner@redhat.com> - 10-1
- new upstream release 10
- build and include man pages, this adds 'make' and 'python3-docutils'
  to the build requirements
- add NEWS.md file with the release notes

* Thu Mar  5 2020 Christian Kellner <ckellner@redhat.com> - 9-1
- new upstream release: 9
- Remove host runner link, it now is being auto-detected
- Cleanup use of mixed use of spaces/tabs

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Packit Service <user-cont-team+packit-service@redhat.com> - 7-1
- new upstream release: 7

* Sat Nov 30 2019 Tom Gundersen <teg@jklm.no> - 6-1
- new upstream release: 6

* Wed Oct 30 2019 Lars Karlitski <lars@karlitski.net> - 5-1
- new upstream release: 5

* Wed Oct 16 2019 Tom Gundersen <tgunders@redhat.com> - 4-1
- new upstream release: 4

* Fri Oct 04 2019 Lars Karlitski <lars@karlitski.net> - 3-1
- new upstream release: 3

* Wed Sep 18 2019 Martin Sehnoutka <msehnout@redhat.com> - 2-1
- new upstream release: 2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1-3
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Martin Sehnoutka <msehnout@redhat.com> - 1-2
- update upstream URL to the new Github organization

* Wed Jul 17 2019 Martin Sehnoutka <msehnout@redhat.com> - 1-1
- Initial package
