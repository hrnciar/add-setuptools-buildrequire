%global rpm_name pg_activity

Name:           %{rpm_name}
Version:        2.1.4
Release:        1%{?dist}
Summary:        Command line tool for PostgreSQL server activity monitoring

License:        PostgreSQL
URL:            https://github.com/dalibo/pg_activity/
Source0:        https://github.com/dalibo/pg_activity/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# for check
BuildRequires:  pytest
BuildRequires:  python3dist(blessed)
BuildRequires:  python3dist(humanize)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(psycopg2)

Requires:       python3dist(psutil) >= 0.4.1
Requires:       python3dist(psycopg2)

%{?python_provide:%python_provide python3-%{rpm_name}}

%description
Top like application for PostgreSQL server activity monitoring

%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -k "not test_ui.txt"

%files
%license LICENSE.txt
%doc AUTHORS.md README.md
%{_bindir}/pg_activity
%{python3_sitelib}/pgactivity
%{python3_sitelib}/pg_activity-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Apr 03 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.4-1
- Version update to 2.1.4

* Wed Mar 17 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.3-1
- Version update to 2.1.3

* Fri Mar 12 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.2-1
- Version update to 2.1.2
- Fix #1937228 FTBFS with Python-3.10

* Thu Mar 11 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.1-1
- Version update to 2.1.1

* Mon Mar 08 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.0-1
- Version update to 2.1.0
- Add check section

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.6.0-1
- Initial package.
- fix autosetup usage and license
