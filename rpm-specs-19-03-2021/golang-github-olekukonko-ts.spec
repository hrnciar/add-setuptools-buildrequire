# Generated by go2rpm
%bcond_without check

# https://github.com/olekukonko/ts
%global goipath         github.com/olekukonko/ts
%global commit          78ecb04241c0121483589a30b0814836a746187d

%gometa

%global common_description %{expand:
Simple Go application to get terminal size. So many implementations do not
support windows but ts has full windows support. }

%global golicenses      LICENCE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.17%{?dist}
Summary:        Simple Go application to get terminal size

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

# Remove in F33
# Remove erroneous glide.lock folder
%pretrans devel -p <lua>
path = "%{gopath}/src/%{goipath}/glide.lock"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path)
end

%if %{with check}
%check
# .: ENOENT
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 17:31:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.12.20190603git78ecb04
- Bump to commit 78ecb04241c0121483589a30b0814836a746187d

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitecf753e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.10.gitecf753e
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitecf753e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gitecf753e
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitecf753e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitecf753e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitecf753e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitecf753e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.3.gitecf753e
- Polish the spec file
  resolves: #1405558

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitecf753e
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Mar 21 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitecf753e
- First package for Fedora
  resolves: #1319716
