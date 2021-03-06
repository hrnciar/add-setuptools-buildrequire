# Generated by go2rpm
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/magiconair/properties
%global goipath         github.com/magiconair/properties
Version:                1.8.4

%gometa

%global common_description %{expand:
Properties is a Go library for reading and writing properties files.

It supports reading from multiple files or URLs and Spring style recursive
property expansion of expressions like ${key} to their corresponding value.
Value expressions can refer to other keys like in ${key} or to environment
variables like in ${USER}. Filenames can also contain environment variables like
in /home/${USER}/myapp.properties.

Properties can be decoded into structs, maps, arrays and values through struct
tags.

Comments and the order of keys are preserved. Comments can be modified and can
be written to the output.

The properties library supports both ISO-8859-1 and UTF-8 encoded data.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        4%{?dist}
Summary:        Java properties scanner for Go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock
# Fix for Go 1.16
# Upstreamed here: https://github.com/magiconair/properties/pull/53
Patch0:         0001-Properly-compare-versions-equal-or-over-to-1.15-in-T.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 17:45:09 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.4-3
- Better fix for FTBFS

* Sun Jan 24 16:28:13 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.4-2
- Fix FTBFS

* Sun Jan  3 14:20:41 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.4-1
- Update to 1.8.4
- Close: rhbz#1872504

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 00:58:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.1-1
- Release 1.8.1

* Tue Feb 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.0-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-9.git0723e35
- Upload glide files

* Wed Mar 07 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-8.git0723e35
- Update to spec 3.0

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-7
- Switch to __go_ignore macro

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-6
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-1
- Bump to upstream 0723e352fa358f9322c938cc2dadda874e9151a9
  related: #1413067

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.5.3-5
- Polish the spec file
  resolves: #1413067

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git6240095
- First package for Fedora
  resolves: #1270054
