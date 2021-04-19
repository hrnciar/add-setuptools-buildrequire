Name:           libucl
Version:        0.8.1
Release:        7%{?dist}
Summary:        Universal configuration library parser

License:        BSD and MIT
URL:            https://github.com/vstakhov/libucl
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  libtree-devel
BuildRequires:  mum-hash-devel

# Partial http://troydhanson.github.io/uthash (BSD) - 2.x is shipped in Fedora.
Provides: bundled(uthash) = 1.9.8

# Partial and patched https://github.com/attractivechaos/klib (MIT).
# Upstream is not released as a single archive and only provide per-file
# versioning.
Provides: bundled(klib)

%description
%{summary}.

%package        devel
Summary:        libucl development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%package     -n python3-libucl
Summary:        Python bindings for libucl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-libucl
%{summary}.

%prep
%autosetup

# pkg-config: remove trailing slash from standard include dir.
sed -i 's/includedir}\/$/includedir}/' libucl.pc.in

# Remove bundled libraries.
sed -i '/mum\.h/d' src/Makefile.am
sed -i '/tree\.h/d' src/Makefile.am
sed -i 's/ucl_chartable.h \\/ucl_chartable.h/' src/Makefile.am
rm src/mum.h src/tree.h

# Set include/lib dir for python bindings.
sed -i "s%language = 'c'%language = \'c\', include_dirs = [ \"../include\"],  library_dirs = [ \"../src/.libs\"]%" python/setup.py

# Run autoconf.
./autogen.sh

# Remove network-dependent tests.
for def in schema/ref.json schema/refRemote.json schema/definitions.json; do
  rm tests/$def
done

%configure --disable-static

%build
V=1 %make_build
(cd python; %py3_build)

%install
%make_install
(cd python; %py3_install)

# Remove useless la file (SHOULD NOT be included per Fedora packaging
# policies).
rm %{buildroot}%{_libdir}/%{name}.la

%check
%make_build check

%files
%license COPYING
%doc README.md
%{_libdir}/libucl.so.*
%{_mandir}/man3/libucl.3*

%files devel
%{_libdir}/pkgconfig/libucl.pc
%{_libdir}/libucl.so
%{_includedir}/ucl*

%files -n python3-libucl
%{python3_sitearch}/ucl*

%changelog
* Fri Apr 09 2021 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-7
- Add missing python3-devel dependency.
- Fix include and lib dirs when building python subpackage.

* Wed Mar 24 2021 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-6
- Unbundle mum-hash and libtree.

* Sat Mar 06 2021 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-5
- Mark bundled libraries and adapt license.
- Package Python bindings.

* Sun Dec 27 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-4
- Remove statically compiled output and .la libtool file from devel subpackage.
- Move check section after install section.
- Patch pkgconfig includes.

* Sun Dec 27 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-3
- Run test suite in check section.
- Make devel subpackage requires on base package arch-dependent.

* Sun Apr 19 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-2
- Build with automake instead of incomplete Makefile.unix

* Mon Feb 24 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-1
- Let there be package.
