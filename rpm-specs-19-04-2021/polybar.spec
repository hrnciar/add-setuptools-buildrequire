# Git submodules
# * i3ipcpp
%global commit1         cb008b30fc5f3febfe467884cb0211ee3c16386b
%global shortcommit1    %(c=%{commit1}; echo ${c:0:7})

# * xpp
%global commit2         044e69d05db7f89339bda1ccd1efe0263b01c8f6
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

%global url1    https://github.com/%{name}

Name:           polybar
Version:        3.5.5
Release:        1%{?dist}
Summary:        Fast and easy-to-use status bar

# BSD 2-clause "Simplified" License
# ---------------------------------
# lib/concurrentqueue/
#
# Expat License
# -------------
# lib/i3ipcpp/
# lib/xpp/
#
License:        MIT and BSD
URL:            https://polybar.github.io/
Source0:        %{url1}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Bundled libs
Source1:        %{url1}/i3ipcpp/archive/%{commit1}/i3ipcpp-%{shortcommit1}.tar.gz
Source2:        %{url1}/xpp/archive/%{commit2}/xpp-%{shortcommit2}.tar.gz

BuildRequires: make
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  i3-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  libnl3-devel
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-sphinx
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp) >= 1.7.7
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb)

Provides:       bundled(i3ipcpp) = 0.7.1~git%{shortcommit1}
Provides:       bundled(xpp) = 1.4.0~git%{shortcommit2}

%description
Polybar aims to help users build beautiful and highly customizable status bars
for their desktop environment, without the need of having a black belt in shell
scripting.


%prep
%setup -q
%setup -q -D -T -a1
%setup -q -D -T -a2

mv i3ipcpp-%{commit1}/* lib/i3ipcpp
mv xpp-%{commit2}/*     lib/xpp

mkdir -p {,doc/}%{_vpath_builddir}


%build
# Build man page
%cmake                              \
    -B $PWD/doc/%{_vpath_builddir}  \
    -S $PWD/doc
%make_build -C doc/%{_vpath_builddir} doc_man

%cmake                                  \
    -DBUILD_DOC=false                   \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo   \
    -B $PWD/%{_vpath_builddir}          \
    -S $PWD
%make_build -C %{_vpath_builddir}


%install
%make_install -C %{_vpath_builddir}

# Install man page
install -Dpm 0644 doc/%{_vpath_builddir}/man/%{name}.1 \
    %{buildroot}/%{_mandir}/man1/%{name}.1


%files
%license LICENSE
%doc README.md SUPPORT.md
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/
%{_docdir}/%{name}/config
%{_mandir}/man1/*.1.*


%changelog
* Wed Mar 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.5.5-1
- build(update): 3.5.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.5.4-1
- build(update): 3.5.4

* Mon Dec 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.5.3-1
- build(update): 3.5.3

* Sun Dec 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.5.2-1
- build(update): 3.5.2

* Sat Dec 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.5.1-1
- build(update): 3.5.1

* Wed Dec  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.5.0-1
- build(update): 3.5.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Björn Esser <besser82@fedoraproject.org> - 3.4.3-4
- Update xpp snapshot with Python 3.9 fix

* Thu Jun 04 2020 Björn Esser <besser82@fedoraproject.org> - 3.4.3-3
- Update Python 3.9 patch with upstreamed version

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 3.4.3-2
- Rebuild (jsoncpp)
- Add a patch to fix build with Python 3.9
- Small spec file optimizations

* Sun May 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.4.3-1
- Update to 3.4.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.4.2-2
- Replace wireless-tools-devel with libnl3-devel (upstream recommendation)

* Fri Dec 27 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.4.2-1
- Update to 3.4.2

* Sat Dec 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.4.1-4
- Update to 3.4.1
- Packaging fixes

* Thu Sep 05 2019 Franco Comida <fcomida@users.sourceforge.net> - 3.4.0-1
- Version 3.4.0
