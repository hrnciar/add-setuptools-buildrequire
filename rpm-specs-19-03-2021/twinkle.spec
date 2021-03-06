%undefine __cmake_in_source_build

%global commit b7965d023cb68bce6d9495eb6afbc73206c1afef
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snap .git%{shortcommit}

Name:           twinkle
Version:        1.10.2
Release:        9%{?snap}%{?dist}
Summary:        SIP-based VoIP client

# Incorrect FSF addresses: https://github.com/LubosD/twinkle/issues/71
License:        GPLv2+
URL:            https://github.com/LubosD/%{name}
%if 0%{?commit:1}
Source0:        https://github.com/LubosD/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:        https://github.com/LubosD/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  alsa-lib-devel
BuildRequires:  bcg729-devel
BuildRequires:  bison
BuildRequires:  ccrtp-devel
BuildRequires:  flex
# The Fedora package is incompatible with the version required by twinkle
# BuildRequires:  ilbc-devel
BuildRequires:  libatomic
BuildRequires:  libsndfile-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzrtpcpp-devel
BuildRequires:  file-devel
BuildRequires:  gsm-devel
BuildRequires:  readline-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  ucommon-devel

Requires:       hicolor-icon-theme


%description
Twinkle is a SIP-based VoIP client.


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif


%build
# QT clients need to build with -fPIC to avoid local binding and copy
# relocs.
export CXXFLAGS="-fPIC $RPM_OPT_FLAGS"

%cmake -DWITH_ZRTP=On \
    -DWITH_SPEEX=On \
    -DWITH_ILBC=Off \
    -DWITH_DIAMONDCARD=Off \
    -DWITH_GSM=On \
    -DWITH_G729=On
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop || :

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_bindir}/%{name}-console
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/twinkle.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%doc %{_mandir}/man1/%{name}.1*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-9.gitb7965d0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 2020 Sandro Mani <manisandro@gmail.com> - 1.10.2-8.gitb7965d0
- Update to latest git
- Enable bcg729 codec

* Thu Oct 1 2020 Jeff Law <law@redhat.com> - 1.10.2-7
- Build application with -fPIC to avoid local binding
- Re-enable LTO

* Mon Aug 17 2020 Sandro Mani <manisandro@gmail.com> - 1.10.2-6
- Disable LTO, causes segfault on startup

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.10.2-2
- Rebuild for readline 8.0

* Fri Feb 15 2019 Sandro Mani <manisandro@gmail.com> - 1.10.2-1
- Update to 1.10.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-10.gitda70392
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Sandro Mani <manisandro@gmail.com> - 1.10.1-9.gitda70392
- Update to latest git

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.10.1-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.10.1-2
- Rebuild for readline 7.x

* Fri Oct 07 2016 Sandro Mani <manisandro@gmail.com> - 1.10.1-1
- Update to 1.10.1

* Fri Jul 22 2016 Sandro Mani <manisandro@gmail.com> - 1.10.0-4
- Disable G729 support

* Wed Jul 20 2016 Sandro Mani <manisandro@gmail.com> - 1.10.0-3
- Add twinkle_phone-role.patch

* Wed Jul 20 2016 Sandro Mani <manisandro@gmail.com> - 1.10.0-2
- Remove git snapshot macros
- Enable gsm, g729
- Use cmake style dependencies
- Add BR: gcc-c++
- Mark man as %%doc

* Mon Jul 18 2016 Sandro Mani <manisandro@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Thu Jul 14 2016 Sandro Mani <manisandro@gmail.com> - 1.9.0-1.gitbe8b8df
- Initial package of Qt5 port
