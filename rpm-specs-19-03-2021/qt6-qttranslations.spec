%global qt_module qttranslations

Summary: Qt6 - QtTranslations module
Name:    qt6-%{qt_module}
Version: 6.0.1
Release: 1%{?dist}

License: LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

BuildArch: noarch

BuildRequires: cmake
BuildRequires: ninja-build
## versioning recently dropped, but could do >= %%majmin if needed --rex
BuildRequires: qt6-qtbase-devel
# for lrelease
BuildRequires: qt6-linguist
BuildRequires: qt6-qttools-devel

# help system-config-language and dnf/yum langpacks pull these in
%if 0%{?_qt6:1}
Provides: %{_qt6}-ar = %{version}-%{release}
Provides: %{_qt6}-ca = %{version}-%{release}
Provides: %{_qt6}-cs = %{version}-%{release}
Provides: %{_qt6}-da = %{version}-%{release}
Provides: %{_qt6}-de = %{version}-%{release}
Provides: %{_qt6}-es = %{version}-%{release}
Provides: %{_qt6}-fa = %{version}-%{release}
Provides: %{_qt6}-fi = %{version}-%{release}
Provides: %{_qt6}-fr = %{version}-%{release}
Provides: %{_qt6}-gl = %{version}-%{release}
Provides: %{_qt6}-gd = %{version}-%{release}
Provides: %{_qt6}-he = %{version}-%{release}
Provides: %{_qt6}-hu = %{version}-%{release}
Provides: %{_qt6}-hr = %{version}-%{release}
Provides: %{_qt6}-it = %{version}-%{release}
Provides: %{_qt6}-ja = %{version}-%{release}
Provides: %{_qt6}-ko = %{version}-%{release}
Provides: %{_qt6}-lt = %{version}-%{release}
Provides: %{_qt6}-lv = %{version}-%{release}
Provides: %{_qt6}-nl = %{version}-%{release}
Provides: %{_qt6}-nn = %{version}-%{release}
Provides: %{_qt6}-pl = %{version}-%{release}
Provides: %{_qt6}-pt = %{version}-%{release}
Provides: %{_qt6}-pt_BR = %{version}-%{release}
Provides: %{_qt6}-ru = %{version}-%{release}
Provides: %{_qt6}-sk = %{version}-%{release}
Provides: %{_qt6}-sl = %{version}-%{release}
Provides: %{_qt6}-sv = %{version}-%{release}
Provides: %{_qt6}-uk = %{version}-%{release}
Provides: %{_qt6}-zh_CN = %{version}-%{release}
Provides: %{_qt6}-zh_TW = %{version}-%{release}
%endif

%description
%{summary}.


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}


%build
%cmake_qt6

%cmake_build


%install
%cmake_install

# not used currently, since we track locales manually to keep %%files/Provides sync'd -- rex
#find_lang qttranslations --all-name --with-qt --without-mo

%files
%license LICENSE.*
%lang(ar) %{_qt6_translationdir}/*_ar.qm
%lang(bg) %{_qt6_translationdir}/*_bg.qm
%lang(ca) %{_qt6_translationdir}/*_ca.qm
%lang(cs) %{_qt6_translationdir}/*_cs.qm
%lang(da) %{_qt6_translationdir}/*_da.qm
%lang(de) %{_qt6_translationdir}/*_de.qm
%lang(es) %{_qt6_translationdir}/*_es.qm
%lang(en) %{_qt6_translationdir}/*_en.qm
%lang(fa) %{_qt6_translationdir}/*_fa.qm
%lang(fi) %{_qt6_translationdir}/*_fi.qm
%lang(fr) %{_qt6_translationdir}/*_fr.qm
%lang(gl) %{_qt6_translationdir}/*_gd.qm
%lang(gl) %{_qt6_translationdir}/*_gl.qm
%lang(he) %{_qt6_translationdir}/*_he.qm
%lang(hu) %{_qt6_translationdir}/*_hu.qm
%lang(hu) %{_qt6_translationdir}/*_hr.qm
%lang(it) %{_qt6_translationdir}/*_it.qm
%lang(ja) %{_qt6_translationdir}/*_ja.qm
%lang(ko) %{_qt6_translationdir}/*_ko.qm
%lang(lt) %{_qt6_translationdir}/*_lt.qm
%lang(lv) %{_qt6_translationdir}/*_lv.qm
%lang(nl) %{_qt6_translationdir}/*_nl.qm
%lang(nn) %{_qt6_translationdir}/*_nn.qm
%lang(pl) %{_qt6_translationdir}/*_pl.qm
%lang(pt) %{_qt6_translationdir}/*_pt.qm
%lang(pt_BR) %{_qt6_translationdir}/*_pt_BR.qm
%lang(ru) %{_qt6_translationdir}/*_ru.qm
%lang(sk) %{_qt6_translationdir}/*_sk.qm
%lang(sl) %{_qt6_translationdir}/*_sl.qm
%lang(sv) %{_qt6_translationdir}/*_sv.qm
%lang(sv) %{_qt6_translationdir}/*_tr.qm
%lang(uk) %{_qt6_translationdir}/*_uk.qm
%lang(zh_CN) %{_qt6_translationdir}/*_zh_CN.qm
%lang(zh_TW) %{_qt6_translationdir}/*_zh_TW.qm


%changelog
* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-1
- 6.0.0
