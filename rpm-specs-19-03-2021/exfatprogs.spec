Name:           exfatprogs
Version:        1.0.4
Release:        2%{?dist}
Summary:        Userspace utilities for exFAT filesystems
License:        GPLv2
URL:            https://github.com/%{name}/%{name}

Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
Utilities for formatting and repairing exFAT filesystems.

%prep
%autosetup

%build
autoreconf -vif
%configure \
    --enable-shared=yes \
    --enable-static=no
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_sbindir}/fsck.exfat
%{_sbindir}/mkfs.exfat
%{_sbindir}/tune.exfat
%{_mandir}/man8/fsck.exfat.*
%{_mandir}/man8/mkfs.exfat.*
%{_mandir}/man8/tune.exfat.*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Simone Caronni <negativo17@gmail.com> - 1.0.4-1
- Update to 1.0.4.

* Wed May 20 2020 Simone Caronni <negativo17@gmail.com> - 1.0.3-1
- Update to 1.0.3, no more shared libraries.

* Mon Apr 27 2020 Simone Caronni <negativo17@gmail.com> - 1.0.2-1
- Review fixes.
- Update to 1.0.2.

* Thu Apr 23 2020 Simone Caronni <negativo17@gmail.com> - 1.0.1-2
- Rename to exfatprogs.
- Removed provides/obsoletes on Fuse implementation.

* Wed Apr 15 2020 Simone Caronni <negativo17@gmail.com> - 1.0.1-1
- First build.
