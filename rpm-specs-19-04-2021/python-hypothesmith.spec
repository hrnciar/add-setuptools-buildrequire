# Created by pyp2rpm-3.3.5
%global pypi_name hypothesmith

%global common_description %{expand:
Hypothesis strategies for generating Python programs, something like CSmith.}

Name:           python-%{pypi_name}
Version:        0.1.8
Release:        1%{?dist}
Summary:        Hypothesis strategies for generating Python programs

License:        MPLv2.0
URL:            https://github.com/Zac-HD/hypothesmith
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(black)
BuildRequires:  python3dist(hypothesis) >= 5.41
BuildRequires:  python3dist(lark-parser) >= 0.7.2
BuildRequires:  python3dist(libcst) >= 0.3.8
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pytest)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} == 32
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Tox configuration is passing unsupported arguments to pytest
rm tox.ini

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Mar 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1.8-1
- Initial package.
