Name:           fennel
Version:        0.9.1
Release:        1%{?dist}
Summary:        A Lisp that compiles to Lua

License:        MIT
URL:            https://fennel-lang.org/
Source0:        https://git.sr.ht/~technomancy/fennel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  lua-devel >= 5.1
BuildRequires: make

Provides:       lua-fennel = %{version}-%{release}
%if 0%{?fedora} < 33 && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif
Recommends:     lua-readline

%description
Fennel is a Lisp that compiles to Lua. It aims to be easy to use, expressive,
and has almost zero overhead compared to handwritten Lua.

* *Full Lua compatibility* - You can use any function or library from Lua.
* *Zero overhead* - Compiled code should be just as or more efficient than
   hand-written Lua.
* *Compile-time macros* - Ship compiled code with no runtime dependency on
   Fennel.
* *Embeddable* - Fennel is a one-file library as well as an executable. Embed it
   in other programs to support runtime extensibility and interactive
   development.

At https://fennel-lang.org there's a live in-browser repl you can use without
installing anything.


%prep
%autosetup -p1


%build
%make_build


%install
%make_install PREFIX=%{_prefix}
MAN1=%{buildroot}%{_mandir}/man1/
mkdir -p ${MAN1}
cp -p fennel.1 ${MAN1}/


%check
make test


%files
%license LICENSE
%doc README.md CODE-OF-CONDUCT.md CONTRIBUTING.md
%doc api.md changelog.md lua-primer.md reference.md tutorial.md
%{_bindir}/fennel
%{lua_pkgdir}/fennel.lua
%{lua_pkgdir}/fennelview.lua
%{_mandir}/man1/fennel.1*


%changelog
* Fri Apr 16 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Tue Feb  9 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Wed Jan 27 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0
- Add Requires on lua(abi) for older releases

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 14:47:54 PST 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.7.0-2
- Recommend installing lua-readline

* Mon Nov 23 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Wed Sep 23 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Fri Aug 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.0-1
- Initial Fedora package
