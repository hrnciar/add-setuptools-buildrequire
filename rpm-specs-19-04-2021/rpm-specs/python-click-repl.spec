# Created by pyp2rpm-3.3.4
%global pypi_name click-repl

Name:           python-%{pypi_name}
Version:        0.1.6
Release:        3%{?dist}
Summary:        REPL plugin for Click

License:        MIT
URL:            https://github.com/untitaker/click-repl
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

# Patch adapts tests to a newer python-click (present in Fedora)
Patch0:         %{url}/pull/53.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-click
BuildRequires:  python3-pytest
BuildRequires:  python3-prompt-toolkit
BuildRequires:  python3-six

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/click_repl/
%{python3_sitelib}/click_repl-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 František Zatloukal <fzatlouk@redhat.com> - 0.1.6-2
- BR: python3-six (fixes RHBZ#1908293)

* Tue Sep 29 2020 František Zatloukal <fzatlouk@redhat.com> - 0.1.6-1
- Initial package.
