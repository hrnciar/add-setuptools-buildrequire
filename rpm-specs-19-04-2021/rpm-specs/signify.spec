Name:     signify
Version:  30
Release:  3%{?dist}
Summary:  Sign and encrypt files

License:  ISC and MIT and BSD
URL:      https://github.com/aperezdc/%{name}
Source0:  %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  libbsd-devel
BuildRequires:  gcc
BuildRequires:  make

%description
Sign and verify signatures on files, as used by the OpenBSD release maintainers.

%prep
# remove upstream bundled optional library libwaive from source
%autosetup
rm -rf libwaive

%build
%set_build_flags
export LD=ld
%make_build

%check
%{__make} check


%install
%make_install PREFIX=%{_prefix}


%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/signify
%{_mandir}/man1/signify.*

%changelog
* Sun Feb 28 2021 Marcus Müller <marcus@hostalia.de> - 30-3
- Fixed License tag
- rid of unescaped macros in %%changelog

* Wed Feb 24 2021 Marcus Müller <marcus@hostalia.de> - 30-2
- enable tests

* Wed Feb 24 2021 Marcus Müller <marcus@hostalia.de> - 30-1
- Bump upstream version
- Include the upstreamed license file
- Add newlines to changelog
- set LD explicitly (thanks sagitter)

* Sat Jan 11 2020 Marcus Müller <marcus@hostalia.de> - 27-2
- removed bundled library libwaive from source

* Fri Jan 10 2020 Marcus Müller <marcus@hostalia.de> - 27-1
- updated to release v27
- prepared `%%check` for as soon as regression tests are released
- fixed `%%set_build_flags` (thanks Antonio <anto.trande@gmail.com>)
- proper _prefix (thanks Vít Ondruch <vondruch@redhat.com>)

* Fri Nov 01 2019 Marcus Müller <marcus@hostalia.de> - 26-1
- Initial import
