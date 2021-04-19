%bcond_without tests

Name:           luminance-hdr
Version:        2.6.1.1
Release:        2%{?dist}
Summary:        GUI that provides a complete workflow for HDR imaging

# The entire source is GPLv2+, except:
#
# GPLv2:
#   src/HelpBrowser/schelptreemodel.{cpp,h}
#   src/HelpBrowser/treeitem.{cpp,h}
#   src/HelpBrowser/treemodel.{cpp,h}
#
# GPLv3+:
#   src/StopWatch.h
#   src/gauss.h
#   src/mytime.h
#   src/noncopyable.h
#   src/opthelper.h
#   src/Libpfs/rt_algo.{cpp,h}
#   src/MainCli/ezETAProgressBar.hpp
#
# LGPLv2+:
#   src/HdrCreation/fusionoperator.{cpp,h}
#   src/HdrCreation/weights.h
#   src/Libpfs/array2d.{hxx,h}
#   src/Libpfs/channel.{cpp,h}
#   src/Libpfs/fixedstrideiterator.h
#   src/Libpfs/frame.{cpp,h}
#   src/Libpfs/pfs.h
#   src/Libpfs/strideiterator.h
#   src/Libpfs/tag.{cpp,h}
#   src/Libpfs/colorspace/colorspace.{cpp,h}
#   src/Libpfs/exif/exifdata.{cpp,hpp}
#   src/Libpfs/manip/shift.{cpp,hxx,h}
#   src/Libpfs/utils/dotproduct.{hxx,h}
#   src/Libpfs/utils/minmax.{hxx,h}
#   src/Libpfs/utils/numeric.{hxx,h}
#
# BSD:
#   src/UI/FlowLayout.cpp
#
# MIT:
#   src/contrib/qtwaitingspinner/QtWaitingSpinner.{cpp,h}
#
# Boost: (see https://github.com/LuminanceHDR/LuminanceHDR/issues/239)
#   src/helpersse2.h
#   src/sleef.c
#   src/sleefsseavx.c
License:        GPLv2+ and GPLv2 and GPLv3+ and LGPLv2+ and BSD and MIT and Boost
# Additionally, the following are only build system files and do not contribute
# to the License field:
#
# Boost:
#   build_files/Modules/GetGitRevisionDescription.cmake{,.in}
URL:            http://qtpfsgui.sourceforge.net/
%global forgeurl https://github.com/LuminanceHDR/LuminanceHDR/
Source0:        %{forgeurl}/archive/v.%{version}/%{name}-%{version}.tar.gz
# https://github.com/LuminanceHDR/LuminanceHDR/issues/242
Source1:        %{name}.1
Source2:        %{name}-cli.1

# https://github.com/LuminanceHDR/LuminanceHDR/issues/239
Patch0:         %{name}-2.6.1.1-sleef-boost-license.patch
Patch1:         %{name}-2.6.1.1-external-librtprocess.patch

BuildRequires:  cmake
# We choose to use the ninja backend instead of the make backend. Either works.
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# INSTALL.md:
# To compile Luminance HDR your system will need a set of tools and code
# libraries called "dependencies". The following is a list of dependencies
# needed to compile the latest version of Luminance HDR:
# - [Qt5](https://www.qt.io/), the widget toolkit used by the graphical user interface (GUI).
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
BuildRequires:  qt5-qtwebengine-devel
%else
BuildRequires:  qt5-qtwebkit-devel
%endif
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
# - [Exiv2](https://www.exiv2.org/), used to read and write image metadata
#   (Exif, IPTC, XMP).
BuildRequires:  exiv2-devel
# - [Little CMS](http://www.littlecms.com/), LCMS2 is used for color
#   management.
BuildRequires:  lcms2-devel
# - [libjpeg-turbo](https://libjpeg-turbo.org/) (or libjpeg), used to read and
#   write JPEG files.
BuildRequires:  libjpeg-devel
# - [LibTIFF](http://www.libtiff.org/), used to read and write TIFF files.
BuildRequires:  libtiff-devel
# - [libpng](http://www.libpng.org/pub/png/libpng.html), used to read and write
#   PNG files.
BuildRequires:  libpng-devel
# - [LibRaw](https://www.libraw.org/), used to read raw files.
BuildRequires:  LibRaw-devel
# - [OpenEXR](http://www.openexr.com/), used to read and write high dynamic
#   range EXR files. Some distributions refer to the package as `ilmbase`.
BuildRequires:  OpenEXR-devel
# - [CFITSIO](https://heasarc.gsfc.nasa.gov/fitsio/), an optional library for
#   reading and writing FITS files, commonly used by the astrophotographer
#   community.
BuildRequires:  cfitsio-devel
# - [FFTW](www.fftw.org), used for computing discrete Fourier transforms.
#   Luminance HDR requires the single-precision "float" version of FFTW3,
#   usually called `fftw3f` or `fftw-3-single` on MacPorts.
BuildRequires:  fftw-devel
# - [Boost](https://www.boost.org/), a set of C++ support libraries.
BuildRequires:  boost-devel
# - [GNU Scientific Library](https://www.gnu.org/software/gsl/), GSL is used by
#   the Mantiuk08 tone mapping operator.
BuildRequires:  gsl-devel
# - [Eigen3](http://eigen.tuxfamily.org/), a C++ template library required by
#   by the Lischinski tone mapping operator.
BuildRequires:  eigen3-devel

