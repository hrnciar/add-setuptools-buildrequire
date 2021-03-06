Name:           spim
Version:        20200117
Release:        0.3.svn%{?dist}
Summary:        An assembly language MIPS32 simulator
License:        BSD
URL:            http://spimsimulator.sourceforge.net/

# These source files are generated from SPIM's Subversion repository.
#
# Run "svn co http://svn.code.sf.net/p/spimsimulator/code/ spimsimulator"
#     "cd spimsimulator"
# For each PROJECT: spim, CPU, and Documentation:
#     "tar czvf spimsimulator-[PROJECT]-[DATE].tar.gz [PROJECT]"
#
# The sources are taken from SVN because the upstream tarballs contain
# compiled code.
Source0:        spimsimulator-spim-20200117.tar.gz
Source1:        spimsimulator-CPU-20200117.tar.gz
Source2:        spimsimulator-Documentation-20200117.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++ flex bison

%description
spim is a self-contained simulator that runs MIPS32 programs. It reads and
executes assembly language programs written for this processor. spim also
provides a simple debugger and minimal set of operating system services.

%prep
%setup -q -T -a 0 -c
%setup -q -T -D -a 1 -c
%setup -q -T -D -a 2 -c -n spim-%{version}/spim

# Fix EOL encoding.
sed 's/\r//' README > README.unix
touch -r README README.unix
mv -f README.unix README

# Fix some permissions.
find . -type f -perm /0111 -print0 | xargs -0 chmod a-x

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 -D Documentation/spim.man %{buildroot}%{_mandir}/man1/spim.1

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%doc README

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200117-0.3.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200117-0.2.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 W. Michael Petullo <mike[@]flyn.org> - 20200117-0.1.svn
- New upstream version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190413-0.8.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 W. Michael Petullo <mike[@]flyn.org> - 20190413-0.7.svn
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20171115-0.6.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20171115-0.5.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 W. Michael Petullo <mike[@]flyn.org> - 20171115-0.4.svn
- Add gcc-c++ to BuildRequires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171115-0.3.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20171115-0.2.svn
- Escape macros in %%changelog

* Wed Nov 15 2017 Stephen Benjamin <stephen@bitbin.de> - 20151117-0.1.svn
- Fix %%setup macros
- Update to latest version in SVN
- Makefile patch no longer required

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20111122-0.14.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20111122-0.13.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20111122-0.12.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20111122-0.11.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-0.10.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20111122-0.9.svn
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-0.8.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-0.7.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-0.6.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-0.5.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-0.4.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-0.3.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 W. Michael Petullo <mike[@]flyn.org> - 20111122-0.1.svn
- Install README
- Fix ownership of files in /usr/share
- Fix permissions

* Tue Nov 22 2011 W. Michael Petullo <mike[@]flyn.org> - 20111122-0.1.svn
- Update to upstream subversion
- Add instructions documenting how to create source tarballs
- Remove Makefile patch; it is upstream
- Use optflags
- Fix ownership of man pages
- BuildRequires flex
- Fix EOL encoding of README
- Fix typo in smp_mflags

* Tue Apr 19 2011 W. Michael Petullo <mike[@]flyn.org> - 9.0.5-1
- Initial package
