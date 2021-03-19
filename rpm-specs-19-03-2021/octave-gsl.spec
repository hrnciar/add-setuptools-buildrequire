%global octpkg gsl

Name:		octave-%{octpkg}
Version:	2.1.1
Release:	2%{?dist}
Summary:	Octave bindings to the GNU Scientific Library
# Some test files are GPLv3+ but they're not shipped.
License:	GPLv2+
URL:		http://octave.sourceforge.net/gsl/
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:	octave-devel
BuildRequires:	gsl-devel

Requires:	octave(api) = %{octave_api}
Requires(post):	octave
Requires(postun): octave

%description
The octave-gsl package provides an Octave binding to functions
in the Gnu Scientific Library, such as
* Airy functions
* Bessel functions
* Conical functions
* Debye functions
* Riemann Beta and Gamma functions
* Sine and cosine integrals
* Wigner coefficients 3-j, 6-j and 9-j coefficients

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/on_uninstall.m

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Orion Poplawski <orion@nwra.com> - 2.1.1-1
- Update to 2.1.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 2.0.0-12
- Rebuild with octave 64bit indexes

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.0-11
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 2.0.0-9
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-7
- Rebuild for octave 4.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 9 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-1
- Update to 2.0.0
- Use %%license

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.8-15
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.8-13
- Patch to build against gsl v2. 

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.8-12
- Rebuild for octave 4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.8-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 1.0.8-7
- Rebuild for octave 3.8.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.8-3
- Bump spec.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 27 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.8-1
- Initial release.
