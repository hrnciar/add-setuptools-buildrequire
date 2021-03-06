# Generated by go2rpm
%ifnarch %{arm} %{ix86}
%bcond_without check
%endif

# https://github.com/golang/snappy
%global goipath         github.com/golang/snappy
Version:                0.0.2

%gometa

%global goaltipaths     github.com/syndtr/gosnappy

%global common_description %{expand:
Implementation of the Snappy compression format for Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README

Name:           %{goname}
Release:        3%{?dist}
Summary:        Implementation of the Snappy compression format for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# bug fix to encode_arm64.s: some registers overwritten in memmove call
Patch0:         https://github.com/golang/snappy/commit/f81760ec4c9208e6e6866cf18e1888544fd2dbc9.patch#/0001-bug-fix-to-encode_arm64.s.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

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
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 00:42:58 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-2
- Add patch to fix bug in encode_arm64.s

* Tue Dec 22 03:33:38 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-1
- Update to 0.0.2
- Close: rhbz#1881247

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 18:56:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- Release 0.0.1

* Wed Apr 10 14:30:11 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.15.20190409git2e65f85
- Provides compaitbility for gosnappy/snappy

* Tue Apr 09 22:26:47 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.14.20190409git2e65f85
- Bump to commit 2e65f85255dbc3072edf28d6b5b8efc472979f5a
- Update to new go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git156a073
- https://fedoraproject.org/wiki/Changes/golang1.7

* Fri Apr 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.git156a073
- Polish the spec file
- Extend the spec with github.com/golang/snappy (which is newer version of gosnappy)
  related: #1220164

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git156a073
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git156a073
- Update spec file to spec-2.0
  related: #1220164

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git156a073
- Bump to upstream 156a073208e131d7d2e212cb749feae7c339e846
  resolves: #1220164

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitce8acff
- First package for Fedora
  resolves: #1190411
