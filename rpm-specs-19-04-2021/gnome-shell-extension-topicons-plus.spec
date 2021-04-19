%global  commit_date   20210319
%global  commit_long   295026aab84b89eb149d620847f041758191f855
%global  commit_short  %(c=%{commit_long}; echo ${c:0:7})

Name:       gnome-shell-extension-topicons-plus
Summary:    Move all legacy tray icons to the top panel
Version:    27
# Release:    XX%%{?dist}
Release:    7.%{commit_date}.%{commit_short}%{?dist}
URL:        https://extensions.gnome.org/extension/1031/topicons/
License:    GPLv2
BuildArch:  noarch

# There haven't been any *tagged* releases in a long time, but this is where they would be:
# https://github.com/phocean/TopIcons-plus/releases
# Source0: https://github.com/phocean/TopIcons-plus/archive/%%{version}/TopIcons-plus-%%{version}.tar.gz
Source0: https://github.com/kofemann/TopIcons-plus/archive/%{commit_short}/TopIcons-plus-%{commit_short}.tar.gz

BuildRequires: glib2
BuildRequires: make

Requires: gnome-shell >= 40
Requires: gnome-shell-extension-common

Recommends: ( gnome-extensions-app  or  %{_bindir}/gnome-shell-extension-prefs )
Recommends: gnome-shell-extension-appindicator
Recommends: ( gnome-tweaks  or  gnome-tweak-tool )



%description
Many applications, such as chat clients, downloaders, and some media
players, are meant to run long-term in the background even after you
close their window.  These applications remain accessible by adding an
icon to the GNOME Shell Legacy Tray. However, the Legacy Tray is hidden
until you push your mouse into the lower-left of the screen and click on
the small tab that appears. TopIcons Plus brings all icons back to the
top panel, so that it's easier to keep track of apps running in the
background. You also get some options to control the look and feel: You
can leave the icons in full color, or dynamically convert them to
grayscale, etc.



# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  TopIcons@phocean.net
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}

%prep
# %%autosetup -n TopIcons-plus-%%{version}
%autosetup -n TopIcons-plus-%{commit_long}

cat > ./README-fedora.md << EOF
After installing, each user that wants it must still manually enable
TopIcons Plus before it will take effect. You can do so a few different
ways.

First, restart GNOME Shell (Open the command dialog with Alt-F2, type
\`r\`, and hit enter), or log out and log back in. Then:

- If you've already set up the GNOME Shell web browser plugin, go to
  <https://extensions.gnome.org/local/>, find the extension, and click
  the switch to "ON."
- Open GNOME Tweaks, go to the Extensions tab, find the extension,
  and click the switch to "ON."
- Open a terminal or the desktop's command dialog, and (as your normal
  user account) run:
  \`gnome-extensions enable %{UUID}\`
EOF



%build
# `build` make target is included in `make install`.



%install
%make_install  INSTALL_PATH=%{buildroot}/%{gnome_extensions_dir}

rm %{final_install_dir}/locale/*/LC_MESSAGES/*.po
mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/
%find_lang TopIcons-Plus

# README also gets copied to the standard documentation directory, so we don't
# need it here.
rm  %{final_install_dir}/README.md

# RPM will take care of gschemas, so we don't need to include a precompiled copy.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.topicons.gschema.xml  \
	%{buildroot}/%{_datadir}/glib-2.0/schemas/
rm --recursive %{final_install_dir}/schemas/



%files -f TopIcons-Plus.lang
%doc README.md  README-fedora.md
%license gpl-2.0.txt
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.topicons.gschema.xml



%changelog
* Fri Apr 2 2021 Audrey Toskin <audrey@tosk.in> - 27-7.20210319.295026a
- Recommend also installing GNOME Shell extension for libappindicator.
  (TopIcons Plus and libappindicator provide overlapping functionality
  and use case, but cover the gaps in each other's supported apps and
  sessions, without stepping on each other's toes. So a user who wants
  to see status icons in the top panel will probably want both Shell
  extensions.)

* Tue Mar 23 2021 Audrey Toskin <audrey@tosk.in> - 27-6.20210319.295026a
- Source the commit from contributor kofemann on GitHub directly.
  With this revision, TopIcons Plus no longer supports GNOME 3.x, only
  GNOME 40+.

* Tue Mar 23 2021 Hans de Goede <hdegoede@redhat.com> - 27-5
- Fix GNOME 40 incompatiblity, fixing #1936207, #1938441, #1941009

* Wed Mar 10 2021 Audrey Toskin <audrey@tosk.in> - 27-4
- Minor rebuild to mark TopIcons Plus 27 as incompatible with GNOME 40.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
