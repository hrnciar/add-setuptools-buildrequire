# Created by pyp2rpm-3.3.2
%global pypi_name userpath

Name:           python-%{pypi_name}
Version:        1.4.2
Release:        3%{?dist}
Summary:        Cross-platform tool for adding locations to the user PATH

License:        MIT OR ASL 2.0
URL:            https://github.com/ofek/userpath
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
Ever wanted to release a cool new app but found it difficult to add its
location to PATH for users? Me too! This tool does that for you on all major
operating systems and does not require elevated privileges! Fear not, this
only modifies the user PATH; the system PATH is never touched nor even looked
at!

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(click)
Requires:       python3dist(distro)
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
Ever wanted to release a cool new app but found it difficult to add its
location to PATH for users? Me too! This tool does that for you on all major
operating systems and does not require elevated privileges! Fear not, this
only modifies the user PATH; the system PATH is never touched nor even looked
at!

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE-APACHE LICENSE-MIT
%doc README.rst
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Feb 18 2021 Lumír Balhar <lbalhar@redhat.com> - 1.4.2-3
- No longer provide the old package name

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Lumír Balhar <lbalhar@redhat.com> - 1.4.2-1
- Update to 1.4.2 (#1917150)

* Tue Aug 04 2020 Lumír Balhar <lbalhar@redhat.com> - 1.4.1-4
- Fix FTBFS — remove unversioned python macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.4.1-1
- Update to 1.4.1 (#1851126)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Lumír Balhar <lbalhar@redhat.com> - 1.4.0-1
- Update to 1.4.0 (#1833676)

* Sat Feb 08 2020 Lumír Balhar <lbalhar@redhat.com> - 1.3.0-3
- Provide more variants of the old package name

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Lumír Balhar <lbalhar@redhat.com> - 1.3.0-1
- Initial package.
- Replacement for python-adduserpath
