Name:           wf-config
Version:        0.7.0
Release:        2%{?dist}
Summary:        Library for managing configuration files, written for wayfire

License:        MIT
URL:            https://github.com/WayfireWM/wf-config
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  cmake(glm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wlroots) >= 0.12.0

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%{_libdir}/lib%{name}.so.0*
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/wayfire/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Feb 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-2
- build: Switch to BR: glm-devel instead of pkgconfig

* Fri Jan 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- build(update): 0.7.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.0-1
- build(update): 0.6.0

* Tue Aug 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.1-1
- Update to 0.4.1
- Remove GCC 10 patch, upstreamed now | GH-23
- Disable LTO

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-2
- Enable LTO

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Thu Mar 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3-1.20200313gitfdcc040
- Update to latest git snapshot

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5.20190904gite8d57d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-4.20190904gite8d57d1
- Fix soname version

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-3.20190904gite8d57d1
- Cosmetic fixes

* Thu Sep 26 2019 gasinvein <gasinvein@gmail.com>
- Initial package
