#
# If we should enable docs building
# Currently we cannot until we get a stack of needed packages added and a few bugs fixed
#
%bcond_with docs

#
# If we should enable tests by default
#
%bcond_with tests

# Set this when there's a beta version
%global betaver b4

Name: ansible-core
Summary: A radically simple IT automation system
Version: 2.11.0
Release: 0.1.%{betaver}%{?dist}

License: GPLv3+
Source0: %pypi_source ansible-core 2.11.0b4

Source1: ansible.attr
Source2: ansible-generator
Source3: macros.ansible
Url: http://ansible.com
BuildArch: noarch

#Provides: ansible = %%{version}-%%{release}
#Obsoletes: ansible <= 2.9.99
# For now conflict with the ansible 'classic' package.
Conflicts: ansible <= 2.9.99
#
# obsoletes/provides for ansible-base
#
Provides: ansible-base = 2.10.7
Obsoletes: ansible-base < 2.10.6-1%{?dist}

# A 2.10.3 async test uses /usr/bin/python, which we do not have by default. 
# Patch the test to use /usr/bin/python3 as we have for our build.
Patch1:  2.10.3-test-patch.patch

%if %{with tests}
#
# For tests
#
# These two exist on both fedora and rhel8
#
BuildRequires: make
BuildRequires: git-core
BuildRequires: python3-packaging
BuildRequires: python3-pexpect
BuildRequires: openssl
BuildRequires: python3-systemd
#
# These only exist on Fedora. RHEL8 will just skip tests that need them.
#
%if 0%{?fedora}
BuildRequires: python3-paramiko
BuildRequires: python3-winrm

BuildRequires: python3-crypto
BuildRequires: python3-pbkdf2
BuildRequires: python3-httmock
BuildRequires: python3-gitlab
BuildRequires: python3-boto3
BuildRequires: python3-botocore
BuildRequires: python3-coverage
BuildRequires: python3-passlib
%endif
%endif
%if %{with docs}
BuildRequires: make
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-theme-alabaster
BuildRequires: python3-sphinx-notfound-page
BuildRequires: asciidoc
BuildRequires: python3-straight-plugin
BuildRequires: python3-rstcheck
BuildRequires: python3-pygments
BuildRequires: antsibull
%endif

#
# main buildrequires to build
#
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-nose
BuildRequires: %{py3_dist pytest}
BuildRequires: python3-pytest-xdist
BuildRequires: python3-pytest-mock
BuildRequires: python3-requests
BuildRequires: python3-mock
BuildRequires: python3-jinja2
BuildRequires: python3-pyyaml
BuildRequires: python3-cryptography
BuildRequires: python3-pyvmomi

# RHEL8 doesn't have python3-paramiko or python3-winrm (yet), but Fedora does
Recommends: python3-paramiko
Recommends: python3-winrm

# needed for json_query filter
Requires: python3-jmespath

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This is the base part of ansible (the engine).

%package -n ansible-base-doc
Summary: Documentation for Ansible Base

%description -n ansible-base-doc

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package installs extensive documentation for ansible-base

%prep
%autosetup -p1 -n %{name}-%{version}%{betaver}
cp -a %{S:1} %{S:2} %{S:3} .

%build

# Fix some files shebangs
sed -i -e 's|/usr/bin/env python|/usr/bin/python3|' test/lib/ansible_test/_data/*.py test/lib/ansible_test/_data/*/*.py test/lib/ansible_test/_data/*/*/*.py docs/bin/find-plugin-refs.py

# These we have to supress or the package will depend on /usr/bin/pwsh and not be installable.
sed -i -s 's|/usr/bin/env pwsh||' test/lib/ansible_test/_data/sanity/validate-modules/validate_modules/ps_argspec.ps1
sed -i -s 's|/usr/bin/env pwsh||' test/lib/ansible_test/_data/sanity/pslint/pslint.ps1
sed -i -s 's|/usr/bin/env pwsh||' test/lib/ansible_test/_data/requirements/sanity.ps1

# disable the python -s shbang flag as we want to be able to find non system modules
%global py3_shbang_opts %(echo %{py3_shbang_opts} | sed 's/-s//')
%py3_build

%if %{with docs}
  make PYTHON=/usr/bin/python3 SPHINXBUILD=sphinx-build-3 webdocs
%else
  # we still need things to build these minimal docs too.
  # make PYTHON=/usr/bin/python3 -Cdocs/docsite config cli keywords modules plugins testing
%endif

%install
%py3_install

