# Generated by go2rpm
%bcond_without check

# https://github.com/rakyll/statik
%global goipath         github.com/rakyll/statik
Version:                0.1.7

%gometa

%global common_description %{expand:
Statik allows you to embed a directory of static files into your Go binary to be
later served from an http.FileSystem.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Embed files into a Go executable

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Use Modified.UTC() instead of ModTime() for Go 1.13
Patch0:         0001-Use-Modified.UTC-instead-of-ModTime.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%build
%gobuild -o %{gobuilddir}/bin/statik %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck -d fs
%endif

%files
%license LICENSE
%doc example README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 17:37:04 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.7-1
- Update to 0.1.7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 16:58:28 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.6-1
- Release 0.1.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitf19d7c2
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitf19d7c2
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitf19d7c2
- Remove superfluous Provides
  related: #1250500

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.gitf19d7c2
- Update spec file to spec-2.0
  resolves: #1250500

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitf19d7c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.gitf19d7c2
- First package for Fedora
  resolves: #1162091
