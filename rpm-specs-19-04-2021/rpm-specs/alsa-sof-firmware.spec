# This is a firmware package, so binaries (which are not run on the host)
# in the end package are expected.
%define _binaries_in_noarch_packages_terminate_build   0
%global _firmwarepath  /usr/lib/firmware

%global sof_version 1.6.1
%global sof_commit f31c9ce30ac2792ec39e19da489aee7631e00654
%global sof_shortcommit %(c=%{sof_commit}; echo ${c:0:7})

%global tplg_version 1.2.4

Summary:        Firmware and topology files for Sound Open Firmware project
Name:           alsa-sof-firmware
Version:        %{sof_version}
Release:        4%{?dist}
# See later in the spec for a breakdown of licensing
License:        BSD
URL:            https://github.com/thesofproject/sof-bin
Source:         https://github.com/thesofproject/sof-bin/archive/%{sof_commit}/sof-bin-%{sof_shortcommit}.tar.gz
BuildRequires:  alsa-topology >= %{tplg_version}
BuildRequires:  alsa-topology-utils >= %{tplg_version}
Conflicts:      alsa-firmware <= 1.2.1-6

# noarch, since the package is firmware
BuildArch:      noarch

%description
This package contains the firmware binaries for the Sound Open Firmware project.

%package debug
Requires:       alsa-sof-firmware
Summary:        Debug files for Sound Open Firmware project
License:        BSD

%description debug
This package contains the debug files for the Sound Open Firmware project.

%prep
%autosetup -n sof-bin-%{sof_commit}

cd lib/firmware

# we have the version in the package name
mv intel/sof/v%{sof_version}/* intel/sof
rmdir intel/sof/v%{sof_version}

# rename intel signed firmware files
for platform in apl cnl ehl icl tgl tgl-h; do
  mv intel/sof/intel-signed/sof-$platform-v%{sof_version}.ri intel/sof/intel-signed/sof-$platform.ri
  ln -sf intel-signed/sof-$platform.ri intel/sof/sof-$platform.ri
done

# rename public signed firmware files
for platform in apl cnl icl jsl tgl tgl-h; do
  mv intel/sof/public-signed/sof-$platform-v%{sof_version}.ri intel/sof/public-signed/sof-$platform.ri
done

# rename unsigned firmware files
for platform in bdw byt cht; do
  mv intel/sof/sof-$platform-v%{sof_version}.ri intel/sof/sof-$platform.ri
done

# rename debug files
for platform in apl bdw byt cht cnl ehl icl tgl tgl-h; do
  mv intel/sof/sof-$platform-v%{sof_version}.ldc intel/sof/sof-$platform.ldc
done

# add missing symlinks
ln -s intel-signed/sof-apl.ri intel/sof/sof-glk.ri
ln -s intel-signed/sof-cnl.ri intel/sof/sof-cml.ri
ln -s intel-signed/sof-cnl.ri intel/sof/sof-cfl.ri

# move topology files
rm -f intel/sof-tplg
mv intel/sof-tplg-v%{sof_version} intel/sof-tplg

# remove NXP firmware files
rm -rf nxp ../../LICENCE.NXP
rm -rf intel/sof-tplg/sof-imx8*

%build
# SST topology files (not SOF related, but it's a Intel hw support
# and this package seems a good place to distribute them
alsatplg -c /usr/share/alsa/topology/hda-dsp/skl_hda_dsp_generic-tplg.conf \
         -o lib/firmware/skl_hda_dsp_generic-tplg.bin

%install
mkdir -p %{buildroot}%{_firmwarepath}
cp -ra lib/firmware/* %{buildroot}%{_firmwarepath}

# gather files and directories
FILEDIR=$(pwd)
pushd %{buildroot}/%{_firmwarepath}
find -P . -name "*.ri" | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.files
#find -P . -name "*.tplg" | sed -e '/^.$/d' >> $FILEDIR/alsa-sof-firmware.files
find -P . -name "*.ldc" | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.debug-files
find -P . -type d | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.dirs
popd
sed -i -e 's:^./::' alsa-sof-firmware.{files,debug-files,dirs}
sed -i -e 's!^!/usr/lib/firmware/!' alsa-sof-firmware.{files,debug-files,dirs}
sed -e 's/^/%%dir /' alsa-sof-firmware.dirs >> alsa-sof-firmware.files
cat alsa-sof-firmware.files

%files -f alsa-sof-firmware.files
%license LICENCE*
%doc README*
%dir %{_firmwarepath}

# Licence: 3-clause BSD
%{_firmwarepath}/*.bin

# Licence: 3-clause BSD
# .. for files with suffix .tplg
%{_firmwarepath}/intel/sof-tplg

# Licence: SOF (3-clause BSD plus others)
# .. for files with suffix .ri

%files debug -f alsa-sof-firmware.debug-files

%pretrans -p <lua>
path = "%{_firmwarepath}/intel/sof-tplg"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%changelog
* Thu Mar 11 2021 Jaroslav Kysela <perex@perex.cz> - 1.6.1-4
- Add SST Skylake HDA topology binary (bug#1933423)

* Fri Mar  5 2021 Jaroslav Kysela <perex@perex.cz> - 1.6.1-3
- Add TGL-H firmware files

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 Jaroslav Kysela <perex@perex.cz> - 1.6.1-1
- Update to v1.6.1

* Thu Dec 10 2020 Jaroslav Kysela <perex@perex.cz> - 1.6-4
- Update to v1.6 (Dec 9)

* Thu Nov 19 2020 Jaroslav Kysela <perex@perex.cz> - 1.6-3
- Update to v1.6 (Nov 19)

* Wed Oct 14 2020 Jaroslav Kysela <perex@perex.cz> - 1.6-1
- Update to v1.6 (Oct 13)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  1 2020 Jaroslav Kysela <perex@perex.cz> - 1.5-1
- Update to v1.5

* Tue May 12 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-6
- Fix the upgrade (make /usr/lib/firmware/intel/sof-tplg directory again)
- Remove the version from all paths

* Thu Apr 30 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-5
- Add missing symlink for sof-cfl.ri

* Thu Mar 12 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-4
- Add missing symlink for sof-cml.ri

* Mon Mar  2 2020 Jaroslav Kysela <perex@perex.cz> - 1.4.2-3
- Initial version, SOF firmware 1.4.2
