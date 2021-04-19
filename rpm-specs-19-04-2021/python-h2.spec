# Created by pyp2rpm-3.3.2
%global pypi_name h2

%global common_description %{expand:
HTTP/2 Protocol Stack This repository contains a pure-Python
implementation of a HTTP/2 protocol stack. It's written from the ground up to
be embeddable in whatever program you choose to use, ensuring that you can
speak HTTP/2 regardless of your programming paradigm.}

%bcond_without docs

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        4%{?dist}
Summary:        HTTP/2 State-Machine based protocol implementation

License:        MIT
URL:            https://hyper-h2.readthedocs.io
Source0:        %pypi_source
# Workaround the issues with hypothesis 6.6
Patch0:         https://patch-diff.githubusercontent.com/raw/python-hyper/h2/pull/1248.patch#/0001-Workaround-the-issues-with-hypothesis-6.6.patch
# Workaround for Python 3.10 new repr() behavior
# https://github.com/python-hyper/h2/pull/1254
Patch1:         0001-Fix-repr-checks-for-Python-3.10.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(hpack) >= 4 with python3dist(hpack) < 5)
BuildRequires:  (python3dist(hyperframe) >= 6 with python3dist(hyperframe) < 7)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)

%if %{with docs}
# Unbundle
BuildRequires:  js-jquery
BuildRequires:  js-underscore
%endif

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%if %{with docs}
%package doc
Summary:        Documentation for %{name}

Requires: js-jquery
Requires: js-underscore

%description doc
%{common_description}

This is the documentation package for h2.
%endif

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

# Unbundle JS
rm -v html/_static/underscore.js
ln -s /usr/share/javascript/underscore/underscore-min.js html/_static/underscore.js
rm -v html/_static/underscore-1.12.0.js
ln -s /usr/share/javascript/underscore/underscore.js html/_static/underscore-1.12.0.js
rm -v html/_static/jquery.js
ln -s /usr/share/javascript/jquery/3.2.1/jquery.min.js html/_static/jquery.js
rm -v html/_static/jquery-3.5.1.js
ln -s /usr/share/javascript/jquery/3.2.1/jquery.js html/_static/jquery-3.5.1.js
%endif

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif


%changelog
* Tue Apr 13 21:52:01 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.0-4
- Add workaround for Python 3.10 new repr() behavior
- Fix: rhbz#1948992

* Tue Mar  9 08:32:35 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.0-3
- Add patch to workaround the issues with hypothesis 6.6
- Close: rhbz#1936524

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 15:28:57 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.0-1
- Update to 4.0.0
- Close: rhbz#1880732

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.9

* Mon Feb 17 03:14:38 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.1-1
- Release 3.1.1 (#1742451)

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-6
- Subpackage python2-h2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt to update automatic Python dependencies

* Fri Mar 08 2019 Jeroen van Meeuwen <vanmeeuwen+fedora@kolabsys.com> - 3.1.0-2
- Add bcond_without docs

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.0-1
- Release 3.1.0
- Run tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-1
- Initial package.
