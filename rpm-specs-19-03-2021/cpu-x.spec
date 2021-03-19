Name:           cpu-x
Version:        4.1.0
Release:        3%{?dist}
Summary:        Gathers information on CPU, motherboard and more
ExclusiveArch:  i686 x86_64

License:        GPLv3+
URL:            https://github.com/X0rg/CPU-X
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# dmidecode: apply upstream patch
Patch0:         https://github.com/X0rg/CPU-X/commit/23de736465a14cf31191afd64a245e35c7542665.patch#/dmidecode-apply-upstream-patch.patch

# CMake: disable format-security for dmidecode
Patch1:         https://github.com/X0rg/CPU-X/commit/0d79f3ef545660075d9cb396396046ef11872d1b.patch#/cmake-disable-format-security-for-dmidecode.patch

# Removed potentially dangerous compiler flags.
Patch2:         https://github.com/X0rg/CPU-X/commit/4b6fa113ede304e660d4c4f14c51b85a6172a5c2.patch#/removed-potentially-dangerous-compiler-flags.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  nasm
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcpuid) >= 0.4.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(ncursesw)

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme

# https://github.com/X0rg/CPU-X/issues/105
Provides:       bundled(bandwidth) = 1.5.1
Provides:       bundled(dmidecode) = 3.3

%description
Free software that gathers information on CPU, motherboard and more.

CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.

This software is written in C and built with CMake tool. It can be used in
graphical mode by using GTK or in text-based mode by using NCurses. A dump
mode is present from command line.


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


%prep
%autosetup -n CPU-X-%{version} -p1


%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build


%install
%cmake_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/384x384

# invalid-lc-messages-dir
rm -r %{buildroot}%{_datadir}/locale/zh_Hant/

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/polkit-1/actions/org.%{name}-daemon.policy
%{_datadir}/zsh/site-functions/_%{name}
%{_libexecdir}/%{name}-daemon
%{_metainfodir}/*.appdata.xml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions

%files data
%{_datadir}/%{name}/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 4.1.0-2
- build: dmidecode - apply upstream patch & remove -Wno-format-security flag

* Sun Jan 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 4.1.0-1
- build(update): 4.1.0

* Sun Dec 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.1-5
- Rebuild | Fix RH#1911068

* Wed Sep  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.1-4
- Rebuild | Fix RH#1871467

* Mon Jul 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.1-3
- Rebuild with out-of-source builds new CMake macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.1-1
- Update to 4.0.1

* Sun May 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Sun May 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.0-0.1rc1
- Update to 4.0.0-rc1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-6.20191114gitfa0fe58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.4-5.20191114gitfa0fe58
- Add exclusive arches

* Thu Nov 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.4-4.20191114gitfa0fe58
- Update to latest git snapshot

* Wed Nov 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.4-3.20191106gite8cb544
- Format-Security fix

* Wed Nov 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.4-2.20191106gite8cb544
- Update to latest git snapshot
- Packaging fixes

* Sat Aug 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.4-7.20190806git11158d2
- Initial package