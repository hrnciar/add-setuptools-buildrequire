%global pypi_name aiosecretsdump

Name:           python-%{pypi_name}
Version:        0.0.2
Release:        2%{?dist}
Summary:        Secrets dumper

License:        MIT
URL:            https://github.com/skelsec/aiosecretsdump
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Dump secrets feature for aiosmb.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Dump secrets feature for aiosmb.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove shebang
sed -i -e '/^#!\//, 1d' aiosecretsdump/__init__.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/aiosecretsdump
%{python3_sitelib}/%{pypi_name}
# https://github.com/skelsec/aiosecretsdump/issues/2
%{python3_sitelib}/bins
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.2-1
- Update to latest upstream release 0.0.2

* Mon Nov 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.1-2
- Add missing BRs (#1825592)

* Sun Apr 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.1-1
- Initial packagefor Fedora