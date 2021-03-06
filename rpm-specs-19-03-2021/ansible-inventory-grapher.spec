%global archive_name ansible-inventory-grapher
%global lib_name ansibleinventorygrapher

%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
# Ansible stopped shipping Python 2 modules in Fedora 29+
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           %{archive_name}
Version:        2.5.0
Release:        5%{?dist}
Summary:        Creates graphs representing ansible inventory

License:        GPLv3+
URL:            http://github.com/willthames/ansible-inventory-grapher
Source0:        https://github.com/willthames/ansible-inventory-grapher/archive/v%{version}.tar.gz

BuildArch:      noarch

%global _description\
ansible-inventory-grapher creates a dot file suitable for use by graphviz.\

%description %_description

%if %{with python2}
%package -n python2-%{archive_name}
Summary:        %summary
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  ansible
Requires:       ansible
%{?python_provide:%python_provide python2-%{archive_name}}
Provides:       %{archive_name} = %{version}-%{release}
Obsoletes:      %{archive_name} < 2.4.4-2

%description  -n python2-%{archive_name} %_description
%endif

%package -n python3-%{archive_name}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  ansible-python3
Requires:       ansible-python3
%{?python_provide:%python_provide python3-%{archive_name}}
%if ! %{with python2}
Provides:       %{archive_name} = %{version}-%{release}
Obsoletes:      %{archive_name} < 2.4.5-4
%endif

%description  -n python3-%{archive_name} %_description

%prep
%autosetup -n %{archive_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%py3_install

%if %{with python2}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3
%py2_install
%else
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3
%endif


%check
%if %{with python2}
%{__python2} setup.py test
%endif
%{__python3} setup.py test

%if %{with python2}
%files -n python2-%{archive_name}
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{python2_sitelib}/%{lib_name}
%{python2_sitelib}/ansible_inventory_grapher-%{version}-py2.*.egg-info
%endif

%files -n python3-%{archive_name}
%doc README.md
%license LICENSE.txt
%if ! %{with python2}
%{_bindir}/%{name}
%endif
%{_bindir}/%{name}-3
%{python3_sitelib}/%{lib_name}
%{python3_sitelib}/ansible_inventory_grapher-%{version}-py3.*.egg-info

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.5.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Parag Nemade <pnemade AT redhat DOT com> - 2.5.0-1
- Update to 2.5.0 version (#1747773)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.4.5-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.4.5-4
- Drop python2 subpackage in F29+

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.4.5-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.4.5-1
- Update to 2.4.5 version (#1535260)

* Tue Dec 12 2017 Jan Beran <jberan@redhat.com> - 2.4.4-2
- Python 2 binary package renamed to python2-ansible-inventory-grapher
- Python 3 subpackage

* Tue Nov 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.4-1
- Update to 2.4.4 version (#1514766)

* Wed Nov 08 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.2-1
- Update to 2.4.2 version (#1510677)

* Mon Nov 06 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.1-1
- Update to 2.4.1 version (#1509732)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.0-1
- Update to 2.4.0 version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.2-1
- Update to 2.3.2

* Thu Jul 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.1-1
- Update to 2.3.1

* Mon Jul 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.0-1
- Update to 2.3.0

* Sun Jul 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-1
- Update to 2.2.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-2
- Use github source that provided license and test files

* Mon May 09 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-1
- Update to 2.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-2
- Rename to ansible-inventory-grapher

* Sat Oct 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- Update to 1.0.1

* Thu Sep 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging

