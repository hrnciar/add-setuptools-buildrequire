Name:    trezor-common
Version: 2.3.6
Release: 1%{?dist}
Summary: udev rules and protobuf messages for the hardware wallet Trezor

License:       LGPLv3+
URL:           https://github.com/trezor
Source0:       https://github.com/trezor/trezor-firmware/archive/refs/tags/core/v%{version}.tar.gz#/trezor-firmware-core-v%{version}.tar.gz

BuildArch:     noarch

BuildRequires: systemd
Conflicts:     python3-trezor <= 0.12.2-2

%description
Provides udev rules and protobuf messages for all the hardware wallets from
TREZOR.

%prep
%autosetup -n trezor-firmware-core-v%{version}


%build
#Nothing to build

%install
pushd common
install -Dpm 644 udev/51-trezor.rules %{buildroot}%{_udevrulesdir}/51-trezor.rules

for file in $(find ./protob -name \*.proto); do
  install -Dpm 644 $file %{buildroot}%{_datadir}/trezor/$file
done
popd

%files
%doc common/README.md
%license common/COPYING
%{_udevrulesdir}/51-trezor.rules
%{_datadir}/trezor

%changelog
* Fri Apr 02 2021 Jonny Heggheim <hegjon@gmail.com> - 2.3.6-1
- Updated to 2.3.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Jonny Heggheim <hegjon@gmail.com> - 0-0.1
- Initial package
