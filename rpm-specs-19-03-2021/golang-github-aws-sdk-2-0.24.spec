# Generated by go2rpm
%bcond_without check

# https://github.com/aws/aws-sdk-go-v2
%global goipath         github.com/aws/aws-sdk-go-v2-0.24
%global forgeurl        https://github.com/aws/aws-sdk-go-v2
Version:                0.24.0

%gometa

%global goname golang-github-aws-sdk-2-0.24
%global godevelname golang-github-aws-sdk-2-devel-0.24

%global common_description %{expand:
aws-sdk-go-v2 is the Developer Preview for the v2 of the AWS SDK for the Go
programming language.}

%global golicenses      LICENSE.txt NOTICE.txt
%global godocs          example CHANGELOG.md CHANGELOG_PENDING.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        AWS SDK for the Go programming language

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: https://github.com/aws/aws-sdk-go-v2/issues/655
Patch0:         0001-Convert-id-to-string-using-strconv.Itoa.patch

BuildRequires:  golang(github.com/jmespath/go-jmespath)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
sed -i 's|github.com/aws/aws-sdk-go-v2|github.com/aws/aws-sdk-go-v2-0.24|' $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
# aws/external: needs network
%gocheck -t aws/external -d aws/retry -t internal/repotools/changes -d service/internal/benchmark/dynamodb
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 22:29:16 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.24.0-1
- Initial package
