%if 0%{?rhel} == 7
%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_libdir: %global lua_libdir %{_libdir}/lua/%{lua_version}}
%endif

Summary:        Binding to libunbound for Lua
Name:           lua-unbound
Version:        0.5
Release:        1%{?dist}
License:        MIT
URL:            https://www.zash.se/luaunbound.html
Source0:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz
Source1:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz.asc
Source2:        gpgkey-3E52119EF853C59678DBBF6BADED9A77B67AD329.gpg
Requires:       lua(abi) = %{lua_version}
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  unbound-devel

%description
Lua bindings for the Unbound APIs.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n luaunbound-%{version}

%build
%make_build \
  LUA_VERSION=%{lua_version} \
  MYCFLAGS="$RPM_OPT_FLAGS" \
  MYLDFLAGS="$RPM_LD_FLAGS" \
  LD=%{__cc}

%install
%make_install LUA_LIBDIR=%{lua_libdir}

# Correct strange upstream file permission
chmod 755 %{buildroot}%{lua_libdir}/lunbound.so

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   local lunbound = require("lunbound");
   print("Hello from "..lunbound._LIBVER.."!");'

%files
%license LICENSE
%doc README.markdown
%{lua_libdir}/lunbound.so

%changelog
* Sun Jan 10 2021 Robert Scheck <robert@fedoraproject.org> 0.5-1
- Upgrade to 0.5 (#1914678)
- Initial spec file for Fedora and Red Hat Enterprise Linux
