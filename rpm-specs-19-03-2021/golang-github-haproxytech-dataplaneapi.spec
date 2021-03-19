%bcond_without check

%global gorepo          dataplaneapi
%global haproxy_user    haproxy
%global haproxy_group   %{haproxy_user}
%global haproxy_homedir %{_localstatedir}/lib/haproxy

%global _hardened_build 1

# https://github.com/haproxytech/dataplaneapi
%global goipath         github.com/haproxytech/dataplaneapi
Version:                2.2.0

%gometa

# %%global extractdir      %%(echo %%{extractdir} | sed -e 's/~/-/g')
# %%global gosource        %%(echo %%{gosource} | sed -e 's/~/-/g')

%global goaltipaths     %{goipath}/v2

%global common_description %{expand:
HAProxy Data Plane API.}

%global golicenses      LICENSE e2e/libs/bats-assert/LICENSE e2e/libs/bats-\\\
                        support/LICENSE
%global godocs          CONTRIBUTING.md README.md e2e/README.md\\\
                        e2e/libs/bats-assert/README.md e2e/libs/bats-\\\
                        support/CHANGELOG.md e2e/libs/bats-support/README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        HAProxy Data Plane API

Group:          System Environment/Daemons

# Upstream license specification: CC0-1.0 and Apache-2.0
License:        CC0 and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{gorepo}.service
Source2:        %{gorepo}.logrotate
Source3:        %{gorepo}.sysconfig

Patch0:         dataplaneapi-go-openapi-errors.patch

BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/dustinkirkland/golang-petname)
BuildRequires:  golang(github.com/GehirnInc/crypt)
BuildRequires:  golang(github.com/GehirnInc/crypt/md5_crypt)
BuildRequires:  golang(github.com/GehirnInc/crypt/sha256_crypt)
BuildRequires:  golang(github.com/GehirnInc/crypt/sha512_crypt)
BuildRequires:  golang(github.com/getkin/kin-openapi/openapi2)
BuildRequires:  golang(github.com/getkin/kin-openapi/openapi2conv)
BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/go-openapi/loads)
BuildRequires:  golang(github.com/go-openapi/runtime)
BuildRequires:  golang(github.com/go-openapi/runtime/flagext)
BuildRequires:  golang(github.com/go-openapi/runtime/middleware)
BuildRequires:  golang(github.com/go-openapi/runtime/security)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/go-openapi/validate)
BuildRequires:  golang(github.com/google/renameio)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/haproxytech/client-native/v2)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/configuration)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/errors)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/runtime)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/spoe)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/storage)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/common)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/types)
BuildRequires:  golang(github.com/haproxytech/models/v2)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/oklog/ulid/v2)
BuildRequires:  golang(github.com/rs/cors)
BuildRequires:  golang(github.com/shirou/gopsutil/host)
BuildRequires:  golang(github.com/shirou/gopsutil/mem)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/net/netutil)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  systemd-units
BuildRequires:  help2man
BuildRequires:  gzip

Requires:         haproxy >= 2.0
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

Suggests: logrotate

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# https://github.com/haproxytech/dataplaneapi/pull/127
%patch0 -p1
mv e2e/libs/bats-assert/LICENSE LICENSE-e2e-libs-bats-assert
mv e2e/libs/bats-support/LICENSE LICENSE-e2e-libs-bats-support
mv e2e/libs/bats-assert/README.md README-e2e-libs-bats-assert.md
mv e2e/libs/bats-support/CHANGELOG.md CHANGELOG-e2e-libs-bats-support.md
mv e2e/libs/bats-support/README.md README-e2e-libs-bats-support.md
mv e2e/README.md README-e2e.md

%build
LDFLAGS="-X main.GitRepo=%{url}/archive/v%{version}/%{gorepo}-%{version}.tar.gz "
LDFLAGS+="-X main.GitTag=v%{version} -X main.GitCommit= -X main.GitDirty= "
LDFLAGS+="-X main.BuildTime=%(date '+%%Y-%%m-%%dT%%H:%%M:%%S') "
%gobuild -o %{gobuilddir}/sbin/%{gorepo} %{goipath}/cmd/%{gorepo}/
mkdir -p %{gobuilddir}/share/man/man8
help2man -n "%{summary}" -s 8 -o %{gobuilddir}/share/man/man8/%{gorepo}.8 -N --version-string="%{version}" %{gobuilddir}/sbin/%{gorepo}
gzip %{gobuilddir}/share/man/man8/%{gorepo}.8

%install
%gopkginstall
install -m 0755 -vd                      %{buildroot}%{_sbindir}
install -m 0755 -vp %{gobuilddir}/sbin/* %{buildroot}%{_sbindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man8
install -m 0644 -vp %{gobuilddir}/share/man/man8/* %{buildroot}%{_mandir}/man8/

install -d -m 0755 %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{gorepo}.service
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{goname}
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{gorepo}

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_post %{gorepo}.service

%preun
%systemd_preun %{gorepo}.service

%postun
%systemd_postun_with_restart %{gorepo}.service

%files
%license LICENSE LICENSE-e2e-libs-bats-assert LICENSE-e2e-libs-bats-support
%doc CONTRIBUTING.md README.md README-e2e.md README-e2e-libs-bats-assert.md
%doc CHANGELOG-e2e-libs-bats-support.md README-e2e-libs-bats-support.md
%{_mandir}/man8/%{gorepo}.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{goname}
%config(noreplace) %{_sysconfdir}/sysconfig/%{gorepo}
%{_unitdir}/%{gorepo}.service
%{_sbindir}/*

%gopkgfiles

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 16:09:32 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.0-1
- Update to 2.2.0
- Close: rhbz#1916914

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-2
- Modify gosource so that Source0 resolves correctly  (Fixes rhbz#1914254)

* Tue Jan 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-1
- Update to version 2.2.0-rc1 (Fixes rhbz#1914254)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 2.1.0-4
- Patch for changes in go-openapi/errors v0.19.6
  https://github.com/haproxytech/dataplaneapi/pull/127

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Brandon Perkins <bperkins@redhat.com> - 2.1.0-1
- Update to version 2.1.0 (Fixes rhbz#1859325)
- Add golang(github.com/getkin/kin-openapi/openapi2),
  golang(github.com/getkin/kin-openapi/openapi2conv), and
  golang(github.com/google/renameio) BuildRequires

* Mon Jun 01 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.3-1
- Update to version 2.0.3

* Mon May 18 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.2-1
- Update to version 2.0.2

* Fri May 08 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.1-1
- Update to version 2.0.1

* Tue Apr 28 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-2
- Add LDFLAGS for GitRepo, GitTag, GitCommit, GitDirty, and
  BuildTime variables
- Simplify gobuild action to only build dataplaneapi

* Mon Apr 27 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-1
- Upgrade to version 2.0.0

* Wed Apr 15 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.5-1
- Update to version 1.2.5

* Tue Apr 14 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.4-7
- Change haproxy requires to >= 2.0 as 1.9 was never packaged
- Add specific versions for haproxytech BuildRequires

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.4-6
- Use global instead of define macro
- Remove defattr macro that is not needed

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.4-5
- Clean changelog

* Thu Nov 21 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-4
- Suggest logrotate and fix logrotate configuration

* Wed Nov 20 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-3
- Add man page

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-2
- Implement systemd

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-1
- Initial package

