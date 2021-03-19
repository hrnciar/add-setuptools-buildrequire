%bcond_with tests

Name:           adb-enhanced
Version:        2.5.10
Release:        1%{?dist}
Summary:        Tool for Android testing and development

License:        ASL 2.0
URL:            https://github.com/ashishb/adb-enhanced
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
ADB-Enhanced is a Swiss-army knife for Android testing and development. A
command-line interface to trigger various scenarios like screen rotation,
battery saver mode, data saver mode, doze mode, permission grant/revocation.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%pytest -v tests/adbe_tests.py
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/adbe
%{python3_sitelib}/adbe/
%{python3_sitelib}/adb_enhanced*.egg-info/

%changelog
* Wed Feb 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.10-1
- Update to latest upstream release 2.5.10 (#1922957)

* Tue Feb 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.9-1
- Update to latest upstream release 2.5.9 (#1922957)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.8-1
- Update to latest upstream release 2.5.8 (#1910345)

* Tue Dec 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.7-1
- Update to latest upstream release 2.5.7 (#1898458)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.4-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.4-1
- Update prep section
- Update to latest upstream release (#1819115)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.2-1
- Initial package for Fedora
