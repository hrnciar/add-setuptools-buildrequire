# Created by pyp2rpm-3.3.5
%if 0%{?rhel}
%bcond_with docs
%else
%bcond_without docs
%endif
%bcond_without tests

%global pypi_name drgn

%global common_description %{expand:
drgn (pronounced "dragon") is a debugger with an emphasis on programmability.
drgn exposes the types and variables in a program for easy, expressive
scripting in Python.}

Name:           python-%{pypi_name}
Version:        0.0.11
Release:        2%{?dist}
Summary:        Scriptable debugger library

License:        GPLv3+
URL:            https://github.com/osandov/drgn
Source0:        %{pypi_source}
# Needed until https://github.com/osandov/drgn/pull/100 is merged and a new
# release is cut
Source1:        %{url}/raw/v%{version}/COPYING
# examples: add missing shebangs
Patch0:         %{url}/pull/97.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with docs}
BuildRequires:  sed
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-docs
%endif
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  bzip2-devel
BuildRequires:  elfutils-devel
BuildRequires:  libkdumpfile-devel
BuildRequires:  zlib-devel
BuildRequires:  xz-devel

# https://github.com/osandov/drgn/issues/98
ExcludeArch:    armv7hl i686
# https://github.com/osandov/drgn/issues/99
ExcludeArch:    s390x

%description
%{common_description}

%package -n     %{pypi_name}
Summary:        %{summary}

%description -n %{pypi_name}
%{common_description}

%if %{with docs}
%package -n %{pypi_name}-doc
Summary:        %{pypi_name} documentation
BuildArch:      noarch
Requires:       python3-docs

%description -n %{pypi_name}-doc
Documentation for %{pypi_name}.
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif
# Add missing license file
cp %SOURCE1 .

%build
# verbose build
V=1 %py3_build

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install
mkdir -p %{buildroot}%{_datadir}/drgn
cp -PR examples tools %{buildroot}%{_datadir}/drgn

%if %{with tests}
%check
%pytest
%endif

%files -n %{pypi_name}
%license COPYING
%doc README.rst
%{_bindir}/drgn
%{_datadir}/drgn
%{python3_sitearch}/_%{pypi_name}.pyi
%{python3_sitearch}/_%{pypi_name}.cpython*.so
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n %{pypi_name}-doc
%license COPYING
%doc html
%endif

%changelog
* Tue Apr  6 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.0.11-2
- Make doc subpackage noarch
- Add license file

* Tue Apr  6 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.0.11-1
- Initial package.
