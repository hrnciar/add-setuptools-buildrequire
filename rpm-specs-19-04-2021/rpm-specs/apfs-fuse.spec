# Force out of source build
%undefine __cmake_in_source_build

%global date         20200928
%global gittag       290028bea888fa80a9389ddeab26b8123c7c9474
%global short_gittag %(c=%{gittag}; echo ${c:0:7})

Name:          apfs-fuse
Summary:       A read-only FUSE driver for Apple's APFS
Version:       0
Release:       15.%{date}git%{short_gittag}%{?dist}
License:       GPLv2+
URL:           https://github.com/sgan81/apfs-fuse
Source0:       https://github.com/sgan81/%{name}/archive/%{short_gittag}/%{name}-%{short_gittag}.tar.gz
Source1:       https://github.com/lzfse/lzfse/archive/lzfse-1.0.tar.gz
Provides:      bundled(lzfse) = 1.0
Requires:      fuse3
BuildRequires: gcc gcc-c++
BuildRequires: fuse3-devel libicu-devel zlib-devel bzip2-devel
BuildRequires: cmake git

%description
apfs-fuse is a read-only driver for the new Apple File System, APFS. Since
Apple didn't document the disk format, this driver should be considered
experimental. Not all compression methods are supported yet, thus the driver
may return compressed files instead of uncompressed ones.

%prep
%autosetup -n %{name}-%{gittag} -S git
cd 3rdparty
rmdir lzfse
tar zxf %{SOURCE1}
mv lzfse-* lzfse

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a %{_vpath_builddir}/apfs-* %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_sbindir}
ln -sr %{buildroot}/%{_bindir}/apfs-fuse %{buildroot}/%{_sbindir}/mount.apfs

%files
%{_bindir}/apfs-*
%{_sbindir}/mount.apfs
%doc README.md
%license LICENSE

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20200928git290028b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0-14.20200928git290028b
- Require fuse3 not fuse as it's built against that

* Mon Sep 28 2020 Bastien Nocera <bnocera@redhat.com> - 0-13.20200928git290028b
- Update to latest version
- Remove -march=native work-around

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20190723git309ecb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 Bastien Nocera <bnocera@redhat.com> - 0-11.git
+ apfs-fuse-0-11.git
- Update to latest git version, and fuse3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20180628gitbe55741
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0-9.20180628gitbe55741
- Rebuild for ICU 65

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20180628gitbe55741
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20180628gitbe55741
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0-6.20180628gitbe55741
- Rebuild for ICU 63

* Thu Jul 19 2018 Bastien Nocera <bnocera@redhat.com> - 0-5.git
+ apfs-fuse-0-5.git
- Use glib'c xattr.h instead of libattr's
- Use git to apply patches

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20180628gitbe55741
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0-3.20180628gitbe55741
- Rebuild for ICU 62

* Mon Jul 02 2018 Bastien Nocera <bnocera@redhat.com> - 0-2.git20180628gitbe55741
- Add a "mount.apfs" link

* Mon Jul 02 2018 Bastien Nocera <bnocera@redhat.com> - 0-1.git20180628gitbe55741
- First Fedora version based off package by Lawrence
  R. Rogers <lrr@cert.org>
