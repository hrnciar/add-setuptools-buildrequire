%bcond_without check

# https://github.com/haproxytech/config-parser
%global goipath         github.com/haproxytech/config-parser
Version:                3.1.0

%gometa

# %%global extractdir      %%(echo %%{extractdir} | sed -e 's/~/-/g')
# %%global gosource        %%(echo %%{gosource} | sed -e 's/~/-/g')

%global goaltipaths     %{goipath}/v3

%global common_description %{expand:
HAProxy configuration parser.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        HAProxy configuration parser

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gofrs/flock)
BuildRequires:  golang(github.com/google/renameio)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Fri Mar 19 2021 Brandon Perkins <bperkins@redhat.com> - 3.1.0-1
- Update to version 3.1.0 (Fixes rhbz#1940974)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 16:15:02 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Update to 3.0.0
- Close: rhbz#1916916

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.0~rc2-2
- Modify gosource so that Source0 resolves correctly  (Fixes rhbz#1912980)

* Tue Jan 12 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.0~rc2-1
- Update to version 3.0.0-rc2 (Fixes rhbz#1912980)

* Thu Sep 03 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.5-1
- Update to version 2.0.5 (Fixes rhbz#1875169)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.4-1
- Update to version 2.0.4 (Fixes rhbz#1859324)
- Add golang(github.com/google/renameio) BuildRequires

* Mon May 18 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.2-1
- Update to version 2.0.2

* Mon Apr 27 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.1-1
- Upgrade to version 2.0.1

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.0-1
- Upgrade to version 1.2.0
- Clean changelog

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.1.10-1
- Initial package

