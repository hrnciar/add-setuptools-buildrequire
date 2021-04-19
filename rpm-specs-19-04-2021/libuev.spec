Name:           libuev
Version:        2.3.2
Release:        1%{?dist}
Summary:        Simple event loop for Linux

License:        MIT
URL:            https://github.com/troglobit/libuev
Source0:        https://github.com/troglobit/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         00TestMakefile.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make

%description
libuEv is a small event loop that wraps the Linux epoll() family
of APIs. It is similar to the more established libevent, libev 
and the venerable Xt(3) event loop. The µ in the name refers to 
both its limited feature set and the size impact of the library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for
developing application that use %{name}.

%prep
%setup -q

# CFLAGS used in tests/Makefile are hard coded, instead of
# using default cflags
# https://github.com/troglobit/libuev/issues/23
%patch0 -p0

# Reported upstream https://github.com/troglobit/libuev/issues/22
sed -i 's|AM_CONFIG_HEADER|AC_CONFIG_HEADERS|' configure.ac
./autogen.sh

%build
%configure --disable-static
%make_build

%check
make check

%install
%make_install

# examples directory: remove unuseful files
find examples -type f \( -name "Makefile*" -or -name ".gitignore" \) -exec rm -f {} ';'

# remove docs from buildroot
rm -rf %{buildroot}%{_docdir}/libuev

# remove something unnecessary
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%files
%license LICENSE
%doc README.md AUTHORS LICENSE ChangeLog.md
%{_libdir}/%{name}.so.2*

%files devel
%doc examples
%doc HACKING.md API.md
%{_includedir}/uev
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Mar 31 2021 Alessio <alessio@fedoraproject.org> - 2.3.2-1
- Initial RPM version
