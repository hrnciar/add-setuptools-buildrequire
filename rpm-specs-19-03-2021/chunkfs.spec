Name:           chunkfs
Version:        0.8
Release:        2%{?dist}
Summary:        FUSE based filesystem that allows you to mount an arbitrary file or block device

License:        GPLv2+
URL:            https://chunkfs.florz.de/
Source0:        https://chunkfs.florz.de/%{name}_%{version}.tar.xz
Source100:      CMakeLists.txt

BuildRequires:  cmake gcc
# For pod2man
BuildRequires:  perl-podlators
BuildRequires:  fuse-devel

%description
ChunkFS is a FUSE based filesystem that allows you to mount an arbitrary file
or block device as a directory tree of files that each represent a chunk of
user-specified size of the mounted file. The chunk size is global per mount,
but at mount time any value can be specified. (If the file size isn't a
multiple of the specified chunk size, the last file in the tree simply will be
smaller than the chunk size.) Only read access is supported at the moment.

UnChunkFS is the inversion of ChunkFS—it allows you to mount a ChunkFS tree (or
a copy of it, of course), and gives you a single file named image that has the
same contents as the file or device you created the tree from by mounting it as
a ChunkFS.


%prep
%autosetup -p1
install %{SOURCE100} .


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc README
%{_bindir}/*
%{_docdir}/%{name}/examples/
%{_mandir}/man1/*chunkfs.1*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Richard Shaw <hobbes1069@gmail.com> - 0.8-1
- Initial packaging.
