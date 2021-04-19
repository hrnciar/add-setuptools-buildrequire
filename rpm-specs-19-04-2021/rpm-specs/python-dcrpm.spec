%bcond_without tests

# Created by pyp2rpm-3.3.5
%global pypi_name dcrpm

Name:           python-%{pypi_name}
Version:        0.6.2
Release:        4%{?dist}
Summary:        A tool to detect and correct common issues around RPM database corruption

License:        GPLv2
URL:            https://github.com/facebookincubator/dcrpm
Source0:        %{pypi_source}
# tests: fix Popen mock
Patch0:         %{url}/commit/efc0166793db58e08b57ba3839638f7571355b93.patch
# tests: properly mock bdb in db_stat test
Patch1:         %{url}/commit/f7f89146e37c009a164e0e81de9b6b23d4874ffc.patch
# tests: properly mock yum process name
Patch2:         %{url}/commit/efcc4337821b3e498d832d2b6bf4241716acc0b3.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(setuptools)
%if 0%{?el8}
# pypandoc is an optional dependency and is not available in EPEL 8
%else
BuildRequires:  python3dist(pypandoc)
%endif
%if %{with tests}
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(testslide)
BuildRequires:  dnf
BuildRequires:  libdb-utils
%endif

%description
dcrpm is a tool to detect and correct common issues around RPM database
corruption.

%package -n     %{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} < 33 || 0%{?rhel} < 9
%py_provides    python3-%{pypi_name}
%endif

Requires:       python3dist(psutil)
Requires:       python3dist(setuptools)
Requires:       lsof
Recommends:     libdb-utils
%description -n %{pypi_name}
dcrpm is a tool to detect and correct common issues around RPM database
corruption.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove unnecessary shebang
sed -e '\|#!/usr/bin/env python|d' -i dcrpm/*.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} setup.py test
%endif

%files -n %{pypi_name}
%license LICENSE
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%doc HISTORY.md MANUAL_RPM_CLEANUP.md
%{_bindir}/dcrpm
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.6.2-3
- Enable tests for EPEL builds

* Sun Jan  3 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.6.2-2
- Update patches

* Wed Dec 30 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 0.6.2-1
- Initial package.
