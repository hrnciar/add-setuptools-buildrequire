# Variables for if/when I need to source a commit instead of a release tag.
%global  commit_date   20210401
%global  commit_long   8e245647228df2f8bfbcd85924384e413788886e
%global  commit_short  %(c=%{commit_long}; echo ${c:0:7})


Name:       gnome-shell-extension-freon
Summary:    GNOME Shell extension to display system temperature, voltage, and fan speed
Epoch:      2
Version:    44
Release:    1%{?dist}
# Release:    XX.%%{commit_date}.%%{commit_short}%%{?dist}
URL:        https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki
License:    GPLv2
BuildArch:  noarch

# You can see the latest source releases here:
# https://github.com/UshakovVasilii/gnome-shell-extension-freon/releases
Source0: https://github.com/UshakovVasilii/%{name}/archive/EGO-%{version}/%{name}-EGO-%{version}.tar.gz
# Source0: https://github.com/UshakovVasilii/%%{name}/archive/%%{commit_long}/%%{name}-%%{commit_short}.tar.gz

BuildRequires: glib2

# Dependencies described here:
# https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki/Dependency
Requires: gnome-shell >= 40
Requires: gnome-shell-extension-common
Requires: lm_sensors

Recommends: ( gnome-extensions-app  or  %{_bindir}/gnome-shell-extension-prefs )
Recommends: ( gnome-tweaks  or  gnome-tweak-tool )
Recommends: nvme-cli
Recommends: ( udisks2  or  smartmontools  or ( nc and hddtemp ))


%description
Freon is a GNOME Shell extension for displaying the temperature of your
CPU, hard disk, solid state, and video card (NVIDIA, Catalyst, and
Bumblebee supported), as well as power supply voltage, and fan
speed. You can choose which HDD/SSD or other devices to include, what
temperature units to use, and how often to refresh the sensors readout,
and they will appear in the GNOME Shell top bar.

**NOTE** that if you want to see GPU temperature, you will need to
install the vendor's driver and any related packages. (Nouveau
unfortunately won't work for Nvidia cards.)

* hard drive temperatures requires udisks2, or smartmontools, or both
  hddtemp and GNU netcat. (udisks2 should already be installed by
  default on Fedora Workstation, but if you want to use hddtemp instead,
  you will need to install it and netcat yourself, and enable the
  hddtemp daemon.)
* Nvidia GPU temperatures require the `nvidia-settings` application,
  typically installed with the proprietary Nvidia drivers.
* Bumblebee + Nvidia requires `optirun`.
* AMD GPU temperatures requires `aticonfig`, part of AMD Radeon Software
  (formerly known as AMD Catalyst).



# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  freon@UshakovVasilii_Github.yahoo.com
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}

%prep
%autosetup -n %{name}-EGO-%{version}
# %%autosetup -n %%{name}-%%{commit_long}

cat > ./README-fedora.md << EOF
**NOTE** that if you want to see GPU temperature, you will need to
install the vendor's official driver and any related packages. (Nouveau
unfortunately won't work for Nvidia cards.)

- hard drive temperatures requires udisks2, or smartmontools, or both
  hddtemp and GNU netcat. (udisks2 should already be installed by
  default on Fedora Workstation, but if you want to use hddtemp instead,
  you will need to install it and netcat yourself, and enable the
  hddtemp daemon.)
- Nvidia GPU temperatures require the `nvidia-settings` application,
  typically installed with the proprietary Nvidia drivers
- AMD GPU temperatures requires `aticonfig`, part of AMD Radeon Software
  (formerly known as AMD Catalyst)
- Bumblebee + Nvidia requires `optirun`

You can read more about this and other tips
**on the Freon [wiki](https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki)**.

Also, after installing this GNOME Shell extension, each user that wants
it must still manually enable Freon before it will take effect. You can
do so a few different ways.

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
cp --recursive --preserve=mode,timestamps  %{UUID}/*  %{final_install_dir}

# RPM will take care of gschemas, but they should be installed to system-wide directory.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.sensors.gschema.xml  \
    %{buildroot}/%{_datadir}/glib-2.0/schemas/
rmdir %{final_install_dir}/schemas/

# Remove source .po localization files, move binary .mo to system directory.
rm --recursive %{final_install_dir}/po/
mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/

# NOTE: Upstream needs to rename their Turkish translation file.
mv  %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES/tr.mo  %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES/freon.mo

%find_lang freon



%files -f freon.lang
%doc README.md  README-fedora.md
%license LICENSE
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.sensors.gschema.xml



%changelog
* Sun Apr 18 2021 Audrey Toskin <audrey@tosk.in> - 2:44-1
- Bump to Freon 44, which merges the upstream pull request used in
  43-4.20210401.8e24564.

* Mon Apr 5 2021 Audrey Toskin <audrey@tosk.in> - 2:43-4.20210401.8e24564
- Update based on unmerged upstream pull request, which fixes GNOME 40
  compatibility.

* Thu Mar 11 2021 Audrey Toskin <audrey@tosk.in> - 2:43-3
- Minor rebuild to mark Freon 43 as incompatible with GNOME 40.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Audrey Toskin <audrey@tosk.in> - 2:43-1
- Bump to upstream version 43, which fixes support for GNOME 3.38.

* Tue Oct 06 2020 Audrey Toskin <audrey@tosk.in> - 2:42-1
- Bump to upstream version 42, which updates some translations, icons,
  and how average temperatures are calculated.
