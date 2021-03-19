%global plugin_name fas
%global ipa_version 4.8.2

%if 0%{?rhel}
%global freeipa_prefix ipa
%global freeipa_altprefix freeipa
%else
%global freeipa_prefix freeipa
%global freeipa_altprefix ipa
%endif

Name:           freeipa-%{plugin_name}
Version:        0.0.4
Release:        2%{?dist}
Summary:        Fedora Account System extension for FreeIPA

License:        GPLv3+
URL:            https://github.com/fedora-infra/freeipa-%{plugin_name}
Source0:        %{url}/archive/v%{version}/freeipa-%{plugin_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

%if ! 0%{?rhel}
Provides:        %{freeipa_altprefix}-%{plugin_name} = %{version}-%{release}
Requires:        freeipa-server >= %{ipa_version}
Requires(post):  freeipa-server >= %{ipa_version}
%endif

%description
A module for FreeIPA with extensions for Fedora Account System.

%if 0%{?rhel}
%package -n ipa-%{plugin_name}
Summary:        Fedora Account System extension for IdM

Provides:        %{freeipa_altprefix}-%{plugin_name} = %{version}-%{release}
Requires:        ipa-server >= %{ipa_version}
Requires(post):  ipa-server >= %{ipa_version}

%description -n ipa-%{plugin_name}
A module for IdM with extensions for Fedora Account System.
%endif

%prep
%autosetup -n freeipa-%{plugin_name}-%{version}

%build
# Nothing to build

%install

mkdir -p %{buildroot}%{python3_sitelib}/ipaserver/plugins
for j in $(find ipaserver/plugins -name '*.py') ; do
    cp -a $j %{buildroot}%{python3_sitelib}/ipaserver/plugins
done

mkdir -p %{buildroot}/%{_datadir}/ipa/schema.d
for j in $(find schema.d/ -name '*.ldif') ; do
    cp -a $j %{buildroot}/%{_datadir}/ipa/schema.d/
done

mkdir -p %{buildroot}/%{_datadir}/ipa/updates
for j in $(find updates/ -name '*.update') ; do
    cp -a $j %{buildroot}/%{_datadir}/ipa/updates/
done

mkdir -p %{buildroot}/%{_datadir}/ipa/ui/js/plugins
for j in $(find ui/ -name '*.js') ; do
    destdir=%{buildroot}/%{_datadir}/ipa/ui/js/plugins/$(basename ${j%%.js})
    mkdir -p $destdir
    cp -a $j $destdir/
done

%posttrans -n %{freeipa_prefix}-%{plugin_name}
%python3 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    # This must be run in posttrans so that updates from previous
    # execution that may no longer be shipped are not applied.
    /usr/sbin/ipa-server-upgrade --quiet >/dev/null || :

    # Restart IPA processes. This must be also run in postrans so that plugins
    # and software is in consistent state
    # NOTE: systemd specific section
    /bin/systemctl try-restart ipa.service >/dev/null 2>&1 || :
fi

%files -n %{freeipa_prefix}-%{plugin_name}
%license COPYING
%doc README.md CONTRIBUTORS.txt
%{python3_sitelib}/ipaserver/plugins/*.py
%{python3_sitelib}/ipaserver/plugins/__pycache__/*.pyc
%{_datadir}/ipa/schema.d/*.ldif
%{_datadir}/ipa/updates/*.update
%{_datadir}/ipa/ui/js/plugins/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.4-1
- Update to 0.0.4

* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.2-1.git20200921.04a0d2b
- Update to new git snapshot

* Sun Jul 26 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.2-1.git20200610.b82302d
- Update to new git snapshot

* Mon Apr 20 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.2-1.git20200422.2b4470e
- Small cleanups and consistency fixes of the packaging

* Wed Feb 12 2020 Christian Heimes <cheimes@redhat.com> - 0.0.2-1
- Make new fields readable
- Make mail attribute writeable

* Tue Nov 19 2019 Christian Heimes <cheimes@redhat.com> - 0.0.1-1
- Initial release
