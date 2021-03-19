Name:       gnome-shell-extension-activities-configurator
Summary:    Configure the top bar and Activities button in GNOME Shell
URL:        https://extensions.gnome.org/extension/358/activities-configurator/
Version:    89
Release:    3%{?dist}
License:    GPLv2
BuildArch:  noarch

# You can see the latest source releases here:
# https://nls1729.github.io/activities_config_zip.html
# With the changelog here:
# https://nls1729.github.io/latestupdate.html
Source0: https://extensions.gnome.org/extension-data/activities-confignls1729.v%{version}.shell-extension.zip

BuildRequires: glib2

Requires: gnome-shell >= 3.36, gnome-shell < 3.39
Requires: gnome-shell-extension-common

Recommends: ( gnome-tweaks  or  gnome-tweak-tool )
Recommends: ( gnome-extensions-app  or  %{_bindir}/gnome-shell-extension-prefs )



%description
Activities Configurator gives you all sorts of options to control the
look and feel of the top bar and Activities button in GNOME Shell,
possibly even overriding your current Shell theme. You can change or
remove the Activities button text, add an icon, move it to right corner,
change the top bar's background color and transparency... You can toggle
the Overview if no applications are running (at login and whenever the
last application window is closed). You can also adjust the "pressure"
threshold for the hot corner, or disable it altogether.



# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  activities-config@nls1729
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}


%prep
%autosetup -c %{name}-%{version}

cat > ./README-fedora.md << EOF
After installing, each user that wants it must still manually enable
Activities Configurator before it will take effect. You can do so a few
different ways.

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
# No compilation necessary.


%install
mkdir -p %{final_install_dir}
cp --recursive --preserve=mode,timestamps  ./*  %{final_install_dir}

# License and README get copied to system directories for docs and license.
rm  %{final_install_dir}/COPYING  %{final_install_dir}/README.txt

# RPM will take care of gschemas, we don't need to include a precompiled copy.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.activities-config.gschema.xml  \
    %{buildroot}/%{_datadir}/glib-2.0/schemas/
rm --recursive %{final_install_dir}/schemas/

mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/
%find_lang activities-config-extension



%files -f activities-config-extension.lang
%doc README.txt  README-fedora.md
%license COPYING
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.activities-config.gschema.xml



%changelog
* Thu Mar 11 2021 Audrey Toskin <audrey@tosk.in> - 89-3
- Minor rebuild to mark Activities Configurator 89 as incompatible with
  GNOME 40.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Audrey Toskin <audrey@tosk.in> - 89-1
- Bump to upstream version 89, which adds better support for GNOME 3.38.

* Fri Aug 07 2020 Audrey Toskin <audrey@tosk.in> - 87-1
- Bump to upstream version 87, which reimplements how it handles the
  GNOME Shell "hot corner".

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Audrey Toskin <audrey@tosk.in> - 86-1
- Bump to upstream version 86, which adds an option controlling the
  delayed extension restart after resuming GNOME Shell from the lock
  screen.
