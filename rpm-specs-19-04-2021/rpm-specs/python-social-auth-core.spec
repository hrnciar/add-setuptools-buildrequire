%global pypi_name social-auth-core
%global egginfo_name social_auth_core
%global relver 4.0.2
# The Python module name is different from the package name published to PyPI.
%global module_name social_core

%global desc %{expand:
Python Social Auth aims to be an easy-to-setup social authentication and
authorization mechanism for Python projects supporting protocols like OAuth (1
and 2), OpenID and others.

The initial codebase is derived from django-social-auth with the idea of
generalizing the process to suit the different frameworks around, providing
the needed tools to bring support to new frameworks.

django-social-auth itself was a product of modified code from
django-twitter-oauth and django-openid-auth projects.

The project is now split into smaller modules to isolate and reduce
responsibilities and improve reusability.

Documentation: https://python-social-auth.readthedocs.io/en/latest/
Release notes: https://github.com/python-social-auth/%{module_name}/releases/tag/%{relver}
}

%global summary Python Social Auth is an easy to setup social authentication\/registration mechanism with support for several frameworks and auth providers.

Name:           python-%{pypi_name}
Version:        %{relver}
Release:        2%{?dist}
Summary:        %{summary}
License:        BSD
URL:            https://github.com/python-social-auth/social-core/
Source0:        %{pypi_source}

# Remove this patch when fixed in upstream
Patch1:         disable-test-LiveJournalOpenIdTest.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# Requirements for running social-core
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(requests-oauthlib)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pyjwt)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(python-jose)
BuildRequires:  python3dist(defusedxml)
BuildRequires:  python3dist(python3-openid)
BuildRequires:  python3dist(python3-saml)

# Requirements for running tests
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cryptography)
Requires:       python3dist(defusedxml)
Requires:       python3dist(oauthlib)
Requires:       python3dist(pyjwt)
Requires:       python3dist(python3-openid)
Requires:       python3dist(requests)
Requires:       python3dist(requests-oauthlib)
Requires:       python3dist(six)

%description -n python3-%{pypi_name}
%{desc}
If you want social-core to work with azuread (the Azure Active Directory), this
is the package you need.

%package -n python3-%{pypi_name}+saml
Summary: %{pypi_name} with SAML support.
%{?python_provide:%python_provide python3-%{pypi_name}+saml}

Requires:       python3dist(%{pypi_name}) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3dist(python3-saml)

Obsoletes:      python3-%{pypi_name}-saml <= %{version}

%description -n python3-%{pypi_name}+saml
%{pypi_name} with SAML support. Install the dependencies only. No code is included.

For detailed description, please refer to package python3-%{pypi_name}

%package -n python3-%{pypi_name}+openidconnect
Summary: %{pypi_name} with OpenIDConnect support.
%{?python_provide:%python_provide python3-%{pypi_name}+openidconnect}

Requires:       python3dist(%{pypi_name}) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3dist(python-jose)

Obsoletes:      python3-%{pypi_name}-openidconnect <= %{version}

%description -n python3-%{pypi_name}+openidconnect
%{pypi_name} with OpenIDConnect support. Install the dependencies only. No code is included.

For detailed description, please refer to package python3-%{pypi_name}

%prep
%autosetup -p0 -n %{pypi_name}-%{version}

rm -rf %{egginfo_name}.egg-info

# Use Python3 builtin unittest module instead
sed -i /unittest2/d social_core/tests/requirements-python3.txt
sed -i s/unittest2/unittest/ \
    %{module_name}/tests/*.py \
    %{module_name}/tests/actions/*.py \
    %{module_name}/tests/backends/*.py

%build
%py3_build

%install
%py3_install

rm -r %{buildroot}%{python3_sitelib}/%{module_name}/tests/

%check
%{pytest} %{module_name}/tests/

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{module_name}/
%{python3_sitelib}/%{egginfo_name}-%{version}-py*.egg-info

%files -n python3-%{pypi_name}+saml
%ghost %{python3_sitelib}/*.egg-info

%files -n python3-%{pypi_name}+openidconnect
%ghost %{python3_sitelib}/*.egg-info

%changelog
* Sat Mar 06 2021 Chenxiong Qi <qcxhome@gmail.com> - 4.0.2-2
- Bump release 4.0.2-2

* Sat Mar 06 2021 Chenxiong Qi <qcxhome@gmail.com> - 4.0.2-1
- Rebuilt for upstream version 4.0.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Chenxiong Qi <qcxhome@gmail.com> - 3.3.3-3
- Fix subpackage requires

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Chenxiong Qi <qcxhome@gmail.com> - 3.3.3-1
- Rebuilt version 3.3.3

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.7.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.0-9
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.7.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-5
- Change the defusedxml requirement to not have rc1, which confused the python auto dep script.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.7.0-1
- Initial package.
