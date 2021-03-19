
%global debug_package %{nil}

Name:		mupen64plus
Version:	2.5
Release:	11%{?dist}

Summary:	Nintendo 64 Emulator
License:	GPLv2+ and CC-BY-SA
URL:		http://www.mupen64plus.org/
Source:		https://github.com/mupen64plus/mupen64plus-core/releases/download/2.5/mupen64plus-bundle-src-2.5.tar.gz
Patch1:		mupen64plus-multiple-definitions.patch
Patch2:		mupen64plus-make-archs.patch


BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(lirc)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	boost-devel
BuildRequires:	gzip
BuildRequires:	pkgconfig(glew)
BuildRequires:	binutils
BuildRequires:	gcc-c++

Requires:	hicolor-icon-theme

Conflicts:	mupen64plus-qt
Conflicts:	mupen64plus-cli

ExcludeArch:	s390x

%description
Mupen64plus is a Nintendo 64 Emulator.
This package includes all the plug-ins.

%package devel
Summary:	Development files for mupen64plus
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mupen64plus

%prep
%setup -q -n %{name}-bundle-src-%{version}
%patch1 -p1 -b.multipledefinitions
%patch2 -p1 -b.makearchs

# Need to avoid filename conflicts so they can be included in the package
cp -a source/mupen64plus-rsp-hle/LICENSES LICENSE-rsp-hle
cp -a source/mupen64plus-rom/mupen64plus/assets/LICENSES LICENSE-assets
cp -a source/mupen64plus-rom/LICENSES LICENSE-rom
cp -a source/mupen64plus-input-sdl/LICENSES LICENSE-input-sdl
cp -a source/mupen64plus-video-glide64mk2/LICENSES LICENSE-video-glide64mk2
cp -a source/mupen64plus-video-rice/LICENSES LICENSE-video-rice
cp -a source/mupen64plus-ui-console/LICENSES LICENSE-ui-console
cp -a source/mupen64plus-core/LICENSES LICENSE-core
cp -a source/mupen64plus-audio-sdl/LICENSES LICENSE-audio-sdl

%build

# Architecture build flags
ADDITIONAL_FLAGS=""
if [[ "$(uname -m)" = arm* ]] ; then
	ADDITIONAL_FLAGS="NEON=1 VFP_HARD=1 NO_SSE=1"
elif [[ "$(uname -m)" = aarch64 ]] ; then
	ADDITIONAL_FLAGS="NO_SSE=1"
elif [[ "$(uname -m)" = ppc* ]] ; then
	ADDITIONAL_FLAGS="NO_SSE=1"
fi

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
sh m64p_build.sh LIRC=1 $ADDITIONAL_FLAGS

%install

# NOTE: set LDCONFIG to true so it's not run during this script
./m64p_install.sh DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir} LIBDIR=%{_libdir} DEBUG=1 LDCONFIG='true'
find %{buildroot}%{_libdir} -type f -name "*.so*" -exec chmod 0755 "{}" \;

# NOTE: The build system should probably create this...
ln -sf %{_libdir}/libmupen64plus.so.2.0.0 %{buildroot}%{_libdir}/libmupen64plus.so

desktop-file-validate %{buildroot}/%{_datadir}/applications/mupen64plus.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_libdir}/libmupen64plus.so.2
%{_libdir}/libmupen64plus.so.2.0.0
%{_datadir}/%{name}/
%{_datadir}/applications/mupen64plus.desktop
%{_datadir}/icons/hicolor/48x48/apps/mupen64plus.png
%{_datadir}/icons/hicolor/scalable/apps/mupen64plus.svg
%{_mandir}/man6/mupen64plus.6.gz
%license LICENSE-rsp-hle LICENSE-assets LICENSE-rom LICENSE-input-sdl LICENSE-video-glide64mk2 LICENSE-video-rice LICENSE-core LICENSE-audio-sdl


%files devel
%{_includedir}/mupen64plus/
%{_libdir}/libmupen64plus.so

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.5-10
- Rebuilt for Boost 1.75

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 2.5-8
- Rebuilt for Boost 1.73

* Mon May 25 2020 Wade Berrier <wberrier@gmail.com> - 2.5-7
- Fix builds on arm, aarch64, and ppc64le

* Sun May 24 2020 Wade Berrier <wberrier@gmail.com> - 2.5-6
- Fix build with gcc 10

* Sat Apr 25 2020 Wade Berrier <wberrier@gmail.com> - 2.5-5
- Add gcc-c++ to BuildRequires

* Sat Jan 27 2018 Wade Berrier <wberrier@gmail.com> - 2.5-4
- Additional updates for Fedora package review (#1535549)

* Sat Jan 20 2018 Wade Berrier <wberrier@gmail.com> - 2.5-3
- Various updates for Fedora package review (#1535549)

* Thu Jan 11 2018 Wade Berrier <wberrier@gmail.com> - 2.5-2
- Update homepage url
- Remove references to nonexistant gtk gui
- add lirc build option
- split out devel package

* Fri Oct 02 2015 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 2.5-1
- Updated to 2.5

* Fri Jul 04 2014 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 2.0-6
- Excluded innecesary sources

* Fri Nov 22 2013 David Vasquez <davidjeremias82[AT]gmail [DOT] com> - 2.0-5
- Added Modules Input SDL

* Wed Sep 25 2013 David Vasquez <davidjeremias82[AT]gmail [DOT] com> - 2.0-4
- Initial build rpm
