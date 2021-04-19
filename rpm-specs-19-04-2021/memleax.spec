Name:           memleax
Version:        1.1.1
Release:        1%{?dist}
Summary:        Debugs memory leak of a running process

License:        GPLv2
URL:            http://wubingzheng.github.io/memleax/
Source0:        https://github.com/WuBingzheng/memleax/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/WuBingzheng/memleax/master/CMakeLists.txt
%if 0%{?el7}
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires: gcc-c++
BuildRequires: libdwarf-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: libunwind-devel

ExclusiveArch: %{ix86} x86_64 aarch64 armv7hl
%description
Memleax debugs memory leak of a running process by attaching it.
It is very convenient to use, and suitable for production environment.
There is no need to recompile the program or restart the target process.


%prep
%setup -q
cp %{SOURCE1} .

%build
%if 0%{?el7}
%cmake3
%else
%cmake
%endif
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_build
%else
%make_build
%endif

%install
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_install
%else
%make_install
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/memleax
%{_mandir}/man1/memleax.1*


%changelog
* Sun Apr 04 2021 Germano Massullo <germano.massullo@gmail.com> - 1.1.1-1
- first Fedora release


