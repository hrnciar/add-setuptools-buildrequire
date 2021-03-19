Name:           reprotest
Version:        0.7.16
Release:        3%{?dist}
Summary:        Build packages and check them for reproducibility
URL:            https://salsa.debian.org/reproducible-builds/%{name}
License:        GPLv3+
Source0:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}_%{version}.tar.xz
Source1:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}_%{version}.tar.xz.asc
Source2:        https://salsa.debian.org/reproducible-builds/reproducible-website/-/raw/master/reproducible-builds-developers-keys.asc
BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-rstr
Requires:       diffoscope
Requires:       disorderfs
Requires:       faketime
Requires:       fakeroot
Requires:       glibc-all-langpacks
Requires:       rpm-build

%description
reprotest builds the same source code twice in different environments, and
then checks the binaries produced by each build for differences. If any are
found, then diffoscope (or if unavailable then diff) is used to display them
in detail for later analysis.

It supports different types of environment such as a "null" environment (i.e.
doing the builds directly in /tmp) or various other virtual servers, for
example schroot, ssh, qemu, and several others.

reprotest is developed as part of the "reproducible builds" Debian project.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%{_bindir}/reprotest
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 09 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-3
- Use sources signature verification

* Mon Feb 08 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-2
- Update requirements

* Wed Feb 03 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-1
- version 0.7.16

* Mon Jan 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.15-1
- Initial RPM packaging.
