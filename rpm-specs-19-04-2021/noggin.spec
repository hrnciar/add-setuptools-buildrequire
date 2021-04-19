%global commit 3b487ed4bb90d32b82a992b5422b9807c02bf7be
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20210323

Name:           noggin
Version:        0.0.1%{?snapdate:^git%{snapdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Self-service user portal for FreeIPA for communities

License:        MIT
URL:            https://noggin-aaa.readthedocs.io/
Source0:        https://github.com/fedora-infra/noggin/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        noggin.service
Source2:        noggin.sysconfig

# Fedora-specific patches
## Fix dependencies to be satisfied by Fedora packages
Patch1001:      noggin-pyproject-Fix-runtime-dependencies-for-Fedora-33.patch
Patch1002:      noggin-pyproject-Remove-extras-marker-for-WTForms-dep.patch
## Prevent causing broken install
Patch1003:      0001-Revert-Include-additional-files-in-the-sdist.patch

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros >= 0-14
BuildRequires:  systemd-rpm-macros
BuildRequires:  /usr/bin/pathfix.py
Requires:       (python3dist(gunicorn) with /usr/bin/gunicorn-3)

%description
Noggin is a self-service portal for FreeIPA.

The primary purpose of the portal is to allow users to sign up
and manage their account information and group membership.

%package tests
Summary:        Unit tests for Noggin
Requires:       %{name} = %{version}-%{release}

%description tests
Provides unit tests files and data for Noggin.

%package theme-fas
Summary:        Fedora Account System theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-fas
Provides a theme for Noggin used for the Fedora Account System.

%package theme-centos
Summary:        CentOS Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-centos
Provides a theme for Noggin used for CentOS Accounts.

%package theme-openSUSE
Summary:        openSUSE Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-openSUSE
Provides a theme for Noggin used for openSUSE Accounts.


%prep
%autosetup -n %{name}-%{commit} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files noggin

mkdir -p %{buildroot}%{_bindir}
install -pm 0755 deployment/scripts/sar.py %{buildroot}%{_bindir}/noggin-sar
# Fix shebangs for noggin-sar
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/noggin-sar

mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_localstatedir}/log/noggin
install -pm 0644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service
install -pm 0644 %{S:2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg
touch %{buildroot}%{_localstatedir}/log/noggin/access.log
touch %{buildroot}%{_localstatedir}/log/noggin/error.log

%files -f %{pyproject_files}
%license LICENSE
%doc README.md noggin.cfg.example
%{_bindir}/noggin-sar
%{_unitdir}/%{name}.service
%ghost %{_sysconfdir}/%{name}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_localstatedir}/log/noggin
%ghost %{_localstatedir}/log/noggin/*.log
%exclude %{python3_sitelib}/%{name}/tests
%exclude %{python3_sitelib}/%{name}/themes/fas
%exclude %{python3_sitelib}/%{name}/themes/centos
%exclude %{python3_sitelib}/%{name}/themes/openSUSE


%files tests
%{python3_sitelib}/%{name}/tests


%files theme-fas
%{python3_sitelib}/%{name}/themes/fas


%files theme-centos
%{python3_sitelib}/%{name}/themes/centos


%files theme-openSUSE
%{python3_sitelib}/%{name}/themes/openSUSE


%changelog
* Tue Mar 23 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1^git20210323.3b487ed-1
- Bump to new git snapshot

* Sun Mar 21 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20210319.511d606-1.1
- Bump to new git snapshot
- Refresh patches

* Fri Oct 30 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20201028.542001b-0.1
- Bump to new git snapshot

* Sat Oct 24 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20200923.6ed6757-0.2
- Add CentOS theme subpackage

* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20200923.6ed6757-0.1
- Bump to new git snapshot

* Sun Jul 26 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20200722.fcba2d8-0.1
- Bump to new post-release git snapshot

* Sun Apr 19 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1-0.1
- Initial packaging