# Create system directories that Ansible defines as default locations in
# ansible/config/base.yml
DATADIR_LOCATIONS='%{_datadir}/ansible/collections
%{_datadir}/ansible/collections/ansible_collections
%{_datadir}/ansible/plugins/doc_fragments
%{_datadir}/ansible/plugins/action
%{_datadir}/ansible/plugins/become
%{_datadir}/ansible/plugins/cache
%{_datadir}/ansible/plugins/callback
%{_datadir}/ansible/plugins/cliconf
%{_datadir}/ansible/plugins/connection
%{_datadir}/ansible/plugins/filter
%{_datadir}/ansible/plugins/httpapi
%{_datadir}/ansible/plugins/inventory
%{_datadir}/ansible/plugins/lookup
%{_datadir}/ansible/plugins/modules
%{_datadir}/ansible/plugins/module_utils
%{_datadir}/ansible/plugins/netconf
%{_datadir}/ansible/roles
%{_datadir}/ansible/plugins/strategy
%{_datadir}/ansible/plugins/terminal
%{_datadir}/ansible/plugins/test
%{_datadir}/ansible/plugins/vars'

UPSTREAM_DATADIR_LOCATIONS=$(grep -ri default lib/ansible/config/base.yml| tr ':' '\n' | grep '/usr/share/ansible')

if [ "$SYSTEM_LOCATIONS" != "$UPSTREAM_SYSTEM_LOCATIONS" ] ; then
  echo "The upstream Ansible datadir locations have changed.  Spec file needs to be updated"
  exit 1
fi

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/plugins/
for location in $DATADIR_LOCATIONS ; do
	mkdir $RPM_BUILD_ROOT"$location"
done
mkdir -p $RPM_BUILD_ROOT/etc/ansible/
mkdir -p $RPM_BUILD_ROOT/etc/ansible/roles/

cp examples/hosts $RPM_BUILD_ROOT/etc/ansible/
cp examples/ansible.cfg $RPM_BUILD_ROOT/etc/ansible/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp -v docs/man/man1/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

install -Dpm0644 -t %{buildroot}%{_fileattrsdir} ansible.attr
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} macros.ansible
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} ansible-generator

# no need to ship zero length files
find %{buildroot}/%{python3_sitelib} -name .git_keep -exec rm -f {} \;
find %{buildroot}/%{python3_sitelib} -name .travis.yml -exec rm -f {} \;

%check
%if %{with tests}
ln -s /usr/bin/pytest-3 bin/pytest
pathfix.py -i %{__python3} -p test/lib/ansible_test/_data/cli/ansible_test_cli_stub.py
# This test needs a module not packaged in Fedora so disable it.
#rm -f test/units/modules/cloud/cloudstack/test_cs_traffic_type.py
# These tests are failing with pytest 6
rm -f test/units/galaxy/test_collection_install.py
rm -f test/units/module_utils/urls/test_prepare_multipart.py
make PYTHON=/usr/bin/python3 tests-py3
%endif

%files
%license COPYING
%doc README.rst PKG-INFO changelogs/CHANGELOG-v2.11.rst
%dir %{_sysconfdir}/ansible/
%config(noreplace) %{_sysconfdir}/ansible/*
%{_mandir}/man1/ansible*
%{_bindir}/ansible*
%{_datadir}/ansible/
%{python3_sitelib}/ansible
%{python3_sitelib}/ansible_test
%{python3_sitelib}/*egg-info
%{_fileattrsdir}/ansible.attr
%{_rpmmacrodir}/macros.ansible
%{_rpmconfigdir}/ansible-generator

%files -n ansible-base-doc
%doc docs/docsite/rst
%if %{with docs}
%doc docs/docsite/_build/html
%endif

%changelog
* Sat Apr 03 2021 Kevin Fenzi <kevin@scrye.com> - 2.11.0-0.1.b4
- Rename to ansible-base, update to b4 beta version.

* Sat Feb 20 2021 Kevin Fenzi <kevin@scrye.com> - 2.10.6-1
- Update to 2.10.6.
- Fixes CVE-2021-20228

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Kevin Fenzi <kevin@scrye.com> - 2.10.5-1
- Update to 2.10.5.

* Sat Dec 19 2020 Kevin Fenzi <kevin@scrye.com> - 2.10.4-1
- Update to 2.10.4

* Sat Nov 07 2020 Kevin Fenzi <kevin@scrye.com> - 2.10.3-2
- Various review fixes

* Tue Nov 03 2020 Kevin Fenzi <kevin@scrye.com> - 2.10.3-1
- Update to 2.10.3

* Sat Oct 10 2020 Kevin Fenzi <kevin@scrye.com> - 2.10.2-1
- Update to 2.10.2

* Sat Sep 26 2020 Kevin Fenzi <kevin@scrye.com> - 2.10.1-1
- Initial version for review.

