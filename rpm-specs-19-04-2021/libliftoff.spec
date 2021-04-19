%global commit 24abeb923f52176808461e664776b56d52960d3e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20201110

Name:           libliftoff
Version:        0.0.0%{?snapdate:~git%{snapdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Lightweight KMS plane library

License:        MIT
URL:            https://github.com/emersion/libliftoff
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  meson >= 0.52.0
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconfig(libdrm)

%description
libliftoff eases the use of KMS planes from userspace without
standing in your way. Users create "virtual planes" called
layers, set KMS properties on them, and libliftoff will
allocate planes for these layers if possible.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.0*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.0.0~git20201110.24abeb9-1
- Update to git snapshot required for gamescope 3.7.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0~git20201031.0095702-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov  3 13:38:26 EST 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20201031.0095702-1
- Update to new git snapshot

* Sun Oct  4 15:05:36 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20200526.b004282-1
- Initial packaging
