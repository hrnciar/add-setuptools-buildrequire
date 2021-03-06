Name:           atari++
Version:        1.83
Release:        3%{?dist}
Summary:        Unix based emulator of the Atari eight bit computers

License:        TPL
URL:            http://www.xl-project.com/
Source0:        http://www.xl-project.com/download/%{name}_%{version}.tar.gz
Source1:        http://www.xl-project.com/download/os++doc.pdf
Source2:        http://www.xl-project.com/download/basic++doc.pdf
Source3:        http://www.xl-project.com/download/system.atr
Source4:        %{name}.desktop
# borrowed from atari800 project
Source5:        atari2.svg
# be verbose during compile
Patch1:         %{name}-verbose.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  zlib-devel
BuildRequires:  ncurses-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires: make


%description
The Atari++ Emulator is a Unix based emulator of the Atari eight bit
computers, namely the Atari 400 and 800, the Atari 400XL, 800XL and 130XE,
and the Atari 5200 game console. The emulator is auto-configurable and
will compile on a variety of systems (Linux, Solaris, Irix).
Atari++ 1.30 and up contain a built-in ROM emulation that tries to mimic
the AtariXL operating system closely.


%prep
%setup -q -n %{name}
%patch1 -p1 -b .verbose

# fix encoding
f=README.History
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

# fix permissions for sources
chmod a-x *.cpp *.hpp

# additional docs
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
%configure
make %{?_smp_mflags} OPTIMIZER="$RPM_OPT_FLAGS -DDEBUG_LEVEL=0 -DCHECK_LEVEL=0" V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT

# remove installed docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

# install system disk into %%_datadir
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}

# install icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/pixmaps

# desktop file
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        %{SOURCE4}


%files
%doc COPYRIGHT CREDITS README.LEGAL README.History README.licence manual
%doc os++doc.pdf basic++doc.pdf
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.*
%{_datadir}/%{name}
%{_datadir}/pixmaps/atari2.svg
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Dan Hor??k <dan[at]danny.cz> - 1.83-1
- updated to version 1.83

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Dan Hor??k <dan[at]danny.cz> - 1.81-1
- updated to version 1.81 (#1405251)
- add desktop integration (#1353851)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Dan Hor??k <dan[at]danny.cz> - 1.80-1
- updated to version 1.80

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.73-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 22 2015 Dan Hor??k <dan[at]danny.cz> - 1.73-4
- switch to polling for Alsa sound (#1201805)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Dan Hor??k <dan[at]danny.cz> - 1.73-1
- updated to version 1.73

* Tue Dec 03 2013 Dan Hor??k <dan[at]danny.cz> 1.72-3
- fix build with -Werror=format-security (#1036993)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Dan Hor??k <dan[at]danny.cz> 1.72-1
- updated to version 1.72

* Thu Jan 31 2013 Dan Hor??k <dan[at]danny.cz> 1.71-1
- updated to version 1.71

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.60-2
- Rebuild for new libpng

* Fri May 13 2011 Dan Hor??k <dan[at]danny.cz> 1.60-1
- updated to version 1.60

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 30 2009 Dan Hor??k <dan[at]danny.cz> 1.58-1.1
- rebuilt with updated source archive

* Mon Nov 30 2009 Dan Hor??k <dan[at]danny.cz> 1.58-1
- updated to version 1.58
- used better patch for the making the build output verbose

* Tue Aug 25 2009 Dan Hor??k <dan[at]danny.cz> 1.57-1
- update to version 1.57

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Dan Hor??k <dan[at]danny.cz> 1.56-2
- add patch for sparc

* Mon May 18 2009 Dan Hor??k <dan[at]danny.cz> 1.56-1
- update to version 1.56

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Dan Hor??k <dan[at]danny.cz> 1.55-2
- disable the verbose patch

* Wed Nov 19 2008 Dan Hor??k <dan[at]danny.cz> 1.55-1
- initial Fedora version
