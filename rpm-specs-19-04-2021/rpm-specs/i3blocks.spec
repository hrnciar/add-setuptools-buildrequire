Name:     i3blocks
Version:  1.5
Release:  2%{?dist}
Summary:  A feed generator for text based status bars
License:  GPLv3+
URL:      https://github.com/vivien/%{name}
Source:   %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

%description
A feed generator for text based status bars

i3blocks executes your command lines and generates a status line from
their output. Commands are scheduled at configured time intervals,
upon signal reception or on clicks.

The generated line is meant to be displayed by the i3 window manager
through its i3bar component, as an alternative to i3status.

i3blocks is meant to be highly flexible but intuitive. No library
package is required, just output what your status bar expects, from
your favorite programming language and your preferred format.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%install
%make_install
# these are useless in a i3bar/swaybar:
rm -rf %{buildroot}/usr/share/bash-completion

%files
%license COPYING

%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Mar 16 2021 Bob Hepple <bob.hepple@gmail.com> - 1.5-2
- rebuilt per RHBZ#1938637

* Mon Mar 15 2021 Bob Hepple <bob.hepple@gmail.com> - 1.5-1
- new version and duplicating abandoned RHBZ#1549011

* Mon Feb 26 2018 Alice Rum <irum@redhat.com> - 1.4-1
- Initial version of the package
