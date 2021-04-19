# https://github.com/genuinetools/reg
# EPEL build is curently broken due to golang macros not working
%global goipath         github.com/genuinetools/reg
Version:                0.16.1

%gometa

%global common_description %{expand:
Docker registry v2 command line client and repo listing generator with security
checks.}

%global golicenses      LICENSE
%global godocs          VERSION.txt README.md

Name:       reg
Release:    3%{?dist}
Summary:    Docker registry v2 command line client


License:    MIT
URL:        %{gourl}
Source0:    %{gosource}

# Upstream advertises this as something that's meant to be run in a container
# and doesn't provide a systemd unit or sysV init script or sysconfig files
# so I'm providing them here.
Source1:    reg-server.service
Source2:    sysconfig.reg-server

# https://github.com/genuinetools/reg/pull/200
Patch0: fix-row-cell-index-for-server-searching-feature.patch

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang-ipath(golang.org/x/net)
BuildRequires:  golang-ipath(golang.org/x/sys)
BuildRequires:  golang-ipath(golang.org/x/text)

# These are not packaged in EPEL
%if 0%{!?epel}
BuildRequires:  golang-ipath(github.com/Azure/go-ansiterm)
BuildRequires:  golang-ipath(github.com/containerd/containerd)
BuildRequires:  golang-ipath(github.com/davecgh/go-spew)
BuildRequires:  golang-ipath(github.com/deckarep/golang-set)
BuildRequires:  golang-ipath(github.com/docker/cli)
BuildRequires:  golang-ipath(github.com/docker/distribution)
BuildRequires:  golang-ipath(github.com/docker/docker)
BuildRequires:  golang-ipath(github.com/docker/docker-credential-helpers)
BuildRequires:  golang-ipath(github.com/docker/go-connections)
BuildRequires:  golang-ipath(github.com/docker/go-units)
BuildRequires:  golang-ipath(github.com/docker/libtrust)
BuildRequires:  golang-ipath(github.com/fernet/fernet-go)
BuildRequires:  golang-ipath(github.com/gogo/protobuf)
BuildRequires:  golang-ipath(github.com/golang/protobuf)
BuildRequires:  golang-ipath(github.com/google/go-cmp)
BuildRequires:  golang-ipath(github.com/gorilla/mux)
BuildRequires:  golang-ipath(github.com/grpc-ecosystem/grpc-gateway)
BuildRequires:  golang-ipath(github.com/mitchellh/go-wordwrap)
BuildRequires:  golang-ipath(github.com/morikuni/aec)
BuildRequires:  golang-ipath(github.com/opencontainers/go-digest)
BuildRequires:  golang-ipath(github.com/opencontainers/image-spec)
BuildRequires:  golang-ipath(github.com/opencontainers/runc)
BuildRequires:  golang-ipath(github.com/pkg/errors)
BuildRequires:  golang-ipath(github.com/pmezard/go-difflib)
BuildRequires:  golang-ipath(github.com/shurcooL/httpfs)
BuildRequires:  golang-ipath(github.com/sirupsen/logrus)
BuildRequires:  golang-ipath(github.com/stretchr/testify)
BuildRequires:  golang-ipath(google.golang.org/genproto)
BuildRequires:  golang-ipath(google.golang.org/grpc)
%endif

# The following section is populated by parsing the modules.txt file
# in the vendor dir of the source code.
#
# Bundled Provides are defined as per Fedora Guidelines:
#   https://fedoraproject.org/wiki/Packaging:Guidelines#Bundling_and_Duplication_of_system_libraries
#
Provides: bundled(golang(github.com/coreos/clair)) = 2.0.1-0.20190910143208
Provides: bundled(golang(github.com/genuinetools/pkg)) = 0.0.0-20181022210355
Provides: bundled(golang(github.com/konsorten/go-windows-terminal-sequences)) = 1.0.1
Provides: bundled(golang(github.com/Microsoft/go-winio)) = 0.4.14
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = 0.8.6
Provides: bundled(golang(github.com/peterhellberg/link)) = 1.0.0

