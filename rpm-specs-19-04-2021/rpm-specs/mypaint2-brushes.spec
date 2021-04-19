%global debug_package %{nil}

Name: mypaint2-brushes
Version: 2.0.2
Release: 2%{?dist}
Summary: Collections of brushes for MyPaint
License: CC0
URL: https://github.com/mypaint/mypaint-brushes
Source0: https://github.com/mypaint/mypaint-brushes/releases/download/v%{version}/mypaint-brushes-%{version}.tar.xz
BuildArch: noarch

BuildRequires: make

%description
Brushes used by MyPaint 2 and other software using libmypaint2.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains files needed for development with %{name}.

%prep
%autosetup -n mypaint-brushes-%{version}

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc README
%{_datadir}/mypaint-data/2.0

%files devel
%{_datadir}/pkgconfig/mypaint-brushes-2.0.pc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.1-1
- Initial package
