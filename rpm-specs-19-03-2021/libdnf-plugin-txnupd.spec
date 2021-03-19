# Minimum compatible version
%global libdnf_minver 0.60
%global tukit_minver 3.1.2

Name:           libdnf-plugin-txnupd
Version:        0.1.2
Release:        1%{?dist}
Summary:        libdnf plugin to implement transactional updates

License:        LGPLv2+
URL:            https://code.opensuse.org/microos/libdnf-plugin-txnupd
#Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Use pagure.io mirror as code.opensuse.org doesn't have on-demand archives yet
Source0:        https://pagure.io/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdnf) >= %{libdnf_minver}
BuildRequires:  pkgconfig(tukit) >= %{tukit_minver}

# We need a minimum version of these libraries beyond soname for working APIs
Requires:       libdnf%{?_isa} >= %{libdnf_minver}
Requires:       libtukit%{?_isa} >= %{tukit_minver}

# We need the transactional update dracut module
Requires:       dracut-transactional-update

# To ensure directories for configuration files are in place
Requires:       dnf-data

# This is intended to be used alongside MicroDNF and PackageKit
Recommends:     (microdnf or PackageKit)

# Do not permit normal DNF snapper plugin on the same system
Conflicts:      dnf-plugin-snapper

%description
This package contains the plugin to implement transactional updates
as a libdnf plugin. This plugin hooks into the DNF "context" for
Micro DNF and PackageKit to enable this functionality in normal use.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

# Add configuration to mark this package as protected by libdnf
mkdir -p %{buildroot}%{_sysconfdir}/dnf/protected.d
echo "%{name}" > %{buildroot}%{_sysconfdir}/dnf/protected.d/txnupd.conf


%files
%license LICENSE
%doc README.md
%{_libdir}/libdnf/plugins/txnupd.so
%{_sysconfdir}/dnf/protected.d/txnupd.conf


%changelog
* Sun Mar 07 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.2-1
- Rebase to 0.1.2
- Add protected.d file for self-protection

* Mon Feb 01 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20210127.6a91d55-0.1
- Update to support tukit 3.0.0

* Tue Dec 29 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20201223.2f7a284-0.2
- Add dracut-transactional-update dependency

* Thu Dec 24 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.0~git20201223.2f7a284-0.1
- Initial packaging
