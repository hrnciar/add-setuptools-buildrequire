%global uuid com.chatterino.chatterino

# Git submodules
#   * libcommuni
%global commit2         05e929254b43a464b2345066fc1ff007e40077ff
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

#   * settings
%global commit3         6a71d6c395af2134ff56c50a5d056866ac4f3134
%global shortcommit3    %(c=%{commit3}; echo ${c:0:7})

#   * signals
%global commit4         baf5bb04bd13b090e405e0447c89a811f7e23ddc
%global shortcommit4    %(c=%{commit4}; echo ${c:0:7})

#   * serialize
%global commit5         7d37cbfd5ac3bfbe046118e1cec3d32ba4696469
%global shortcommit5    %(c=%{commit5}; echo ${c:0:7})

#   * qtkeychain
%global commit8         de954627363b0b4bff9a2616f1a409b7e14d5df9
%global shortcommit8    %(c=%{commit8}; echo ${c:0:7})

Name:           chatterino2
Version:        2.3.0
Release:        1%{?dist}
Summary:        Chat client for twitch.tv

# Boost Software License (v1.0) Boost Software License 1.0
# -----------------------------------------------------------------------
# resources/licenses/boost_boost.txt
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# lib/libcommuni/
#
# Expat License
# -------------
# lib/serialize/
# lib/signals/
# resources/
#
# Mozilla Public License (v1.1) GNU General Public License (v2 or later) or GNU Lesser General Public License (v2.1 or later)
# ---------------------------------------------------------------------------------------------------------------------------
# lib/libcommuni/
#
# zlib/libpng license Aladdin Free Public License
# -----------------------------------------------
# lib/websocketpp/
#
License:        MIT and Boost and BSD and zlib and GPLv2+ and LGPLv2+ and MPLv1.1

URL:            https://github.com/Chatterino/chatterino2
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source2:        https://github.com/hemirt/libcommuni/archive/%{commit2}/libcommuni-%{shortcommit2}.tar.gz
Source3:        https://github.com/pajlada/settings/archive/%{commit3}/settings-%{shortcommit3}.tar.gz
Source4:        https://github.com/pajlada/signals/archive/%{commit4}/signals-%{shortcommit4}.tar.gz
Source5:        https://github.com/pajlada/serialize/archive/%{commit5}/serialize-%{shortcommit5}.tar.gz
Source8:        https://github.com/Chatterino/qtkeychain/archive/%{commit8}/qtkeychain-%{shortcommit8}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libsecret-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  rapidjson-devel
BuildRequires:  websocketpp-devel

BuildRequires:  cmake(Qt5Core) >= 5.12
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)

Requires:       hicolor-icon-theme

# Current submodules patched so not possible to build with system packages
#   * https://github.com/Chatterino/chatterino2/issues/1444
Provides:       bundled(libcommuni) = 3.6.0
Provides:       bundled(qtkeychain) = 0.9.1~git%{shortcommit8}
Provides:       bundled(serialize) = 0~git%{shortcommit5}
Provides:       bundled(settings) = 0~git%{shortcommit3}
Provides:       bundled(signals) = 0~git%{shortcommit4}

%description
Chatterino 2 is the second installment of the Twitch chat client series
"Chatterino".


%prep
%setup -q
%setup -q -D -T -a2
%setup -q -D -T -a3
%setup -q -D -T -a4
%setup -q -D -T -a5
%setup -q -D -T -a8

mv libcommuni-%{commit2}/*  lib/libcommuni
mv settings-%{commit3}/*    lib/settings
mv signals-%{commit4}/*     lib/signals
mv serialize-%{commit5}/*   lib/serialize
mv qtkeychain-%{commit8}/*  lib/qtkeychain

mkdir -p %{_vpath_builddir}


%build
pushd %{_vpath_builddir}
%qmake_qt5 \
    PREFIX=%{buildroot}%{_prefix} \
    RAPIDJSON_SYSTEM=1 \
    WEBSOCKETPP_SYSTEM=1 \
    ..
popd

%make_build -C %{_vpath_builddir}


%install
%make_install -C %{_vpath_builddir}
install -Dpm 0644 resources/%{uuid}.appdata.xml   \
    %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
install -Dpm 0644 resources/icon.png              \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/chatterino.png


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md BUILDING_ON_LINUX.md docs/
%{_bindir}/chatterino
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml


%changelog
* Wed Apr 14 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.0-1
- build(update): 2.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.2-2
- Rebuilt for Boost 1.75

* Thu Nov  5 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.2-1
- build(update): 2.2.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 2.1.7-2
- Rebuilt for Boost 1.73

* Fri Feb 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.7-1
- Update to 2.1.7
- Add new submodule 'qtkeychain'
- Drop patches (upstreamed now)
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.4-8
- Build with system 'rapidjson'

* Fri Dec 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.4-7
- Initial package
