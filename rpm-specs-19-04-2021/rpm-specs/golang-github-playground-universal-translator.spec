# Generated by go2rpm 1
%bcond_without check

# https://github.com/go-playground/universal-translator
%global goipath         github.com/go-playground/universal-translator
Version:                0.17.0

%gometa

%global common_description %{expand:
i18n Translator for Go/Golang using CLDR data + pluralization
rules.}

%global golicenses      LICENSE
%global godocs          _examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        i18n Translator for Go/Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-playground/locales)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/go-playground/locales/en)
BuildRequires:  golang(github.com/go-playground/locales/en_CA)
BuildRequires:  golang(github.com/go-playground/locales/nl)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jul 26 18:57:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.0-1
- Initial package
