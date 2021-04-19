# Generated by go2rpm
%bcond_without check

# https://github.com/pierrec/lz4
%global goipath         github.com/pierrec/lz4
Version:                4.1.3

%gometa

%global goaltipaths     github.com/pierrec/lz4/v4

%global common_description %{expand:
Package lz4 implements reading and writing lz4 compressed data (a frame), as
specified in
http://fastcompression.blogspot.com/2013/04/lz4-streaming-format-final.html.

This package is compatible with the LZ4 frame format although the block level
compression and decompression functions are exposed and are fully compatible
with the LZ4 block format definition, they are low level and should not be
used directly.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        LZ4 compression and decompression in pure Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(code.cloudfoundry.org/bytefmt)
BuildRequires:  golang(github.com/pierrec/cmdflag)
BuildRequires:  golang(github.com/schollz/progressbar/v3)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 18:06:48 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 4.1.3-1
- Update to 4.1.3
- Close: rhbz#1912532

* Mon Dec 21 10:58:01 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.1.2-1
- Update to 4.1.2
- Close: rhbz#1885756

* Thu Sep 17 21:21:55 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.2-1
- Update to 4.0.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 19:44:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-1
- Release 3.0.1

* Thu Jul 25 00:23:40 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.4-1
- Release 2.2.4

* Tue Apr 23 20:28:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.3-1
- Release 2.2.3

* Tue Apr 02 21:57:17 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.1-1
- Release 2.1.1 (#1693414)

* Mon Oct 29 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- First package for Fedora
