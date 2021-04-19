Summary:        Library for accessing USB devices
Name:           libusb1
Version:        1.0.24
Release:        3%{?dist}
Source0:        https://github.com/libusb/libusb/releases/download/v%{version}/libusb-%{version}.tar.bz2
License:        LGPLv2+
URL:            http://libusb.info
BuildRequires:  systemd-devel doxygen libtool
BuildRequires:  make
BuildRequires:  gcc
# libusbx was removed in F34
Provides:       libusbx = %{version}-%{release}
Obsoletes:      libusbx < %{version}-%{release}

Patch001:       0001-linux_usbfs-Accept-sysfs-attributes-not-terminated-w.patch
Patch002:       0001-linux_usbfs-Fix-parsing-of-descriptors-for-multi-con.patch
Patch003:       0002-linux_usbfs-Gracefully-handle-buggy-devices-with-a-c.patch

%description
This package provides a way for applications to access USB devices.

libusb is a library for USB device access from Linux, macOS,
Windows, OpenBSD/NetBSD, Haiku and Solaris userspace.

libusb is abstracted internally in such a way that it can hopefully
be ported to other operating systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusbx-devel = %{version}-%{release}
Obsoletes:      libusbx-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package devel-doc
Summary:        Development files for %{name}
Requires:       libusb1-devel = %{version}-%{release}
Provides:       libusbx-devel-doc = %{version}-%{release}
Obsoletes:      libusbx-devel-doc < %{version}-%{release}
BuildArch:      noarch

%description devel-doc
This package contains API documentation for %{name}.


%package        tests-examples
Summary:        Tests and examples for %{name}
# The fxload example is GPLv2+, the rest is LGPLv2+, like libusb itself.
License:        LGPLv2+ and GPLv2+
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusbx-tests-examples = %{version}-%{release}
Obsoletes:      libusbx-tests-examples < %{version}-%{release}

%description tests-examples
This package contains tests and examples for %{name}.


%prep
%autosetup -p1 -n libusb-%{version}
chmod -x examples/*.c
mkdir -p m4


%build
%configure --disable-static --enable-examples-build
%{make_build}
pushd doc
make docs
popd
pushd tests
make
popd


%install
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 tests/.libs/stress $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
install -m 755 examples/.libs/testlibusb \
    $RPM_BUILD_ROOT%{_bindir}/libusb-test-libusb
# Some examples are very device-specific / require specific hw and miss --help
# So we only install a subset of more generic / useful examples
for i in fxload listdevs xusb; do
    install -m 755 examples/.libs/$i \
        $RPM_BUILD_ROOT%{_bindir}/libusb-example-$i
done
rm $RPM_BUILD_ROOT%{_libdir}/*.la


%check
LD_LIBRARY_PATH=libusb/.libs ldd $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-libusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-example-listdevs


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libusb-1.0.pc

%files devel-doc
%doc doc/api-1.0 examples/*.c

%files tests-examples
%{_bindir}/libusb-example-fxload
%{_bindir}/libusb-example-listdevs
%{_bindir}/libusb-example-xusb
%{_bindir}/libusb-test-stress
%{_bindir}/libusb-test-libusb


%changelog
* Tue Jan 19 18:47:55 CET 2021 Benjamin Berg <bberg@redhat.com> - 1.0.24-3
- New libusb1 package replacing libusbx
  Resolves: #1918269