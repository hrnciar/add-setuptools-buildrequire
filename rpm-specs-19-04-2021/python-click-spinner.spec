# Created by pyp2rpm-3.3.4
%global pypi_name click-spinner

Name:           python-%{pypi_name}
Version:        0.1.10
Release:        3%{?dist}
Summary:        Spinner for Click

License:        MIT
URL:            https://github.com/click-contrib/click-spinner
Source0:        %{pypi_source}
BuildArch:      noarch

Provides:       python-blindspin = %{version}-%{release}
Obsoletes:      python-blindspin < 2.0.1

%description
Click Spinner shows the user some progress when a progress bar is
not suitable because you don’t know how much longer it would take.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Click Spinner shows the user some progress when a progress bar is
not suitable because you don’t know how much longer it would take.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/click_spinner/
%{python3_sitelib}/click_spinner-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.10-2
- Obsolete python-blindspin (#1883154)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.10-1
- Initial package for Fedora
