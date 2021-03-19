%global srcname calcephpy

Name:           python-%{srcname}
Version:        3.4.7
Release:        3%{?dist}
Summary:        Astronomical library to access planetary ephemeris files

License:        CeCILL or CeCILL-B or CeCILL-C
URL:            https://pypi.python.org/pypi/calcephpy
Source0:        %{pypi_source}

%global _description %{expand:
This is the Python module of calceph.
Calceph is a library designed to access the binary planetary ephemeris files,
such INPOPxx, JPL DExxx and SPICE ephemeris files.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?rhel} == 7
BuildRequires:  python36-Cython
%else
BuildRequires:  python3-Cython
%endif

# Needed by EPEL7
%py_provides python3-%{srcname}

%description -n python3-%{srcname} %_description


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%autosetup -n %{srcname}-%{version}

# Remove executable bit set on license files
chmod -x COPYING*

# Remove egg files from source
rm -r %{srcname}.egg-info


%build
%py3_build

# Remove hidden files from docdir
find doc -name .buildinfo -exec rm -f {} \;


%install
%py3_install


%files -n       python3-%{srcname}
%license COPYING_CECILL_V2.1.LIB COPYING_CECILL_B.LIB COPYING_CECILL_C.LIB
%{python3_sitearch}/*.so
%{python3_sitearch}/*egg-info/


%files      doc
%doc doc/calceph_python.pdf doc/html/python/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-2
- Create a doc subpackage
- Remove executable bit set on license files
- Add py_provides macro for EPEL7

* Sat Nov 07 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-1
- Update to 3.4.7

* Tue Nov 3 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.6-1
- Initial packaging
