Name:           rubiks
Version:        20070912
Release:        2%{?dist}
Summary:        Rubiks cube solvers

# See the description for the licensing breakdown
License:        GPL+ and GPLv2+ and MIT
URL:            https://git.sagemath.org/sage.git/plain/build/pkgs/rubiks/
Source0:        http://mirrors.xmission.com/sage/spkg/upstream/%{name}/%{name}-%{version}.tar.bz2
# Man pages courtesy of Debian
Source1:        rubiks_cubex.1
Source2:        rubiks_dikcube.1
Source3:        rubiks_optimal.1

# Fix various makefile infelicities
Patch0:         %{name}-makefile.patch
# Add some missing #includes
Patch1:         %{name}-includes.patch
# Tonight we're going to party like it's 1989
Patch2:         %{name}-ansi-c.patch
# Provide missing function prototypes
Patch3:         %{name}-prototypes.patch
# Use unsigned int for a 32-bit type, instead of unsigned long
Patch4:         %{name}-longtype.patch
# Fix some mixed signed/unsigned operations
Patch5:         %{name}-signed.patch
# Add attributes for better compiled code quality
Patch6:         %{name}-attributes.patch

BuildRequires:  gcc-c++
BuildRequires:  make

# This can be removed when F36 reaches EOL
Obsoletes:      sagemath-rubiks < 9.2
Provides:       sagemath-rubiks = %{version}-%{release}

%description
This package contains several different Rubik's cube solvers.  They can
be invoked from the command line or used through sagemath.

Michael Reid (GPLv2+)

-  optimal - uses many pre-computed tables to find an optimal
   solution to the 3x3x3 Rubik's cube

Dik T. Winter (MIT)

-  dikcube - uses Kociemba's algorithm to iteratively find a short
   solution to the 3x3x3 Rubik's cube
-  size222 - solves a 2x2x2 Rubik's cube

Eric Dietz (GPL+)

-  cu2 - A fast, non-optimal 2x2x2 solver
-  cubex - A fast, non-optimal 3x3x3 solver
-  mcube - A fast, non-optimal 4x4x4 solver

%prep
%autosetup -p0

# Use our flags
sed -i 's|^\(CFLAGS = \)-O|\1%{build_cflags}|' dik/makefile
sed -e 's|^\(CFLAGS[[:blank:]]*=\).*|\1%{build_cflags}|' \
    -e 's|^\(LFLAGS[[:blank:]]*=\).*|\1%{build_ldflags}|' \
    -i dietz/{cu2,mcube,solver}/Makefile reid/Makefile

# Fix end of line encodings
for fil in dietz/{cu2,mcube}/readme.txt; do
  sed -i.orig 's/\r//g' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
%set_build_flags
export LFLAGS="$LDFLAGS"
%make_build

%install
%make_install

# Rename binaries with overly generic names (to match Debian)
for fil in cu2 cubex dikcube mcube optimal size222; do
  mv %{buildroot}%{_bindir}/$fil %{buildroot}%{_bindir}/rubiks_$fil
done

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_mandir}/man1

# Too many documentation & license files with the same name.  Rename them.
cp -p dietz/license.txt dietz-license.txt
cp -p dietz/cu2/readme.txt cu2-readme.txt
cp -p dietz/mcube/readme.txt mcube-readme.txt
cp -p dietz/solver/readme.txt cubex-readme.txt
cp -p dik/Description dik-Description
cp -p dik/license.txt dik-license.txt
cp -p dik/README dik-README
cp -p reid/license.txt reid-license.txt
cp -p reid/README reid-README

%check
# Basic sanity check only
for v in cu2 cubex mcube; do
  echo | %{buildroot}%{_bindir}/rubiks_${v} random <<< ''
done

%files
%doc cu2-readme.txt cubex-readme.txt mcube-readme.txt
%doc dik-Description dik-README
%doc reid-README
%license dietz-license.txt dik-license.txt reid-license.txt
%{_bindir}/rubiks_cu2
%{_bindir}/rubiks_cubex
%{_bindir}/rubiks_dikcube
%{_bindir}/rubiks_mcube
%{_bindir}/rubiks_optimal
%{_bindir}/rubiks_size222
%{_mandir}/man1/rubiks_cubex.1*
%{_mandir}/man1/rubiks_dikcube.1*
%{_mandir}/man1/rubiks_optimal.1*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20070912-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 2020 Jerry James <loganjerry@gmail.com> - 20070912-1
- Initial RPM
