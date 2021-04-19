Name:           oksh
Version:        6.8.1
Release:        2%{?dist}
Summary:        Portable OpenBSD ksh, based on the Public Domain Korn Shell

# The main license is "public domain", with some support files
# being under ISC and BSD license.
License:        Public Domain and ISC and BSD
URL:            https://github.com/ibara/%{name}
Source0:        https://github.com/ibara/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Default configuration file from the oksh-repository
Source1:        ksh.kshrc

# Makes it so that we can stop the configure-generated
# Makefile from stripping binaries in the `install`-target.
#
# This patch has been incorporate to upstream, and
# will get removed in the next stable release.
Patch0:         v6.8.1-stop-executable-strip.diff

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncursesw)

%description
Portable OpenBSD ksh, based on the Public Domain Korn Shell.

%prep
%autosetup

%build
%configure --no-strip
%make_build

%install
%make_install
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/ksh.kshrc

%post
if [ "$1" = 1 ]; then
    if [ ! -f %{_sysconfdir}/shells ] ; then
        echo "%{_bindir}/%{name}" > %{_sysconfdir}/shells
        echo "/bin/%{name}" >> %{_sysconfdir}/shells
    else
        grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells || echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells
        grep -q "^/bin/%{name}$" %{_sysconfdir}/shells || echo "/bin/%{name}" >> %{_sysconfdir}/shells
    fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
    sed -i '\!^%{_bindir}/%{name}$!d' %{_sysconfdir}/shells
    sed -i '\!^/bin/%{name}$!d' %{_sysconfdir}/shells
fi

%files
%license LEGAL
%doc NOTES README.md README.pdksh CONTRIBUTORS
%{_bindir}/oksh
%{_mandir}/man1/%{name}.1.*
%config(noreplace) %{_sysconfdir}/ksh.kshrc

%changelog
* Sun Apr 18 2021 Jani Juhani Sinervo <jani@sinervo.fi> - 6.8.1-2
- Add default configuration file
* Sat Apr 17 2021 Jani Juhani Sinervo <jani@sinervo.fi> - 6.8.1-1
- Initial packaging effort
