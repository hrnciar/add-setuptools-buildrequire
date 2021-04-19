%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		lua-ldoc
Version:	1.4.6
Release:	12%{?dist}
BuildArch:	noarch
Summary:	Lua documentation generator
# the included css code is BSD licensed
License:	MIT and BSD
URL:		https://github.com/stevedonovan/ldoc
Source0:	https://github.com/stevedonovan/LDoc/archive/%{version}/LDoc-%{version}.tar.gz
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-markdown
BuildRequires:	lua-penlight >= 1.4.0
BuildRequires:	make
Requires:	lua >= %{luaver}
Requires:	lua-markdown
Requires:	lua-penlight >= 1.4.0

%global __requires_exclude_from %{_docdir}

%description
LDoc is a second-generation documentation tool that can be used as a
replacement for LuaDoc. It is mostly compatible with LuaDoc, except
that certain workarounds are no longer needed. For instance, it is not
so married to the idea that Lua modules should be defined using the
module function.


%package doc
Summary:	Docs for lua-ldoc
Requires:	%{name} = %{version}-%{release}

%description doc
%{summary}


%prep
%setup -q -n LDoc-%{version}

%build
# nothing to do here


%install
mkdir -p %{buildroot}%{luapkgdir}
mkdir -p %{buildroot}%{_bindir}
make install \
  "LUA_SHAREDIR=%{luapkgdir}" \
  "LUA_BINDIR=%{_bindir}" \
  "DESTDIR=%{buildroot}"

# fix scripts
sed -i %{buildroot}%{_bindir}/ldoc -e '1i#!/bin/sh'
sed -i %{buildroot}%{luapkgdir}/ldoc.lua -e '1{/^#!/d}'

# create documentation
pushd doc
lua ../ldoc.lua .
popd
markdown.lua readme.md > readme.html
markdown.lua changes.md > changes.html

# fix permissions
chmod u=rwX,go=rX -R out

# fix line-endings
sed -i 's/\r//' COPYRIGHT

# we depend on lua-markdown instead
rm %{buildroot}%{luapkgdir}/ldoc/markdown.lua

# cleanup
rm %{buildroot}%{luapkgdir}/ldoc/SciTE.properties \
   %{buildroot}%{luapkgdir}/ldoc/config.ld

# install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -av %{!?_licensedir:COPYRIGHT} readme.html changes.html out/* \
  %{buildroot}%{_pkgdocdir}


%files
%dir %{_pkgdocdir}
%license COPYRIGHT
%{_pkgdocdir}/readme.html
%{_bindir}/ldoc
%{luapkgdir}/ldoc
%{luapkgdir}/ldoc.lua


%files doc
%{_pkgdocdir}/index.html
%{_pkgdocdir}/ldoc_pale.css
%{_pkgdocdir}/examples
%{_pkgdocdir}/manual
%{_pkgdocdir}/programs
%{_pkgdocdir}/changes.html


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug  5 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.6-11
- Update for Lua 5.4.
- Add BR on make.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.6-1
- Update to 1.4.6.

* Wed Aug 31 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.5-1
- Update to 1.4.5.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.3-4
- Mark license with %%license.
- Remove obsolete conditionals for lua version.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.4.3-2
- rebuild for lua 5.3

* Sun Nov 23 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.3-1
- Update to 1.4.3.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.2-1
- Update to 1.4.2.

* Sun Nov 17 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.0-1
- Update to 1.4.0.
- Use a single package doc dir.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 1.3.11-2
- rebuild for lua 5.2

* Sat Apr 13 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.11-1
- Update to 1.3.11.

* Thu Mar 21 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.7-2
- Require lua-markdown also at run time.

* Thu Mar 21 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.7-1
- Update to 1.3.7.

* Sat Feb 16 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.4-1
- Update to 1.3.4.

* Wed Jan 30 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.3-1
- Update to 1.3.3.

* Wed Jan  9 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-2
- Fix requirements.
- Move docs to a separate package.

* Fri Jan  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-1
- New package.
