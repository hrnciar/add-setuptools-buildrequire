%global pypi_name apypie

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        2%{?dist}
Summary:        Apipie bindings for Python

License:        MIT
URL:            https://github.com/Apipie/apypie
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Python bindings for the Apipie - Ruby on Rails API documentation tool.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Apipie bindings for Python

%description -n python%{python3_pkgversion}-%{pypi_name}
Apipie bindings for Python3

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.3.2-1
- Update to apypie 0.3.2

* Wed Oct 21 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.3.1-1
- Update to apypie 0.3.1

* Mon Oct 19 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.3.0-1
- Update to apypie 0.3.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.9

* Thu Apr 09 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.2.2-1
- Release python-apypie 0.2.2

* Tue Apr 07 2020 Ondřej Gajdušek <ogajduse@redhat.com> - 0.2.1-2
- Build customization for Fedora

* Mon Nov 25 2019 Evgeni Golov - 0.2.1-1
- Release python-apypie 0.2.1

* Mon Nov 04 2019 Evgeni Golov - 0.2.0-1
- Release python-apypie 0.2.0

* Tue Sep 10 2019 Evgeni Golov - 0.1.0-1
- Update to apypie 0.1.0

* Thu Aug 15 2019 Evgeni Golov - 0.0.5-1
- Update to apypie 0.0.5

* Fri Aug 09 2019 Evgeni Golov - 0.0.4-1
- Update to apypie 0.0.4

* Wed Jul 17 2019 Evgeni Golov - 0.0.3-1
- Initial package.

