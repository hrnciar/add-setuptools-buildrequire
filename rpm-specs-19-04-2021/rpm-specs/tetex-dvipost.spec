%define real_name dvipost
%{!?_texmf_vendor: %define _texmf %(eval "echo `kpsewhich -expand-var '$TEXMFDIST'`")}

Name:           tetex-%{real_name}
Version:        1.1
Release:        33%{?dist}
Summary:        LaTeX post filter command to support change bars and overstrike mode

License:        GPLv2+
URL:            http://efeu.cybertec.at/
Source0:        http://efeu.cybertec.at/%{real_name}.tar.gz
Patch0:         %{name}-destdir.patch

BuildRequires: make
BuildRequires:  tex(latex)
BuildRequires:  /usr/bin/kpsewhich
BuildRequires:  gcc-c++

Requires:	tex(latex)

%description
The command dvipost is a post procesor for dvi files, created by latex
or tex. It is used for special modes, which normally needs the support
of dvi drivers (such as dvips). With dvipost, this features could be
implemented independent of the preferred driver. Currently, the post
processor supports layout raster, change bars and overstrike mode.

%prep
%setup -q -n %{real_name}-%{version}
%patch0 -p1


%build
%configure
%make_build

%install
%make_install


%post -p /usr/bin/texhash


%postun -p /usr/bin/texhash


%files
%license COPYING
%{_bindir}/*
%{_texmf_vendor}/tex/latex/misc/*

%doc README NOTES dvipost.html
%{_mandir}/man*/*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1-28
- Add gcc-c++ as BR
- spec cleanup

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.1-21
- Fix build

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Jos?? Matos <jamatos@fedoraproject.org> - 1.1-16
- Update spec file to take into account the new texlive (F18+)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1-9
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-8
- License fix, rebuild for devel (F8).

* Sat Apr 21 2007 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-7
- Rebuild (for F7).

* Mon Sep 11 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-6
- Rebuild for FC6

* Sat May  6 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-5
- Clean up spec file

* Thu Apr 27 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-4
- Rename package to tetex-dvipost

* Thu Apr 27 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-3
- Capitalize Summary, fix spell error in description, rework
  invocation of post and postun calls (thanks to Patrice Dumas)
- Add tetex-latex to Requires and BuildRequires.
- Add tetex-fonts to Requires to satisfy direct dependency on texhash

* Thu Apr 27 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-2
- Add new entries to %%doc and expand description

* Wed Apr 26 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.1-1
- First build
