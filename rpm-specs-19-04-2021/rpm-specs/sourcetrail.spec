Name:		sourcetrail
Version:	2021.1.30
Release:	1%{?dist}
Summary:	a free and open-source interactive source explorer

License:	GPLv3
URL:		https://www.sourcetrail.com/
Source0:	https://github.com/CoatiSoftware/Sourcetrail/archive/%{version}.tar.gz

# See https://github.com/catchorg/Catch2/issues/2178
Patch2:		minsigstksz.patch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	boost-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	systemd-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	openssl-devel
BuildRequires:	libdrm-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXrender-devel
BuildRequires:	libXi-devel
BuildRequires:	ImageMagick
BuildRequires:	clang11-devel
BuildRequires:	llvm11-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick

Requires:	boost-system
Requires:	boost-program-options
Requires:	boost-filesystem
Requires:	boost-date-time
Requires:	qt5-qtbase
Requires:	qt5-qtsvg

%description

Sourcetrail is a free and open-source cross-platform source explorer that helps
you get productive on unfamiliar source code.


%prep
%autosetup -n Sourcetrail-%{version} -p1


%build

%cmake -GNinja -DBoost_USE_STATIC_LIBS=OFF -DBUILD_SHARED_LIBS=OFF\
  -DBUILD_CXX_LANGUAGE_PACKAGE=ON -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_PREFIX_PATH=%{_libdir}/llvm11/lib/cmake/clang

%cmake_build

%check

%install
mkdir -p %{buildroot}/%{_bindir}
cp "%{_vpath_builddir}"/app/Sourcetrail %{buildroot}/%{_bindir}/sourcetrail
cp "%{_vpath_builddir}"/app/sourcetrail_indexer %{buildroot}/%{_bindir}/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications setup/Linux/data/sourcetrail.desktop
mkdir -p %{buildroot}/%{_datadir}/mime/packages
cp setup/Linux/data/sourcetrail-mime.xml %{buildroot}/%{_datadir}/mime/packages/
for sz in 48 64 128 256 512
do
  mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/${sz}x${sz}/apps/
  convert bin/app/data/gui/icon/logo_1024_1024.png -resize ${sz}x${sz} %{buildroot}/%{_datadir}/icons/hicolor/${sz}x${sz}/apps/sourcetrail.png
done

%files
%license LICENSE.txt

%{_bindir}/sourcetrail
%{_bindir}/sourcetrail_indexer
%{_datadir}/applications/sourcetrail.desktop
%{_datadir}/icons/hicolor/*/apps/sourcetrail.png
%{_datadir}/mime/packages/sourcetrail-mime.xml


%changelog
* Tue Mar 16 2021 sguelton@redhat.com - 2021.1.30-1
- Upstream release

* Thu Mar 11 2021 sguelton@redhat.com - 2020.4.35-1
- Upstream release

* Thu Mar 11 2021 sguelton@redhat.com - 2020.2.43-13
- LLVM 12.0.0 rc3

* Wed Mar 10 2021 sguelton@redhat.com - 2020.2.43-12
- rebuilt

* Thu Feb 25 2021 sguelton@redhat.com - 2020.2.43-11
- Rebuild for llvm 12.0.0rc2

* Thu Feb 18 2021 sguelton@redhat.com - 2020.2.43-10
- rebuilt for llvm 12.0.0rc1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.2.43-8
- Rebuilt for Boost 1.75

* Fri Jan 22 2021 Tom Stellard <tstellar@redhat.com> - 2020.2.43-7
- Rebuild for clang-11.1.0

* Wed Dec 02 2020 sguelton@redhat.com - 2020.2.43-6
- Rebuilt for llvm 11.0.1rc1

* Wed Oct 14 2020 sguelton@redhat.com - 2020.2.43-5
- Rebuilt for llvm 11.0.0

* Wed Oct 07 2020 sguelton@redhat.com - 2020.2.43-4
- rebuilt for llvm-11.0.0rc5

* Wed Jul 29 2020 sguelton@redhat.com - 2020.2.43-3
- Use %%license macro

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 sguelton@redhat.com 2020.1.117-1
- Initial version
