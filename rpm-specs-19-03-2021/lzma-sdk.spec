Name:           lzma-sdk
Version:        4.6.5
Release:        27%{?dist}
Summary:        SDK for lzma compression

License:        LGPLv2
URL:            http://sourceforge.net/projects/sevenzip/
Source0:        http://downloads.sourceforge.net/sevenzip/lzma465.tar.bz2
Source1:        lzma-sdk-LICENSE.fedora
Patch0:         lzma-sdk-4.6.5-sharedlib.patch
Patch1:         lzma-sdk-fprintf-format.patch

BuildRequires: make
BuildRequires:  gcc-c++
%description
LZMA SDK provides the documentation, samples, header files, libraries,
and tools you need to develop applications that use LZMA compression.

LZMA is default and general compression method of 7z format
in 7-Zip compression program (www.7-zip.org). LZMA provides high
compression ratio and very fast decompression.

LZMA is an improved version of famous LZ77 compression algorithm. 
It was improved in way of maximum increasing of compression ratio,
keeping high decompression speed and low memory requirements for
decompressing.

%package devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%prep
%setup -q -c -n lzma465
%patch0 -p1 -b .shared
%patch1 -p0 -b .fprintf
rm lzma.exe

for f in .h .c .cpp .dsw .dsp .java .cs .txt makefile; do
   find . -iname "*$f" | xargs chmod -x
done

# correct end-of-line encoding
sed -i 's/\r//' *.txt 

for i in \
7zFormat.txt \
CS/7zip/Compress/LzmaAlone/LzmaAlone.sln \
7zC.txt \
CS/7zip/Compress/LzmaAlone/LzmaAlone.csproj \
CPP/7zip/Bundles/Alone7z/resource.rc \
history.txt \
lzma.txt \
CPP/7zip/Compress/LZMA_Alone/makefile.gcc \
CPP/Build.mak \
C/LzmaUtil/makefile.gcc \
CPP/7zip/Bundles/Format7zR/resource.rc \
C/Archive/7z/makefile.gcc \
CPP/7zip/Archive/Archive.def \
CPP/7zip/Bundles/Format7zExtractR/resource.rc \
C/LzmaLib/resource.rc \
CPP/7zip/Archive/Archive2.def \
CPP/7zip/MyVersionInfo.rc \
Methods.txt \
C/LzmaLib/LzmaLib.def; do
    iconv -f iso-8859-1 -t utf-8 $i > $i.utf8
    touch -r $i $i.utf8
    mv $i.utf8 $i
done

install -p -m 0644 %{SOURCE1} .

%build
cd CPP/7zip/Compress/LZMA_Alone
make -f makefile.gcc clean all CXX="g++ %{optflags} -fPIC" CXX_C="gcc %{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}
install -m0755 CPP/7zip/Compress/LZMA_Alone/liblzmasdk.so.4.6.5 %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s liblzmasdk.so.4.6.5 liblzmasdk.so.4
ln -s liblzmasdk.so.4.6.5 liblzmasdk.so
popd
mkdir -p %{buildroot}/%{_includedir}/lzma465/
find -iname '*.h' | xargs -I {} install -m0644 -D {} %{buildroot}/%{_includedir}/lzma465/{}

%ldconfig_scriptlets

%files
%doc lzma.txt history.txt lzma-sdk-LICENSE.fedora
%{_libdir}/liblzmasdk.so.*

%files devel
%doc 7z*.txt Methods.txt
%{_includedir}/lzma465/
%{_libdir}/liblzmasdk.so

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 14 2015 Adam Jackson <ajax@redhat.com> 4.6.5-16
- Pass ldflags to make so hardening works

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.6.5-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jon Ciesla <limburgher@gmail.com> - 4.6.5-11
- Fix format-security FTBFS, BZ 1037188.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-6
- Changed first gcc on make line to g++ to silence rpmlint.

* Tue Aug  9 2011 Tom Callaway <spot@fedoraproject.org> - 4.6.5-5
- rework package to be more normal

* Wed Apr 27 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-4
- Additional provides macro.

* Mon Apr 11 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-3
- Stripped perl(SevenZip) provides.

* Tue Apr 05 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-2
- Licensing clarification.

* Wed May 26 2010 Jon Ciesla <limb@jcomserv.net> - 4.6.5-1
- Initial build
