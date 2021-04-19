# Generated by go2rpm
%bcond_without check

# https://gitlab.com/cznic/lexer
%global goipath         modernc.org/lexer
%global forgeurl        https://gitlab.com/cznic/lexer
Version:                1.0.2
%global tag             v1.0.2

%gometa

%global common_description %{expand:
Run time generator of action less scanners (lexeme recognizers).}

%global golicenses      LICENSE LICENSE-GO
%global godocs          AUTHORS CONTRIBUTORS README

Name:           %{goname}
Release:        2%{?dist}
Summary:        Run time generator of action less scanners

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/exp/ebnf)
BuildRequires:  golang(modernc.org/fileutil)

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

* Fri Jan  8 13:14:14 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- Update to 1.0.2
- Close: rhbz#1867045

* Thu Aug 06 15:56:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Updat to 1.0.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 19:13:51 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-4
- Add workaround for calling flag.Parse() in init

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 17:10:53 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package
