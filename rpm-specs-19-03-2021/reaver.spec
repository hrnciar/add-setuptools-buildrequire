Name:           reaver
Version:        1.6.6
Release:        3%{?dist}
Summary:        Brute force attack against Wifi Protected Setup

License:        GPLv2
URL:            https://github.com/t6x/reaver-wps-fork-t6x
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         reaver-lwe-unbundle.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  wireless-tools-devel
BuildRequires:  sqlite-devel
# https://fedorahosted.org/fpc/ticket/418
Provides:       bundled(wpa_supplicant) = 0.7.3
# change to requires once pixiewps will get stable
Recommends:     pixiewps

%description
Reaver implements a brute force attack against Wifi Protected Setup (WPS)
registrar PINs in order to recover WPA/WPA2 passphrases, as described in
http://sviehb.files.wordpress.com/2011/12/viehboeck_wps.pdf.

%prep
%autosetup -p1

# Remove executable mode from sources
find . -type f -perm /111 -regex ".*\.[ch]" -exec chmod a-x {} \;

# Unbundle wireless-tools
rm -rf src/lwe

%build
pushd src
    %configure
    %make_build
popd

%install
pushd src
    %make_install
popd
mkdir -p %{buildroot}%{_mandir}/man1
install -pm0644 docs/reaver.1 %{buildroot}%{_mandir}/man1/
touch %{buildroot}%{_localstatedir}/lib/reaver/reaver.db

%files
%doc docs/README docs/README.REAVER docs/README.WASH
%license docs/LICENSE
%{_bindir}/reaver
%{_bindir}/wash
%ghost %{_localstatedir}/lib/reaver/reaver.db
%{_mandir}/man1/*.1*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.6-1
- Update to 1.6.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Jaroslav ??karvada <jskarvad@redhat.com> - 1.6.5-1
- New version
  Resolves: rhbz#1577430

* Fri Apr 06 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.4-1
- Swith to fork and update to 1.6.4
- Clean spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Jaroslav ??karvada <jskarvad@redhat.com> - 1.4-3
- Fixed CFLAGS in wps/libwps and built them with -fPIC (by cflags patch)

* Fri Nov 14 2014 James W. Harshaw <jwharshaw@gmail.com> - 1.4-2
- Added bundled library modification

* Sat Feb 22 2014 Jaroslav ??karvada <jskarvad@redhat.com> - 1.4-1
- Initial release
