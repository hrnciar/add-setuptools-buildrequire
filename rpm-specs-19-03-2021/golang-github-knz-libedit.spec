# Generated by go2rpm
%bcond_without check

# https://github.com/knz/go-libedit
%global goipath         github.com/knz/go-libedit
Version:                1.10.1

%gometa

%global godevelheader %{expand:
Requires:       pkgconfig(libedit)}

%global common_description %{expand:
Go wrapper around libedit, a replacement to GNU readline using the BSD license.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %{?dist}.1
Summary:        Go wrapper around the BSD libedit replacement to GNU readline

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Patch to use system libedit
Patch0:         0001-Use-system-libedit.patch

BuildRequires:  pkgconfig(libedit)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 19:43:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.10.1-1
- Update to 1.10.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 22:29:30 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.1-1
- Initial package