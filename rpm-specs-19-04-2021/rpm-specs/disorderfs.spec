Name:           disorderfs
Version:        0.5.11
Release:        1%{?dist}
Summary:        FUSE filesystem that introduces non-determinism
URL:            https://salsa.debian.org/reproducible-builds/%{name}
License:        GPLv3+
Source0:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        https://salsa.debian.org/reproducible-builds/reproducible-website/-/raw/master/reproducible-builds-developers-keys.asc

BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  fuse-devel
BuildRequires:  pkg-config
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  fuse
BuildRequires:  bc

Requires:       fuse

%description
disorderfs is an overlay FUSE filesystem that introduces non-determinism
into filesystem metadata.  For example, it can randomize the order
in which directory entries are read.  This is useful for detecting
non-determinism in the build process.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=/usr

%check
make -C tests test || true

%files
%doc README
%license COPYING
%{_bindir}/disorderfs
%{_datadir}/man/man1/disorderfs.1*

%changelog
* Tue Feb 09 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.11-1
- version 0.5.11

* Thu Feb 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.10-2
- Update spec and add tests.

* Mon Jan 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.10-1
- Initial RPM packaging.
