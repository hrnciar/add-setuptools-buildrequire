Name:           sdorfehs
Version:        1.1
Release:        2%{?dist}
Summary:        A tiling window manager

License:        GPLv2
URL:            https://github.com/jcs/sdorfehs
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Makefile: Add support for DESTDIR
Patch0:         %{url}/commit/b17b0eb1d44c8a52828d1a0707fc66fff3e2606d.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel

%description
sdorfehs (pronounced "starfish") is a tiling window manager descended from
ratpoison (which itself is modeled after GNU Screen).

sdorfehs divides the screen into one or more frames, each only displaying one
window at a time but can cycle through all available windows (those which are
not being shown in another frame).

Like Screen, sdorfehs primarily uses prefixed/modal key bindings for most
actions. sdorfehs's command mode is entered with a configurable keystroke which
then allows a number of bindings accessible with just a single keystroke or any
other combination.

%prep
%autosetup
# Do not strip binaries on install so we can get debuginfo
sed -e 's/install -s/install -p/' -i Makefile
# Convert AUTHORS to UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.utf8
touch -r AUTHORS AUTHORS.utf8
mv AUTHORS.utf8 AUTHORS

%build
%set_build_flags
%make_build

%install
export PREFIX="%{_prefix}"
%make_install MANDIR="%{buildroot}%{_mandir}/man1"

%files
%license COPYING
%doc README.md AUTHORS
%{_bindir}/sdorfehs
%{_mandir}/man1/sdorfehs.1*

%changelog
* Wed Mar 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.1-2
- Update build requires
- Preserve timestamps when installing
- Convert AUTHORS to UTF-8

* Sat Mar 13 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.1-1 
- Initial package
