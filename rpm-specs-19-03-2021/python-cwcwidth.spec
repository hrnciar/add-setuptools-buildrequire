Summary:        Python bindings for wc(s)width
Name:           python-cwcwidth
Version:        0.1.4
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/sebastinas/cwcwidth
Source0:        %{pypi_source cwcwidth}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.28
BuildRequires:  python3dist(setuptools)
%global _description \
Python bindings for wc(s)widthcwcwidth provides Python bindings for \
wcwidth and wcswidth functions defined in POSIX.1-2001 and \
POSIX.1-2008 based on Cython . These functions compute the printable \
length of a unicode character/string on a terminal.
%description %_description

%package     -n python3-cwcwidth
Summary:        %{summary}
%{?fc32:%py_provides python3-cwcwidth}
%description -n python3-cwcwidth %_description

%prep
%autosetup -n cwcwidth-%{version}
rm -rf cwcwidth.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-cwcwidth
%license LICENSE
%doc README.md
%{python3_sitearch}/cwcwidth
%{python3_sitearch}/cwcwidth-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Mar 11 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1.4-2
- Fix license and source tags

* Mon Mar 08 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1.4-1
- 0.1.4
- Fix python provide for Fedora 32

* Sun Feb 07 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1.2-1
- 0.1.2

* Tue Jan 26 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1-1
- initial package
