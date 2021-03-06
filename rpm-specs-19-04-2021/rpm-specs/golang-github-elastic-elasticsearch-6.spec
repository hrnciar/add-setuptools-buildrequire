# Generated by go2rpm 1
%bcond_without check

# https://github.com/elastic/go-elasticsearch/v6
%global goipath         github.com/elastic/go-elasticsearch/v6
Version:                6.8.10

%gometa

%global common_description %{expand:
The official Go client for Elasticsearch.}

%global golicenses      LICENSE
%global godocs          _examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        The official Go client for Elasticsearch

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/chroma/formatters)
BuildRequires:  golang(github.com/alecthomas/chroma/lexers)
BuildRequires:  golang(github.com/alecthomas/chroma/styles)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/tools/imports)
BuildRequires:  golang(gopkg.in/yaml.v2)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 23:54:11 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 6.8.10-1
- Initial package
