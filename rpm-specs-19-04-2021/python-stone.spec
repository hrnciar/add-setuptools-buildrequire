%global pypi_name stone
Name:           python-%{pypi_name}
Version:        3.2.1
Release:        3%{?dist}
Summary:        The Official Api Spec Language for Dropbox
License:        MIT

URL:            https://github.com/dropbox/stone
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner

%description
%{summary}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}

%prep
%setup -q -n %{pypi_name}-%{version}


%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/stone
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.2.1-2
- Review fixes.

* Mon Dec 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.2.1-1
- Initial package.
