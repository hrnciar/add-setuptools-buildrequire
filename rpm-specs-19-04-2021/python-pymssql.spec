%global srcname pymssql
%global _description %{expand:A simple database interface for Python that builds on top of FreeTDS to provide
a Python DB-API (PEP-249) interface to Microsoft SQL Server.}

Name:           python-%{srcname}
Version:        2.1.5
Release:        2%{?dist}
Summary:        DB-API interface to Microsoft SQL Server

License:        LGPLv2+
URL:            http://pymssql.org/
Source0:        https://github.com/pymssql/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Disable dependency on setuptools_git, actually not needed to build the library
Patch0:         %{name}-2.1.3-disable_setuptools_git.patch

BuildRequires:  freetds-devel
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist setuptools}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


# No %%check (unit tests require a running SQL Server database)


%files -n python3-%{srcname}
%doc ChangeLog README.rst
%license LICENSE
%{python3_sitearch}/pymssql*
%{python3_sitearch}/_mssql*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-4
- Rebuilt for Python 3.8

* Tue Jul 30 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.4-3
- Fix build with Python >= 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-7
- Remove remaining bits of Python 2 legacy

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.3-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.3-2
- Use python2- prefix for Fedora dependencies

* Sun Jul  2 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.3-1
- Initial RPM release
