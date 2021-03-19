%{!?_iconsbasedir: %global _iconsbasedir %{_datadir}/icons/hicolor}
%{?rhel: %global cmake %cmake3}

Name:           freedv
Version:        1.4
Release:        6%{?dist}
Summary:        FreeDV Digital Voice
License:        GPLv2+

URL:            http://freedv.org
Source0:        https://github.com/drowe67/freedv-gui/archive/v%{version}/%{name}-%{version}.tar.gz

Source100:      freedv.appdata.xml
Source101:      freedv48x48.png
Source102:      freedv64x64.png
Source103:      freedv128x128.png
Source104:      freedv256x256.png

# Get some AVX detection improvements since the 1.4 release.
Patch0:         freedv-master.patch

BuildRequires:  cmake%{?rhel:3} gcc-c++
BuildRequires:  wxGTK3-devel
BuildRequires:  codec2-devel >= 0.8
BuildRequires:  lpcnetfreedv-devel
BuildRequires:  portaudio-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
%if 0%{?fedora}
BuildRequires:  libappstream-glib
BuildRequires:  speexdsp-devel
%else
BuildRequires:  speex-devel
%endif
BuildRequires:  hamlib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libao-devel
BuildRequires:  gsm-devel
BuildRequires:  desktop-file-utils 


%description
FreeDV is a GUI application for Windows and Linux that allows any SSB radio to
be used for low bit rate digital voice.

Speech is compressed down to 1400 bit/s then modulated onto a 1100 Hz wide QPSK
signal which is sent to the Mic input of a SSB radio. On receive, the signal is
received by the SSB radio, then demodulated and decoded by FreeDV.

FreeDV was built by an international team of Radio Amateurs working together on
coding, design, user interface and testing. FreeDV is open source software,
released under the GNU Public License version 2.1. The FDMDV modem and Codec 2
Speech codec used in FreeDV are also open source.


%prep
%autosetup -p1 -n freedv-gui-%{version}


%build
export CFLAGS="%{optflags} -fPIC -pie -Wl,-z,relro -Wl,-z,now"
export CXXFLAGS="%{optflags} -fPIC -pie -Wl,-z,relro -Wl,-z,now"
export LDFLAGS="-Wl,--as-needed"
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DWXCONFIG="%{_bindir}/wx-config-3.0" \
       -DWXRC="%{_bindir}/wxrc-3.0" \
       -DUSE_STATIC_SPEEXDSP=FALSE \
       ../

%cmake_build


%install
%cmake_install

# Install desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?fedora}
# install appdata file
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm 0644 %{SOURCE100} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/*.appdata.xml
%endif


%if 0%{?rhel} && 0%{?rhel} < 8
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif


%files
%license COPYING
%doc README.md USER_MANUAL.md
%{_bindir}/%{name}
%{?fedora:%{_datadir}/appdata/*.appdata.xml}
%{_datadir}/applications/%{name}.desktop
%{_iconsbasedir}/*/apps/%{name}.png


%changelog
* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4-6
- Rebuild for hamlib 4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Richard Shaw <hobbes1069@gmail.com> - 1.4-2
- Rebuild with lpcnetfreedv.

* Thu Apr 16 2020 Richard Shaw <hobbes1069@gmail.com> - 1.4-1
- Update to 1.4.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.1-7
- Rebuild for hamlib 4.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Richard Shaw <hobbes1069@gmail.com> - 1.3.1-3
- Rebuild for hamlib 3.3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Richard Shaw <hobbes1069@gmail.com> - 1.3.1-1
- Update to 1.3.1.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Richard Shaw <hobbes1069@gmail.com> - 1.2.2-1
- Update to latest upstream release.

* Tue Feb 21 2017 Richard Shaw <hobbes1069@gmail.com> - 1.2-1
- Update to latest upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Richard Shaw <hobbes1069@gmail.com> - 1.1-5
- Update config.guess and config.sub in bundled sox.

* Wed Jan 20 2016 Richard Shaw <hobbes1069@gmail.com> - 1.1-4
- Create appdata file.

* Tue Dec  8 2015 Richard Shaw <hobbes1069@gmail.com> - 1.1-3
- Add sox to sources so it is not downloaded during the build.
- Add necessary build flags for RELO and PIE.

* Fri Dec  4 2015 Richard Shaw <hobbes1069@gmail.com> - 1.1-2
- Move to bundled sox to work around now private function in 14.4.2.

* Thu Sep 24 2015 Richard Shaw <hobbes1069@gmail.com> - 1.1-1
- Update to latest upstream release.

* Tue Aug 25 2015 Richard Shaw <hobbes1069@gmail.com> - 1.0-1
- Update to latest upstream release.

* Sat Jul  4 2015 Richard Shaw <hobbes1069@gmail.com> - 0.98.0-1
- Update to latest upstream release.

* Sun May 31 2015 Richard Shaw <hobbes1069@gmail.com> - 0.97.0-3
- Update to latest svn checkout.

* Tue Jun 17 2014 Richard Shaw <hobbes1069@gmail.com> - 0.97.0-1
- Update to latest upstream release.

* Sat May 24 2014 Richard Shaw <hobbes1069@gmail.com> - 0.96.7-1
- Latest release.

* Fri Mar 28 2014 Richard Shaw <hobbes1069@gmail.com> - 0.96.5-5
- Update to later svn checkout, 1481.

* Sun Mar 23 2014 Richard Shaw <hobbes1069@gmail.com> - 0.96.5-4
- Try test build with patch to remove libctb dependence.

* Sun Sep 15 2013 Richard Shaw <hobbes1069@gmail.com> - 0.96.5-3
- Update to latest checkout.

* Fri Apr 12 2013 Richard Shaw <hobbes1069@gmail.com> - 0.96-1
- Updated to lastest svn checkout (rev 1231).
- Updated spec to meet Fedora Packaging Guidelines.
- Created new icon and desktop files
- Implemented cmake based build configuration.

* Sun Dec 23 2012 Mike Heitmann <mheitmann@n0so.net> 0.91-3
- Made libctb, wxWidgets, codec2 separate rpm packages

* Sat Dec 22 2012 Mike Heitmann <mheitmann@n0so.net> 0.91-2
- Updated spec to use %%{_libdir} and %%{_bindir} macros

* Sun Dec 16 2012 Mike Heitmann <mheitmann@n0so.net> 0.91-1
- Initial SPEC

