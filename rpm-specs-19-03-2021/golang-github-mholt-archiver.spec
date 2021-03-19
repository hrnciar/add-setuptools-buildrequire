# Generated by go2rpm
%bcond_without check

# https://github.com/mholt/archiver
%global goipath         github.com/mholt/archiver
Version:                3.5.0

%gometa

%global goaltipaths     github.com/mholt/archiver/v3

%global common_description %{expand:
Package Archiver makes it trivially easy to make and extract common archive
formats such as zip and tarball (and its compressed variants). Simply name the
input and output file(s). The arc command runs the same on all platforms and has
no external dependencies (not even libc). It is powered by the Go standard
library and several third-party, pure-Go libraries.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Easily create and extract archive files with Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/andybalholm/brotli)
BuildRequires:  golang(github.com/dsnet/compress/bzip2)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/klauspost/compress/zstd)
BuildRequires:  golang(github.com/klauspost/pgzip)
BuildRequires:  golang(github.com/nwaples/rardecode)
BuildRequires:  golang(github.com/pierrec/lz4)
BuildRequires:  golang(github.com/ulikunitz/xz)
BuildRequires:  golang(github.com/xi2/xz)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/archiver %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Jan 31 02:52:04 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 3.5.0-3
- Add alternate import path

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Dominik Mierzejewski <rpm@greysector.net> - 3.5.0-1
- update to 3.5.0 (#1882880)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Dominik Mierzejewski <dominik@greysector.net> - 3.3.0-1
- update to 3.3.0 (#1772601)

* Sat Aug 03 23:28:56 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.2.0-1
- Release 3.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 18:11:30 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.1-1
- Release 3.1.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 2.0-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.0-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 2.0-1
- initial package for Fedora
