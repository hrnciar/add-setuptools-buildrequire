Name:           libxls
Version:        1.6.2
Release:        2%{?dist}
Summary:        Read binary Excel files from C/C++

License:        BSD
URL:            https://github.com/libxls/libxls
Source0:        https://github.com/libxls/libxls/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
This is libxls, a C library for reading Excel files in the old binary OLE
format, plus a command-line tool for converting XLS to CSV (named,
appropriately enough, libxls2csv).


%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}


%prep
%autosetup -p1


%build
# Add prefix to not conflict executables with catdoc.
%configure --program-prefix=lib
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete


%check
PATH=%{buildroot}%{_bindir}:$PATH LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
    make check || ( cat ./test-suite.log && exit 1 )


%files
%doc README.md AUTHORS
%license LICENSE
%{_bindir}/libxls2csv
%{_libdir}/libxlsreader.so.8
%{_libdir}/libxlsreader.so.8.*
%{_mandir}/man1/libxls2csv.1*

%files devel
%{_includedir}/xls.h
%{_includedir}/libxls
%{_libdir}/libxlsreader.so
%{_libdir}/pkgconfig/libxls.pc


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.2-1
- Update to latest version (#1911771)

* Tue Dec 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.1-2
- Fix CVE-2020-27819

* Wed Sep 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.1-1
- Update to latest version (#1873754)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.3-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.2-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-2
- Fix number loading on big-endian systems

* Mon Mar 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Un-retire package to latest version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 01 2013 Christopher Meng <rpm@cicku.me> - 1.3.4-3
- Drop the binary.

* Wed Jul 31 2013 Christopher Meng <rpm@cicku.me> - 1.3.4-2
- Fix the license.
- Correct the description.

* Mon May 20 2013 Christopher Meng <rpm@cicku.me> - 1.3.4-1
- Initial Package.
