Name:           pngcheck
Version:        3.0.2
Release:        1%{?dist}
Summary:        Verifies the integrity of PNG, JNG and MNG files

# Note that the main package contains only pngcheck, compiled from a single
# source file, pngcheck.c, under a minimal MIT license. The new utilities
# licensed under GPLv2+ are compiled from the gpl/ subdirectory and packaged in
# the extras subpackage.
License:        MIT
URL:            http://www.libpng.org/pub/png/apps/pngcheck.html
Source0:        http://www.libpng.org/pub/png/src/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  make

# Default on Fedora; still needed for EPEL
%global _hardened_build 1

%description
pngcheck verifies the integrity of PNG, JNG and MNG files (by checking the
internal 32-bit CRCs [checksums] and decompressing the image data); it can
optionally dump almost all of the chunk-level information in the image in
human-readable form. For example, it can be used to print the basic statistics
about an image (dimensions, bit depth, etc.); to list the color and
transparency info in its palette (assuming it has one); or to extract the
embedded text annotations. This is a command-line program with batch
capabilities.

The current release supports all PNG, MNG and JNG chunks, including the newly
approved sTER stereo-layout chunk. It correctly reports errors in all but two
of the images in Chris Nokleberg's brokensuite-20061204.


%package extras
Summary:        Helper utilities distributed with %{name}
License:        GPLv2+

%description extras
Included with pngcheck (since version 2.1.0) are two helper utilities:

  - pngsplit - break a PNG, MNG or JNG image into constituent chunks (numbered
    for easy reassembly)
  - png-fix-IDAT-windowsize - fix minor zlib-header breakage caused by libpng
    1.2.6


%prep
%autosetup


%build
%set_build_flags
%make_build -f Makefile.unx \
    CFLAGS="${CFLAGS-} -DUSE_ZLIB $(pkg-config --cflags zlib)" \
    LIBS="${LDFLAGS-} $(pkg-config --libs zlib)"


%install
install -d '%{buildroot}%{_bindir}'
install -t '%{buildroot}%{_bindir}' -p \
    pngcheck pngsplit png-fix-IDAT-windowsize
install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p *.1 gpl/*.1


%files
%license LICENSE
%doc CHANGELOG
%doc README
%{_bindir}/pngcheck
%{_mandir}/man1/pngcheck.1*


%files extras
%license gpl/COPYING
%doc CHANGELOG
%doc README
%{_bindir}/pngsplit
%{_bindir}/png-fix-IDAT-windowsize
%{_mandir}/man1/pngsplit.1*
%{_mandir}/man1/png-fix-IDAT-windowsize.1*


%changelog
* Mon Feb 01 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.2-1
- New upstream release 3.0.2

* Sun Jan 31 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.1-1
- New upstream version 3.0.1 with upstreamed patches

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-4
- Fix buffer overflow on large MNG LOOP chunk (RHBZ#1908559); not built in
  Fedora

* Mon Dec 14 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-3
- Fix a buffer overrun for certain invalid MNG PPLT chunk contents
  (RHBZ#1907428); not built in Fedora

* Mon Dec 14 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-2
- Previous fix for buffer overrun printing the contents of the sPLT chunk in
  certain malformed inputs (RHBZ#1905775) was incomplete; it should be properly
  fixed now.

* Sun Dec 13 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-1
- New upstream version 3.0.0 incorporating all patches in 2.4.0-4, and removing
  the -f option

* Sun Dec 13 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-4
- Bounds-check all accesses into enumerated-value name arrays; a malformed file
  could have caused a buffer overrun in several of these cases. (RHBZ#1902810)
- Fix buffer overrun when print_buffer() is passed a nonpositive size, which
  can occur in practice for certain malformed inputs. (RHBZ#1902810)
- In some cases, the chunk length from the file data (sz) is used to index into
  the read buffer without sufficient bounds-checking, leading to a buffer
  overrun. Fix this for PPLT, hIST, sCAL, FRAM, SAVE, nEED, PAST, DISC, DROP,
  DBYK, ORDR, and SEEK chunks. (RHBZ#1902810)
- Fix buffer overrun printing the contents of the sPLT chunk in certain
  malformed inputs. (RHBZ#1905775)
- Backport fix for off-by-one bug in check_magic() from 3.0.0
- Backport fix for zlib version warnings going to stdout from 3.0.0

* Mon Nov 30 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-3
- Fix null pointer dereference in pngcheck when -f is given and the sCAL chunk
  is missing the pixel height.
- Use name macro when referencing patches.
- Add BR on make in anticipation of
  https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot.

* Fri Nov 13 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-2
- Fix buffer overflow (RHBZ #1897485)

* Sun Nov  1 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-1
- New upstream version 2.4.0
- Added new license file for main package (same MIT-style license)
- Drop format-security patch, now upstreamed
- Use upstreamed man pages; no need to generate with help2man anymore

* Sat Oct 31 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-5
- Add rpmlintrc rules for -extras subpackage

* Sat Oct 31 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-4
- Add rpmlintrc file to suppress spurious rpmlint warnings

* Wed Oct 28 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-3
- Add _hardened_build macro for EPEL

* Wed Oct 28 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-2
- Work around Makefile.unx not actually using LDFLAGS; this fixes hardened
  build (PIE)

* Thu Oct 15 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-1
- Initial import (#1886858)
