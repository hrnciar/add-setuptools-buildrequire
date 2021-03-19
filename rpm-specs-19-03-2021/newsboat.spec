# Not all test dependencies are packaged for fedora
%bcond_with check

Name:    newsboat
Version: 2.22.1
Release: 1%{?dist}
Summary: RSS/Atom feed reader for the text console

License: MIT
URL:     https://www.newsboat.org
Source0: https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz
Source1: https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2: https://newsboat.org/newsboat.pgp

Patch:  0001-make-do-not-require-Cargo.lock.patch
Patch:  0002-libnewsboat-relax-backtrace-requirements.patch

# Source file verification
BuildRequires: make
BuildRequires: gnupg2

BuildRequires: asciidoctor
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: pkgconfig(json-c) >= 0.11
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(stfl)
# Rust parts
BuildRequires:  git
BuildRequires:  rust-packaging

Provides: podboat = %{version}-%{release}

%description
Newsboat is a fork of Newsbeuter, an RSS/Atom feed reader for the text console.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
%cargo_prep
# Remove executable bit from example scripts
find contrib/ -type f -exec chmod -x '{}' +

%generate_buildrequires
INTERNAL_CRATES=$'libnewsboat\nlibnewsboat-ffi\nregex-rs\nstrprintf'

find rust/ -type f -name Cargo.toml|while read -r manifest
do
    cargo-inspector --all-features -BR "${manifest}"|grep -vwe "${INTERNAL_CRATES}"
%if %{with check}
    cargo-inspector --all-features -TR "${manifest}"|grep -vwe "${INTERNAL_CRATES}"
%endif
done

%build
# Respect RPM settings
%set_build_flags
# Do not fail build because our GCC emits different warnings
export CFLAGS="-Wno-error ${CFLAGS}" CXXFLAGS="-Wno-error ${CXXFLAGS}"
# CARGO_BUILD_FLAGS is used/appended to by this Makefile
export CARGO_BUILD_FLAGS="%{__cargo_common_opts}"

# Verify non-rust deps and setup LDFLAGS
sh config.sh

# Build the project
# Replace bare `cargo` with the one used by %%cargo_* macros
%make_build CARGO="%{__cargo}" all %{?with_check:test}

%install
%make_install prefix="%{_prefix}"

%find_lang %{name}

%check
%if %{with check}
# TMPDIR=%%{_tmppath} ./test/test  # Have issues with permission in tpmdir
%cargo_test
%endif

%files -f %{name}.lang
%license LICENSE
%doc README.md

%{_bindir}/newsboat
%{_bindir}/podboat

%{_mandir}/man1/newsboat.1*
%{_mandir}/man1/podboat.1*
%{_pkgdocdir}
%{_datadir}/icons/hicolor/scalable/apps/newsboat.svg

%changelog
* Mon Feb 22 2021 Jan Staněk <jstanek@redhat.com> - 2.22.1-1
- Upgrade to version 2.22.1
- Switch to generate_buildrequires for rust dependencies

* Tue Feb 02 2021 Jan Staněk <jstanek@redhat.com> - 2.21-4
- Fix clap dependency constraints

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:26:17 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.21-2
- Rebuild

* Tue Oct 20 2020 Jan Staněk <jstanek@redhat.com> - 2.21-1
- Upgrade to version 2.21

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jan Staněk <jstanek@redhat.com> - 2.20.1-1
- Upgrade to version 2.20.1

* Mon Jun 22 2020 Jan Staněk <jstanek@redhat.com> - 2.20-1
- Upgrade to version 2.20, remove upstreamed patches
- Enable source GPG signature verification

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.19-3
- Rebuild (json-c)

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 2.19-2
- Add support for upcoming json-c 0.14.0

* Mon Mar 23 2020 Jan Staněk <jstanek@redhat.com> - 2.19-1
- Upgrade to version 2.19

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Jan Staněk <jstanek@redhat.com> - 2.17.1-1
- Upgrade to version 2.17.1

* Mon Sep 23 2019 Jan Staněk <jstanek@redhat.com> - 2.17-1
- Upgrade to version 2.17

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jan Staněk <jstanek@redhat.com> - 2.16.1-2
- Import upstream fix for evaluated commands in configuration comments

* Thu Jun 27 2019 Jan Staněk <jstanek@redhat.com> - 2.16.1-1
- Upgrade to version 2.16.1
- Add %%check section

* Mon Mar 25 2019 Jan Staněk <jstanek@redhat.com> - 2.15-1
- Upgrade to version 2.15

* Mon Feb 18 2019 Jan Staněk <jstanek@redhat.com> - 2.14.1-1
- Upgrade to version 2.14.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Lee Keitel <keitellf@fedoraproject.org> - 2.12-1
- Bumped version to 2.12

* Wed Jun 13 2018 Lee Keitel <keitellf@fedoraproject.org> - 2.11.1-1
- Initial version 2.11.1
