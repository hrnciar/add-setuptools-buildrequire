%bcond_without check
%global pypi_name zstandard
%if 0%{!?pytest:1}
%global pytest %{expand:\\\
  CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\\\
  PATH="%{buildroot}%{_bindir}:$PATH"\\\
  PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"\\\
  PYTHONDONTWRITEBYTECODE=1\\\
  /usr/bin/pytest}
%endif

%global desc This project provides Python bindings for interfacing with the Zstandard\
compression library. A C extension and CFFI interface are provided.

Name: python-%{pypi_name}
Version: 0.15.2
Release: 1%{?dist}
Summary: Zstandard bindings for Python
License: BSD and GPLv2
URL: https://github.com/indygreg/python-zstandard
Source0: %{pypi_source}
Patch0: %{name}-fix-estimated_compression_context_size-tolerance-i686.patch
Patch1: %{name}-issue-105.patch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: gcc
BuildRequires: libzstd-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-cffi
%if %{with check}
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
%endif
# https://github.com/indygreg/python-zstandard/issues/48
Provides: bundled(zstd) = 1.4.8

%description -n python3-%{pypi_name}
%{desc}

%prep
%setup -q -n %{pypi_name}-%{version}
%patch0 -p1
%patch1 -p1
rm -r %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
mv zstandard{,.src}
export ZSTD_SLOW_TESTS=1
%pytest -v\
        --numprocesses=auto
mv zstandard{.src,}
%endif

%files -n python3-%{pypi_name}
%license LICENSE zstd/COPYING
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pypi_name}

%changelog
* Mon Mar 01 2021 Dominik Mierzejewski <dominik@greysector.net> 0.15.2-1
- update to 0.15.2 (#1933476)
- fix tests on s390x

* Wed Feb 03 2021 Dominik Mierzejewski <dominik@greysector.net> 0.15.1-1
- update to 0.15.1 (#1924620)
- work around weird test failure
- fix tests on i686 and s390x

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Dominik Mierzejewski <dominik@greysector.net> 0.13.0-1
- initial build
- skip some tests on s390x (https://github.com/indygreg/python-zstandard/issues/105)

