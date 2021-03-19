# Generated by go2rpm
# use of internal package not allowed because not common root
%bcond_with check

# https://gitlab.com/cznic/lldb
%global goipath         modernc.org/lldb
%global forgeurl        https://gitlab.com/cznic/lldb
Version:                1.0.1
%global commit          2a98fa2aab9a3fca9ebc4be463a587de4a474c5f
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Package Lldb implements a low level database engine.}

%global golicenses      LICENSE LICENSE-testdata
%global godocs          AUTHORS CONTRIBUTORS README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Low level database engine

# Upstream license specification: LPL-1.02 and BSD-3-Clause
# main library: BSD
# testdata: LPL
License:        LPL and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(modernc.org/fileutil)
BuildRequires:  golang(modernc.org/internal/buffer)
BuildRequires:  golang(modernc.org/internal/file)
BuildRequires:  golang(modernc.org/mathutil)
BuildRequires:  golang(modernc.org/sortutil)
BuildRequires:  golang(modernc.org/zappy)

%description
%{common_description}

%gopkg

%prep
%goprep
mv testdata/LICENSE LICENSE-testdata

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 12:44:07 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Close: rhbz#1900288

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 17:32:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package
