Name:           netbox
Version:        2.11.0
Release:        2%{?dist}
Summary:        IP address management (IPAM) and data center infrastructure management (DCIM)

License:        ASL 2.0 and MIT and OFL
URL:            https://github.com/netbox-community/netbox/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        netbox.service
Source2:        netbox-rq.service
Source3:        https://github.com/netbox-community/netbox-docker/raw/release/docker/configuration.docker.py
Source4:        https://github.com/netbox-community/netbox-docker/raw/release/docker/ldap_config.docker.py
Source5:        ldap_config.example.py
# Non-upstreamable
Patch0001:      0001-Use-var-lib-netbox-for-the-static-and-media-files.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
Requires:       /usr/bin/gunicorn
Requires(pre):  shadow-utils
# base_requirements.txt
Requires:       python%{python3_version}dist(django)
Requires:       python%{python3_version}dist(django-cacheops)
Requires:       python%{python3_version}dist(django-cors-headers)
Requires:       python%{python3_version}dist(django-debug-toolbar)
Requires:       python%{python3_version}dist(django-filter)
Requires:       python%{python3_version}dist(django-mptt)
Requires:       python%{python3_version}dist(django-pglocks)
Requires:       python%{python3_version}dist(django-prometheus)
Requires:       python%{python3_version}dist(django-rq)
Requires:       python%{python3_version}dist(django-tables2)
Requires:       python%{python3_version}dist(django-taggit)
Requires:       python%{python3_version}dist(django-timezone-field)
Requires:       python%{python3_version}dist(djangorestframework)
Requires:       python%{python3_version}dist(drf-yasg[validation])
Requires:       python%{python3_version}dist(gunicorn)
Requires:       python%{python3_version}dist(jinja2)
Requires:       python%{python3_version}dist(markdown)
Requires:       python%{python3_version}dist(netaddr)
Requires:       python%{python3_version}dist(pillow)
# originally: psycopg2
Requires:       python%{python3_version}dist(psycopg2)
# originally: pycryptodome
Requires:       python%{python3_version}dist(pycryptodomex)
Requires:       python%{python3_version}dist(pyyaml)
Requires:       python%{python3_version}dist(redis)
Requires:       python%{python3_version}dist(svgwrite)
Requires:       python%{python3_version}dist(tablib)
Recommends:     python%{python3_version}dist(django-storages)
Suggests:       python%{python3_version}dist(django-auth-ldap)
# netbox/project-static/bootstrap-*-dist/
# License(s): MIT
Provides:       bundled(js-bootstrap) = 3.4.1
# netbox/project-static/clipboard.js/
# License(s): MIT
Provides:       bundled(js-clipboard) = 2.0.6
# netbox/project-static/flatpickr-*/
# License(s): MIT
Provides:       bundled(js-flatpickr) = 4.6.3
# netbox/project-static/materialdesignicons-*/
# License(s): ASL 2.0 and MIT
Provides:       bundled(materialdesign-webfont) = 5.8.55
# netbox/project-static/jquery/
# License(s): MIT
Provides:       bundled(js-jquery) = 3.5.1
# netbox/project-static/jquery-ui-*/
# License(s): MIT
Provides:       bundled(js-jquery-ui) = 1.12.1
# netbox/project-static/select2-*/
# License(s): MIT
Provides:       bundled(js-select2) = 4.0.13
# netbox/project-static/select2-bootstrap-*/
# License(s): MIT
Provides:       bundled(js-select2-bootstrap-theme) = 0.1.0~beta10

%description
NetBox is an IP address management (IPAM)
and data center infrastructure management (DCIM) tool.
Initially conceived by the network engineering team at DigitalOcean,
NetBox was developed specifically to address the needs of network
and infrastructure engineers. It is intended to function
as a domain-specific source of truth for network operations.

%prep
%autosetup -p1
find -type f -name '*.py' \
  -exec sed -i -e 's/from Crypto\./from Cryptodome./' '{}' + \
  -exec pathfix.py -pni '%python3 %{py3_shbang_opts}' '{}' + \
  %{nil}
cat << EOF >> contrib/gunicorn.py

# Configure Gunicorn to cope with prometheus client
# (https://github.com/prometheus/client_python#multiprocess-mode-gunicorn)
from prometheus_client import multiprocess

def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)
EOF

