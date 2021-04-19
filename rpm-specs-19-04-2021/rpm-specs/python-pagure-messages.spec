# Enable Python dependency generation
%{?python_enable_dependency_generator}

%global pypi_name pagure-messages

Name:           python-%{pypi_name}
Version:        0.0.6
Release:        1%{?dist}
Summary:        A schema package for messages sent by pagure

License:        GPLv2+
URL:            https://pagure.io/pagure-messages
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(fedora-messaging)
BuildRequires:  python3dist(setuptools)

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
# Ensure we don't use this with incompatible Pagure versions
Conflicts:      pagure < 5.13

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pagure_messages
%{python3_sitelib}/pagure_messages-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Feb 11 19:50:30 EST 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.6-1
- Update to 0.0.6

* Fri Jan 29 11:29:41 EST 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.5-1
- Update to 0.0.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 09:47:01 EST 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.4-1
- Update to 0.0.4

* Tue Dec  1 08:13:42 EST 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.3-1
- Initial package
