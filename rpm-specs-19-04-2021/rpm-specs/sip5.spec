%global pypi_name sip

Name:           sip5
Version:        5.5.0
Release:        2%{?dist}
Summary:        SIP - Python/C++ Bindings Generator
%py_provides    python3-sip5

# code_generator/parser.{c.h} is GPLv2+ with exceptions (bison)
License:        (GPLv2 or GPLv3) and (GPLv2+ with exceptions)
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%global _description %{expand:
SIP is a collection of tools that makes it very easy to create Python bindings
for C and C++ libraries.  It was originally developed in 1998 to create PyQt,
the Python bindings for the Qt toolkit, but can be used to create bindings for
any C or C++ library.  For example it is also used to generate wxPython, the
Python bindings for wxWidgets.}

%description %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install


%files
%doc README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_bindir}/sip*
%{python3_sitearch}/sip-*
%{python3_sitearch}/sipbuild/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec  6 09:03:55 EST 2020 Scott Talbert <swt@techie.net> - 5.5.0-1
- Update to new upstream release 5.5.0 (#1904676)

* Wed Oct 14 2020 Scott Talbert <swt@techie.net> - 5.4.0-1
- Initial package.
