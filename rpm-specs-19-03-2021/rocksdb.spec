%global forgeurl https://github.com/facebook/rocksdb

Name:    rocksdb
Version: 6.15.5
Release: 1%{?dist}
Summary: A Persistent Key-Value Store for Flash and RAM Storage

License: GPLv2 or ASL 2.0 and BSD
URL:     %{forgeurl}


# rocksdb fails to build successfully on x86
# https://bugzilla.redhat.com/show_bug.cgi?id=1875284
ExcludeArch: %{ix86}

BuildRequires: gcc-c++
BuildRequires: gflags-devel
BuildRequires: make

%forgemeta
Source: %{forgesource}

# https://bugzilla.redhat.com/show_bug.cgi?id=1923386
# https://github.com/facebook/rocksdb/issues/8021
Patch0: gcc-c++-false-positive-warning.patch

%description
RocksDB is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multi-threaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package devel
Summary: Development files for rocksdb
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for rocksdb


%prep
%forgesetup

%patch0 -p1

%build
%{set_build_flags}
PORTABLE=1 USE_RTTI=1 %{make_build} shared_lib

%install
make install-shared PREFIX=%{_prefix} LIBDIR=%{_libdir} DESTDIR=%{buildroot}

%files
%doc README.md
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so.6
%{_libdir}/librocksdb.so.6.15
%{_libdir}/librocksdb.so.6.15.5


%files devel
%doc README.md
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so
%{_libdir}/pkgconfig/rocksdb.pc
%{_includedir}/rocksdb

%changelog
* Wed Mar 03 2021 Jonny Heggheim <hegjon@gmail.com> - 6.15.5-1
- Updated to version 6.15.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Jonny Heggheim <hegjon@gmail.com> - 6.13.3-1
- Updated to version 6.13.3

* Thu Sep 03 2020 Jonny Heggheim <hegjon@gmail.com> - 6.11.4-3
- Disable building on x86 due to compile errors

* Sat Jul 25 2020 Jonny Heggheim <hegjon@gmail.com> - 6.11.4-2
- Use RTTI

* Wed Jul 22 2020 Jonny Heggheim <hegjon@gmail.com> - 6.11.4-1
- Updated to 6.11.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 5.7.3-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Matej Mužila <mmuzila@redhat.com> - 5.7.3-1
- Update to version 5.7.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jan 24 2017 Matej Muzila <mmuzila@redhat.com> 5.2.1-1
- Packaged rocksdb
