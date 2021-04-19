# Generated by go2rpm 1
%bcond_without check

# https://github.com/youmark/pkcs8
%global goipath         github.com/youmark/pkcs8
Version:                1.1

%gometa

%global common_description %{expand:
Go package implementing functions to parse and convert private keys in PKCS#8
format, as defined in RFC5208 and RFC5958.}

%global golicenses      LICENSE
%global godocs          README README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Parse and convert private keys in PKCS#8 format

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/pbkdf2)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 22:27:19 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-1
- Initial package
