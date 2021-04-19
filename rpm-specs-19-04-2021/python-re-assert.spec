%global srcname re_assert
%global pkgname re-assert

Name:    python-%{pkgname}
Version: 1.1.0
Release: 1%{?dist}
Summary: Show where your regex match assertion failed!
License: MIT

URL:     https://github.com/asottile/re-assert
Source0: %{pypi_source}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest

%global _description %{expand:
Show where your regex match assertion failed!
}

%description %{_description}

%package -n python3-%{pkgname}
Summary: %summary

%py_provides python3-%{pkgname}
%description -n python3-%{pkgname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install


%files -n python3-%{pkgname}
%license LICENSE
%{python3_sitelib}/re_assert.py
%{python3_sitelib}/__pycache__/re_assert.*.pyc
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Sun Mar 21 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.1.0-1
- Initial commit
