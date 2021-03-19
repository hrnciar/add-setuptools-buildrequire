%global srcname volatile

Name:           python-%{srcname}
Version:        2.1.0
Release:        3%{?dist}
Summary:        A small extension for the tempfile module
License:        MIT
URL:            https://github.com/mbr/volatile
# pypi_source does not contain the license text
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description %{expand:
Temporary files and directories.

Contains replacement for tempfile.NamedTemporaryFile that does not delete the
file on close(), but still unlinks it after the context manager ends, as well as
a mkdtemp-based temporary directory implementation.

- Mostly reuses the stdlib implementations, supporting the same signatures.
- Due to that, uses the OS’s built-in temporary file facilities, no custom
  schemes.
- Tested on Python 2.6+ and 3.3+}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.1.0-2
- Use GitHub tarball, which includes license text

* Thu Nov 19 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-1
- Initial package
