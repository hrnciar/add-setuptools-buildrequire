# This package installs two private shared libraries, so don't Provide them.
%global __provides_exclude_from  ^%{python3_sitearch}/.*\\.so)$

Name:     python-djvulibre
Version:  0.8.6
Release:  1%{?dist}
Summary:  Python support for the DjVu image format
License:  GPLv2
URL:      https://jwilk.net/software/python-djvulibre

Source0: %{pypi_source %pypi_name}

BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: djvulibre >= 3.5.21
BuildRequires: gcc
BuildRequires: ghostscript
BuildRequires: /usr/bin/pkg-config
BuildRequires: python3-devel >= 3.3
BuildRequires: python3dist(cython) >= 0.20
BuildRequires: python3dist(nose)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(sphinx)

%description
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open-source implementation of DjVu.



%package -n python3-djvulibre
Summary:    %{summary}
%{?python_provide:%python_provide python3-djvulibre}

%description -n python3-djvulibre
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open-source implementation of DjVu.


%package -n python-djvulibre-doc
Summary:    Documentation for python-djvulibre
BuildArch:  noarch

%description -n python-djvulibre-doc
Documentation for python-djvulibre.



%prep
%autosetup -n python-djvulibre-%{version}

# Make sure scripts in the examples directory aren't executable
chmod 0644  ./examples/*



%build
%py3_build
# Move license file to the root of the source directory, so %%license will find it.
mv  ./doc/COPYING  ./
# Generate the HTML documentation.
PYTHONPATH=${PWD} sphinx-build-3 doc/api html
# Remove the sphinx-build leftovers.
rm -rf html/.{doctrees,buildinfo}



%install
%py3_install


# nosetests doesn't work on ARMv7 or s390x.
%ifarch %ix86 x86_64
%check
# For these tests, import from PYTHONPATH instead of upstream's `djvu` subdirectory.
rm -rf ./djvu/
PYTHONPATH=%{buildroot}/%{python3_sitearch} nosetests-%{python3_version}
%endif



%files -n python3-djvulibre
%license COPYING
%{python3_sitearch}/djvu/
%{python3_sitearch}/python_djvulibre-%{version}-py%{python3_version}.egg-info

%files -n python-djvulibre-doc
%license COPYING
%doc     html/  examples/



%changelog
* Wed Mar 10 2021 Audrey Toskin <audrey@tosk.in> - 0.8.6-1
- Bump to upstream version 0.8.6, which drops support for Python 3.2,
  but adds support for Python 3.10, and improves memory usage.

* Wed Mar 10 2021 Audrey Toskin <audrey@tosk.in> - 0.8.5-5
- Minor update to show maximum version of Python supported by
  python-djvulibre v0.8.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Audrey Toskin <audrey@tosk.in> - 0.8.5-2
- Final working build.

* Wed Dec 18 2019 Audrey Toskin <audrey@tosk.in> - 0.8.5-1
- Initial package (starting over from scratch).
