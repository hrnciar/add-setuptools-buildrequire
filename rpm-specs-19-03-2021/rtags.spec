Name:		rtags
Version:	2.33
Release:	7%{?dist}
Summary:	A indexer for the c language family with Emacs integration

License:	GPLv3+
URL:		https://github.com/Andersbakken/rtags
# Source tarball is created from the git repository
# with make package_source and not taken from the
# github releases, due to git submodules that are
# missing from the latter.
#  git clone --recursive https://github.com/Andersbakken/rtags.git
#  cd rtags
#  mkdir build && cd build && cmake -DRTAGS_ENABLE_DEV_OPTIONS=1 ..
#  make package_source
Source0:	%{name}-%{version}.tar.gz
Source1:	rtags.service
Source2:	rtags.socket

BuildRequires:	cmake, llvm-devel, clang-devel
BuildRequires:	emacs
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(bash-completion)
%{?systemd_requires}
BuildRequires: systemd
Requires:	emacs-filesystem >= %{_emacs_version}

%description
RTags is a client/server application that indexes C/C++ code and keeps
a persistent file-based database of references, declarations,
definitions, symbolnames etc. There’s also limited support for
ObjC/ObjC++. It allows you to find symbols by name (including nested
class and namespace scope). Most importantly we give you proper
follow-symbol and find-references support.

%prep
%setup -q

%build
# default to out-of-source builds, the default starting F33, but
# for older releases we need to explicitly opt-in
%undefine __cmake_in_source_build

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_userunitdir}
install -p -m644 -t %{buildroot}%{_userunitdir} %{SOURCE1} %{SOURCE2}

%preun
%systemd_user_preun %{name}.service

%post
%systemd_user_post %{name}.service

%files
%license LICENSE.txt
%doc	 README.org

%{_bindir}/*
%{_mandir}/man7/rc.7*
%{_mandir}/man7/rdm.7*
%{_emacs_sitelispdir}/rtags
%{_datadir}/bash-completion/
%{_userunitdir}/rtags.service
%{_userunitdir}/rtags.socket

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug  7 2020 Christian Kellner <ckellner@redhat.com> - 2.33-6
- Use proper cmake macros for out-of-source builds
  Resolves: rhbz#1865403

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Christian Kellner <ckellner@redhat.com> - 2.33-1
- rtags 2.33 upsream release

* Wed Mar 13 2019 Christian Kellner <ckellner@redhat.com> - 2.31-1
- rtags 2.31 upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar  5 2018 Christian Kellner <ckellner@redhat.com> - 2.18-1
- rtags 2.18 upstream release
- Fix service unit file refer to correct socket file (rhb#1550362)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Christian Kellner <ckellner@redhat.com> - 2.16-1
- New upstream release

* Wed Nov 15 2017 Christian Kellner <ckellner@redhat.com> - 2.15-1
- New upstream relase

* Tue Oct 24 2017 Christian Kellner <ckellner@redhat.com> - 2.14-2
- Rebuild for LLVM 5.0

* Thu Sep 14 2017 Christian Kellner <ckellner@redhat.com> - 2.14-1
- New upstream release
- Proper suppport for systemd unit files
- Fix some packaging issues

* Wed Aug  2 2017 Christian Kellner <ckellner@redhat.com> - 2.12-3
- Add systemd service/socket files

* Tue Aug  1 2017 Christian Kellner <ckellner@redhat.com> - 2.12-1
- New upstream release

* Tue May 23 2017 Christian Kellner <ckellner@redhat.com> - 2.9-2
- Package bash completions

* Mon Mar 27 2017 Christian Kellner <ckellner@redhat.chom> - 2.9-1
- New upstream release

* Wed Mar  1 2017 Chrisian Kellner <ckellner@redhat.com> - 2.8-4.git37eef28
- Package systemd socket/unit files

* Fri Feb 24 2017 Chrisian Kellner <ckellner@redhat.com> - 2.8-3.git37eef28
- Add gcc7.patch to fix compilation on gcc 7.0 (rawhide)

* Fri Jan 13 2017 Chrisian Kellner <ckellner@redhat.com>
- Initial revision.
