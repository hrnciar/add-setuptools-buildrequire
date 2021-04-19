%global pypi_name xbout

Name:           python-%{pypi_name}
Version:        0.2.4
Release:        1%{?dist}
Summary:        Collects BOUT++ data from parallelized simulations into xarray

License:        ASL 2.0
URL:            https://github.com/boutproject/xBOUT
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python3dist(natsort)
BuildRequires:  python3dist(dask[array])
BuildRequires:  python3dist(netcdf4)
BuildRequires:  python3dist(animatplot)
BuildRequires:  python3dist(xarray)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3-boutdata

%description
xBOUT provides an interface for collecting the output data from a
BOUT++ simulation into an xarray dataset in an efficient and
scalable way, as well as accessor methods for common BOUT++ analysis
and plotting tasks.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}}

Requires:  python3dist(natsort)
Requires:  python3dist(dask[array])
Requires:  python3dist(netcdf4)
Requires:  python3dist(animatplot)
Requires:  python3dist(xarray)
Requires:  python3dist(pillow)
Requires:  python3dist(py)
#Requires:  python3dist(boutdata)
Requires:  python3-boutdata


%description -n python3-%{pypi_name}
xBOUT provides an interface for collecting the output data from a
BOUT++ simulation into an xarray dataset in an efficient and
scalable way, as well as accessor methods for common BOUT++ analysis
and plotting tasks.

%package -n python3-%{pypi_name}-doc
Summary:        xBOUT documentation
Recommends:     python3-%{pypi_name}
%description -n python3-%{pypi_name}-doc
Documentation for xBOUT

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf xbout.egg-info
# boutdata doesn't have the provides
# animatplot is to old RHBZ#1885115
sed -e 's/boutdata.*//' -e 's/animatplot.*/animatplot/'  -i requirements.txt -i setup.cfg

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest xbout


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/xbout-%{version}-py?.*.egg-info

%files -n python3-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Apr 17 2021 David Schwörer <davidsch@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 David Schwörer <davidsch@fedoraproject.org> - 0.2.3-0.2
- Fix FTI
- Fix License

* Sun Dec 06 2020 David Schwörer <davidsch@fedoraproject.org> - 0.2.3-0.1
- Initial package.