BuildRequires:  librtprocess-devel

%if %{with tests}
BuildRequires:  gtest-devel
%endif

Obsoletes:      qtpfsgui < 2.2.0
Provides:       qtpfsgui = %{version}-%{release}

# https://github.com/LuminanceHDR/LuminanceHDR/issues/241
# Original version is unclear
Provides:       bundled(pfstools)
# Version based on searching commit messages for “pfstmo”; could be out of date.
Provides:       bundled(pfstmo) = 2.0.5

# A few routines from sleef are included; cannot build with upstream/system
# sleef as there are downstream modifications. It is not clear which version of
# sleef was used as the basis for the fork.
Provides:       bundled(sleef)

Requires:       %{name}-data = %{version}-%{release}

%global app_id net.sourceforge.qtpfsgui.LuminanceHDR

# Fixes linking errors while building tests, like:
#   /usr/bin/ld: /usr/bin/ld: DWARF error: could not find abbrev number 12736
#   /tmp/ccyQxX1y.ltrans0.ltrans.o: in function
#     `solve_pde_dct(pfs::Array2D<float>&, pfs::Array2D<float>&)':
#   <artificial>:(.text+0x4583): undefined reference to `init_fftw()'
%global _lto_cflags %{nil}

%description
Luminance HDR is a graphical user interface (based on the Qt5 toolkit) that
provides a complete workflow for HDR imaging.

Supported HDR formats:

  • OpenEXR (extension: exr)
  • Radiance RGBE (extension: hdr)
  • Tiff formats: 16bit, 32bit (float) and LogLuv (extension: tiff)
  • Raw image formats (extension: various)
  • PFS native format (extension: pfs)

Supported LDR formats:

  • JPEG, PNG, PPM, PBM, TIFF, FITS

Supported features:

  • Create an HDR file from a set of images (JPEG, TIFF 8bit and 16bit, RAW) of
    the same scene taken at different exposure settings
  • Save and load HDR files
  • Rotate and resize HDR files
  • Tonemap HDR images
  • Projective Transformations
  • Copy EXIF data between sets of images
  • Supports internationalization

Raw image formats are supported - and treated as HDR - thanks to LibRAW.

The code is in part based on the existing open source packages:

  • “pfstools”, “pfstmo” and “pfscalibration” by Grzegorz Krawczyk and Rafal
    Mantiuk
  • “qpfstmo”, by Nicholas Phillips.

Without their contribution all of this would have not been possible.


%package data
Summary:        Architecture-independent data files for %{name}

BuildArch:      noarch

# For icon directory:
Requires:       hicolor-icon-theme
# For unbundled hdrhtml:
Requires:       pfstools

%description data
Architecture-independent data files for %{name}, such as HTML help and
translations.


%prep
%autosetup -n LuminanceHDR-v.%{version} -p1

# Just in case the bundled librtprocess shows up in the tarball:
rm -rf librtprocess

# https://github.com/LuminanceHDR/LuminanceHDR/pull/236
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(TestPoissonSolver\b.*pfstmo)'\
'[[:blank:]]*$/\1 common/' \
    test/CMakeLists.txt
# https://github.com/LuminanceHDR/LuminanceHDR/pull/237
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(pfstmo[[:blank:]]+)(Qt5::)/\1pfs \2/' \
     src/TonemappingOperators/CMakeLists.txt
# https://github.com/LuminanceHDR/LuminanceHDR/issues/240
# https://github.com/LuminanceHDR/LuminanceHDR/pull/238
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(pfs[[:blank:]]+)(Qt5::)/\1rtprocess \2/' \
     src/Libpfs/CMakeLists.txt