%install
install -Dpm0644 -t %{buildroot}%{_unitdir} %{S:1}
install -Dpm0644 -t %{buildroot}%{_unitdir} %{S:2}
mkdir -p %{buildroot}%{_sysconfdir}/netbox/{config,reports,scripts}
mkdir -p %{buildroot}%{_sysconfdir}/netbox/config/ldap
install -Dpm0640 netbox/netbox/configuration.example.py %{buildroot}%{_sysconfdir}/netbox/config/configuration.py
install -Dpm0640 %{S:5} %{buildroot}%{_sysconfdir}/netbox/config/ldap/ldap_config.py
install -Dpm0644 contrib/gunicorn.py %{buildroot}%{_sysconfdir}/netbox/gunicorn_config.py

mkdir -p %{buildroot}{%{_datadir},%{_sysconfdir}/netbox}
cp -a netbox %{buildroot}%{_datadir}
install -Dpm0644 %{S:3} %{buildroot}%{_datadir}/netbox/netbox/configuration.py
install -Dpm0644 %{S:4} %{buildroot}%{_datadir}/netbox/netbox/ldap_config.py
rm -v %{buildroot}%{_datadir}/netbox/netbox/configuration.*.py
mkdir -p %{buildroot}%{_sharedstatedir}/netbox/static
rm -v %{buildroot}%{_datadir}/netbox/media/*/.gitignore
cp -a %{buildroot}%{_datadir}/netbox/media %{buildroot}%{_sharedstatedir}/netbox/
rm -r %{buildroot}%{_datadir}/netbox/media

%py_byte_compile %python3 %{buildroot}%{_datadir}/netbox

%pre
getent group netbox >/dev/null || groupadd -r netbox
getent passwd netbox >/dev/null || \
    useradd -r -g netbox -d %{_datadir}/netbox -s /bin/bash \
    -c "NetBox user" netbox
exit 0

%post
%systemd_post netbox.service netbox-rq.service

%preun
%systemd_preun netbox.service netbox-rq.service

%postun
%systemd_postun_with_restart netbox.service netbox-rq.service

%files
%license LICENSE.txt NOTICE
%doc README.md CHANGELOG.md
%{_datadir}/netbox/
%{_unitdir}/netbox.service
%{_unitdir}/netbox-rq.service
%defattr(-,netbox,netbox)
%dir %{_sysconfdir}/netbox/
%dir %{_sysconfdir}/netbox/{config,reports,scripts}/
%config(noreplace) %{_sysconfdir}/netbox/config/configuration.py
%dir %{_sysconfdir}/netbox/config/ldap/
%config(noreplace) %{_sysconfdir}/netbox/config/ldap/ldap_config.py
%config(noreplace) %{_sysconfdir}/netbox/gunicorn_config.py
%{_sharedstatedir}/netbox/

%changelog
* Sat Apr 17 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.11.0-2
- Explicitly require python3-tablib

* Sat Apr 17 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0

* Fri Mar 26 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.8-1
- Update to 2.10.8

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.10.5-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 24 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.5-1
- Update to 2.10.5

* Tue Jan 26 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.4-1
- Update to 2.10.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.3-1
- Update to 2.10.3

* Thu Dec 24 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.2-2
- Add missing scriptlets

* Mon Dec 21 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.2-1
- Update to 2.10.2

* Wed Dec 16 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1

* Tue Dec 15 2020 Igor Raits <ignatenkobrain@fedoraprojec.torg> - 2.10.0-2
- Fixup bundled provides

* Tue Dec 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.10.0-1
- Update to 2.10.0

* Sun Dec 13 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.11-3
- Do not use DynamicUser for the netbox unit

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.11-2
- Make metrics to work out of the box (but not enable them by default)

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.11-1
- Update to 2.9.11

* Fri Dec 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.10-4
- Use /var/lib/netbox/media for the uploaded images

* Fri Dec 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.10-3
- Add support for the LDAP authentication

* Sun Dec 06 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.10-2
- Move gunicorn_config.py to the proper location to avoid loading it as a netbox configuration

* Sun Dec 06 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.10-1
- Update to 2.9.10

* Mon Sep 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.3-1
- Update to 2.9.3

* Tue Sep 01 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.2-2
- Make package a noarch

* Sun Aug 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.9.2-1
- Update to 2.9.2

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.7.3-1
- Initial package
