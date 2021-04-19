Name:             gawk-xml
Summary:          XML support for gawk
Version:          1.1.1
Release:          9%{?dist}
License:          GPL+ and GPLv3+

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
# rpmbuild finds the expat dependency automatically
#Requires:        expat
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    gawkextlib-devel
BuildRequires:    expat-devel

# Make sure the API version is compatible with our source code:
BuildRequires:    gawk(abi) >= 1.1
BuildRequires:    gawk(abi) < 4.0
BuildRequires: make

# At runtime, the ABI must be compatible with the compile-time version
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')

# This is the default as of Fedora 23:
%global _hardened_build 1

%description
%{name} provides the gawk XML extension module, as well as the xmlgawk script
and some gawk include libraries for enhanced XML processing.

# =============================================================================

%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

# The */dir file is not necessary for info pages to work correctly...
rm -f %{buildroot}%{_infodir}/dir

# Install NLS language files:
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS
%doc *.xml
%{_infodir}/*.info*
%{_libdir}/gawk/xml.so
%{_bindir}/xmlgawk
%{_datadir}/awk/*
%{_mandir}/man1/*
%{_mandir}/man3/*

# =============================================================================

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.1-5
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5 major
  api version 3

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.1.1-4
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Andrew J. Schorr <ajschorr@fedoraproject.org> - 1.1.1-1
- Upgrade to release 1.1.1 containing minor packaging fixes
- Remove Requires: expat, since rpmbuild finds this dependency automatically
- Add BuildRequires: gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.0-1
- Update to new upstream release with support for gawk API version 2

* Sat Jul 23 2016 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.7-1
- Rebuilt for new release

* Thu Oct 30 2014 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.0-1
- Now packaged as a separate rpm.

* Fri Aug 31 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.3.9-1
- Update a few obsolete references to xmlgawk to say gawkextlib.

* Sun Jul 22 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.3.0-1
- Rename from gawklib to gawkextlib.

* Sat Jul 21 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.2.0-1
- This version has been tested and should work.

* Thu Jul 19 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.1.9-1
- Initial packaging.  This has not been tested and almost certainly contains
  errors.
