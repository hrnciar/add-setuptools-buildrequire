Name:           udisks2-qt5
Version:        5.0.5
Release:        2%{?dist}
Summary:        Qt5 binding for udisks2
License:        GPLv3+
URL:            https://github.com/linuxdeepin/udisks2-qt5
%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.tar.gz
%endif
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)

%description
This package provides a Qt5 binding for udisks2.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1
sed -i 's|/lib|/%{_lib}|' udisks2.pro

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc CHANGELOG.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.5-1
- new upstream release: 5.0.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr  4 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.1-1
- Initial packaging

