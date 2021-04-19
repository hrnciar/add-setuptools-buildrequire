%global srcname b2sdk

Name:           python-%{srcname}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Backblaze B2 SDK

License:        MIT
URL:            https://github.com/Backblaze/b2-sdk-python
Source0:        %{pypi_source}
BuildArch:      noarch


%global _description %{expand:
Python library and a few handy utilities for easy access to all of the
capabilities of B2 Cloud Storage.

B2 command-line tool is an example of how it can be used to provide command-line
access to the B2 service, but there are many possible applications (including
FUSE filesystems, storage backend drivers for backup applications etc).}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%description -n python3-%{srcname} %_description

%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/test


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Mon Apr 05 2021 Jonny Heggheim <hegjon@gmail.com> - 1.4.0-1
- Updated to version 1.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Jonny Heggheim <hegjon@gmail.com> - 0.1.2-1
- Initial package
