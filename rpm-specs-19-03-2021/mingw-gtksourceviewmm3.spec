%{?mingw_package_header}

%global pkgname gtksourceviewmm3

Name:          mingw-%{pkgname}
Version:       3.18.0
Release:       10%{?dist}
Summary:       MinGW Windows GtkSourceViewmm library
License:       LGPLv2+
BuildArch:     noarch
URL:           https://wiki.gnome.org/Projects/GtkSourceView
Source0:       http://download.gnome.org/sources/gtksourceviewmm/3.18/gtksourceviewmm-%{version}.tar.xz

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gtkmm30
BuildRequires: mingw32-gtksourceview3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gtkmm30
BuildRequires: mingw64-gtksourceview3


%description
MinGW Windows GtkSourceViewmm library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GtkSourceViewmm library

%description -n mingw32-%{pkgname}
MinGW Windows GtkSourceViewmm library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GtkSourceViewmm library

%description -n mingw64-%{pkgname}
MinGW Windows GtkSourceViewmm library.


%{?mingw_debug_package}


%prep
%setup -q -n gtksourceviewmm-%{version}


%build
%mingw_configure --disable-documentation --disable-static
%mingw_make_build


%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libgtksourceviewmm-3.0-0.dll
%{mingw32_includedir}/gtksourceviewmm-3.0/
%{mingw32_libdir}/gtksourceviewmm-3.0/
%{mingw32_libdir}/libgtksourceviewmm-3.0.dll.a
%{mingw32_libdir}/pkgconfig/gtksourceviewmm-3.0.pc

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libgtksourceviewmm-3.0-0.dll
%{mingw64_includedir}/gtksourceviewmm-3.0/
%{mingw64_libdir}/gtksourceviewmm-3.0/
%{mingw64_libdir}/libgtksourceviewmm-3.0.dll.a
%{mingw64_libdir}/pkgconfig/gtksourceviewmm-3.0.pc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:40:04 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.18.0-9
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 22 2017 Sandro Mani <manisandro@gmail.com> - 3.18.0-1
- Update to 3.18.0

* Mon Jun 22 2015 Sandro Mani <manisandro@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Sat Mar 21 2015 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Initial package
