%global upstream_name openslide-python

Name:           python-openslide
Version:        1.1.2
Release:        2%{?dist}
Summary:        Python bindings for the OpenSlide library

License:        LGPLv2
URL:            http://openslide.org/
Source0:        https://github.com/openslide/%{upstream_name}/releases/download/v%{version}/%{upstream_name}-%{version}.tar.xz

# Disable Intersphinx so it won't download inventories at build time
Patch0:         openslide-python-1.0.1-disable-intersphinx.patch

BuildRequires:  gcc
BuildRequires:  openslide >= 3.4.0
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pillow
BuildRequires:  python3-sphinx

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python
programs to use OpenSlide.


%package -n python3-openslide
Summary:        Python 3 bindings for the OpenSlide library
Requires:       openslide >= 3.4.0
Requires:       python3-pillow
Provides:       openslide-python3 = %{version}-%{release}
Provides:       openslide-python3%{?_isa} = %{version}-%{release}
Obsoletes:      openslide-python3 < 1.1.1-5
%{?python_provide:%python_provide python3-openslide}


%description -n python3-openslide
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python 3
programs to use OpenSlide.


%prep
%autosetup -n %{upstream_name}-%{version} -p1

# Examples include bundled jQuery and OpenSeadragon
rm -rf examples


%build
%py3_build
%{__python3} setup.py build_sphinx
rm build/sphinx/html/.buildinfo


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-openslide
%doc CHANGELOG.txt build/sphinx/html
%license LICENSE.txt lgpl-2.1.txt
%{python3_sitearch}/openslide/
%{python3_sitearch}/*.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 18 2020 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.2-1
- New release
