# Generated by go2rpm
%bcond_without check

# https://github.com/nightlyone/lockfile
%global goipath         github.com/nightlyone/lockfile
Version:                1.0.0

%gometa

%global common_description %{expand:
Handle locking via pid files.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Handle locking via pid files

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 12:25:47 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 15:43:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20190530git0ad87ee
- Bump to commit 0ad87eef1443f64d3d8c50da647e2b1552851124

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gite83dc5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.4.gite83dc5e
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gite83dc5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.2.20180315gite83dc5e
- Upload glide files

* Thu Mar 15 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.gite83dc5e
- First package for Fedora
  resolves: #1556915
