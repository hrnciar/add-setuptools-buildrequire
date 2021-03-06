%global srcname qutebrowser

Name:		%{srcname}
Version:	2.1.0
Release:	1%{?dist}
Summary:	A keyboard-driven, vim-like browser based on PyQt5 and QtWebEngine
License:	GPLv3
URL:		http://www.qutebrowser.org
Source0:	https://github.com/%{srcname}/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	asciidoc
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	python3-setuptools
Requires:	qt5-qtbase
Requires:	qt5-qtdeclarative
Requires:	python3-qt5
Requires:	python3-jinja2
Requires:	python3-PyYAML
Requires:	((qt5-qtwebengine and python3-qt5-webengine) or (qt5-qtwebkit and python3-qt5-webkit))
Recommends:	(qt5-qtwebengine and python3-qt5-webengine and qt5-qtwebengine-devtools)
Recommends:	(qt5-qtwebkit and python3-qt5-webkit)
Recommends:	python3-pygments
Recommends:	python3-adblock

%description
qutebrowser is a keyboard-focused browser with a minimal GUI. It’s based on
Python, PyQt5 and QtWebEngine and free software, licensed under the GPL.
It was inspired by other browsers/addons like dwb and Vimperator/Pentadactyl.


%prep
%autosetup -p 1 -n %{srcname}-%{version}


%build
# Compile the man page
a2x -f manpage doc/qutebrowser.1.asciidoc

# Find all *.py files and if their first line is exactly '#!/usr/bin/env python3'
# then replace it with '#!/usr/bin/python3' (if it's the 1st line).
find . -type f -iname "*.py" -exec sed -i '1s_^#!/usr/bin/env python3$_#!/usr/bin/python3_' {} +

%py3_build


%install
%py3_install

# Install desktop and appdata files
desktop-file-install \
	--add-category="Network" \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	misc/org.%{srcname}.%{srcname}.desktop

install -Dm644 misc/org.qutebrowser.qutebrowser.appdata.xml -t %{buildroot}%{_datadir}/metainfo

# Install man page
install -Dm644 doc/%{srcname}.1 -t %{buildroot}%{_mandir}/man1

# Install icons
install -Dm644 icons/qutebrowser.svg \
	-t "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps"
for i in 16 24 32 48 64 128 256 512; do
	install -Dm644 "icons/qutebrowser-${i}x${i}.png" \
		"%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/qutebrowser.png"
done

# Set __main__.py as executable
chmod 755 %{buildroot}%{python3_sitelib}/%{srcname}/__main__.py

# Remove zero-length files:
# https://fedoraproject.org/wiki/Packaging_tricks#Zero_length_files
find %{buildroot} -size 0 -delete

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license LICENSE
%doc README.asciidoc doc/changelog.asciidoc qutebrowser/html/doc
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}
%{_bindir}/%{srcname}
%{_datadir}/applications/org.%{srcname}.%{srcname}.desktop
%{_mandir}/man1/%{srcname}.1*
%{_datadir}/icons/hicolor/scalable/apps/%{srcname}.svg
%{_datadir}/icons/hicolor/16x16/apps/%{srcname}.png
%{_datadir}/icons/hicolor/24x24/apps/%{srcname}.png
%{_datadir}/icons/hicolor/32x32/apps/%{srcname}.png
%{_datadir}/icons/hicolor/48x48/apps/%{srcname}.png
%{_datadir}/icons/hicolor/64x64/apps/%{srcname}.png
%{_datadir}/icons/hicolor/128x128/apps/%{srcname}.png
%{_datadir}/icons/hicolor/256x256/apps/%{srcname}.png
%{_datadir}/icons/hicolor/512x512/apps/%{srcname}.png
%{_datadir}/metainfo/org.qutebrowser.qutebrowser.appdata.xml

%changelog
* Tue Mar 16 2021 Jan Staněk <jstanek@redhat.com> - 2.1.0-1
- New upstream release

* Sun Feb 07 2021 Timothée Floure <fnux@fedoraproject.org> - 2.0.2-1
- New upstream release

* Fri Jan 29 2021 Timothée Floure <fnux@fedoraproject.org> - 2.0.1-1
- New upstream release
- Removing various dependencies that are not used anymore

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Timothée Floure <fnux@fedoraproject.org> - 1.14.1-1
- New upstream release

* Mon Oct 19 2020 Timothée Floure <fnux@fedoraproject.org> - 1.14.0-1
- New upstream release

* Tue Sep 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.13.1-3
- Remove requires on python3-qt5-qtwebenging
- fixes: 1814298

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Timothée Floure <fnux@fedoraproject.org> - 1.13.1-1
- New upstream release

* Sat Jun 20 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.12.0-1
- Update to 1.12.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-2
- Rebuilt for Python 3.9

* Sat May 23 2020 Timothée Floure <fnux@fedoraproject.org> - 1.11.1-1
- New upstream release (addresses CVE-2020-11054)

* Fri May 01 2020 Timothée Floure <fnux@fedoraproject.org> - 1.11.0-1
- New upstream release

