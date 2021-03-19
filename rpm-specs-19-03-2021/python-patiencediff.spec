%global pypi_name patiencediff
Name:           python-%{pypi_name}
Version:        0.2.1
Release:        2%{?dist}
Summary:        Python implementation of the patiencediff algorithm

License:        GPLv2+
URL:            https://www.breezy-vcs.org/
Source0:        %{pypi_source}

# Remove redundant shebang and conditional from __main__.py
Patch1:   https://github.com/breezy-team/patiencediff/pull/5.patch
# Remove redundant shebang from _patiencediff_py.py
Patch2:   https://github.com/breezy-team/patiencediff/commit/7b2657d92ac7b56b07a92e5acfebf05f67a70e9c.patch
# Fix typo in README
Patch3:   https://github.com/breezy-team/patiencediff/pull/6.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  gcc

%global _description %{expand:
This package contains the implementation of the patiencediff algorithm, as
first described by Bram Cohen. Like Python's difflib, this module provides
both a convenience unified_diff function for the generation of unified diffs of
text files as well as a SequenceMatcher that can be used on arbitrary
lists. Patiencediff provides a good balance of performance, nice output for
humans, and implementation simplicity.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Ondřej Pohořelský <opohorel@redhat.com> - 0.2.1-1
- Initial package.
