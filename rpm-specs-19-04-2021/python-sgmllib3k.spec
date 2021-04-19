%{?!python3_pkgversion:%global python3_pkgversion 3}

%global pypi_name sgmllib3k

Name:           python-sgmllib3k
Version:        1.0.0
Release:        3%{?dist}
Summary:        python3 copy of sgmllib
License:        BSD
URL:            http://hg.hardcoded.net/sgmllib
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
sgmllib was dropped in Python 3. For those depending on it,
that’s somewhat unfortunate. This is a quick and dirty
port of this old module. I just ran 2to3 on it and published it.
I don’t intend to maintain it, so it might be a good idea to
eventually think about finding another module to use.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
sgmllib was dropped in Python 3. For those depending on it,
that’s somewhat unfortunate. This is a quick and dirty
port of this old module. I just ran 2to3 on it and published it.
I don’t intend to maintain it, so it might be a good idea to
eventually think about finding another module to use.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build


%install
%py3_install


%files -n  python%{python3_pkgversion}-%{pypi_name}
%doc README
%pycached %{python3_sitelib}/sgmllib.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.0-2
- Various tweaks from review.

* Sat Dec 26 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.0-1
- Initial version for Fedora
