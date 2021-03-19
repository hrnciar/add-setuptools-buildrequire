# Generated by go2rpm
%bcond_without check

# https://github.com/coreos/go-log
%global goipath         github.com/coreos/go-log
%global commit          b22fd89e1882702b3ba97bc792ca6b45e7e6b635

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-coreos-go-log-devel < 0-0.24
}

%global common_description %{expand:
Go logging library with systemd journal support.}

%global golicenses      LICENSE NOTICE
%global godocs          README.md code-of-conduct.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.29%{?dist}
Summary:        Go logging library with systemd journal support

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/coreos/go-systemd/journal)
BuildRequires:  golang(github.com/kardianos/osext)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.25.20190703gitb22fd89
- Add Obsoletes for old name

* Thu May 30 17:35:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.24.20190703gitb22fd89
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.gitb22fd89
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.22.20181114gitb22fd89
- Bump to commit b22fd89e1882702b3ba97bc792ca6b45e7e6b635

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.21.20131126git840af6b
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20131126git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.19.git840af6b
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.18.20131126git840af6b
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.git840af6b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.git840af6b
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.10.git840af6b
- Update to spec-2.1
  related: #1248717

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.git840af6b
- Update spec file to spec-2.0
  resolves: #1248717

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git840af6b
- Update [Build]Requires for github.com/coreos/go-systemd/journal
- Polish spec file
- Do not redefine gopath
  related: #1018523

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git840af6b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.git840af6b
- removed double quotes from provides and requires

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.git840af6b
- defattr removed

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.git840af6b
- Requires kardianos/osext and coreos/go-systemd

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.git840af6b
- URL corrected
- License corrected

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git840af6b
- Initial fedora package
