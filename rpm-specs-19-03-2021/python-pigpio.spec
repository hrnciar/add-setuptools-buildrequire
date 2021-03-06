%global pypi_name pigpio

Name:           python-%{pypi_name}
Version:        1.78
Release:        2%{?dist}
Summary:        Raspberry Pi GPIO module

License:        Unlicense
URL:            http://abyz.co.uk/rpi/pigpio/python.html
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Raspberry Pi Python module to access the pigpio daemon.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Raspberry Pi Python module to access the pigpio daemon.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 16:20:14 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.78-1
- Update to 1.78

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.46-1
- Update to 1.46

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.40-7.post1
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-6.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.40-5.post1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.40-4.post1
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-3.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-2.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.40.post1-1
- Initial package
