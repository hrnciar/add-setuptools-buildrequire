Name:           webp-pixbuf-loader
Version:        0.0.2
Release:        2%{?dist}
Summary:        WebP image loader for GTK+ applications

License:        LGPLv2+
URL:            https://github.com/aruiz/webp-pixbuf-loader
Source0:        https://github.com/aruiz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc gcc-c++
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libwebp-devel

Requires:       gdk-pixbuf2%{?_isa}

%description
webp-pixbuf-loader contains a plugin to load WebP images in GTK+ applications

%prep
%autosetup

%build
%meson -Dgdk_pixbuf_query_loaders_path=gdk-pixbuf-query-loaders-%{__isa_bits}
%meson_build

%install
%meson_install

%files
%license LICENSE.LGPL-2
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-webp.so
%{_datadir}/thumbnailers/webp-pixbuf.thumbnailer

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.2
- Update to 0.0.2
- Install webp-pixbuf.thumbnailer
- Remove extra license text file, now bundled in the release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-10.20191003gitfb04954
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-9.20191003gitfb04954
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct  3 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.1-8.20191003gitfb04954
- Newer snapshot moving to meson

* Mon Sep 30 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.1-7.20190930gitddbcacf
- Pick an upstream crasher fix with a recent snapshot

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6.20180710git9b92950
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5.20180710git9b92950
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4.20180710git9b92950
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Yanko Kaneti <yaneti@declera.com> - 0.0.1-3.20180710git9b92950
- Initial packaging
- Address review commments (#1599839)
- Add license text from gnu.org
- BR: gcc-c++ for some Cmake reason
