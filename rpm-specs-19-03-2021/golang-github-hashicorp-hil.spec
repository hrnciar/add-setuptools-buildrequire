# Generated by go2rpm
%bcond_without check

# https://github.com/hashicorp/hil
%global goipath         github.com/hashicorp/hil
%global commit          43f73a9c70075edef29491640d19f4b69580753d

%gometa

%global common_description %{expand:
HIL (HashiCorp Interpolation Language) is a lightweight embedded language used
primarily for configuration interpolation. The goal of HIL is to make a simple
language for interpolations in the various configurations of HashiCorp tools.

HIL is built to interpolate any string, but is in use by HashiCorp primarily
with HCL. HCL is not required in any way for use with HIL.

HIL isn't meant to be a general purpose language. It was built for basic
configuration interpolations. Therefore, you can't currently write functions,
have conditionals, set intermediary variables, etc. within HIL itself. It is
possible some of these may be added later but the right use case must exist.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        Small embedded language for string interpolations

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/mitchellh/reflectwalk)

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 20:35:48 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.15.20210109git43f73a9
- Bump to commit 43f73a9c70075edef29491640d19f4b69580753d

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 15:05:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.10.20190531git97b3a9c
- Bump to commit 97b3a9cdfa9349086cfad7ea2fe3165bfe3cbf63

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git1e86c6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.git1e86c6b
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git1e86c6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.git1e86c6b
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.20160712git1e86c6b
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git1e86c6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git1e86c6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git1e86c6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git1e86c6b
- First package for Fedora
  resolves: #1410378
