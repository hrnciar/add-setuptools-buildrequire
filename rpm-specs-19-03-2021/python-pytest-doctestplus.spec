%global srcname pytest-doctestplus
%global pythonicname pytest_doctestplus
%global sum The py.test doctestplus plugin

Name:           python-%{srcname}
Version:        0.9.0
Release:        1%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
The doctestplus plugin provides advanced features for testing example Python
code that is included in Python docstrings and in standalone documentation
files.

Good documentation for developers contains example code. This is true of both
standalone documentation and of documentation that is integrated with the
code itself. Python provides a mechanism for testing code snippets that are
provided in Python docstrings. The unit test framework pytest provides a
mechanism for running doctests against both docstrings in source code and in
standalone documentation files.

This plugin augments the functionality provided by Python and pytest by
providing the following features:
* approximate floating point comparison for doctests that produce floating 
  point results 
* skipping particular classes, methods, and functions when running doctests
* handling doctests that use remote data in conjunction with the
  pytest-remotedata plugin
* optional inclusion of *.rst files for doctests}

%description %_description


%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six

Requires:       python3-numpy
Requires:       python3-pytest
Requires:       python3-six
# remotedata is useful for some tests, but not a hard requirement
Recommends:     python3-pytest-remotedata

%py_provides python3-%{srcname}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{pythonicname}.egg-info


%build
%py3_build


%install
%py3_install


# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{srcname}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{pythonicname}/
%{python3_sitelib}/*.egg-info/


%changelog
* Sun Feb 28 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.9.0-1
- Update to 0.9.0
- Fixes rhbz#1916541

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Mattia Verga <mattia.verga@protonmail.com> - 0.8.0-1
- Update to 0.8.0
- Fixes rhbz#1862639

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Christian Dersch <lupinix@fedoraproject.org> - 0.7.0-1
- new version

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.3.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.3.0-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.1.3-1
- new version

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.7

* Sat Mar 17 2018 Christian Dersch <lupinix@mailbox.org> - 0.1.2-1
- initial packaging effort

