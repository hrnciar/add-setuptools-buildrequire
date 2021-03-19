%global srcname openpaperwork-gtk

Name:           python-%{srcname}
Version:        2.0.2
Release:        1%{?dist}
Summary:        OpenPaperwork GTK plugins

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork/tree/master/openpaperwork-gtk
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(openpaperwork-core)
BuildRequires:  python3dist(pygobject)
BuildRequires:  gdk-pixbuf2
BuildRequires:  gtk3
BuildRequires:  pango

%description
Paperwork is a program to make papers searchable.

A bunch of plugins for Paperwork related to GLib and GTK.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(pygobject)
Requires:       gdk-pixbuf2
Requires:       gtk3
Requires:       pango

%description -n python3-%{srcname}
Paperwork is a GUI to make papers searchable.

A bunch of plugins for Paperwork related to GLib and GTK.


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
%{python3_sitelib}/openpaperwork_gtk/
%{python3_sitelib}/openpaperwork_gtk-%{version}-py%{python3_version}.egg-info/


%changelog
* Sat Feb 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Initial package.
