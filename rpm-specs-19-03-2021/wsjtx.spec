#global rctag rc4

Name:           wsjtx
Version:	    2.3.0
Release:	    1%{?dist}
Summary:	    Weak Signal communication by K1JT
License:	    GPLv3+

URL:		    http://physics.princeton.edu/pulsar/k1jt/wsjtx.html
Source0:	    http://physics.princeton.edu/pulsar/k1jt/%{name}-%{version}%{?rctag:-%{rctag}}.tgz
Source100:	    wsjtx.appdata.xml

Patch0:		    wsjtx-2.0.0-compile-fix.patch

BuildRequires:	cmake
BuildRequires:	dos2unix
BuildRequires:	tar
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran

BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	desktop-file-utils
BuildRequires:	hamlib-devel
BuildRequires:	fftw-devel
BuildRequires:	libusbx-devel
%if 0%{?rhel}
BuildRequires:	boost169-devel
%else
BuildRequires:	boost-devel
%endif
BuildRequires:	portaudio-devel
%if 0%{?fedora}
BuildRequires:	asciidoc
BuildRequires:	rubygem-asciidoctor
BuildRequires:	libappstream-glib
%endif

%description
WSJT-X is a computer program designed to facilitate basic amateur radio
communication using very weak signals. It implements communication protocols
or "modes" called JT4, JT9, JT65, QRA64, ISCAT, MSK144, and WSPR, as well as
one called Echo for detecting and measuring your own radio signals reflected
from the Moon.


%prep
%setup -n %{name}-%{version}%{?rctag:-%{rctag}}

# remove bundled hamlib
rm -f src/hamlib*.tgz* src/hamlib*.tar.gz*
tar -xzf src/%{name}.tgz
%patch0 -p1

# remove archive
rm -f src/wsjtx.tgz*

cd %{name}

%if ! 0%{?rhel} < 8
# remove bundled boost. EL 7 is not required version.
rm -rf boost
%endif

# convert CR + LF to LF
dos2unix *.ui *.iss *.txt


%build
# The fortran code in this package is not type safe and will thus not work
# with LTO.  Additionally there are numerous bogus strncat calls that also
# need to be fixed for this package to work with LTO
%define _lto_cflags %{nil}

# Workaround for build with gcc-10, problem reported upstream
export CFLAGS="%{optflags} -fcommon"
export LDFLAGS="%{?__global_ldflags}"
# workaround for hamlib check, i.e. for hamlib_LIBRARY_DIRS not to be empty
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1

cd %{name}
%cmake -Dhamlib_STATIC=FALSE \
       -DBoost_NO_SYSTEM_PATHS=FALSE \
%if 0%{?rhel}
       -DBOOST_INCLUDEDIR=%{_includedir}/boost169 \
	   -DBOOST_LIBRARYDIR=%{_libdir}/boost169 \
       -DWSJT_GENERATE_DOCS=FALSE \
       -DWSJT_SKIP_MANPAGES=TRUE
%endif

%cmake_build


%install
cd %{name}
%cmake_install

# Make sure the right style is used.
desktop-file-edit --set-key=Exec --set-value="wsjtx --style=fusion" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
# desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/wsjtx.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/message_aggregator.desktop

%if 0%{?fedora}
# appdata file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE100} %{buildroot}%{_metainfodir}/
%endif

# fix docs
install -p -m 0644 -t %{buildroot}%{_datadir}/doc/%{name} GUIcontrols.txt jt9.txt \
  v1.7_Features.txt wsjtx_changelog.txt


%if 0%{?fedora}
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%endif


%files
%license COPYING
%doc %{_datadir}/doc/%{name}
%{_bindir}/fcal
%{_bindir}/fmeasure
%{_bindir}/fmtave
%{_bindir}/fst4sim
%{_bindir}/jt4code
%{_bindir}/jt65code
%{_bindir}/jt9
%{_bindir}/jt9code
%{_bindir}/ft8code
%{_bindir}/message_aggregator
%{_bindir}/msk144code
%{_bindir}/qra64code
%{_bindir}/qra64sim
%{_bindir}/udp_daemon
%{_bindir}/wsjtx
%{_bindir}/wsjtx_app_version
%{_bindir}/wsprd
%{?fedora:%{_mandir}/man1/*.1.gz}
%{?fedora:%{_metainfodir}/*.xml}
%{_datadir}/applications/wsjtx.desktop
%{_datadir}/applications/message_aggregator.desktop
%{_datadir}/pixmaps/wsjtx_icon.png
%{_datadir}/%{name}


%changelog
* Wed Feb 03 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.0-1
- Update to 2.3.0 final.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.2-8
- Rebuild for hamlib 4.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.2-6
- Rebuilt for hamlib 4.0 release.

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.2-5
- Fixed FTBFS
  Resolves: rhbz#1865629

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 2.2.2-2
- Disable LTO

* Mon Jun 22 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.2-1
- Update to 2.2.2.

* Sat Jun 06 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-1
- Update to 2.2.1.

* Tue Jun 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.2-4
- Rebuilt with hamlib 4.0.

* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-3
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1800262

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.2-1
- Update to 2.1.2.

* Tue Nov 26 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-1
- Upate to 2.2.1.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-1
- Update to 2.1.0.

* Mon Feb 25 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.1-1
- Update to 2.0.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Richard Shaw <hobbes1069@gmail.com> - 2.0.0-8
- Update to 2.0.0 GA.

* Fri Sep 28 2018 Richard Shaw <hobbes1069@gmail.com> - 1.9.1-2
- Rebuild for hamlib 3.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Richard Shaw <hobbes1069@gmail.com> - 1.9.1-1
- Update to 1.9.1.
- Update compile patch to deal with qt5_use_modules no longer being available in
  rawhide/f29.

* Tue May 29 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-1
- New version
- Dropped gcc-8.0.1-compile-fix patch (not needed)

* Wed May  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-0.3.rc4
- New version
- De-fuzzified patches

* Wed Mar 21 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-0.2.rc3
- New version
- Updated gcc-8.0.1-compile-fix patch

* Fri Mar 16 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.0-0.1.rc2
- New version
- Fixed compilation with gcc-8.0.1
  Resolves: rhbz#1556544
- De-fuzzified compile-fix patch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-3
- Rebuilt for new fortran

* Fri Jan 19 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-2
- Do not force non-executable stack
  Resolves: rhbz#1535987
  Resolves: rhbz#1523446

* Mon Jan 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-1
- New version
  Resolves: rhbz#1534099
- De-fuzzified compile-fix patch

* Fri Sep  8 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-0.3.rc2
- Dropped rigctl*-wsjtx (hamlib copy)

* Sun Sep  3 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-0.2.rc2
- New version

* Fri Sep  1 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-0.1.rc1
- Initial version
