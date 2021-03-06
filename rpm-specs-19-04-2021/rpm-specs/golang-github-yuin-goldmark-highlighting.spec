# Generated by go2rpm 1
%bcond_without check

# https://github.com/yuin/goldmark-highlighting
%global goipath         github.com/yuin/goldmark-highlighting
%global commit          60d527fdb691b855b41a5b21ac612baca3a1dc1a

%gometa

%global common_description %{expand:
A Syntax highlighting extension for the goldmark markdown parser.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        A Syntax highlighting extension for the goldmark markdown parser

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/chroma)
BuildRequires:  golang(github.com/alecthomas/chroma/formatters/html)
BuildRequires:  golang(github.com/alecthomas/chroma/lexers)
BuildRequires:  golang(github.com/alecthomas/chroma/styles)
BuildRequires:  golang(github.com/yuin/goldmark)
BuildRequires:  golang(github.com/yuin/goldmark/ast)
BuildRequires:  golang(github.com/yuin/goldmark/parser)
BuildRequires:  golang(github.com/yuin/goldmark/renderer)
BuildRequires:  golang(github.com/yuin/goldmark/renderer/html)
BuildRequires:  golang(github.com/yuin/goldmark/text)
BuildRequires:  golang(github.com/yuin/goldmark/util)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 18:44:50 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20210113git60d527f
- Bump to commit 60d527fdb691b855b41a5b21ac612baca3a1dc1a

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 04:12:16 EST 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20200218gitd1af22c
- Initial package
