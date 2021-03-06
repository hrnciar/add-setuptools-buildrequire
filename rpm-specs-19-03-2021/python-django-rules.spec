%global shortname django-rules
Name:          python-%{shortname}
Version:       2.2.0
Release:       3%{?dist}
Summary:       Awesome Django authorization, without the database

License:       MIT
URL:           https://github.com/dfunckt/%{shortname}/
Source0:       https://github.com/dfunckt/%{shortname}/archive/v%{version}/%{shortname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Awesome Django authorization, without the database.

%package -n python3-%{shortname}
Summary:       Awesome Django authorization, without the database
%{?python_provide:%python_provide python3-%{shortname}}
Requires:      python3-django

%description -n python3-%{shortname}
Awesome Django authorization, without the database.

%prep
%autosetup -n %{shortname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{shortname}
%license LICENSE
%{python3_sitelib}/rules/
%{python3_sitelib}/rules-*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Adam Williamson <awilliam@redhat.com> - 2.2.0-1
- Update to 2.2.0 (compatible with Django 3)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-2
- Review updates

* Thu Dec 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-1
- Initial package