# Remove bundled copy of hdrhtml from pfstools package; let the build system
# install an empty directory, then replace it with a symbolic link to the
# pfstools copy.
rm -rf hdrhtml/*


%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DENABLE_UNIT_TEST:BOOL=%{?with_tests:ON}%{?!with_tests:OFF} \
    -GNinja
%cmake_build


%install
%cmake_install

# Upstream installs AUTHORS, Changelog, LICENSE, and README.md. We install
# documentation and license files with the %%doc and %%license macros instead,
# putting them in the usual locations favored by Fedora.
rm -rvf '%{buildroot}%{_datadir}/%{name}/doc'

# Install mimeinfo file
install -d '%{buildroot}/%{_datadir}/mime/packages'
install -t '%{buildroot}/%{_datadir}/mime/packages' -p -m 0644 %{name}.xml

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications \
    %{app_id}.desktop

# We need to move the AppData file to the correct location. We also choose to
# rename the file from upstream using the legacy .appdata.xml name to the
# current .metainfo.xml used for AppData. See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/.
install -d '%{buildroot}%{_metainfodir}'
mv -v '%{buildroot}%{_datadir}/appdata/%{app_id}.appdata.xml' \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE1}' '%{SOURCE2}'

%find_lang lang --with-qt

rm -rvf '%{buildroot}%{_datadir}/%{name}/hdrhtml'
ln -s ../pfstools '%{buildroot}%{_datadir}/%{name}/hdrhtml'


%if %{with tests}
%check
# https://github.com/LuminanceHDR/LuminanceHDR/issues/154
x='Mantiuk06Pyramid'
%ifarch %{ix86}
# TestPoissonSolver sometimes hangs on this arch only. It exists only for
# multilib on x86_64 anyway, so there is very little reason to try to find a
# solution.
x="${x}|PoissonSolver"
%endif
%ctest --exclude-regex "^Test(${x})\$"
%endif


%pretrans data -p <lua>
--[[Back up any bundled hdrhtml directory from the old package. See:
https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement
]]
path = "%{_datadir}/%{name}/hdrhtml"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end


%files
%doc AUTHORS
%doc BUGS
%doc Changelog
%doc README.i18n
%doc README.md
%doc TODO

%{_bindir}/%{name}
%{_bindir}/%{name}-cli

# While the following are technically arch-independent data files, they have
# configuration-like functionality and should not be installed without the
# actual application, so they belong here instead of in -data.

# Shared directory ownership with shared-mime-info
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/%{name}.xml

%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/applications/%{app_id}.desktop


%files data -f lang.lang
%license LICENSE LICENSE.txt

%dir %{_datadir}/%{name}

# Relative symbolic link to %%{_datadir}/pfstools
%{_datadir}/%{name}/hdrhtml
# A backed-up bundled hdrhtml directory from a previous upgrade may be present:
%ghost %{_datadir}/%{name}/hdrhtml.rpmmoved

%{_datadir}/%{name}/help

# Contents of this directory are listed by %%find_lang
%dir %{_datadir}/%{name}/i18n

%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-cli.1*


%changelog
* Mon Apr 12 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.1.1-2
- Drop accommodations for Fedora 32

* Fri Apr 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.1.1-1
- New upstream version 2.6.1.1
- Adjust whitespace to personal preference
- Update summary and description from upstream
- Associate dependencies with INSTALL.md entries
- Correct CCfits-devel BR to cfitsio-devel
- Do not “rm -rf” the buildroot
- Remove obsolete icon cache, mimeinfo, and desktop-database scriptlets
- Change CMAKE_BUILD_TYPE from Release to RelWithDebInfo
- Do not ask CMake to disable shared libraries
- Clean up CMake macro invocations
- Remove bogus BR on git
- Build with ninja backend instead of make
- Properly handle localization files with %%find_lang, and stop manually
  installing them
- Simplify desktop-file-install usage
- Improve installation and listing of data files
- Add required AppData file validation
- No need to apply sed to Changelog anymore
- Correct License field from “GPLv2+” to “GPLv2+ and GPLv2 and GPLv3+ and
  LGPLv2+ and BSD and MIT and Boost”
- Unbundle librtprocess
- Build and run the tests
- Add virtual Provides for bundled parts of sleef
- Restore missing copyright statement and Boost license text for files forked
  from SLEEF
- Disable LTO to fix linking errors in tests
- Unbundle hdrhtml, from pfstools
- Rename AppData file from .appdata.xml to .metainfo.xml
- Add BR on gcc-c++
- Add a -data subpackage for large noarch data files
- Add man pages

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.6.0-11
- Rebuilt for Boost 1.75

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.6.0-10
- Rebuild for OpenEXR 2.5.3.

* Tue Aug 04 2020 Franco Comida <francocomida@gmail.com> - 2.6.0-9
- fix build on f33/rawhide

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 2.6.0-6
- Rebuilt for Boost 1.73

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-5
- Rebuild for new LibRaw

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-3
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Franco Comida <francocomida@gmail.com> - 2.6.0-1
- Update to Release 2.6.0

* Mon Apr 29 2019 Franco Comida <fcomida@users.sourceforge.net> - 2.5.1-20
- Fix compilation with gcc 9

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2.5.1-19
- Rebuild for OpenEXR 2.3.0.
- Move LICENSE to %%license.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.5.1-17
- rebuild (exiv2)

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.5.1-16
- Rebuilt for Boost 1.69

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.5.1-15
- Rebuild with fixed binutils

* Thu Jul 26 2018 Adam Williamson <awilliam@redhat.com> - 2.5.1-14
- Rebuild for new libraw

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 2.5.1-12
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.5.1-11
- rebuilt for cfitsio 3.420 (so version bump)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.5.1-9
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.1-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 2.5.1-5
- Rebuilt for Boost 1.64

* Thu May 11 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-4
- Fix date in specfile

* Thu May 11 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-3
- Fix qtwebkit patch again

* Thu May 11 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-2
- Fix qtwebkit patch

* Wed May 10 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-1
- Release 2.5.1

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.5.0-4
- rebuild (exiv2)

* Tue Apr 18 2017 Franco Comida <francocomida@gmail.com> - 2.5.0-3
- Upstream retired previous 2.5.0, now it's out again. Let's start again from there.

* Mon Apr 10 2017 Dan Horák <dan[at]danny.cz> - 2.5.0-2
- fix build with qtwebengine vs. qtwebkit

* Sun Apr 09 2017 Franco Comida <francocomida@gmail.com> - 2.5.0-1
- Update to Release 2.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-12
- Rebuilt for Boost 1.63

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 2.4.0-11
- Rebuild for new LibRaw.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-10
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-8
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-7
- Rebuilt for Boost 1.59

* Thu Aug 20 2015 Jon Ciesla <limburgher@gmail.com> - 2.4.0-6
- Rebuild for new LibRaw.

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.4.0-4
- rebuild for Boost 1.58

* Tue Jul 07 2015 Franco Comida <francocomida@gmail.com> - 2.4.0-3
- Fix saving TMO parameters

* Sat Jul 04 2015 Franco Comida <francocomida@gmail.com> - 2.4.0-2
- Fix Application Icon Size

* Thu Jul 02 2015 Franco Comida <francocomida@gmail.com> - 2.4.0-1
- Updated to Luminance HDR 2.4.0

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-15
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.1-13
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.3.1-12
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.3.1-11
- Rebuild for boost 1.57.0

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.1-10
- rebuild (openexr)

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.1-9
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.3.1-6
- Rebuild for boost 1.55.0

* Wed Jan 22 2014 Jon Ciesla <limburgher@gmail.com> - 2.3.1-5
- Rebuild for new LibRaw.

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-4
- rebuild (exiv2)

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-3
- rebuild (openexr)

* Fri Sep 20 2013 Dan Horák <dan[at]danny.cz> - 2.3.1-2
- fix build on non-x86 arches

* Fri Sep 13 2013 Franco Comida <francocomida@googlemail.com> - 2.3.1-1
- Updated to Luminance HDR 2.3.1

* Mon Sep 09 2013 Rex Dieter <rdieter@fedoraproject.org> 2.3.0-9
- rebuild (OpenEXR)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.0-7
- Rebuild for new LibRaw.

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0-6
- rebuild (OpenEXR)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.3.0-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.3.0-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Franco Comida <francocomida@googlemail.com> - 2.3.0-1
- Updated to Luminance HDR 2.3.0

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-4
- rebuild (exiv2)

* Wed Mar 28 2012 Dan Horák <dan[at]danny.cz> - 2.2.1-3
- fix build on non-x86 arches

* Tue Mar 13 2012 Franco Comida <francocomida@googlemail.com> - 2.2.1-2
- Removed unused PATH from luminance-hdr.desktop

* Sun Mar 11 2012 Franco Comida <fcomida@users.sourceforge.net> 2.2.1-1
- Updated to Luminance HDR 2.2.1

* Tue Feb 21 2012 Franco Comida <fcomida@users.sourceforge.net> 2.2.0-1
- Luminance HDR 2.2.0

