Name:           progman
Version:        1.0
Release:        2%{?dist}
Summary:        Simple X11 window manager modeled after Program Manager

License:        MIT
URL:            https://github.com/jcs/progman
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  /usr/bin/xxd

%description
progman is a simple X11 window manager modeled after Program Manager from the
Windows 3 era. It is descended from aewm by Decklin Foster and retains its MIT
license.

%prep
%autosetup
# Do not strip binaries on install so we can get debuginfo
sed -e 's/install -s/install -p/' -i Makefile

%build
%set_build_flags
%make_build

%install
export PREFIX="%{buildroot}%{_prefix}"
%make_install

%files
%license LICENSE
%doc README.md progman.ini themes
%{_bindir}/progman

%changelog
* Thu Mar 18 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0-2
- Update build requires
- Preserve timestamps on install

* Sat Mar 13 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0-1
- Initial package
