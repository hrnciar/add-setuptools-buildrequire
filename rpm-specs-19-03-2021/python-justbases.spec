%{?python_enable_dependency_generator}
%global srcname justbases
Name:       python-%{srcname}
Version:    0.15
Release:    2%{?dist}
Summary:    A small library for precise conversion between arbitrary bases

License:    LGPLv2+
URL:        http://pypi.python.org/pypi/justbases
Source0:    https://pypi.io/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch

%description
A small library for precise conversion between arbitrary bases and native
Python numbers.

%package -n python3-%{srcname}
Summary:    A small library for precise conversion between arbitrary bases
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
A small library for precise conversion between arbitrary bases and native
Python numbers.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf justbases.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m unittest discover --verbose tests/test_deterministic

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/justbases/
%{python3_sitelib}/justbases-%{version}-*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 mulhern <amulhern@redhat.com> - 0.15-1
- Update to 0.15

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14-2
- Rebuilt for Python 3.9

* Thu Apr 23 2020 mulhern <amulhern@redhat.com> - 0.14-1
- Update to new release

* Thu Apr 23 2020 mulhern <amulhern@redhat.com> - 0.13-2
- Remove license macro; upstream is not currently packaging its license file

* Thu Apr 23 2020 mulhern <amulhern@redhat.com> - 0.13-1
- Change license to LGPLv2+

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9-9
- Enable python dependency generator

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-8
- Subpackage python2-justbases has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-2
- Rebuild for Python 3.6

* Tue Aug 2 2016 mulhern <amulhern@redhat.com> - 0.9
- New release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 16 2016 mulhern <amulhern@redhat.com> - 0.6
- Initial release
