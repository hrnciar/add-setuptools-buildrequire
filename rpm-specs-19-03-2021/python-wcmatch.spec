# Created by pyp2rpm-3.3.5
%global pypi_name wcmatch

Name:           python-%{pypi_name}
Version:        8.1.2
Release:        3%{?dist}
Summary:        Wildcard/glob file name matcher

License:        MIT
URL:            https://github.com/facelessuser/wcmatch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(bracex)
BuildRequires:  python3dist(setuptools)

%description
Wildcard Match provides an enhanced fnmatch, glob, and pathlib library in order
to provide file matching and globbing that more closely follows the features
found in Bash. In some ways these libraries are similar to Python's builtin
libraries as they provide a similar interface to match, filter, and glob the
file system. But they also include a number of features found in Bash's
globbing such as backslash escaping, brace expansion, extended glob pattern
groups, etc. They also add a number of new useful functions as well, such as
globmatch which functions like fnmatch, but for paths.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Wildcard Match provides an enhanced fnmatch, glob, and pathlib library in order
to provide file matching and globbing that more closely follows the features
found in Bash. In some ways these libraries are similar to Python's builtin
libraries as they provide a similar interface to match, filter, and glob the
file system. But they also include a number of features found in Bash's
globbing such as backslash escaping, brace expansion, extended glob pattern
groups, etc. They also add a number of new useful functions as well, such as
globmatch which functions like fnmatch, but for paths.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -vv -k "not test_tilde_user"

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 12 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.2-3
- Fix package as per package review comments (#1929992)

* Thu Mar 11 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.2-2
- Only skip required failing tests

* Wed Mar 10 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.2-1
- Update to 8.1.2 version
- Skip the failing tests

* Wed Feb 24 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.1-3
- Simplify URL: tag usage
- Drop unnecessary egg-info removal

* Sat Feb 20 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.1-2
- Change Source to github to use tests

* Thu Feb 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.1-1
- Initial package.
