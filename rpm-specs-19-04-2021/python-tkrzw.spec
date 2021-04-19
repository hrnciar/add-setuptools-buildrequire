%global	module	tkrzw

Name:		python-%{module}
Version:	0.1.4
Release:	2%{?dist}
License:	ASL 2.0
Summary:	TKRZW Python bindings
URL:		https://dbmx.net/tkrzw/
Source0:	https://dbmx.net/tkrzw/pkg-python/%{module}-python-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	python3-setuptools
# python3-devel
BuildRequires:	pkgconfig(python3)
# zlib-devel
#BuildRequires:	pkgconfig(zlib)
# tkrzw-devel
BuildRequires:	pkgconfig(tkrzw)
# python3-sphinx
BuildRequires:	python3dist(sphinx)
# https://bugzilla.redhat.com/show_bug.cgi?id=1920195
ExcludeArch:	%ix86

%description
TKRZW is a library of routines for managing a key-value database.

%package -n	python3-%{module}
Summary:	%{summary}
%if 0%{?epel} && 0%{?epel} < 9
%{?python_provide:%python_provide python3-%{module}}
%endif
%if 0%{?fedora} == 32
%py_provides python3-%{module}
%endif

%description -n	python3-%{module}
TKRZW is a library of routines for managing a key-value database.

%package	doc
Summary:	%{summary} - API documentation
BuildArch:	noarch

%description	doc
TKRZW is a library of routines for managing a key-value database.
This package contains API documentation of it.


%prep
%autosetup -n %{module}-python-%{version}


%build
%py3_build
%make_build apidoc


%install
%py3_install


%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%make_build check


%files -n python3-%{module}
%license COPYING
%{python3_sitearch}/Tkrzw-0.1-py%{python3_version}.egg-info
%if 0%{?epel} && 0%{?epel} < 9
%{python3_sitearch}/tkrzw.cpython-%{python3_version_nodots}m-*-linux-gnu*.so
%else
%{python3_sitearch}/tkrzw.cpython-%{python3_version_nodots}-*-linux-gnu*.so
%endif

%files doc
%license COPYING
%doc README CONTRIBUTING.md example?.py api-doc/

%changelog
* Sun Feb 14 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.4-2
- python_provide fix
- -doc subpackage added
- check introduced
- epel8 compatible

* Sat Feb 06 2021 TI_Eugene <ti.eugene@gmail.com> - 0.1.4-1
- Initial build
