# Created by pyp2rpm-3.3.2
%global pypi_name hyperframe

%global common_description %{expand:
Pure-Python HTTP/2 framing This library contains the HTTP/2
framing code used in the hyper project. It provides a pure-Python codebase
that is capable of decoding a binary stream into HTTP/2 frames. This library is
used directly by hyper and a number of other projects to provide HTTP/2 frame
decoding logic.}

Name:           python-%{pypi_name}
Version:        6.0.0
Release:        2%{?dist}
Summary:        HTTP/2 framing layer for Python

License:        MIT
URL:            http://hyper.rtfd.org
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 15:39:27 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 6.0.0-1
- Update to 6.0.0
- Close: rhbz#1876208

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.2.0-4
- Drop Python 2 subpackage (#1750718)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.2.0-1
- Release 5.2.0
- Add actual tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 5.1.0-1
- Initial package.
