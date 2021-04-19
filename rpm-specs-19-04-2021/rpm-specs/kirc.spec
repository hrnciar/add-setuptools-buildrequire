Name:           kirc
Version:        0.2.6
Release:        1%{?dist}
Summary:        Tiny IRC client written in POSIX C99

License:        MIT
URL:            https://github.com/mcpcpc/kirc
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
kirc ("KISS for IRC") is a tiny open-source Internet Relay Chat (IRC) client
designed with usability and cross-platform compatibility in mind.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README
%{_bindir}/kirc
%{_mandir}/man1/kirc.1*

%changelog
* Wed Apr 07 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Fri Mar 19 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.5-1
- New upstream release
- Update build requires

* Fri Mar  5 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.4-1
- New upstream release

* Mon Jan 25 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.3-2
- Update tarball URL
- Use set_build_flags macro
- Do not assume man pages will be gzipped

* Sun Jan 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.3-1
- Initial package
