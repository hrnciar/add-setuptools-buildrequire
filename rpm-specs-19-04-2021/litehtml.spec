%global commit b4c815c0ed7e2140bc4a239be01f01c00b9cf431
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20210323

Name:           litehtml
Version:        0.5
Release:        4%{?commit:.%{gitdate}git%{shortcommit}}%{?dist}
Summary:        Fast and lightweight HTML/CSS rendering engine

License:        BSD
URL:            https://github.com/litehtml/litehtml
%if 0%{?commit:1}
Source0:        https://github.com/litehtml/litehtml/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/litehtml/litehtml/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
# Downstream patch
# The Fedora gumbo-parser package does not contain a cmake module,
# so don't look for it
Patch0:         litehtml_gumbo.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gumbo-parser-devel
BuildRequires:  make
BuildRequires:  /usr/bin/xxd


%description
litehtml is the lightweight HTML rendering engine with CSS2/CSS3 support.
Note that litehtml itself does not draw any text, pictures or other graphics
and that litehtml does not depend on any image/draw/font library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gumbo-parser-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-v%{version}
%endif

# Ensure no bundled gumbo and xxd are used
rm -rf src/gumbo
rm -rf xxd


%build
%cmake -DBUILD_TESTING=ON -DEXTERNAL_GUMBO=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}


%changelog
* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 0.5-4.20210323gitb4c815c
- Add litehtml_gumbo.patch

* Tue Mar 23 2021 Sandro Mani <manisandro@gmail.com> - 0.5-3.20210323gitb4c815c
- Update to git b4c815c
- Drop upstreamed patches

* Tue Mar 23 2021 Sandro Mani <manisandro@gmail.com> - 0.5-2.20210317gitb6442d9
- Delete bundled xxd.exe in prep
- Fix changelog formatting

* Fri Mar 19 2021 Sandro Mani <manisandro@gmail.com> - 0.5-1.20210317gitb6442d9
- Update to git b6442d9
- Drop upstreamed patches
- Unbundle downstream
- Enable tests

* Wed Mar 17 2021 Sandro Mani <manisandro@gmail.com> - 0.5-1.gitdb7f59d
- Initial package
