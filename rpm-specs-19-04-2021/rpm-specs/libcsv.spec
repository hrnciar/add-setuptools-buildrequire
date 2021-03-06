Name:		libcsv
Version:	3.0.3
Release:	15%{?dist}
Summary:	Small, simple and fast CSV library

License:	LGPLv2+
URL:		http://sourceforge.net/projects/libcsv/
Source0:	http://downloads.sourceforge.net/project/libcsv/libcsv/libcsv-%{version}/libcsv-%{version}.tar.gz
Patch0:		fix-soname-version.patch

BuildRequires:  gcc
BuildRequires: make
%description
libcsv is a small, simple and fast CSV library written in pure ANSI C89
that can read and write CSV data. It provides a straight-forward interface
using callback functions to handle parsed fields and rows and can parse
improperly formatted CSV files.

%package devel
Summary:	Small, simple and fast CSV library - development package
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
libcsv is a small, simple and fast CSV library written in pure ANSI C89
that can read and write CSV data. It provides a straight-forward interface
using callback functions to handle parsed fields and rows and can parse
improperly formatted CSV files.

This package contains header file and development libraries.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%{_libdir}/libcsv.so.3
%{_libdir}/libcsv.so.3.0.3
%doc ChangeLog FAQ COPYING.LESSER

%files devel
%{_includedir}/csv.h
%{_libdir}/libcsv.so
%doc %{_mandir}/man3/csv.3*
%exclude %{_libdir}/libcsv.la

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Jan Holcapek <holcapek@gmail.com> - 3.0.3-2
- Fixed trailing white space in fix-soname-version.patch.

* Fri Jun 13 2014 Jan Holcapek <holcapek@gmail.com> - 3.0.3-1
- Initial build.
