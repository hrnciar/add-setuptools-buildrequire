# Generated by go2rpm
%bcond_without check

# https://github.com/jmespath/go-jmespath
%global goipath         github.com/jmespath/go-jmespath
Version:                0.4.0

%gometa

%global common_description %{expand:
A JMESPath implementation in Go.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang implementation of JMESPath

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib)
BuildRequires:  golang(github.com/stretchr/objx)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 14:01:53 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Update to 0.4.0
- Close: rhbz#1880704

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-2.20181005gitc2b33e8
- Add Obsoletes for old name

* Fri Apr 19 10:39:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1.20181005gitc2b33e8
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.11.gitc2b33e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.2.2-0.10.gitbd40a43
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Oct 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-0.9.20181005gitbd40a43
- Bump to upstream c2b33e8439af944379acbdd9c3a5fe0bc44bd8a5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.8.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.2.2-0.7.gitbd40a43
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.2.2-0.6.20160803gitbd40a43
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.5.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.4.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.3.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.2.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.2.2-0.1.gitbd40a43
- Bump to upstream bd40a432e4c76585ef6b72d3fd96fb9b6dc7b68d
  resolves: #1413287

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git0b12d6b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Fri Apr 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git0b12d6b
- First package for Fedora
  resolves: #1297550
