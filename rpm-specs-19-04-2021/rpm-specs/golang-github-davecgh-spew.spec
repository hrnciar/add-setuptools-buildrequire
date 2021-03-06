# Generated by go2rpm
%bcond_without check

# https://github.com/davecgh/go-spew
%global goipath         github.com/davecgh/go-spew
Version:                1.1.1

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-davecgh-go-spew-devel < 1.1.1-3
}

%global common_description %{expand:
Go-spew implements a deep pretty printer for Go data structures to aid in
debugging. A comprehensive suite of tests with 100% test coverage is
provided to ensure proper functionality.}

%global golicenses      LICENSE
%global godocs          README.md test_coverage.txt

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        8%{?dist}
Summary:        Implements a deep pretty printer for go data structures to aid in debugging

License:        ISC
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-4
- Add Obsoletes for old name.

* Mon Apr 15 18:20:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-3
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1.20181029git272ad12
- Update to upstream v1.1.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.1.0-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1.0-2
- Upload glide files

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Update to upstream v1.1.0
- Update to new guidelines for Go

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.20161107git6d21280
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git6d21280
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git6d21280
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git6d21280
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git6d21280
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git6d21280
- Bump to upstream 6d212800a42e8ab5c146b8ace3490ee17e5225f9
  related: #1248791

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git3e6e67c
- Polish the spec file
  related: #1248791

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git3e6e67c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git3e6e67c
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git3e6e67c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git3e6e67c
- Update to spec-2.1
  related: #1248791

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git3e6e67c
- Update spec file to spec-2.0
  resolves: #1248791

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git3e6e67c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git3e6e67c
- Bump to upstream 3e6e67c4dcea3ac2f25fd4731abc0e1deaf36216
  related: #1172198

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git1aaf839
- Bump to upstream 1aaf839fb07e099361e445273993ccd9adc21b07
  related: #1172198

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git83f84dc
- First package for Fedora
  resolves: #1172198

