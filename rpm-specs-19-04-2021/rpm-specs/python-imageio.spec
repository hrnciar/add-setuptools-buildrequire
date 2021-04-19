
%global srcname imageio

Name: python-%{srcname}
Version: 2.9.0
Release: 1%{?dist}
Summary: Python IO of image, video, scientific, and volumetric data formats.
License: BSD
URL: https://imageio.github.io
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# testing
# BuildRequires: python3-pytest
# BuildRequires: python3-numpy

%description
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.

%package -n python3-%{srcname}
Summary: Python IO of image, video, scientific, and volumetric data formats.
BuildRequires: python3-devel python3-setuptools

%description -n python3-%{srcname}
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Testing requires image sample, either local or from the internet
# %%check 
# export IMAGEIO_NO_INTERNET="1"
# %%pytest  --ignore=tests/test_ffmpeg.py  --ignore=tests/test_ffmpeg_info.py tests/

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
# Downloads binary freeimage library
%exclude %{_bindir}/imageio*
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info

%changelog
* Wed Feb 03 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 2.9.0-1
- Initial package

