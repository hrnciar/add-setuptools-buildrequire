%global pypi_name publicsuffix2

%global desc This module allows you to get the public suffix, as well as the registrable\
domain, of a domain name using the Public Suffix List from\
http://publicsuffix.org\
\
This module builds the public suffix list as a Trie structure, making it more\
efficient than other string-based modules available for the same purpose. It can\
be used effectively in large-scale distributed environments, such as PySpark.\
\
The code is a fork of the publicsuffix package and includes the same base API.\
In addition, it contains a few variants useful for certain use cases, such as\
the option to ignore wildcards or return only the extended TLD (eTLD). You just\
need to import publicsuffix2 instead.

Name: python-%{pypi_name}
Version: 2.20191221
Release: 3%{?dist}
Summary: Get a public suffix for a domain name using the Public Suffix List
License: MIT
URL: https://github.com/nexb/python-publicsuffix2
Source0: %{pypi_source}
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-requests
Requires: publicsuffix-list

%description -n python3-%{pypi_name}
%{desc}

%prep
%setup -q -n %{pypi_name}-%{version}
rm -r src/%{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
rm %{buildroot}%{python3_sitelib}/%{pypi_name}/public_suffix_list.dat
ln -s ../../../../share/publicsuffix/public_suffix_list.dat %{buildroot}%{python3_sitelib}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20191221-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20191221-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Dominik Mierzejewski <dominik@greysector.net> 2.20191221-1
- initial build
- unbundle public_suffix_list.dat file