* Mon Feb 17 2020 Timothée Floure <fnux@fedoraproject.org> - 1.10.1-1
- New upstream release

* Wed Feb 05 2020 Timothée Floure <fnux@fedoraproject.org> - 1.10.0-1
- New upstream release

* Fri Jan 10 2020 Timothée Floure <fnux@fedoraproject.org> - 1.9.0-1
- New upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Sep 28 2019 Timothée Floure <fnux@fedoraproject.org> - 1.8.1-1
- New upstream release

* Tue Aug 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Timothée Floure <fnux@fedoraproject.org> - 1.7.0-3
- Fix desktop file installation (broken due to changes in upstream 1.7.x)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Timothée Floure <fnux@fedoraproject.org> - 1.7.0-1
- New upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.3-1
- New upstream release

* Tue May 14 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.2-1
- New upstream release

* Fri Apr 05 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.1-1
- New upstream release

* Fri Mar 08 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.0-2
- Patch invalid desktop file shipped with upstream 1.6.0 (fix-desktop-file-actions.patch)

* Sun Mar 03 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.0-1
- New upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Timothée Floure <fnux@fedoraproject.org> - 1.5.2-1
- Rebase to 1.5.2

* Thu Oct 11 2018 Timothée Floure <fnux@fedoraproject.org> - 1.5.1-1
- Rebase to 1.5.1

* Wed Oct 03 2018 Timothée Floure <fnux@fedoraproject.org> - 1.5.0-1
- Rebase to 1.5.0

* Mon Sep 03 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.2-1
- Rebase to 1.4.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.1-1
- Rebase to 1.4.1
- Remove patch introduced in 1.4.0-2, since included in upstream release 1.4.1

* Tue Jul 10 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.0-2
- Patch critical CSRF issues with qute://settings/set URL, leading to arbitrary
  code exexution.

* Tue Jul 03 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.0-1
- Rebase to 1.4.0

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.3-1
- Rebase to 1.3.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.2-1
- Rebase to 1.3.2

* Tue May 29 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.1-1
- Rebase to 1.3.1

* Fri May 04 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.0-1
- Rebase to 1.3.0

* Tue Mar 20 2018 Timothée Floure <fnux@fedoraproject.org> - 1.2.1-1
- Rebase to 1.2.1

* Mon Mar 12 2018 Timothée Floure <fnux@fedoraproject.org> - 1.2.0-1
- Rebase to 1.2.0

* Mon Mar 05 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.2-1
- Rebase to 1.1.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.1-1
- Rebase to 1.1.1

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-2
- Remove obsolete scriptlets

* Mon Jan 15 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.0-1
- Rebase to 1.1.0

* Tue Nov 28 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.4-1
- Rebase to 1.0.4

* Tue Nov 14 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.3-2
- Fix typos in some (weak) Qt dependencies

* Tue Nov 07 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.3-1
- Rebase to 1.0.3
- Fix dependency issue for architectures unsupported by qt5-qtwebengine

* Fri Oct 20 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.2-1
- Rebase to 1.0.2
- Remove the deprecated Group tag
- Add the python3-attrs dependency
- Adapt the descriptions and dependencies to the QtWebEngine backend (new default)
- Doc tag: do not package the PKG-INFO file anymore
- Doc tag: package the full HTML documentation instead of sparse asciidoc files

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Tomas Orsava <torsava@redhat.com> - 0.10.1-1
- Rebased to 0.10.1

* Mon Feb 27 2017 Tomas Orsava <torsava@redhat.com> - 0.10.0-1
- Rebased to 0.10.0
- Updated Source URL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Tomas Orsava <torsava@redhat.com> - 0.9.1-1
- Rebased to 0.9.1

* Mon Jan 02 2017 Tomas Orsava <torsava@redhat.com> - 0.9.0-1
- Rebased to 0.9.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-2
- Rebuild for Python 3.6

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 0.8.2-1
- New upstream release 0.8.2

* Thu Jul 28 2016 Tomas Orsava <torsava@redhat.com> - 0.8.1-1
- Rebased onto a new upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 13 2016 Tomas Orsava <torsava@redhat.com> - 0.7.0-1
- Updated to a new version
- Removed soft dependency on `colorama` as it is no longer needed

* Fri May 06 2016 Tomas Orsava <torsava@redhat.com> - 0.6.2-1
- Updated to a new upstream version.
- Remover patches specific to the version 0.6.1

* Wed Apr 27 2016 Tomas Orsava <torsava@redhat.com> - 0.6.1-2
- Added 3 upstream patches from the mailing list to help with PyQT crashes
  until 0.6.2 comes out.

* Tue Apr 12 2016 Tomas Orsava <torsava@redhat.com> - 0.6.1-1
- Updated to a new upstream version.
- Simplified the sed command that replaces shebangs.
- Fixed issue with python3-qt5-webkit not being provided by python-qt5 in f23.

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-2
- Requires: python3-qt5-webkit

* Mon Feb 22 2016 Tomas Orsava <torsava@redhat.com> - 0.5.1-1
- Let there be package.
