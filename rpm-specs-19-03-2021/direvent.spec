Name:           direvent
Version:        5.2
Release:        1%{?dist}
Summary:        GNU directory event monitoring daemon

License:        GPLv3+
URL:            https://www.gnu.org.ua/software/direvent
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-325F650C4C2B6AD58807327A3602B07F55D0C732.gpg

BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  gnupg2
BuildRequires:  texinfo

%description
GNU Direvent monitors events in the file system directories. For each
event that occurs in a set of pre-configured directories, the program
calls an external program associated with it, supplying it with the
information about the event and the location within the file system
where it occurred.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man5/direvent.conf.5*
%{_mandir}/man8/direvent.8*

%changelog
* Sun Oct 11 15:14:27 UTC 2020 Rafael Fontenelle <rafaelff@gnome.org> - 5.2-1
- Initial package
