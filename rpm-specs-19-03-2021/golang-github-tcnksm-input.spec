# Generated by go2rpm
%bcond_without check

# https://github.com/tcnksm/go-input
%global goipath         github.com/tcnksm/go-input
%global commit          548a7d7a8ee8fcb3d013fae6acf857da56165975

%gometa

%global common_description %{expand:
Go-input is a Go package for reading user input in console.}

%global golicenses      LICENSE
%global godocs          _example README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Go package for ideal TTY prompt

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 13:54:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190630git548a7d7
- Initial package