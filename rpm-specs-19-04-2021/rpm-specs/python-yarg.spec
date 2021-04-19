%{?python_enable_dependency_generator}
%global srcname yarg

%global _description\
Yarg is an easy to use PyPI client built on top of Python's requests library.

Name:           python-%{srcname}
Version:        0.1.9
Release:        14%{?dist}
Summary:        An easy to use PyPI client

License:        MIT
URL:            https://yarg.readthedocs.org/
Source0:        https://github.com/kura/yarg/archive/%{version}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE-REQUESTS LICENSE
%doc README.rst
%exclude %{python3_sitelib}/tests

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.9-13
- Switch to pyproject rpm macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-5
- Enable python dependency generator

* Sun Jan 13 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.1.9-4
- Fix Bug #1655700 - Exclude 'tests' folder

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.1.9-2
- Add additional build dependency for tests

* Sun Jun 24 2018 Dhanesh B. Sabane <dhanesh95@disroot.org> - 0.1.9-1
- Initial package.
