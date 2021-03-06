# golang-github-cli-shurcool-graphql.spec
# Generated by go2rpm 2
%bcond_without check

# https://github.com/cli/shurcooL-graphql
%global goipath         github.com/cli/shurcooL-graphql
%global commit          0f7232a2bf7e6d8f393025a8f5cafbd219a7ebeb

%gometa

%global common_description %{expand:
Package graphql provides a GraphQL client implementation.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        GraphQL client implementation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/graph-gophers/graphql-go)
BuildRequires:  golang(github.com/graph-gophers/graphql-go/relay)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/shurcooL/graphql|github.com/cli/shurcooL-graphql|' $(find . -name "*.go" -type f)
%install
%gopkginstall


%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 23:14:00 CEST 2020 Joe Doss <joe@solidadmin.com> - 0-0.1.20200930gitd48a9a7
- Initial package
