# Generated by go2rpm
%bcond_without check

# https://github.com/libgit2/git2go
%global goipath         github.com/libgit2/git2go
Version:                31.4.7

%gometa

%global godevelheader %{expand:
Requires:      (pkgconfig(libgit2) >= 1.1.0 with pkgconfig(libgit2) < 1.2.0)}

%global common_description %{expand:
Go bindings for libgit2.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Bindings for libgit2

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         0001-Skip-tests-that-use-the-network.patch

BuildRequires: (pkgconfig(libgit2) >= 1.1.0 with pkgconfig(libgit2) < 1.2.0)
BuildRequires: golang(github.com/google/shlex)
BuildRequires: golang(golang.org/x/crypto/ssh)
%if %{with check}
BuildRequires: git-core
BuildRequires: golang(golang.org/x/crypto/openpgp)
BuildRequires: golang(golang.org/x/crypto/openpgp/packet)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 31.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 31.4.7-1
- Update to 31.4.7

* Tue Jul 28 22:24:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 30.0.5-1
- Update to 30.0.5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.28.4.1-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.28.4-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.28.3.20190703gitb2e2b2f
- Re-enable 32-bit builds

* Wed Jul 03 22:47:03 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.28.2.20190703gitb2e2b2f
- Bump to commit b2e2b2f71bb47ae3d4cfde07b39f524f13d0df93

* Sun Jun 02 20:23:48 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.27.2.20190223gitecaeb7a
- Update to new macros

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.27.1.20190223gitecaeb7a
- First package for Fedora
