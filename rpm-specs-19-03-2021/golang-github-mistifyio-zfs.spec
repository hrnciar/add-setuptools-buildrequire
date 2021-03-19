# Generated by go2rpm
# Needs a working ZFS setup
%bcond_with check

# https://github.com/mistifyio/go-zfs
%global goipath         github.com/mistifyio/go-zfs
Version:                2.1.1
%global commit          f784269be439d704d3dfa1906f45dd848fed2beb

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-mistifyio-go-zfs-devel < 2.1.1-2
}

%global common_description %{expand:
Simple wrappers for ZFS command line tools.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        8%{?dist}
Summary:        Go wrappers for ZFS commands

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/google/uuid)

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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-3.20190627gitf784269
- Add Obsoletes for old name

* Sat May 04 23:02:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.1-2.20190627gitf784269
- Bump to commit f784269be439d704d3dfa1906f45dd848fed2beb

* Wed Apr 03 22:33:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.1-1.20190403gitd5b1632
- Release 2.1.1, commit d5b163290a48f624cbf244ebe4e89ce38653064c (#1695231)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.11.git1b4ae6f
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git1b4ae6f
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git1b4ae6f
- Excluder aarch64 architecture
  resolves: #1465016

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git1b4ae6f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Jun 07 2016 jchaloup <jchaloup@redhat.com> - 0-0.2.git1b4ae6f
- Don't build on arm architectures (missing zfs-fuse)
  resolves: #1341333

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git1b4ae6f
- First package for Fedora
  resolves: #1327291
