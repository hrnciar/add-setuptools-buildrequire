Name:           luarocks
Version:        3.5.0
Release:        1%{?dist}
Summary:        A deployment and management system for Lua modules

License:        MIT
URL:            http://luarocks.org
Source0:        http://luarocks.org/releases/luarocks-%{version}.tar.gz
Patch0:         luarocks-3.5.0-dynamic_libdir.patch

BuildArch:      noarch
# this package was previously arched, and needs to be obsoleted
# to have an upgrade path
Obsoletes:      luarocks < 3.5.0-1

BuildRequires:  lua-devel
BuildRequires:  make
%if 0%{?el7}
BuildRequires:  lua-rpm-macros
%endif
%if 0%{?fedora} < 33 && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif
Requires:       unzip
Requires:       zip

%if 0%{?fedora}
Recommends:     lua-sec
Suggests:       lua-devel
%endif

%description
LuaRocks allows you to install Lua modules as self-contained packages
called "rocks", which also contain version dependency
information. This information is used both during installation, so
that when one rock is requested all rocks it depends on are installed
as well, and at run time, so that when a module is required, the
correct version is loaded. LuaRocks supports both local and remote
repositories, and multiple local rocks trees.


%prep
%autosetup -p1


%build
./configure \
  --prefix=%{_prefix} \
  --lua-version=%{lua_version} \
  --with-lua=%{_prefix}
%make_build


%install
%make_install

mkdir -p %{buildroot}%{_prefix}/lib/luarocks/rocks-%{lua_version}

%check
# TODO - find how to run this without having to pre-download entire rocks tree
# ./test/run_tests.sh


%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/luarocks
%config(noreplace) %{_sysconfdir}/luarocks/config-%{lua_version}.lua
%{_bindir}/luarocks
%{_bindir}/luarocks-admin
%{_prefix}/lib/luarocks
%{lua_pkgdir}/luarocks


%changelog
* Wed Jan 27 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0
- This package is now noarch, tested on x86_64 and i386

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-2
- Rebuilt for Lua 5.4

* Tue Mar  3 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Tom Callaway <spot@fedoraproject.org> - 3.0.3-1
- update to 3.0.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Tom Callaway <spot@fedoraproject.org> - 2.4.3-1
- update to 2.4.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul  5 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0
- Use license macro
- On Fedora, add weak dependencies on lua-sec (recommended)
  and lua-devel (suggested)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Tom Callaway <spot@fedoraproject.org> - 2.2.3-0.2.rc2
- update to 2.2.3-rc2
- fix another case of /usr/lib pathing

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2
- Add runtime dependencies on unzip and zip (h/t Ignacio Burgueño)

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 2.2.0-2
- rebuild for lua 5.3

* Fri Oct 17 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Michel Salim <salimma@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.13-2
- rebuild for lua 5.2

* Mon Apr 22 2013 Michel Salim <salimma@fedoraproject.org> - 2.0.13-1
- Update to 2.0.13

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov  5 2012 Michel Salim <salimma@fedoraproject.org> - 2.0.12-1.1
- Fix macro problem affecting EPEL builds

* Mon Nov  5 2012 Michel Salim <salimma@fedoraproject.org> - 2.0.12-1
- Update to 2.0.12

* Fri Sep 28 2012 Michel Salim <salimma@fedoraproject.org> - 2.0.11-1
- Update to 2.0.11

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Michel Salim <salimma@fedoraproject.org> - 2.0.8-2
- Add support for RHEL's older lua packaging

* Tue May  8 2012 Michel Salim <salimma@fedoraproject.org> - 2.0.8-1
- Initial package
