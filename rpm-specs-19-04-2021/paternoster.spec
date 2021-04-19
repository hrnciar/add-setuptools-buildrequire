Name:           paternoster
Version:        3.3.0
Release:        5%{?dist}
Summary:        Allows to run ansible playbooks like ordinary python or bash scripts

License:        MIT
URL:            https://github.com/uberspace/%{name}
Source0:        https://github.com/Uberspace/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel} == 7
Requires:       ansible-python3
BuildRequires:  python3-devel
BuildRequires:  ansible-python3
BuildRequires:  python3-setuptools
BuildRequires:  python36-six
BuildRequires:  python36-tldextract >= 2.0.1
%else
Requires:       python3dist(ansible)
BuildRequires:  python3-devel
BuildRequires:  python3dist(ansible)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(tldextract) >= 2.0.1
%endif

%description
Paternoster enables ansible playbooks to be run like normal bash or python
scripts. It parses the given parameters using python's argparse and then passes
them on to the actual playbook via the ansible API. In addition it provides an
automated way to run commands as another user, which can be used to give normal
shell users special privileges, while still having a sleek and easy to
understand user interface.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%check
# disable on epel because of py.test-name
%if 0%{?fedora}
%global __pytest /usr/bin/py.test
%pytest
%endif

%files
%doc README.md
%doc doc/*
%license LICENSE.txt
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-*.egg-info

%changelog
* Mon Apr 12 2021 Tobias Florek <me@ibotty.net> - 3.3.0-5
- allow building against python 3.10-alpha*
* Mon Apr 05 2021 Tobias Florek <me@ibotty.net> - 3.3.0-4
- Fix ansible require on epel7.
* Mon Apr 05 2021 Tobias Florek <me@ibotty.net> - 3.3.0-3
- Disable test on epel.
- Fix requires on epel.
* Mon Mar 29 2021 Tobias Florek <me@ibotty.net> - 3.3.0-2
- Fix minor details from package review.
* Mon Mar 22 2021 Tobias Florek <me@ibotty.net> - 3.3.0-1
- Bump to new upstream version.
* Wed Apr 01 2020 Justus Rossmeier <pkg-fedora@juro.me> - 3.1.0-1
- Initial package.
