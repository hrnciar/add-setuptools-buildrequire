%global srcname pynetbox

Name:           python-%{srcname}
Version:        6.1.0
Release:        1%{?dist}
Summary:        Python API client library for Netbox

License:        ASL 2.0
URL:            https://github.com/digitalocean/pynetbox
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pytest)
BuildRequires:  (python3dist(requests) >= 2.20 with python3dist(requests) < 3)
BuildRequires:  (python3dist(six) >= 1 with python3dist(six) < 2)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -vv tests/test_*.py tests/unit

%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Wed Apr 07 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 6.1.0-1
- Update to 6.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Tue Jan 05 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Wed Dec 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Wed Dec 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Fri Dec 25 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2

* Thu Oct 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Wed Sep 02 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.0.8-1
- Update to 5.0.8

* Thu Aug 20 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.0.7-1
- Update to 5.0.7

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1

* Tue Feb 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.2.5-1
- Update to 4.2.5

* Thu Jan 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.2.4-1
- Initial package
