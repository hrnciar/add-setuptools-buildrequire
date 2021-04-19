# Generated by go2rpm
%bcond_without check

# https://github.com/milochristiansen/axis2
%global goipath         github.com/milochristiansen/axis2
%global commit          20ad74518c74a422cbc5d888d03e339d896aa5f9

%gometa

%global common_description %{expand:
AXIS is based on a few simple interfaces and a set of API functions that operate
on these interfaces. Clients use the provided implementations of these
interfaces (or provide their own custom implementations) to create "data
sources" that may be mounted on a "file system" and used for OS-independent file
IO.

AXIS was originally written to allow files inside of archives to be handled with
exactly the same API as used for files inside of directories, but it has since
grown to allow "logical" files and directories as well as "multiplexing"
multiple items on the same location (to, for example, make two directories look
and act like one). These properties make AXIS perfect for handling data and
configuration files for any program where flexibility is important, the program
does not need to know where its files are actually located, it simply needs them
to be at a certain place in it's AXIS file system. Changing where a program
loads it's files from is then as simple as changing the code that initializes
the file system.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.15%{?dist}
Summary:        AXIS Virtual File System

# Upstream license specification: Zlib
License:        zlib
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 16:11:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.10.20190602git20ad745
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git20ad745
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git20ad745
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git20ad745
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git20ad745
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git20ad745
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Ben Rosser <rosser.bjr@gmail.com> - 0-0.4.git20ad745
- Remove conditional around with_devel defines to actually build on EPEL > 6.

* Wed Apr 05 2017 Ben Rosser <rosser.bjr@gmail.com> - 0-0.3.git20ad745
- Updated to latest upstream release, with license file.

* Wed Mar 29 2017 Ben Rosser <rosser.bjr@gmail.com> - 0-0.2.gitb5183a8
- Clean up template golang spec file, removing Godeps path and an empty ifdef block.
- Renamed download of Source0 to include the project prefix.
- Change versioning to pre-release snapshot versions.
- Include link to upstream bug requesting a license/copying file.
- Added comment asking upstream to add license file.

* Sat Dec 31 2016 Ben Rosser <rosser.bjr@gmail.com> - 0-0.1.gitb5183a8
- First package for Fedora
