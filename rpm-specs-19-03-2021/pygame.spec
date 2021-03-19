Name:           pygame
Version:        2.0.1
Release:        2%{?dist}
Summary:        Python modules for writing games

License:        LGPLv2+
URL:            http://www.pygame.org
Source0:	https://files.pythonhosted.org/packages/c7/b8/06e02c7cca7aec915839927a9aa19f749ac17a3d2bb2610b945d2de0aa96/pygame-2.0.1.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-numpy python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  SDL2_ttf-devel SDL2_image-devel SDL2_mixer-devel
BuildRequires:  SDL2-devel freetype-devel
BuildRequires:  libpng-devel libjpeg-devel libX11-devel
BuildRequires:  portmidi-devel
BuildRequires:  gcc

%global _description\
Pygame is a set of Python modules designed for writing games. It is\
written on top of the excellent SDL library. This allows you to create\
fully featured games and multimedia programs in the python language.\
Pygame is highly portable and runs on nearly every platform and\
operating system.

%description %_description

%package devel
Summary:        Files needed for developing programs which use pygame
Requires:       python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires:       SDL2_ttf-devel SDL2_mixer-devel
Requires:       python3-devel

%description devel
This package contains headers required to build applications that use
pygame.

%package -n python%{python3_pkgversion}-pygame
Summary:        Python3 modules for writing games
Requires:       gnu-free-sans-fonts
Recommends:     python%{python3_pkgversion}-numpy
%{?python_provide:%python_provide python%{python3_pkgversion}-pygame}

%description -n python%{python3_pkgversion}-pygame
Pygame is a set of Python modules designed for writing games. It is
written on top of the excellent SDL library. This allows you to create
fully featured games and multimedia programs in the python language.
Pygame is highly portable and runs on nearly every platform and
operating system.


%prep
%setup -q

# rpmlint fixes
find examples/ -type f -print0 | xargs -0 chmod -x 
find docs/ -type f -print0 | xargs -0 chmod -x
find src_c/ -type f -name '*.h' -print0 | xargs -0 chmod -x

iconv -f iso8859-1 -t utf-8 WHATSNEW > WHATSNEW.conv && mv -f WHATSNEW.conv WHATSNEW
iconv -f iso8859-1 -t utf-8 README.txt > README.txt.conv && mv -f README.txt.conv README.txt


# These files must be provided by pygame-nonfree(-devel) packages on a
# repository that does not have restrictions on providing non-free software
rm -f src_c/ffmovie.[ch]


%build
%py3_build cython

%install
%py3_install

#use system font.
rm -f $RPM_BUILD_ROOT%{python3_sitearch}/%{name}/freesansbold.ttf
ln -s /usr/share/fonts/gnu-free/FreeSansBold.ttf $RPM_BUILD_ROOT%{python3_sitearch}/%{name}/freesansbold.ttf

# Fix permissions
chmod 755 $RPM_BUILD_ROOT%{python3_sitearch}/%{name}/*.so

%check
# base_test fails in mock, unable to find soundcard
PYTHONPATH="$RPM_BUILD_ROOT%{python3_sitearch}" %{__python3} test/base_test.py || :
PYTHONPATH="$RPM_BUILD_ROOT%{python3_sitearch}" %{__python3} test/rect_test.py
#image_test now fails in mock, unable to find video device.
#PYTHONPATH="$RPM_BUILD_ROOT%{python3_sitearch}" %{__python3} test/image_test.py
 
%files -n python%{python3_pkgversion}-pygame
%doc docs/ README* WHATSNEW*
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}*

%files devel
%doc examples/
%dir %{_includedir}/python*/%{name}
%{_includedir}/python*/%{name}/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.0.1-1
- 2.0.1

* Thu Nov 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-1
- 2.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.6-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.9.6-6
- Patch for python 3.9

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.9.6-5
- Drop Python 2.

* Tue Oct 29 2019 Petr Viktorin <pviktori@redhat.com> - 1.9.6-4
- Only Recommend NumPy
  The only part of pygame that needs NumPy is pygame.surfarray,
  but pygame is otherwise useful without it.
  See: https://www.pygame.org/docs/ref/surfarray.html

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.6-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.6-2
- Rebuilt for Python 3.8

* Thu Aug 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.9.6-1
- 1.9.6

* Wed Aug 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.9.4-9
- Mode -devel to Python 3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Sérgio Basto <sergio@serjux.com> - 1.9.4-7
- Fix one missing %%{python3_pkgversion}

