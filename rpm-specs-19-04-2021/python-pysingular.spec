%global srcname pysingular
%global upname  PySingular

Name:           python-%{srcname}
Version:        0.9.7
Release:        5%{?dist}
Summary:        Python interface to Singular

License:        GPLv2+
URL:            https://github.com/sebasguts/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Singular)
BuildRequires:  python3-devel

%global _description %{expand:
This package contains a basic interface to call Singular from python.
It is meant to be used in the Jupyter interface to Singular.}

%description %_description

%package     -n python3-%{srcname}
Summary:        Python 3 interface to Singular

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{upname}-%{version}

%build
%py3_build

%install
%py3_install

%files       -n python3-%{srcname}
%doc README
%license COPYING GPLv2
%{python3_sitearch}/%{upname}*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 0.9.7-1
- Initial RPM
