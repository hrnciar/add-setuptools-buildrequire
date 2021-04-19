Summary:        Library for real-time audio and video processing
Name:           librem
Version:        1.0.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/baresip/rem
Source0:        https://github.com/baresip/rem/archive/v%{version}/rem-%{version}.tar.gz
# Upstream .so name versioning (not yet available in a release)
Patch0:         librem-1.0.0-eea93d4.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libre-devel
# Cover multiple third party repositories
Obsoletes:      librem0 < 0.6.0-2
Provides:       librem0 = %{version}-%{release}
Provides:       librem0%{?_isa} = %{version}-%{release}
Obsoletes:      rem < 0.6.0-2
Provides:       rem = %{version}-%{release}
Provides:       rem%{?_isa} = %{version}-%{release}

%description
Librem is a portable and generic library for real-time audio and video
processing.

%package devel
Summary:        Development files for the rem library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libre-devel
# Cover multiple third party repositories
Obsoletes:      librem0-devel < 0.6.0-2
Provides:       librem0-devel = %{version}-%{release}
Provides:       librem0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      rem-devel < 0.6.0-2
Provides:       rem-devel = %{version}-%{release}
Provides:       rem-devel%{?_isa} = %{version}-%{release}

%description devel
The librem-devel package includes header files and libraries necessary for
developing programs which use the rem C library.

%prep
%setup -q -n rem-%{version}
%patch0 -p1 -b .eea93d4

%build
%make_build \
  SHELL='sh -x' \
  RELEASE=1 \
  EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
  EXTRA_LFLAGS="$RPM_LD_FLAGS"

%install
%make_install \
  LIBDIR=%{_libdir}

# Remove static library
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a

%ldconfig_scriptlets

%files
%license docs/COPYING
%doc docs/ChangeLog
%{_libdir}/%{name}.so.0*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/rem/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Apr 10 2021 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0 (#1948096)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Robert Scheck <robert@fedoraproject.org> 0.6.0-4
- Rebuilt for libre 1.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.0-2
- Changes to match the Fedora Packaging Guidelines (#1843268 #c1)

* Thu May 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.0-1
- Upgrade to 0.6.0 (#1843268)
- Initial spec file for Fedora and Red Hat Enterprise Linux
