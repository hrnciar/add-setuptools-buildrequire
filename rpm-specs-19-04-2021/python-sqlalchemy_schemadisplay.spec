%global srcname sqlalchemy_schemadisplay

Name:           python-%{srcname}
Version:        1.3
Release:        15%{?dist}
Summary:        Turn SQLAlchemy DB Model into a graph

License:        MIT
URL:            https://github.com/fschulze/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Turn SQLAlchemy DB Model into a graph.


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       graphviz
Requires:       python3-setuptools
Requires:       python3-sqlalchemy
Requires:       python3-pydot
BuildRequires:  graphviz
BuildRequires:  python3-devel
BuildRequires:  python3-pydot
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlalchemy
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Turn SQLAlchemy DB Model into a graph.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


# Tests aren't Python 3 yet
#check


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-7
- Subpackage python2-sqlalchemy_schemadisplay has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 18 2018 Jeremy Cline <jeremy@jcline.org> - 1.3-6
- Add Python 3 package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Jeremy Cline <jeremy@jcline.org> - 1.3-1
- Initial package.
