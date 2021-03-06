%global commit      819b1dde560013003eeac86c2069c5be7af25c6d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20200213

%global corename    gw

Name:           libretro-%{corename}
Version:        0
Release:        3.%{date}git%{shortcommit}%{?dist}
Summary:        Libretro core for Game & Watch simulators

License:        zlib
URL:            https://github.com/libretro/gw-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires: make
Supplements:    retroarch%{?_isa}
Provides:       bundled(lua) = 5.3.0

%description
gw-libretro is a libretro core that runs Game & Watch simulators.

It runs simulators converted from source code for the games available at
MADrigal. Each simulator is converted with pas2lua, which was written
specifically for this purpose, and uses bstree, which was also specifically
written to obfuscate the generated Lua source code as per MADrigal's request.


%prep
%autosetup -n %{corename}-libretro-%{commit} -p1


%build
%set_build_flags
%make_build


%install
install -m 0755 -Dp %{corename}_libretro.so %{buildroot}%{_libdir}/libretro/%{corename}_libretro.so


%files
%license LICENSE
%doc README.md
%{_libdir}/libretro/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20200213git819b1dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20200213git819b1dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20200213git819b1dd
- Initial package
