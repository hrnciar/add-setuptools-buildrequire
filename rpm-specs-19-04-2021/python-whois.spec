%global pypi_name whois

%global pypi_description Python wrapper for the "whois" command with \
a simple interface to access parsed WHOIS data for a given domain, \
able to extract data for all the popular TLDs (com, org, net, biz, info...).

Name: python-%{pypi_name}
Summary: Python module for retrieving WHOIS information of domains
License: MIT

Version: 0.9.10
Release: 1%{?dist}

URL: https://github.com/DannyCork/python-whois/
Source0: %pypi_source

BuildArch: noarch
BuildRequires: python3-devel

Requires: whois

%description
%pypi_description


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%pypi_description


%prep
%setup -q -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license license
%doc README
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info


%changelog
* Wed Apr 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.10-1
- Update to version 0.9.10

* Tue Apr 13 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.9-1
- Update to version 0.9.9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.7-1
- Update to version 0.9.7

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.6-2
- Include the README in the package

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.6-1
- Initial packaging