* Thu May 09 2019 Sérgio Basto <sergio@serjux.com> - 1.9.4-6
- Allow build on EPEL7
- Re-enable tests on ppc64le (#1520016)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.9.4-4
- Requires fixes.

* Thu Oct 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.9.4-3
- Requires fixes.

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.9.4-2
- BR fix.

* Thu Jul 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.9.4-1
- 1.9.4.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-7
- Rebuilt for Python 3.7
- Regenerate Cython C file, apply upstream patch for new Cython

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.3-5
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.3-4
- Python 2 binary package renamed to python2-pygame
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.9.3-1
- 1.9.3, some minor cleanup.

* Sat Apr 08 2017 Till Maas <opensource@till.name> - 1.9.1-27.20150926
- Fix Summary of python 3 package (#1282034)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-26.20150926
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-25.20150926
- Rebuild for Python 3.6

* Tue Nov 08 2016 Hans de Goede <hdegoede@redhat.com> - 1.9.1-24.20150926
- Ignore image_test.py result on ppc64le to avoid build failure (rhbz#1392465)

* Mon Nov 07 2016 Björn Esser <fedora@besser82.io> - 1.9.1-23.20150926
- Rebuilt for ppc64

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-22.20150926
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-21.20150926
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-20.20150926
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Sep 26 2015 Jon Ciesla <limburgher@gmail.com> - 1.9.1-19.20150926
- Add python3-numpy Requires.

* Sat Sep 26 2015 Jon Ciesla <limburgher@gmail.com> - 1.9.1-18.20150926
- Add python3 support.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.9.1-12
- rebuild due to "jpeg8-ABI" feature drop

* Tue Dec 04 2012 Jan Kaluza <jkaluza@redhat.com> - 1.9.1-11
- fix #881545 - fix memory leak when saving png images

* Mon Jul 30 2012 Jon Ciesla <limburgher@gmail.com> - 1.9.1-10
- Use system font, BZ 477444.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.9.1-7
- Rebuild for new libpng

* Thu Jun 23 2011 Jan Kaluza <jkaluza@redhat.com> - 1.9.1-6
- Removed V4L support because V4L has been deprecated from the Linux
  kernel as of 2.6.38

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Jan Kaluza <jkaluza@redhat.com> - 1.9.1-4
- fix #607753 - Do not install tests

* Thu Aug 12 2010 Jan Kaluza <jkaluza@redhat.com> - 1.9.1-3
- fix #585526 - add MIDI support

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Oct 08 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.1-1
- New upstream release, BZ 526365.
- Updated config_unix patch for 1.9.1.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Jon Ciesla <limb@jcomserv.net> - 1.8.1-6
- Dropped f2py deps, unneeded now that numpy is fixed: BZ 496277.

* Fri Apr 17 2009 Jon Ciesla <limb@jcomserv.net> - 1.8.1-5
- Add dep for numpy-f2py to fix broken games, BZ 496218.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.8.1-3
- Rebuild for Python 2.6

* Wed Sep 17 2008 Robin Norwood <robin.norwood@gmail.com> 1.8.1-2
- Bump release to trump F9 version.

* Tue Aug 26 2008 Robin Norwood <robin.norwood@gmail.com> 1.8.1-1
- Update to new upstream version.
- rpmlint fixes

* Mon Aug 25 2008 Robin Norwood <robin.norwood@gmail.com> 1.8.0-3
- Rebase config patch for 1.8.0
- Need to specify BR: SDL-devel

* Mon Aug 25 2008 Robin Norwood <robin.norwood@gmail.com> 1.8.0-2
- Change from requiring python-numeric to numpy
- rhbz#457074

* Thu May 22 2008 Christopher Stone <chris.stone@gmail.com> 1.8.0-1
- Upstream sync
- Remove Obsolets/Provides (been around since FC-4)
- Remove no longer needed 64bit patch
- Remove %%{version} macro from Patch0 definition
- Add png, jpeg, and X11 libraries to BuildRequires
- Simplify %%files section
- Fix up some rpmlint warnings

* Thu Feb 21 2008 Christopher Stone <chris.stone@gmail.com> 1.7.1-16
- Add egginfo file to %%files
- Update %%license
- Fix permissions on .so files

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.7.1-15
- Autorebuild for GCC 4.3

* Tue May 15 2007 Christopher Stone <chris.stone@gmail.com> 1.7.1-14
- Add one more bit to 64-bit patch

* Sat May 12 2007 Christopher Stone <chris.stone@gmail.com> 1.7.1-13
- Apply 64-bit patch for python 2.5 (bz #239899)
- Some minor spec file cleanups

* Mon Apr 23 2007 Christopher Stone <chris.stone@gmail.com> 1.7.1-12
- Revert back to version 1.7.1-9

* Mon Dec 11 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-11
- Remove all Obsolete/Provides
- Remove Requires on all devel packages

* Sun Dec 10 2006 Christopher Stone <chris.stone@gmail.som> 1.7.1-10
- Remove macosx examples
- Move header files into main package
- Move examples into examples subpackage
- python(abi) = 0:2.5

* Wed Sep 06 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-9
- No longer %%ghost pyo files. Bug #205396

* Sat Sep 02 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-8
- FC6 Rebuild

* Wed Jun 28 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-7.fc6.1
- Rebuild bump

* Wed May 03 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-7
- Fix Obsolete/Provides of python-pygame-doc

* Wed Apr 26 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-6
- Bump release for new build on devel

* Wed Apr 26 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-5
- Add Obsolete/Provides tags for python-pygame-docs
- Add Obsolete/Provides tags for python-pygame-devel to devel package
- Hopefully this fixes Bugzilla bug #189991

* Fri Apr 21 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-4
- Add Requires to -devel package
- Remove ffmovie.h from -devel package since it requires smpeg-devel

* Fri Apr 21 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-3
- Obsolete linva python-pygame package
- Added Provides for python-pygame
- Fix equal sign in devel requires

* Thu Apr 20 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-2
- Added a patch to clean up some warnings on 64 bit compiles

* Tue Apr 18 2006 Christopher Stone <chris.stone@gmail.com> 1.7.1-1
- Initial RPM release
