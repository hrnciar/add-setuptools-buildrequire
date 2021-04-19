%global srcname noggin-messages
%global modname noggin_messages

Name:           python-%{srcname}
Version:        0.0.1
Release:        2%{?dist}
Summary:        Fedora Messaging message schemas for Noggin

License:        MIT
URL:            https://github.com/fedora-infra/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

## Downstream fixes
Patch1001:      0001-Revert-Include-additional-files-in-the-sdist.patch

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros >= 0-14

%description
This package contains the fedora-messaging message schemas for Noggin.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Fedora Messaging message schemas for Noggin
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package contains the fedora-messaging message schemas for Noggin.


%prep
%autosetup -n %{srcname}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc docs/index.rst


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jul 26 18:49:27 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1-1
- Update to 0.0.1

* Sun Apr 19 16:50:52 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git20200416.1e93855-1
- Initial packaging
