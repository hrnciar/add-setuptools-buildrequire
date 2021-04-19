%global pypi_name pyspnego
%global pkg_name spnego

Name:           python-%{pkg_name}
Version:        0.1.5
Release:        1%{?dist}
Summary:        Windows Negotiate Authentication Client and Server

License:        MIT
URL:            https://github.com/jborean93/pyspnego
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(cryptography)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Propably issues with with Python 3.9
%pytest -v tests \
  -k "not test_negotiate_through_python_ntlm \
  and not test_negotiate_with_raw_ntlm \
  and not test_sspi_ntlm_auth_no_sign_or_seal \
  and not test_gss_sasl_description_fail \
  and not test_token \
  and not test_ntlm"

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{_bindir}/pyspnego-parse
%{python3_sitelib}/spnego/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Mar 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.5-1
- Update to latest upstream release 0.1.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-2
- Add missing BR (rhbz#1876588)

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora