# Generated by go2rpm 1
%bcond_without check

# https://github.com/evanw/esbuild
%global goipath         github.com/evanw/esbuild-0.8.20
%global forgeurl        https://github.com/evanw/esbuild
Version:                0.8.20

%gometa

%global common_description %{expand:
This is a JavaScript bundler and minifier. It packages up JavaScript and
TypeScript code for distribution on the web.}

%global golicenses      LICENSE.md
%global godocs          docs CHANGELOG.md README.md version.txt

Name:           %{goname}
Release:        2%{?dist}
Summary:        Fast JavaScript bundler and minifier

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/unix)

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i \
    -e 's|"github.com/evanw/esbuild|"github.com/evanw/esbuild-0.8.20|' \
    $(find . -name '*.go')

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 15:12:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.20-1
- Initial package