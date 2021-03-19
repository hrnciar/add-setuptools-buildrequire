Name:           palp
Version:        2.1
Release:        17%{?dist}
Summary:        A Package for Analyzing Lattice Polytopes
License:        GPLv3+
URL:            http://hep.itp.tuwien.ac.at/~kreuzer/CY/CYpalp.html
Source0:        http://hep.itp.tuwien.ac.at/~kreuzer/CY/palp/palp-%{version}.tar.gz
Source1:        https://export.arxiv.org/pdf/1205.4147

# Correct build with -Werror=format-security
Patch0:         %{name}-format.patch
# Fix build with -fno-common (default with GCC 10)
Patch1:         %{name}-fno-common.patch
# Fix some buffer overflows
Patch2:         %{name}-buffer-overflow.patch
# Do not fork and execute a shell just to delete a file
Patch3:         %{name}-unlink.patch
# Fedora changed the name of the latte-integrale "count" binary
Patch4:         %{name}-latte.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  help2man

# Invokes awk, cat, and grep at runtime
Requires:       coreutils
Requires:       gawk
Requires:       grep

# Can invoke latte-integrale's count binary and Singular at runtime
Recommends:     latte-integrale
Recommends:     Singular

%description
PALP contains routines for vertex and facet enumeration, computation of
incidences and symmetries, as well as completion of the set of lattice
points in the convex hull of a given set of points. In addition, there
are procedures specialized to reflexive polytopes such as the enumeration
of reflexive subpolytopes, and applications to toric geometry and string
theory, like the computation of Hodge data and fibration structures for
toric Calabi-Yau varieties.


%prep
%autosetup -p1

%build
cp -p %{SOURCE1} 1205.4147v1.pdf

mkdir bin man
mv Global.h Global.h-template
for dim in 4 5 6 11; do
    echo Building PALP optimized for $dim dimensions
    sed "s/^#define[^a-zA-Z]*POLY_Dmax.*/#define POLY_Dmax $dim/" Global.h-template > Global.h
    make %{?_smp_mflags} CFLAGS="%{optflags}"
    for file in poly class cws nef mori; do
        mv ${file}.x bin/${file}-${dim}d.x
        help2man -N --version-string=%{version} -h -h bin/${file}-${dim}d.x \
            <<< e | sed '$d' | sed '$d' | sed '$d' > man/${file}-${dim}d.x.1
    done
    make cleanall
done
for file in poly class cws nef mori; do
    help2man -N --version-string=%{version} -h -h bin/${file}.x \
        <<< e | sed '$d' | sed '$d' | sed '$d' > man/${file}.x.1
done


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
pushd bin
    for exe in *.x; do
	install -m 755 $exe $RPM_BUILD_ROOT%{_bindir}/$exe
    done
popd
for file in poly class cws nef mori; do
    ln -sf ${file}-6d.x $RPM_BUILD_ROOT%{_bindir}/${file}.x
done
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc COPYING
%doc 1205.4147v1.pdf
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Jerry James <loganjerry@gmail.com> - 2.1-15
- Add -fno-common patch to fix FTBFS with GCC 10 (bz 1799844)
- Add -buffer-overflow, -unlink, and -latte patches
- Fix URL of the PDF file
- Generate man pages with help2man

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1-4
* Correct build with -Werror=format-security (#1037021)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 15 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1-1
- Update to latest upstream release
- Adapt to match sagemath palp build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1-7
- Add arxiv.org palp documentation as %%doc.
- Do not preventive rename files for unlikely name conflicts (#837837).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Conrad Meyer <konrad@tylerc.org> - 1.1-2
- Correct license to GPLv3+.

* Sat Dec 13 2008 Conrad Meyer <konrad@tylerc.org> - 1.1-1
- Initial package.
