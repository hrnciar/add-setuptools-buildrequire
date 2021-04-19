%global srcname openpaperwork-core

Name:           python-%{srcname}
Version:        2.0.2
Release:        1%{?dist}
Summary:        OpenPaperwork's core

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork/tree/master/openpaperwork-core
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Paperwork is a GUI to make papers searchable.

This is the core part of Paperwork. It manages plugins.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Paperwork is a GUI to make papers searchable.

This is the core part of Paperwork. It manages plugins.


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{python3} -m unittest discover --verbose -s tests

%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/openpaperwork_core/
%{python3_sitelib}/openpaperwork_core-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Feb 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Initial package.
