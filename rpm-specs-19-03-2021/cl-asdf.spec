Name:    cl-asdf
Version: 20101028
Release: 19%{?dist}
Source:  %{name}-%{version}.tar.bz2
Summary: Another System Definition Facility
URL:     http://www.cliki.net/asdf
License: MIT
BuildArch: noarch
BuildRequires: make
BuildRequires: texinfo-tex

Patch0:  cl-asdf-20101028-texinfo5.patch

%description
Another System Definition Facility (asdf) is a package format for
Common Lisp libraries.

%prep
%setup -q -n asdf
%patch0 -p1

%install
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-asdf
install -m 644 asdf.lisp %{buildroot}%{_datadir}/common-lisp/source/cl-asdf
install -m 644 wild-modules.lisp %{buildroot}%{_datadir}/common-lisp/source/cl-asdf

%build
cd doc
make

%files
%doc README doc/asdf
%dir %{_datadir}/common-lisp
%dir %{_datadir}/common-lisp/source
%{_datadir}/common-lisp/source/cl-asdf

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20101028-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101028-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 25 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 20101028-8
- Fix FTBFS with texinfo-5 (#992059, #1106048)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101028-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101028-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101028-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101028-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  9 2010 Anthony Green <green@fedoraproject.org> 20101028-1
- Upgrade.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071110-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071110-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 09 2008 Anthony Green <green@redhat.com> 20071110-5
.- Rename install dir "cl-asdf"

* Sun Jul 06 2008 Anthony Green <green@redhat.com> 20071110-4
- Take ownership of all directories we create.

* Thu Jan 03 2008 Anthony Green <green@redhat.com> 20071110-3
- Take ownership of all directories we create.

* Sat Nov 11 2007 Anthony Green <green@redhat.com> 20071110-2
- Update install directory.
- Add documentation.

* Sat Nov 11 2007 Anthony Green <green@redhat.com> 20071110-1
- Initial version.
