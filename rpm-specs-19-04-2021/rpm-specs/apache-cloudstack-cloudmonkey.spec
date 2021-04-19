# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/apache/cloudstack-cloudmonkey
%global goipath         github.com/apache/cloudstack-cloudmonkey
Version:                6.1.0
%global tag             6.1.0

%gometa

%global common_description %{expand:
Apache Cloudstack Cloudmonkey is a command line interface (CLI) for Apache
CloudStack.

CloudMonkey can be use both as an interactive shell and as a command line tool
which simplifies Apache CloudStack configuration and management.}

%global golicenses      LICENSE
%global godocs          README.md CHANGES.md

Name:           apache-cloudstack-cloudmonkey
Release:        2%{?dist}
Summary:        Apache Cloudstack Cloudmonkey

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/briandowns/spinner)
BuildRequires:  golang(github.com/chzyer/readline)
BuildRequires:  golang(github.com/gofrs/flock)
BuildRequires:  golang(github.com/google/shlex)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/olekukonko/tablewriter)
BuildRequires:  golang(gopkg.in/ini.v1)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/cmk %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md CHANGES.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Olivier Lemasle <o.lemasle@gmail.com> - 6.1.0-1
- Initial package

