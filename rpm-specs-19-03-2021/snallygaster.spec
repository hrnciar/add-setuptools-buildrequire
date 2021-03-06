%global pypi_name snallygaster

Name:           snallygaster
Version:        0.0.9
Release:        2%{?dist}
Summary:        Tool to scan for secret files on HTTP servers

License:        CC0
URL:            https://github.com/hannob/snallygaster
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-dns
BuildRequires:  python3-setuptools
BuildRequires:  python3-urllib3

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
snallygaster is a tool that looks for files accessible on web servers that
shouldn't be public and can pose a security risk.Typical examples include
publicly accessible git repositories, backup files potentially containing
passwords or database dumps.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python files or module parts for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Not running the lint test
# Set RUN_ONLINETESTS to run the tests
%{__python3} tests/test_scan_testdata.py

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.9-1
- Update to latest upstream release 0.0.9 (#1911204)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.6-2
- Add comment about running the tests (#839542)

* Sun May 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.6-1
- Initial package for Fedora
