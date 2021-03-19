%{?mingw_package_header}

Name:           mingw-SDL2_mixer
Version:        2.0.4
Release:        6%{?dist}
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

License:        zlib
URL:            http://www.libSDL.org/projects/SDL_mixer/
Source0:        http://www.libSDL.org/projects/SDL_mixer/release/SDL2_mixer-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw32-flac

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw64-flac

%description
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.


# Win32
%package -n mingw32-SDL2_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

%description -n mingw32-SDL2_mixer
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Win64
%package -n mingw64-SDL2_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

%description -n mingw64-SDL2_mixer
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n SDL2_mixer-%{version}


%build
%mingw_configure --disable-static
%mingw_make_build


%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-SDL2_mixer
%license COPYING.txt
%{mingw32_bindir}/SDL2_mixer.dll
%{mingw32_libdir}/libSDL2_mixer.dll.a
%{mingw32_libdir}/pkgconfig/SDL2_mixer.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_mixer
%license COPYING.txt
%{mingw64_bindir}/SDL2_mixer.dll
%{mingw64_libdir}/libSDL2_mixer.dll.a
%{mingw64_libdir}/pkgconfig/SDL2_mixer.pc
%{mingw64_includedir}/SDL2


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Thu Sep 27 2018 Kalev Lember <klember@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 2.0.1-1
- Update to 2.0.1
- Don't set group tags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 21 2014 maci <maci@satgnu.net> - 2.0.0-3
- Fix homepage URL

* Tue May 13 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-2
- Removed redundant BuildRequires

* Mon May 12 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-1
- Initial rpm
