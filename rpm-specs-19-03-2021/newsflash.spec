%global __cargo_skip_build 0

Name:           newsflash
Version:        1.3.0
Release:        1%{?dist}
Summary:        Modern feed reader

# 0BSD or MIT or ASL 2.0
# ASL 2.0
# ASL 2.0 or Boost
# ASL 2.0 or MIT or MPLv2.0
# BSD
# GPLv3+
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
# Unlicense
# Unlicense or MIT
# zlib
License:        GPLv3+ and BSD and ASL 2.0 and MIT and Unlicense and zlib
URL:            https://gitlab.com/news-flash/news_flash_gtk
Source0:        %{url}/-/archive/%{version_no_tilde}/news_flash_gtk-%{version_no_tilde}.tar.bz2

# replace news-flash and diffus git dependencies with proper versions
Patch0:         newsflash-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
A modern feed reader designed for the GNOME desktop. NewsFlash is a program
designed to complement an already existing web-based RSS reader account.

It combines all the advantages of web based services like syncing across all
your devices with everything you expect from a modern desktop program:
Desktop notifications, fast search and filtering, tagging, handy keyboard
shortcuts and having access to all your articles as long as you like.

%prep
%autosetup -n news_flash_gtk-%{version_no_tilde} -p1
# We will build by cargo ourselves
sed -i -e '/\(build_by_default\|install\)/s/true/false/' src/meson.build
sed -i -e '/dependency/d' meson.build
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'meson'
echo '/usr/bin/appstream-util'
echo '/usr/bin/desktop-file-validate'

%build
%meson
%meson_build
export FEEDLY_CLIENT_ID="boutroue"
export FEEDLY_CLIENT_SECRET="FE012EGICU4ZOBDRBEOVAJA1JZYH"
export PASSWORD_CRYPT_KEY="ypsSXCLhJngks9qGUAqShd8JjRaZ824wT3e"
export MERCURY_PARSER_USER="newsflash"
export MERCURY_PARSER_KEY="R4qcKEHpr9RTq6YuRAPkm9kMhjp4GuxiWG44VDk3Na4ZsN7F"
%cargo_build

%install
%meson_install
%cargo_install
mv %{buildroot}%{_bindir}/{news_flash_gtk,com.gitlab.newsflash}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.gitlab.newsflash.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.gitlab.newsflash.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/com.gitlab.newsflash
%{_datadir}/applications/com.gitlab.newsflash.desktop
%{_datadir}/icons/hicolor/*/apps/com.gitlab.newsflash*
%{_datadir}/metainfo/com.gitlab.newsflash.appdata.xml

%changelog
* Mon Mar 08 2021 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Update to version 1.3.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-3
- Update color-backtrace to 0.5

* Mon Dec 28 13:26:28 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-2
- Rebuild

* Sat Dec 26 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Fri Oct 09 2020 Jan Staněk <jstanek@redhat.com> - 1.0.5-3
- Bump gettext-rs dependency to 0.5

* Fri Sep 11 2020 Josh Stone <jistone@redhat.com> - 1.0.5-2
- Update to

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0~rc1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0~rc1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Josh Stone <jistone@redhat.com> - 1.0~rc1-6
- Update gtk-rs

* Sat Jun 13 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-5
- Add secrets for various services

* Sat Jun 13 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-4
- Make copying text with keyboard possible

* Fri Jun 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-3
- Backport fix for 32bit platforms
- Update fix for missing icon in GNOME Shell

* Fri Jun 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-2
- Fixup showing icon

* Sun Jun 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-1
- Initial package
