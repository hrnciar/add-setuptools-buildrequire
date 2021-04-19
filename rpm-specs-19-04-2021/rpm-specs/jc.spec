Name: jc
Summary: Serialize the output of CLI tools and file-types to structured JSON
License: MIT

Version: 1.15.1
Release: 1%{?dist}

URL: https://github.com/kellyjonbrazil/%{name}
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: gzip
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

# Upstream wanted to be helpful and pre-gzipped the man page.
# At the same time, they removed the uncompressed file. Sigh.
if [[ ! -f "man/jc.1" ]]; then
	cd man/
	gunzip jc.1.gz
fi


%build
%py3_build


%install
%py3_install

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p man/jc.1 %{buildroot}%{_mandir}/man1/


%check
# Upstream's CI configuration explicitly sets the time zone to LA
# before running the tests. They fail when run with a different TZ.
TZ='America/Los_Angeles' ./runtests.sh


%files
%doc README.md
%doc docs/
%license LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Apr 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.1-1
- Update to v1.15.1

* Thu Apr 08 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.15.0-1
- Update to v1.15.0
- Include man page in the package

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
