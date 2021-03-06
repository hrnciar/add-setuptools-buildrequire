%global gitcommit 4ba507e27a209a36589191f2fa28fc9983cf57f8
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global snapshotdate 20201128

Name: kdump-anaconda-addon
Version: 006
Release: 2.%{snapshotdate}git%{gitshortcommit}%{?dist}
Url: https://github.com/daveyoung/kdump-anaconda-addon
License: GPLv2
Summary: Kdump configuration anaconda addon

BuildArch: noarch
Requires: anaconda >= 34.13
Requires: hicolor-icon-theme
BuildRequires: intltool gettext
BuildRequires: make
Obsoletes: kexec-tools-anaconda-addon < 2.0.17-9
Provides: kexec-tools-anaconda-addon = %{version}-%{release}

Source0: https://github.com/daveyoung/kdump-anaconda-addon/archive/%{gitcommit}/kdump-anaconda-addon-%{gitshortcommit}.tar.gz

%description
Kdump anaconda addon

%prep
%autosetup -n %{name}-%{gitcommit}

%build

%install
%make_install

%find_lang kdump-anaconda-addon

%files -f kdump-anaconda-addon.lang
%doc README
%license LICENSE
%{_datadir}/anaconda/addons/com_redhat_kdump
%{_datadir}/anaconda/dbus/confs/org.fedoraproject.Anaconda.Addons.Kdump.conf
%{_datadir}/anaconda/dbus/services/org.fedoraproject.Anaconda.Addons.Kdump.service
%{_datadir}/icons/hicolor/scalable/apps/kdump.svg

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 006-2.20201128git4ba507e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Kairui Song <kasong@redhat.com> - 006-1.20201128git4ba507e
- Update to latest git snapshot (20201128)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 005-9.20200220git80aab11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Kairui Song <kasong@redhat.com> - 005-8.20200220git80aab11
- Update to latest git snapshot (20200220)

* Tue Jan 14 2020 Kairui Song <kasong@redhat.com> - 005-7.20200114git122ccd9
- Update to latest git snapshot (20200114)

* Wed Aug 7 2019 Kairui Song <kasong@redhat.com> - 005-6.20190730gitc109552
- Update to latest git snapshot (20190723)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 005-5.20190103gitb16ea2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 005-4.20190103gitb16ea2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 3 2019 Kairui Song <kasong@redhat.com> - 005-3.20190103gitb16ea2c
- Update to latest git snapshot (20190103)

* Tue Aug 7 2018 Kairui Song <kasong@redhat.com> - 005-2.20180730git966223e
- Bump obsoleted kexec-tools-anaconda-addon version
- Remove redundant source files

* Tue Aug 7 2018 Kairui Song <kasong@redhat.com> - 005-1.20180730git966223e
- Update to latest git snapshot (20180730)

* Mon Jul 9 2018 Kairui Song <kasong@redhat.com> - 005-1.20180626git8b243e3
- Initial package for kdump-anaconda-addon
