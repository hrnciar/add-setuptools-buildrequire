# Generated by go2rpm
%bcond_without check

# https://github.com/hashicorp/go-cleanhttp
%global goipath         github.com/hashicorp/go-cleanhttp
Version:                0.5.1

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-hashicorp-go-cleanhttp-devel < 0.5.1-2
}

%global common_description %{expand:
Convenience utilities for acquiring "clean" http.Transport and http.Client
structs}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        8%{?dist}
Summary:        Convenience utilities for "clean" http.Transport and http.Client structs

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock
# https://github.com/hashicorp/go-cleanhttp/issues/14
Patch0:         https://github.com/hashicorp/go-cleanhttp/commit/d3fcbee8e1810ecee4bdbf415f42f84cfd0e3361.patch#/0001-Fix-tests-against-newer-Go.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-3
- Add Obsoletes for old name

* Wed Apr 17 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.5.1-2
- Update to new macros

* Sun Mar 24 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.5.1-1
- Release 0.5.1 (#1690719)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git5df5ddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.12.git5df5ddc
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it???s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git5df5ddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git5df5ddc
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.20151022git5df5ddc
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git5df5ddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git5df5ddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git5df5ddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git5df5ddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git5df5ddc
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git5df5ddc
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git5df5ddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git5df5ddc
- First package for Fedora

