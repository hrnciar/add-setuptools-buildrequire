# Generated by go2rpm 1
%bcond_without check

# https://github.com/bettercap/gatt
%global goipath         github.com/bettercap/gatt
%global commit          569d3d9372bb0b4997ff39514ea7b9ad1356dab6

%gometa

%global common_description %{expand:
Gatt is a Go package for building Bluetooth Low Energy peripherals.}

# xpc and gioctl are bundled
# https://github.com/bettercap/gatt/issues/15
# gatt: BSD
# xpc: MIT
# gioctl: MIT/Expat
%global golicenses      LICENSE.md xpc/LICENSE LICENSE-gioctl.md
%global godocs          examples readme.md linux/gioctl/README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Go package for building Bluetooth Low Energy peripherals

# Upstream license specification: MIT and BSD-3-Clause
License:        MIT and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mgutz/logxi/v1)

%description
%{common_description}

%gopkg

%prep
%goprep
mv %{_builddir}/gatt-%{commit}/linux/gioctl/LICENSE.md LICENSE-gioctl.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.3.20200404git569d3d9
- Add more details about licenses

* Thu Apr 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20200404git569d3d9
- Add details about the bundling (rhbz#1820805)

* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200404git569d3d9
- Initial package
