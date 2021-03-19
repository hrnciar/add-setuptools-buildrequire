Name:           ntfs2btrfs
Version:        20210105
Release:        1%{?dist}
Summary:        Conversion tool from NTFS to Btrfs

License:        GPLv2+
URL:            https://github.com/maharmstone/ntfs2btrfs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.14.3
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake(fmt)

# Adapted for specific use in this program, cannot be reasonably separated
Provides:       bundled(ntfs-3g-system-compression)

# There's hand-written x86_64 assembler
ExclusiveArch:  x86_64

%description
ntfs2btrfs is a tool which does in-place conversion of Microsoft's NTFS
filesystem to the open-source filesystem Btrfs, much as btrfs-convert
does for ext2.

The original image is saved as a reflink copy at image/ntfs.img,
and if you want to keep the conversion you can delete this to
free up space.


%prep
%autosetup


%build
%cmake
%cmake_build

%install
%cmake_install


%files
%license LICENCE
%doc README.md
%{_bindir}/ntfs2btrfs


%changelog
* Mon Mar 15 2021 Neal Gompa <ngompa13@gmail.com> - 20210105-1
- Initial packaging for Fedora (RH#1938464)
