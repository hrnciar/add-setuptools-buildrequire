%bcond_without icu

Name:           xalan-c
Version:        1.12.0
Release:        6%{?dist}
Summary:        Xalan XSLT processor for C/C++

License:        ASL 2.0
URL:            http://xalan.apache.org/%{name}/
%global tag Xalan-C_%(echo '%{version}' | tr . _)
%global tar_name xalan_c-%(echo %{version} | cut -d . -f -2)
%global release_url https://github.com/apache/%{name}/releases/download/%{tag}
Source0:        %{release_url}/%{tar_name}.tar.gz
Source1:        %{release_url}/%{tar_name}.tar.gz.asc
Source2:        %{release_url}/KEYS

BuildRequires:  gnupg2
BuildRequires:  cmake
# Either make or ninja is supported.
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  xerces-c-devel
%if %{with icu}
BuildRequires:  libicu-devel
%endif

%global so_version %(echo %{version} | cut -d . -f -2 | tr -d .)
# Required for EPEL8:
%undefine __cmake_in_source_build

%description
The Apache Xalan-C++ Project provides a library and a command line program to
transform XML documents using a stylesheet that conforms to XSLT 1.0 standards.

Xalan is a project of the Apache Software Foundation.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package doc
Summary:        Documentation for %{name}
BuildRequires:  doxygen
# Explicit BR required for EPEL8:
BuildRequires:  graphviz

%description doc
Documentation for %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n %{tar_name}

# https://github.com/apache/xalan-c/pull/35
chmod a-x NOTICE

# Remove the Autotools build system cruft from the samples; otherwise, it would
# be installed as documentation. We leave the CmakeLists.txt even though it
# cannot be used standalone; it is used in the build (even though the built
# samples are only tested and not installed), and is annoying to exclude.
rm -vf samples/configure samples/configure.in


%build
%cmake \
%if %{with icu}
    -Dtranscoder=icu \
%endif
    -GNinja
%cmake_build


%install
%cmake_install
# Remove CMake-installed docs in favor of using the doc macro. We refer to
# _prefix/share instead of _datadir to mirror how the install path is defined
# in the relevant CMakeLists.txt.
rm -rf %{buildroot}%{_prefix}/share/doc/xalan-c/api


%check
%ctest


# Required for EPEL8:
%ldconfig_scriptlets


%files
%license LICENSE
%doc CREDITS
%doc KEYS
%doc NOTICE
%doc README.md
%{_bindir}/Xalan
%{_libdir}/libxalanMsg.so.%{so_version}
%{_libdir}/libxalanMsg.so.%{so_version}.*
%{_libdir}/libxalan-c.so.%{so_version}
%{_libdir}/libxalan-c.so.%{so_version}.*


%files devel
%{_libdir}/libxalanMsg.so
%{_libdir}/libxalan-c.so
%{_includedir}/xalanc/
%dir %{_libdir}/cmake/XalanC
%{_libdir}/cmake/XalanC/*.cmake
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%license LICENSE
%doc CREDITS
%doc KEYS
%doc NOTICE
%doc README.md
%doc docs/*.md docs/images
%doc %{_vpath_builddir}/docs/doxygen/api
%doc samples


%changelog
* Wed Mar 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.0-6
- Commit KEYS (gpg keychain for source verification) to SCM rather than keeping
  it in the lookaside cache

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec  5 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.0-4
- Make -doc package arch again; there are indeed small differences by
  architecture. Note that 1.12.0-3 never made it to any buildroot, as the arch
  differences were flagged by koji.

* Fri Dec  4 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.0-3
- Make -doc package noarch

* Tue Dec  1 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.0-2
- Make spec file compatible with EPEL8: force CMake out-of-source build, add
  ldconfig_scriptlets macro, and add explicit dependency on graphviz (dot) for
  API docs

* Mon Nov 30 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.0-1
- New upstream version 1.12.0
- Source code signature verification
- New CMake build system
- Enable new optional ICU dependency
- Build API documentation with Doxygen

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.11.0-8
- Use power64 macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.11.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.11.0-3
- Fix build on aarch64

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.11.0-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Tue Oct 08 2013 Nick Le Mouton <nick@noodles.net.nz> - 1.11.0-1
- Rebuilt for xalan-c 1.11, fixes a few problems with using newer xerces-c

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-11
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.10.0-9
- Rebuilt with xerces-c 3.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 05 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.10.0-7
- Rebuild for newer xerces-c

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.10.0-4
- Rebuild for newer xerces-c

* Thu Jan 03 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.10.0-3
- Adding missing includes to fix build with gcc-4.3

* Mon Nov 19 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1.10.0-2
- Fix passing of compiler flags
- Bump to stable source instead of CVS snapshot
- Fixed License tag

* Thu Feb 15 2007 Till Maas <opensource till name> - 1.10.0-1
- Initial spec for fedora extras
