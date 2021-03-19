%global srcname colcon-notification

Name:           python-%{srcname}
Version:        0.2.13
Release:        4%{?dist}
Summary:        Extension for colcon to provide status notifications

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Taken from sources - disables install of data files per platform
Patch0:         %{name}-0.2.8-data-files.patch

BuildArch:      noarch

%description
An extension for colcon-core to provide status notifications.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.7
Requires:       python%{python3_pkgversion}-notify2
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide status notifications.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
BUILD_DEBIAN_PACKAGE=1 \
    %py3_build


%install
BUILD_DEBIAN_PACKAGE=1 \
    %py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_notification/
%{python3_sitelib}/colcon_notification-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.13-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Scott K Logan <logans@cottsay.net> - 0.2.13-1
- Update to 0.2.13 (rhbz#1824385)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.12-1
- Update to 0.2.12 (rhbz#1775866)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Scott K Logan <logans@cottsay.net> - 0.2.10-1
- Update to 0.2.10

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Scott K Logan <logans@cottsay.net> - 0.2.9-1
- Update to 0.2.9

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.2.8-2
- Set BUILD_DEBIAN_PACKAGE to relax setuptools requirement

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.2.8-1
- Update to 0.2.8 (rhbz#1718092)

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.7-2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Mon Mar 18 2019 Scott K Logan <logans@cottsay.net> - 0.2.7-1
- Update to 0.2.7
- Handle automatic dependency generation (f30+)

* Mon Jan 14 2019 Scott K Logan <logans@cottsay.net> - 0.2.6-1
- Update to 0.2.6

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.5-1
- Initial package
