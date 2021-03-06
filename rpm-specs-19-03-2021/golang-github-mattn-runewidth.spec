# Generated by go2rpm
%bcond_without check

# https://github.com/mattn/go-runewidth
%global goipath         github.com/mattn/go-runewidth
Version:                0.0.10

%gometa

%global common_description %{expand:
Package go-runewidth provides functions to get fixed width of a character or
string.}

%global golicenses      LICENSE
%global godocs          README.mkd

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Functions for getting fixed width of a character or string

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/rivo/uniseg)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 17:11:42 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.10-1
- Update to 0.0.10

* Wed Jul 29 20:40:06 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.9-1
- Update to 0.0.9

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.8-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.7-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.4-3
- Add Obsoletes for old name

* Wed Apr 24 22:53:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.4-2
- Update to new macros

* Sat Feb 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.4-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.3-1
- Update to release 0.0.3

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.14.20170201git9e777a8
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git9e777a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git9e777a8
- Upload glide files

* Fri Mar 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git9e777a8
- Update to spec 3.0

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20170201git9e777a8
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git9e777a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.git9e777a8
- Bump to upstream 9e777a8366cce605130a531d2cd6363d07ad7317
  related: #1405690

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git737072b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git737072b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git737072b
- Bump to upstream 737072b4e32b7a5018b4a7125da8d12de90e8045
  related: #1405690

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitd6bea18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.3.gitd6bea18
- Polish the spec file
  resolves: #1405690

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitd6bea18
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Mar 21 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitd6bea18
- First package for Fedora
  resolves: #1319715
