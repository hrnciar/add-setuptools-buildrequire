Name:           rmd
Version:        0.2.1
Release:        4%{?dist}
Summary:        Resource Management Daemon-RMD
License:        ASL 2.0
URL:            https://github.com/intel/rmd
Source0:        https://github.com/arunprabhu123/rmd/blob/master/rmd-0.2.1.tar.gz

#Extra packages can be generated by running script in the RMD source
#./packaging/download_extra_packages.sh <Temp_Download_Dir> <Destination_Dir>
Source1:        rmd-extra.pkg.tar.gz

BuildRequires:  go
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  golang-github-knetic-govaluate-devel
BuildRequires:  golang-github-bgentry-speakeasy-devel
BuildRequires:  golang-github-casbin-devel
BuildRequires:  golang-github-fatih-structs-devel
BuildRequires:  golang-github-globalsign-mgo-devel
BuildRequires:  golang-github-gobwas-glob-devel
BuildRequires:  golang-github-glog-devel
BuildRequires:  golang-github-protobuf
BuildRequires:  golang-github-gopherjs-devel
BuildRequires:  golang-github-hashicorp-hcl-devel
BuildRequires:  golang-github-jtolds-gls-devel
BuildRequires:  golang-github-klauspost-compress-devel
BuildRequires:  golang-github-klauspost-cpuid-devel
BuildRequires:  golang-github-kr-pretty-devel
BuildRequires:  golang-github-magiconair-properties-devel
BuildRequires:  golang-github-mitchellh-mapstructure-devel
BuildRequires:  golang-github-msteinert-pam-devel
BuildRequires:  golang-github-onsi-ginkgo-devel
BuildRequires:  golang-github-onsi-gomega-devel
BuildRequires:  golang-github-sirupsen-logrus-devel
BuildRequires:  golang-github-spf13-afero-devel
BuildRequires:  golang-github-spf13-cast-devel
BuildRequires:  golang-github-spf13-jwalterweatherman-devel
BuildRequires:  golang-github-spf13-pflag-devel
BuildRequires:  golang-github-spf13-viper-devel
BuildRequires:  golang-github-streadway-amqp-devel
BuildRequires:  golang-github-stretchr-testify-devel
BuildRequires:  golang-github-valyala-bytebufferpool-devel
BuildRequires:  golang-github-xeipuuv-gojsonschema-devel
BuildRequires:  golang-github-yudai-gojsondiff-devel
BuildRequires:  golang-github-yudai-golcs-devel
BuildRequires:  golang-etcd-bbolt-devel
BuildRequires:  golang-x-sync-devel
BuildRequires:  golang-x-sys-devel
BuildRequires:  golang-gopkg-yaml-2-devel

# this package does not support big endian arch so far,
# and has been verified only on Intel platforms.
# HW support is documented in https://github.com/intel/rmd/blob/master/docs/Prerequisite.md 
ExclusiveArch: %{ix86} x86_64

%description
RMD is a system daemon providing a central interface for 
hardware resource management tasks on x86 platforms.

%prep
%setup -q
mkdir _pkg
tar -C _pkg -x -v -f %{SOURCE1}
find _pkg -type d -exec chmod 755 {} \;
export GOPATH=$PWD/_pkg/packages:/usr/lib/golang

%build
GOPATH_BACKUP=$GOPATH
unset GOPATH
go env -w GOPATH=$PWD/_pkg/packages
make %{?_smp_mflags}
unset GOPATH
go env -w GOPATH=$GOPATH_BACKUP

%install

mkdir -p %{buildroot}/%{_bindir}/
GOOS=${GOOS:-$(go env GOOS)}
GOARCH=${GOARCH:-$(go env GOARCH)}
if [[ "${GOARCH}" == "amd64" ]]; then
    GOARCH="x86_64"
fi

install -p -m 755 %{_builddir}/%{name}-%{version}/build/$GOOS/$GOARCH/rmd %{buildroot}/%{_bindir}/
install -p -m 755 %{_builddir}/%{name}-%{version}/build/$GOOS/$GOARCH/gen_conf %{buildroot}/%{_bindir}/

install -d %{buildroot}/%{_mandir}/man8
install -m 0644  %{_builddir}/%{name}-%{version}/rmd.8 %{buildroot}/%{_mandir}/man8
ln -sf %{_mandir}/man8/rmd.8 %{buildroot}/%{_mandir}/man8/gen_conf.8

mkdir -p %{buildroot}/%{_datadir}/%{name}/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/setup_rmd_users.sh %{buildroot}/%{_datadir}/%{name}/scripts

mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{_builddir}/%{name}-%{version}/scripts/%{name}.service %{buildroot}/%{_unitdir}

