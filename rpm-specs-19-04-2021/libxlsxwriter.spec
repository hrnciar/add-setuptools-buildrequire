Name:           libxlsxwriter
Version:        1.0.2
Release:        1%{?dist}
Summary:        A C library for creating Excel XLSX files

# BSD: Most files
# Public Domain: third_party/md5/*
# MPL: third_party/tmpfileplus/*
License:        BSD and Public Domain and MPLv2.0
URL:            https://github.com/jmcnamara/libxlsxwriter/
Source0:        https://github.com/jmcnamara/libxlsxwriter/archive/RELEASE_%{version}/%{name}-%{version}.tar.gz

# Add missing include <zlib.h>
# https://github.com/jmcnamara/libxlsxwriter/pull/316
Patch0:         libxlsxwriter_zlib.patch
# Add a soversion
# https://github.com/jmcnamara/libxlsxwriter/pull/316
Patch1:         libxlsxwriter_sover.patch

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  minizip-devel
BuildRequires:  zlib-devel


%description
Libxlsxwriter is a C library that can be used to write text, numbers, formulas
and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-RELEASE_%{version}

# Delete bundled minizip
rm -rf third_party/minizip
rm -f include/xlsxwriter/third_party/zip.h


%build
%cmake -DUSE_SYSTEM_MINIZIP=ON -DBUILD_TESTS=ON
%cmake_build


%install
%cmake_install

%check
%ctest


%files
%license License.txt
%doc Readme.md Changes.txt
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/xlsxwriter.h
%{_includedir}/xlsxwriter/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/xlsxwriter.pc


%changelog
* Fri Apr 16 2021 Sandro Mani <manisandro@gmail.coM> - 1.0.2-1
- Update to 1.0.2

* Wed Mar 31 2021 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Tue Feb 09 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Rebuilt for minizip 3.0.0

* Tue Feb 09 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-4
- Rebuild (minizip)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-2
- Fix license
- Start with soversion 0
- Remove ldconfig scriptlets

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Update to 1.0.0
