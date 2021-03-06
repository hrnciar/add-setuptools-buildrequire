Name: jc
Summary: Serialize the output of CLI tools and file-types to structured JSON
License: MIT

Version: 1.14.4
Release: 1%{?dist}

URL: https://github.com/kellyjonbrazil/%{name}
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(pygments) >= 2.4.2
BuildRequires: python3dist(ruamel.yaml) >= 0.15
BuildRequires: python3dist(xmltodict) >= 0.12


%description
JSON CLI output utility. JC is used to JSONify the output of many
command-line tools and file types for easier parsing in scripts.


%prep
%autosetup


%build
%py3_build


%install
%py3_install


%check
# Some of the tests in the repo are subtly broken
# and produce different results on Ubuntu vs. other distros.
# See: https://github.com/kellyjonbrazil/jc/issues/96
#
# There is a ./run-tests.sh script in the repo, but it fires all tests,
# including those subtly-broken ones. The command below is taken from
# the project's CI configuration, and fires only the non-broken tests.
python3 -m unittest discover tests


%files
%doc README.md
%doc docs/
%license LICENSE.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Mar 06 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.14.4-1
- Update to v1.14.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 02 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.14.0-1
- Update to v1.14.0

* Fri Aug 14 2020 Artur Iwicki <fedora@svgames.pl> - 1.13.4-1
- Update to upstream release v1.13.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Artur Iwicki <fedora@svgames.pl> - 1.11.2-3
- Switch to using only the GitHub source
- Formatting changes

* Fri Jun 05 2020 Artur Iwicki <fedora@svgames.pl> - 1.11.2-2
- Fetch the GitHub sources apart from PyPi sources
  (the latter don't contain documentation and tests)
- Run tests during %%check
- Include the docs in the package

* Tue Jun 02 2020 Kelly Brazil <kellyjonbrazil@gmail.com> - 1.11.2-1
- Initial package.
