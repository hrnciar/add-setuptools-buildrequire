%global srcname logfury

Name:           python-%{srcname}
Version:        0.1.2
Release:        2%{?dist}
Summary:        Library for logging of method calls for Python

License:        BSD
URL:            https://github.com/ppolewicz/logfury
Source0:        %{pypi_source}
BuildArch:      noarch


%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.


%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 01 2020 Jonny Heggheim <hegjon@gmail.com> - 0.1.2-1
- Initial package
