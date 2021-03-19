# Generated by go2rpm 1
%bcond_without check
%global build_timestamp %(date +"%Y%m%d")

# https://github.com/Dreamacro/clash
%global goipath         github.com/Dreamacro/clash
Version:                1.2.0

%gometa

%global common_description %{expand:
A rule-based tunnel in Go.}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           clash
Release:        3%{?dist}
Summary:        A rule-based tunnel in Go

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}
Source1:        clash.service
Source2:        clash@.service

BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(github.com/Dreamacro/go-shadowsocks2/core)
BuildRequires:  golang(github.com/Dreamacro/go-shadowsocks2/shadowaead)
BuildRequires:  golang(github.com/go-chi/chi)
BuildRequires:  golang(github.com/go-chi/cors)
BuildRequires:  golang(github.com/go-chi/render)
BuildRequires:  golang(github.com/gofrs/uuid)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/oschwald/geoip2-golang)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/crypto/argon2)
BuildRequires:  golang(golang.org/x/crypto/chacha20poly1305)
BuildRequires:  golang(golang.org/x/net/publicsuffix)
BuildRequires:  golang(golang.org/x/sync/singleflight)
BuildRequires:  golang(gopkg.in/eapache/channels.v1)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
chmod -x docs/logo.png

%build
export LDFLAGS="-X github.com/Dreamacro/clash/constant.Version=%{version} \
                -X github.com/Dreamacro/clash/constant.BuildTime=%{build_timestamp} \
                $LDFLAGS"
%gobuild -o %{gobuilddir}/bin/clash %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vd                     %{buildroot}%{_userunitdir}
install -m 0755 -vd                     %{buildroot}%{_unitdir}

install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vp %{S:1}              %{buildroot}%{_userunitdir}/
install -m 0755 -vp %{S:2}              %{buildroot}%{_unitdir}/

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_user_post clash.service
%systemd_post clash@.service

%preun
%systemd_user_preun clash.service
# disable --now seems don't work here.
if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ] ; then
        # Package removal, not upgrade
        /usr/bin/systemctl --no-reload stop clash@*.service || :
        /usr/bin/systemctl --no-reload disable clash@.service || :
fi

%postun
%systemd_user_postun_with_restart clash.service
%systemd_postun_with_restart clash@*.service

%files
%license LICENSE
%doc docs README.md
%{_bindir}/clash
%{_userunitdir}/clash.service
%{_unitdir}/clash@.service
%gopkgfiles

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.2.0-1
- update to 1.2.0 upstream release

* Tue Aug 18 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.1.0-1
- update to 1.1.0 upstream release

* Sat Aug 01 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.0-4
- Change systemd scriptlets

* Mon Jul 27 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.0-3
- don't use go mod

* Mon Jul 27 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.0-2
- Add unit files, taken from 
- https://github.com/archlinux/svntogit-community/tree/packages/clash/trunk

