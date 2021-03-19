# Generated by go2rpm
# use of internal package not allowed because not common root
%bcond_with check

# https://gitlab.com/cznic/file
%global goipath         modernc.org/file
%global forgeurl        https://gitlab.com/cznic/file
Version:                1.0.2
%global commit          23b75725dab417c351300644a3015a6f937b6b47
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Package file handles write-ahead logs and space management of os.File-like
entities.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Write-ahead logs and space management of os.File-like entities

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(modernc.org/internal/buffer)
BuildRequires:  golang(modernc.org/internal/file)
BuildRequires:  golang(modernc.org/mathutil)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 11:03:12 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- Update to 1.0.2
- Close: rhbz#1900289

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 16:11:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package
