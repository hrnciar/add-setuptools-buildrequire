# Generated by go2rpm
%bcond_without check

# https://github.com/samalba/dockerclient
%global goipath         github.com/samalba/dockerclient
%global commit          a3036261847103270e9f732509f43b5f98710ace

%gometa

%global common_description %{expand:
Docker client library in Go.}

%global golicenses      LICENSE
%global godocs          examples README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.18%{?dist}
Summary:        Docker client library in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/stretchr/testify/mock)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/docker/docker/daemon/logger/jsonfilelog/jsonlog)
BuildRequires:  golang(github.com/docker/docker/pkg/ioutils)
BuildRequires:  golang(github.com/docker/docker/pkg/stdcopy)
BuildRequires:  golang(github.com/gorilla/mux)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|github.com/docker/docker/pkg/jsonlog|github.com/docker/docker/daemon/logger/jsonfilelog/jsonlog|" "{}" +;
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
# https://github.com/samalba/dockerclient/issues/244
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 20:49:22 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0-0.14.20190601gita303626
- Bump to commit a3036261847103270e9f732509f43b5f98710ace

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.12.gitc37a52f
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it???s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.gitc37a52f
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.gitc37a52f
- Polish spec and exclude ppc64
  related: #1212626

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitc37a52f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitc37a52f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Apr 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitc37a52f
- First package for Fedora
  resolves: #1212626
