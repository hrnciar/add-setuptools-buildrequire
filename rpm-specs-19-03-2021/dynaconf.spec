%global srcname dynaconf
%global common_desc \
Dynaconf is a layered configuration system for Python applications with strong \
support for 12-factor applications and extensions for Flask and Django

Name:           %{srcname}
Version:        3.1.2
Release:        2%{?dist}
Summary:        A dynamic configurator for python projects

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        %{pypi_source}

BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
# Trailing slash is to ensure setuptools behavior instead of distutils since
# the project can use either and .egg-info could end up being a file or a
# directory.
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%{_bindir}/%{srcname}

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 4 2020 David Moreau Simard <moi@dmsimard.com> - 3.1.2-1
- Update to latest upstream release
- Removed dependencies that have been vendored by upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 David Moreau Simard <dmsimard@redhat.com> - 2.2.0-1
- Update to latest upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuilt for Python 3.8

* Fri Jul 5 2019 David Moreau Simard <dmsimard@redhat.com> - 2.0.3-1
- First version of the package
