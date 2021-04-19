%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname cm_rgb

Name:           cm_rgb
Version:        0.3.5
Release:        2%{?dist}
Summary:        Utility to control RGB on AMD Wraith Prism
License:        MIT
URL:            https://github.com/gfduszynski/cm-rgb
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-gobject
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-click
BuildRequires:  python%{python3_pkgversion}-hidapi

%description
Utility to control RGB on AMD Wraith Prism


%prep
%autosetup -n %{srcname}-%{version}
chmod 644 LICENSE README.md

%build
%py3_build


%install
%py3_install
chmod -x %{buildroot}%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/dependency_links.txt

%files
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/*

%changelog
* Wed Apr 14 2021 Dennis Gilmore - 0.3.5-2
- address concerns raised in review
* Sun Jan 24 2021 Dennis Gilmore - 0.3.5-1
- initial packaging
