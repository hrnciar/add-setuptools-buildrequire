Name:           libportal
Version:        0.4
Release:        1%{?dist}
Summary:        Flatpak portal library
License:        LGPLv2+
Url:            https://github.com/flatpak/libportal
Source:         https://github.com/flatpak/libportal/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
# For doc links
BuildRequires:  pipewire-doc

%description
libportal provides GIO-style asynchronous APIs for most Flatpak portals.

%package devel
Summary: Development files and libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with %name.

%package devel-doc
Summary: Development documentation for libportal
BuildArch: noarch

%description devel-doc
libportal provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides development documentations for libportal.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md NEWS
%{_libdir}/libportal.so.0*

%files devel
%{_includedir}/libportal
%{_libdir}/libportal.so
%{_libdir}/pkgconfig/libportal.pc

%files devel-doc
%{_datadir}/gtk-doc/html/libportal

%changelog
* Tue Apr 06 2021 David King <amigadave@amigadave.com> - 0.4-1
- Update to 0.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Bastien Nocera <bnocera@redhat.com> - 0.3-3
+ libportal-0.3-3
- Add forgotten dist tag to Release (#1790258)

* Mon Jan 06 2020 Bastien Nocera <bnocera@redhat.com> - 0.3-2
+ libportal-0.3-2
- Add COPYING file to package

* Mon Jan 06 2020 Bastien Nocera <bnocera@redhat.com> - 0.3-1
+ libportal-0.3-1
- Update to 0.3

* Wed Dec 11 2019 Bastien Nocera <bnocera@redhat.com> - 0.1-0.1.20191211git7355b1e
+ libportal-0.1-0.20191211git7355b1e
