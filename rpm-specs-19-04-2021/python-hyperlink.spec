# Created by pyp2rpm-3.3.2
%global pypi_name hyperlink

%global common_description %{expand:
The humble, but powerful, URL runs everything around us. Chances are you've
used several just to read this text. Hyperlink is a featureful, pure-Python
implementation of the URL, with an emphasis on correctness.}

%bcond_without docs

Name:           python-%{pypi_name}
Version:        21.0.0
Release:        2%{?dist}
Summary:        A featureful, immutable, and correct URL for Python

# MIT: main library
# BSD: searchtools.js, websupport.js and modernizr.min.js
# OFL: Inconsolata-Regular.ttf and Inconsolata-Bold.ttf
License:        MIT and BSD and OFL
URL:            https://github.com/python-hyper/hyperlink
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(idna) >= 2.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_description}

%if %{with docs}
%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for hyperlink.
%endif
# with docs

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif
# with docs

%install
%py3_install

%check
%{__python3} -m unittest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif
# with docs

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 14:00:33 CET 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 21.0.0-1
- Update to 21.0.0
- Close: rhbz#1914100

* Sat Dec 26 14:37:18 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 20.0.1-2
- Fix FTBFS

* Sat Nov 14 20:13:27 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 20.0.1-1
- Update to 20.0.1
- Close: rhbz#1865772

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 19.0.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 23:21:28 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.0.0-5
- Drop Python 2 support (#1761205)

* Fri Sep 27 2019 Petr Viktorin <pviktori@redhat.com> - 19.0.0-4
- Run tests under Python 2
- Remove unused build dependencies on unittest2

* Sat Aug 17 2019 Miro Hron??ok <mhroncok@redhat.com> - 19.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 15:06:03 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.0.0-1
- Release 19.0.0

* Fri Mar 08 2019 Jeroen van Meeuwen <vanmeeuwen+fedora@kolabsys.com> - 18.0.0-6
- Add bcond_without docs

* Thu Mar 07 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 18.0.0-5
- Run tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 18.0.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 18.0.0-1
- Initial package.
