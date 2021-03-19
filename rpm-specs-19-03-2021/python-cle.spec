%global srcname cle

Name:           python-%{srcname}
Version:        9.0.6136
Release:        1%{?dist}
Summary:        Python interface for analyzing binary formats

License:        BSD
URL:            https://github.com/angr/cle
Source0:        %{pypi_source}
BuildArch:      noarch

%description
CLE loads binaries and their associated libraries, resolves imports
and provides an abstraction of process memory the same way as if it was
loader by the OS's loader.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
CLE loads binaries and their associated libraries, resolves imports
and provides an abstraction of process memory the same way as if it was
loader by the OS's loader.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rf %{srcname}.egg-info/

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/cle/

%changelog
* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1929356)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1929356)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1905654)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1905654)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905654)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5327-1
- Update to latest upstream release 9.0.5327 (#1905654)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905654)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905654)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905654)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901718)

* Fri Nov 06 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4663-1
- New upstream version

* Thu Oct 08 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4495-1
- New upstream version

* Sat Aug 01 2020 W. Michael Petullo <mike@flyn.org> - 8.20.7.27-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 W. Michael Petullo <mike@flyn.org> - 8.20.7.6-1
- New upstream version

* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-1
- New upstream version

* Sun Jun 14 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.1-1
- New upstream version
- Drop upstreamed patch

* Thu May 28 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-2
- Add commentary for patch: upstream merge request

* Mon May 25 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-1
- Initial package