mkdir -p %{buildroot}/%{_sysconfdir}/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cpu_map.toml %{buildroot}/%{_sysconfdir}/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/policy.toml %{buildroot}/%{_sysconfdir}/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/policy.yaml %{buildroot}/%{_sysconfdir}/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/rmd.toml %{buildroot}/%{_sysconfdir}/rmd

mkdir -p %{buildroot}/%{_sysconfdir}/rmd/acl/roles/admin
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/roles/admin/cert.pem %{buildroot}/%{_sysconfdir}/rmd/acl/roles/admin

mkdir -p %{buildroot}/%{_sysconfdir}/rmd/acl/roles/user
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/roles/user/user-cert.pem %{buildroot}/%{_sysconfdir}/rmd/acl/roles/user

mkdir -p %{buildroot}/%{_sysconfdir}/rmd/acl/url
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/url/model.conf %{buildroot}/%{_sysconfdir}/rmd/acl/url
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/url/policy.csv %{buildroot}/%{_sysconfdir}/rmd/acl/url

mkdir -p %{buildroot}/%{_sysconfdir}/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/ca.pem %{buildroot}/%{_sysconfdir}/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/cert.pem %{buildroot}/%{_sysconfdir}/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/key.pem %{buildroot}/%{_sysconfdir}/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/user-cert.pem %{buildroot}/%{_sysconfdir}/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/user-key.pem %{buildroot}/%{_sysconfdir}/rmd/cert/client

mkdir -p %{buildroot}/%{_sysconfdir}/rmd/cert/server
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/server/ca.pem %{buildroot}/%{_sysconfdir}/rmd/cert/server
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/server/rmd-cert.pem %{buildroot}/%{_sysconfdir}/rmd/cert/server
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/server/rmd-key.pem %{buildroot}/%{_sysconfdir}/rmd/cert/server

mkdir -p %{buildroot}/%{_sysconfdir}/rmd/pam
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/pam/rmd %{buildroot}/%{_sysconfdir}/rmd/pam

mkdir -p %{buildroot}/%{_sysconfdir}/rmd/pam/test
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/pam/test/rmd %{buildroot}/%{_sysconfdir}/rmd/pam/test

mkdir -p %{buildroot}/%{_docdir}/%{name}
install -m 0644  %{_builddir}/%{name}-%{version}/docs/UserGuide.md %{buildroot}/%{_docdir}/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/docs/Prerequisite.md %{buildroot}/%{_docdir}/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/docs/ConfigurationGuide.md %{buildroot}/%{_docdir}/rmd

%files
%{_bindir}/%{name}
%{_bindir}/gen_conf
%{_mandir}/man8/rmd.8.*
%{_mandir}/man8/gen_conf.8.*
%config(noreplace)  %{_sysconfdir}/rmd/cert/*
%config(noreplace)  %{_sysconfdir}/rmd/acl/*
%config(noreplace)  %{_sysconfdir}/rmd/*.toml
%config(noreplace)  %{_sysconfdir}/rmd/*.yaml
%config(noreplace)  %{_sysconfdir}/rmd/pam/test/rmd
%config(noreplace)  %{_sysconfdir}/rmd/pam/rmd
%{_datadir}/%{name}/
%doc README.md
%doc %{_docdir}/%{name}
%license LICENSE
%{_unitdir}/%{name}.service


%post

%systemd_post %{name}.service

USER="rmd"
useradd $USER || echo "User rmd already exists."

LOGFILE="/var/log/rmd/rmd.log"
if [ ! -d ${LOGFILE%/*} ]; then
    mkdir -p ${LOGFILE%/*}
    chown $USER:$USER ${LOGFILE%/*}
fi

DBFILE="/var/run/rmd/rmd.db"
if [ ! -d ${DBFILE%/*} ]; then
    mkdir -p ${DBFILE%/*}
    chown $USER:$USER  ${DBFILE%/*}
fi

PAMSRCFILE="/etc/rmd/pam/rmd"
PAMDIR="/etc/pam.d"
if [ -d $PAMDIR ]; then
    cp $PAMSRCFILE $PAMDIR
fi

DATA="\"logfile\":\"$LOGFILE\", \"dbtransport\":\"$DBFILE\", \"logtostdout\":false"
gen_conf -path /etc/rmd/rmd.toml -data "{$DATA}"

%preun 
%systemd_preun %{name}.service
USER="rmd"
rm -rf /var/log/rmd/
rm -rf /var/run/rmd/
rm -rf /etc/pam.d/rmd

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 ArunPrabhu Vijayan <arunprabhu.vijayan@intel.com> - 0.2.1-1
- RMD package version 0.2.1
