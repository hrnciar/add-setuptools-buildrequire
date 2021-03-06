%global srcname colcon-core

Name:           python-%{srcname}
Version:        0.6.1
Release:        2%{?dist}
Summary:        Command line tool to build sets of software packages

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Not submitted upstream - make pytest dependency weak
Patch0:         %{name}-0.5.3-remove-pytest.patch
# Not submitted upstream - compatibility with pytest 2.9.X
Patch1:         %{name}-0.3.17-pytest-2.9.patch

BuildArch:      noarch

%description
colcon is a command line tool to improve the workflow of building, testing and
using multiple software packages. It automates the process, handles the ordering
and sets up the environment to use the packages.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-distlib >= 0.2.5
BuildRequires:  python%{python3_pkgversion}-empy
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-distlib >= 0.2.5
Requires:       python%{python3_pkgversion}-empy
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-coloredlogs
Recommends:     python%{python3_pkgversion}-pytest
Recommends:     python%{python3_pkgversion}-pytest-cov
Recommends:     python%{python3_pkgversion}-pytest-repeat
Recommends:     python%{python3_pkgversion}-pytest-rerunfailures
Recommends:     python%{python3_pkgversion}-pytest-runner
%else
Requires:       python%{python3_pkgversion}-coloredlogs
Requires:       python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-pytest-cov
Requires:       python%{python3_pkgversion}-pytest-repeat
Requires:       python%{python3_pkgversion}-pytest-rerunfailures
Requires:       python%{python3_pkgversion}-pytest-runner
%endif

%description -n python%{python3_pkgversion}-%{srcname}
colcon is a command line tool to improve the workflow of building, testing and
using multiple software packages. It automates the process, handles the ordering
and sets up the environment to use the packages.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon/
%{python3_sitelib}/colcon_core/
%{python3_sitelib}/colcon_core-%{version}-py%{python3_version}.egg-info/
%{_bindir}/colcon


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Scott K Logan <logans@cottsay.net> - 0.6.1-1
- Update to 0.6.1 (rhbz#1885437)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Scott K Logan <logans@cottsay.net> - 0.6.0-1
- Update to 0.6.0 (rhbz#1858471)

* Fri Jun 12 2020 Scott K Logan <logans@cottsay.net> - 0.5.10-1
- Update to 0.5.10 (rhbz#1846601)

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.5.9-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.5.9-1
- Update to 0.5.9 (rhbz#1775852)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.4.3-1
- Update to 0.4.3 (rhbz#1762548)

* Fri Oct 11 2019 Scott K Logan <logans@cottsay.net> - 0.4.1-2
- Skip a new test on platforms with older pytest

* Fri Oct 11 2019 Scott K Logan <logans@cottsay.net> - 0.4.1-1
- Update to 0.4.1

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Scott K Logan <logans@cottsay.net> - 0.4.0-1
- Update to 0.4.0 (rhbz#1747248)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.3.23-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Scott K Logan <logans@cottsay.net> - 0.3.23-1
- Update to 0.3.23

* Mon May 20 2019 Scott K Logan <logans@cottsay.net> - 0.3.22-1
- Update to 0.3.22

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.3.20-2
- Drop obsolete Group

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.3.20-1
- Update to 0.3.20
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7

* Mon Mar 18 2019 Scott K Logan <logans@cottsay.net> - 0.3.19-1
- Update to 0.3.19

* Fri Mar 01 2019 Scott K Logan <logans@cottsay.net> - 0.3.18-1
- Update to 0.3.18
- Handle automatic dependency generation (f30+)
- Make pytest and coloredlogs dependencies weak for Fedora

* Mon Feb 11 2019 Scott K Logan <logans@cottsay.net> - 0.3.17-2
- Enable tests on EPEL 7
- Move pytest-cov to Recommends
- Remove pylint from BuildRequires because those tests are skipped
- Target tests at the 'test' subdirectory specifically

* Fri Feb 08 2019 Scott K Logan <logans@cottsay.net> - 0.3.17-1
- Update to 0.3.17

* Mon Feb 04 2019 Scott K Logan <logans@cottsay.net> - 0.3.16-1
- Update to 0.3.16

* Wed Jan 16 2019 Scott K Logan <logans@cottsay.net> - 0.3.15-1
- Update to 0.3.15

* Thu Dec 13 2018 Scott K Logan <logans@cottsay.net> - 0.3.14-1
- Update to 0.3.14

* Wed Nov 21 2018 Scott K Logan <logans@cottsay.net> - 0.3.13-2
- Add Requires: pytest{,-cov,-runner} to satisfy requires.txt

* Fri Nov 09 2018 Scott K Logan <logans@cottsay.net> - 0.3.13-1
- Update to 0.3.13

* Wed Oct 31 2018 Scott K Logan <logans@cottsay.net> - 0.3.12-1
- Update to 0.3.12

* Mon Oct 29 2018 Scott K Logan <logans@cottsay.net> - 0.3.10-3
- Allow both deprecation and pending deprecation warnings

* Mon Oct 29 2018 Scott K Logan <logans@cottsay.net> - 0.3.10-2
- Add patch to allow deprecations (nothing we can do from here)

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.3.10-1
- Update to 0.3.10

* Thu Sep 20 2018 Scott K Logan <logans@cottsay.net> - 0.3.9-1
- Initial package
