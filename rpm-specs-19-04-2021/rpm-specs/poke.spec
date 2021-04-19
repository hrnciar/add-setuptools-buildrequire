Summary:	Extensible editor for structured binary data
Name:		poke
Version:	1.0
Release:	4%{?dist}

# Documentation under GFDL
License:	GPLv3 and GFDL
URL:		http://www.jemarch.net/poke
Source0:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gc-devel
BuildRequires:	json-c-devel
BuildRequires:	libnbd-devel
# RHEL-8 doesn't have libtextstyle, check when 9 is released
%if 0%{?fedora}
BuildRequires:	libtextstyle-devel
%endif
BuildRequires:	make
BuildRequires:	readline-devel
# for check
BuildRequires:	dejagnu

Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

# bundles gnulib commit c9b44f214c7c798c7701c7a281584e262b263655
Provides:	bundled(gnulib) = 0-38.20210221git
# bundles jitter, should be packaged independently in the future
Provides:	bundled(jitter) = 0.9.258

%description
GNU poke is an interactive, extensible editor for binary data. Not
limited to editing basic entities such as bits and bytes, it provides
a full-fledged procedural, interactive programming language designed
to describe data structures and to operate on them.

%package	data
Summary:	Data files for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
%description	data
Data files for %{name}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	libs
Summary:	Library files for %{name}
%description	libs
Libraries for %{name}.

%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
%{make_install}
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/libpoke.a
rm -f %{buildroot}%{_libdir}/libpoke.la

%files
%{_bindir}/%{name}
%{_bindir}/pk-elfextractor
%{_infodir}/poke.info*.*
%{_mandir}/man1/*
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING

%files data
%{_datadir}/%{name}/

%files devel
%{_includedir}/libpoke.h
%{_libdir}/libpoke.so

%files libs
%{_libdir}/libpoke.so.0*
%license COPYING

%changelog
* Thu Mar 18 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0-4
- Check for libtextstyle only in Fedora, as it doesn't exist in RHEL

* Wed Mar 17 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0-3
- More changes for #1939271 review

* Wed Mar 17 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0-2
- Spec changes for #1939271 review

* Mon Mar 15 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0-1
- Initial version of the package
