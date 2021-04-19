Name:           logitech-27mhz-keyboard-encryption-setup
Version:        0.1
Release:        1%{?dist}
Summary:        Logitech 27MHz keyboard encryption setup tool
License:        GPLv2+
URL:            https://gitlab.freedesktop.org/jwrdegoede/logitech-27mhz-keyboard-encryption-setup
Source0:        https://gitlab.freedesktop.org/jwrdegoede/logitech-27mhz-keyboard-encryption-setup/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  make gcc libusb1-devel

%description
A tool for enabling encryption on the 27 MHz wireless connection
used by some (somewhat older) Logitech keyboards.

%prep
%autosetup -n %{name}-v%{version}


%build
%make_build PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
%make_install PREFIX=%{_prefix}


%files
%doc README.md
%license LICENSE
%{_bindir}/lg-27MHz-keyboard-encryption-setup


%changelog
* Sun Apr  4 2021 Hans de Goede <hdegoede@redhat.com> - 0.1-1
- Initial Fedora package
