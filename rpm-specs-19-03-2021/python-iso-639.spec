%global srcname iso-639
%global _description %{expand:%{summary}.
ISO 639-1, ISO 639-2, ISO 639-3, ISO 639-5 are supported.

NOTE: this package must NOT be confused with the python-iso639 package, which is
different.}

Name:           python-%{srcname}
Version:        0.4.5
Release:        15%{?dist}
Summary:        ISO 639 library for Python

License:        AGPLv3
URL:            https://github.com/noumar/iso639/
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# Required for tests
# BuildRequires:  %%{py3_dist pycountry}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n iso639-%{version}


%build
%py3_build


%install
%py3_install


%check
# Tests mostly check compatibility with the pycountry <= 1.11 library, not
# available in Fedora
# PYTHONPATH=$RPM_BUILD_ROOT%%{python3_sitelib}/:$PWD/ %%{__python3} tests/tests.py


%files -n python3-%{srcname}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.5-14
- Add BuildRequires on python3-setuptools
- Spec cleanup

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-6
- Subpackage python2-iso-639 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.5-1
- Initial RPM release