# These are not packaged in EPEL
# We will use the bundled modules
%if 0%{?epel}
Provides: bundled(golang(github.com/Azure/go-ansiterm)) = 0.0.0-20170929234023
Provides: bundled(golang(github.com/containerd/containerd)) = 1.2.9
Provides: bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
Provides: bundled(golang(github.com/deckarep/golang-set)) = 1.7.1
Provides: bundled(golang(github.com/docker/cli)) = 0.0.0-20190913211141
Provides: bundled(golang(github.com/docker/distribution)) = 2.7.1
Provides: bundled(golang(github.com/docker/docker)) = 1.4.2-0.20190916154449
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = 0.6.3
Provides: bundled(golang(github.com/docker/go-connections)) = 0.4.0
Provides: bundled(golang(github.com/docker/go-units)) = 0.4.0
Provides: bundled(golang(github.com/docker/libtrust)) = 0.0.0-20160708172513
Provides: bundled(golang(github.com/fernet/fernet-go)) = 0.0.0-20180830025343
Provides: bundled(golang(github.com/gogo/protobuf)) = 1.3.0
Provides: bundled(golang(github.com/golang/protobuf)) = 1.2.0
Provides: bundled(golang(github.com/google/go-cmp)) = 0.3.1
Provides: bundled(golang(github.com/gorilla/mux)) = 1.7.3
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway)) = 1.11.1
Provides: bundled(golang(github.com/mitchellh/go-wordwrap)) = 1.0.0
Provides: bundled(golang(github.com/morikuni/aec)) = 0.0.0-20170113033406
Provides: bundled(golang(github.com/opencontainers/go-digest)) = 1.0.0-rc1
Provides: bundled(golang(github.com/opencontainers/image-spec)) = 1.0.1
Provides: bundled(golang(github.com/opencontainers/runc)) = 0.1.1
Provides: bundled(golang(github.com/pkg/errors)) = 0.8.1
Provides: bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
Provides: bundled(golang(github.com/shurcooL/httpfs)) = 0.0.0-20190707220628
Provides: bundled(golang(github.com/sirupsen/logrus)) = 1.4.2
Provides: bundled(golang(github.com/stretchr/testify)) = 1.2.2
Provides: bundled(golang(google.golang.org/genproto)) = 0.0.0-20180817151627
Provides: bundled(golang(google.golang.org/grpc)) = 1.23.1
%endif

Obsoletes: reg-server < %{version}

%description
%{common_description}

%gopkg

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

# Do not remove 'vendor' dir entirely
%goprep -ke

# Remove bundled modules packaged in Fedora
rm -rf vendor/golang.org

%if 0%{!?epel}
rm -rf vendor/github.com/Azure
rm -rf vendor/github.com/containerd
rm -rf vendor/github.com/davecgh
rm -rf vendor/github.com/deckarep
rm -rf vendor/github.com/docker
rm -rf vendor/github.com/fernet
rm -rf vendor/github.com/gogo
rm -rf vendor/github.com/golang
rm -rf vendor/github.com/google
rm -rf vendor/github.com/gorilla
rm -rf vendor/github.com/grpc-ecosystem
rm -rf vendor/github.com/mitchellh
rm -rf vendor/github.com/morikuni
rm -rf vendor/github.com/opencontainers
rm -rf vendor/github.com/pkg
rm -rf vendor/github.com/pmezard
rm -rf vendor/github.com/shurcooL
rm -rf vendor/github.com/sirupsen
rm -rf vendor/github.com/stretchr
rm -rf vendor/google.golang.org
%endif

%build
%gobuild -o %{gobuilddir}/bin/reg %{goipath}


%install

# Install the binaries
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# Install templates and static content
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}-server
install -d server/templates/ %{buildroot}/%{_sharedstatedir}/%{name}-server/templates/
install -d server/static/ %{buildroot}%{_sharedstatedir}/%{name}-server/static/
cp -p -r server/templates/* %{buildroot}%{_sharedstatedir}/%{name}-server/templates/
cp -p -r server/static/* %{buildroot}%{_sharedstatedir}/%{name}-server/static/

# Install the systemd unit
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-server.service

# Install the sysconfig file
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0640 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-server


%post
%systemd_post %{name}-server.service

%preun
%systemd_preun %{name}-server.service

%postun
%systemd_postun %{name}-server.service


%files
%doc README.md Dockerfile Makefile
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}-server.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-server
%config(noreplace) %{_sharedstatedir}/%{name}-server/static/
%config(noreplace) %{_sharedstatedir}/%{name}-server/templates/

%gopkgfiles

%changelog
* Tue Feb 23 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.16.1-3
- Use bundled modules for EPEL8

* Sun Feb 21 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.16.1-2
- Use modules from Fedora repository where possible

* Sat Feb 20 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.16.1-1
- Update to 0.16.1
- Fix FTB in F34
- Make use of some Golang macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.15.5-6
- Fix image search

* Thu Apr 23 2020 Mattia Verga <mattia.verga@protonmail.com> - 0.15.5-5
- Fix %%postun directive

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Kevin Fenzi <kevin@scrye.com> - 0.15.5-1
- Update to 0.15.5

* Thu Jul 26 2018 Kevin Fenzi <kevin@scrye.com> - 0.15.4-1
- Update to 0.15.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-5
- Actually apply the patch for single-run execution

* Thu Jun 29 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-4
- Fix epel7 build

* Tue Jun 27 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-3
- Add patch to allow single-run execution of reg-server for static html
  generation

* Mon Jun 19 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-2
- Add ghost file entry for statically generated index.html

* Mon Jun 12 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-1
- Update to latest upstream
- Switch to using upstream versioning, they are tagging versions now.

* Tue Mar 21 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.2.0-2.git.0.94d0af5
- Move static/templates and systemd workingdir to /var/lib/reg-server
- Change Source0 to point to github archive url instead of local git-archive
- Fix tabs vs spaces in the spec file

* Tue Mar 14 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.2.0-1.git.0.94d0af5
- First package for Fedora
