%global api_vers 3.7

Name:           povray
Version:        3.7.0.8
Release:        10%{?dist}
Summary:        The Persistence of Vision Ray Tracer

# Examples below distribution/ are CC-BY-SA
# The sources are AGPLv3+
License:        AGPLv3+
URL:            http://povray.org
Source0:        https://github.com/POV-Ray/povray/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch1:         0001-Fix-encoding.patch
Patch2:         0002-Autotool-massaging.patch
Patch3:         0003-Remove-povuser.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  SDL-devel
BuildRequires:  libXpm-devel
BuildRequires:  autoconf automake

%description
POV-Ray is a free, full-featured ray tracer.

%package scenes
Summary:        POV-Ray example scenes
License:        CC-BY-SA
BuildArch:      noarch

%description scenes
POV-Ray example scenes.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Make sure not to be using bundled libs
rm -rf libraries

cd unix
sed -i \
 -e 's,automake --warnings=all,automake -a -f,' \
 prebuild.sh

./prebuild.sh
cd ..


%build
case x"%{?vendor}" in
xFedora\ Project ) # Building under Fedora's builders
  COMPILED_BY="%{vendor} <povray-owner@fedoraproject.org>"
  ;;
*) # elsewhere
  COMPILED_BY="%{?vendor:%vendor}%{!?vendor:$(id -u -n)}"
  ;;
esac

%configure --disable-silent-rules \
  --disable-optimiz --disable-strip \
  --x-includes=%{_includedir} --x-libraries=%{_libdir} \
  --with-boost-libdir=%{_libdir} \
  COMPILED_BY="${COMPILED_BY}"

# Filter out bogus and potentially harmful
# -I%%{_includedir} -L%%{_libdir}
# from Makefiles
find -name Makefile -exec sed -i \
  -e 's,-I%{_includedir}$,,g;s,-I%{_includedir} ,,g;' \
  -e 's,-L%{_libdir}$,,g;s,-L%{_libdir} ,,g' {} \;

# Adjust bogus paths
sed -i \
  -e '/DEFAULT_DIR=/d' \
  -e 's,SYSCONFDIR=\$DEFAULT_DIR/etc,SYSCONFDIR=%{_sysconfdir},' \
  unix/scripts/{allanim,allscene,portfolio}.sh

make %{?_smp_mflags}

%check
make check

%install
%make_install povdocdir=%{_pkgdocdir}

# Fixup permissions
chmod +x %{buildroot}%{_datadir}/povray-%{api_vers}/scenes/camera/mesh_camera/bake.sh

%files
%doc %{_pkgdocdir}
%{_bindir}/povray
%{_mandir}/man1/povray*
%{_datadir}/povray-%{api_vers}
%exclude %{_datadir}/povray-%{api_vers}/scenes
%dir %{_sysconfdir}/povray
%dir %{_sysconfdir}/povray/%{api_vers}
%config(noreplace) %{_sysconfdir}/povray/%{api_vers}/povray*

%files scenes
%dir %{_datadir}/povray-%{api_vers}
%{_datadir}/povray-%{api_vers}/scenes

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.7.0.8-9
- Rebuilt for Boost 1.75

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.7.0.8-8
- Rebuild for OpenEXR 2.5.3.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 3.7.0.8-6
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 3.7.0.8-3
- Rebuild for OpenEXR 2.3.0.

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 3.7.0.8-2
- Rebuilt for Boost 1.69

* Fri Jan 25 2019 Ralf Cors??pius <corsepiu@fedoraproject.org> - 3.7.0.8-1
- Update to 3.7.0.8.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Ralf Cors??pius <corsepiu@fedoraproject.org> - 3.7.0.7-2
- Once more rebuilt for Boost 1.66.

* Wed Jan 24 2018 Ralf Cors??pius <corsepiu@fedoraproject.org> - 3.7.0.7-1
- Upstream update.

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.7.0.4-2
- Rebuilt for Boost 1.66

* Tue Sep 26 2017 Ralf Cors??pius <corsepiu@fedoraproject.org> - 3.7.0.4-1
- Upstream update.
- Reflect upstream changes.
- Add 0003-Remove-povuser.patch.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-0.23.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-0.22.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.7-0.21.20131116git39ce8a2
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 3.7-0.20.20131116git39ce8a2
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-0.19.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-0.18.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.7-0.17.20131116git39ce8a2
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 3.7-0.16.20131116git39ce8a2
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Ralf Cors??pius <corsepiu@fedoraproject.org> - 3.7-0.15.20131116git39ce8a2
- Append -std=c++03 to CXXFLAGS (Workaround to F24FTBFS).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-0.14.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.7-0.13.20131116git39ce8a2
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.7-0.12.20131116git39ce8a2
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-0.11.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.7-0.10.20131116git39ce8a2
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-0.9.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.7-0.8.20131116git39ce8a2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.7-0.7.20131116git39ce8a2
- Rebuild for boost 1.57.0

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 3.7-0.6.20131116git39ce8a2
- rebuild (openexr)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-0.5.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-0.4.20131116git39ce8a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 3.7-0.3.20131116git39ce8a2
- Rebuild for boost 1.55.0

* Fri Jan 24 2014 Ralf Cors??pius <corsepiu@fedoraproject.org> - 3.7-0.2.20131116git39ce8a2
- Derive COMPILED_BY from %%vendor and id().

* Mon Jan 20 2014 Ralf Cors??pius <corsepiu@fedoraproject.org> - 3.7-0.1.20131116git39ce8a2
- Initial Fedora package.
