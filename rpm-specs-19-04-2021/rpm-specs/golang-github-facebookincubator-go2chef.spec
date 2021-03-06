# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/facebookincubator/go2chef
%global goipath         github.com/facebookincubator/go2chef
%global commit          576f5d4383ec70082c150ac8eb4cd97b904951fc

%gometa

%global common_description %{expand:
go2chef is a Go tool for bootstrapping Chef installations in a flexible and
self-contained way. With go2chef, our goal is to make bootstrapping any node
in a Chef deployment as simple as "get go2chef onto a machine and run it".}

%global golicenses      LICENSE
%global godocs          examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Tool to bootstrap a system from zero so that it's able to run Chef

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/secretsmanager)
BuildRequires:  golang(github.com/mholt/archiver)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/otiai10/copy)
BuildRequires:  golang(github.com/pkg/sftp)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(golang.org/x/crypto/ssh)

%description
%{common_description}

%package -n go2chef
Summary:        Tool to bootstrap a system from zero so that it's able to run Chef
%description -n go2chef
%{common_description}

%gopkg

%prep
%goprep
# these examples aren't useful without the repository itself
rm -rf examples/{custom_binary,plugins}
# fix permissions
chmod -x examples/bundles/{chefctl,chefrepo}/bundle.ps1

%build
%gobuild -o %{gobuilddir}/bin/go2chef %{goipath}/bin
%gobuild -o %{gobuilddir}/bin/go2chef-remote %{goipath}/scripts

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files -n go2chef
%license LICENSE
%doc examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0-0.1.20210105git576f5d4
- Update commit to pick up a fix for #1912666

* Mon Jan  4 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0-0.1.20210104git4dae637
- Initial package

