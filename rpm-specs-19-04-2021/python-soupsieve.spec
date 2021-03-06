%bcond_without tests

Name:           python-soupsieve
Version:        2.2
Release:        1%{?dist}
Summary:        CSS selector library

License:        MIT
URL:            https://github.com/facelessuser/soupsieve
Source0:        https://github.com/facelessuser/soupsieve/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(html5lib)
BuildRequires:  python3dist(beautifulsoup4)
%endif

%global _description %{expand:
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS
selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though some
are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin
select feature, and as of Beautiful Soup version 4.7.0, it now is. Soup Sieve
can also be imported in order to use its API directly for more controlled,
specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS
draft specifications, though there are a number that don't make sense in a
non-browser environment. Selectors that cannot provide meaningful functionality
simply do not match anything.}

%description %_description

%package -n python3-soupsieve
Summary:        %{summary}
%{?python_provide:%python_provide python3-soupsieve}

%description -n python3-soupsieve %_description

%prep
%autosetup -n soupsieve-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
pytest-3 -v tests -k 'not test_namespace_xml_with_namespace'
%endif

%files -n python3-soupsieve
%{python3_sitelib}/soupsieve/
%{python3_sitelib}/soupsieve*.egg-info/
%doc README.md
%license LICENSE.md

%changelog
* Sat Feb 13 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2-1
- Latest version (#1927002)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Joel Capitao <jcapitao@redhat.com> - 2.1.0-1
- Update to 2.1.0 (#1906625)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.0.1-1
- Update to 2.0.1 (#1814999)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-6
- Rebuilt for Python 3.9

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-5
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.2-3
- Subpackage python2-soupsieve has been removed (#1748298)

* Mon Aug 19 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.2-2
- Rebuilt for Python 3.8

* Mon Jun 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.2-1
- Initial packaging
