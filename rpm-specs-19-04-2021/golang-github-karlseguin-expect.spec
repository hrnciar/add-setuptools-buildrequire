# Generated by go2rpm
%bcond_without check

# https://github.com/karlseguin/expect
%global goipath         github.com/karlseguin/expect
Version:                1.0.7

%gometa

%global goaltipaths     gopkg.in/karlseguin/expect.v1

%global common_description %{expand:
A library to help you write tests in Go.}

%global golicenses      license.txt
%global godocs          readme.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Testing framework for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/wsxiaoys/terminal/color)

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|gopkg.in/karlseguin/expect.v1|github.com/karlseguin/expect|" "{}" +;
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d . -d build
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 18:16:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.7-1
- Update to 1.0.7

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 19:22:29 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-5.20190809git778a5f0
- Bump to commit 778a5f0c600305097a09c66558691650b2f5b4b5

* Mon Aug 05 22:21:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-4
- Add patch to disable flag.Parse() in init

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 15:59:56 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Release 1.0.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git5c2eadb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.git5c2eadb
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git5c2eadb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.git5c2eadb
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.20160716git5c2eadb
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git5c2eadb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git5c2eadb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git5c2eadb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 01 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git5c2eadb
- First package for Fedora
  resolves: #1418370
