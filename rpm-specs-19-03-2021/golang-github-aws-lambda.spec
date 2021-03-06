# Generated by go2rpm 1
%bcond_without check

# https://github.com/aws/aws-lambda-go
%global goipath         github.com/aws/aws-lambda-go
Version:                1.22.0

%gometa

%global common_description %{expand:
Libraries, samples and tools to help Go developers develop AWS Lambda
functions.}

%global golicenses      LICENSE LICENSE-LAMBDACODE LICENSE-SUMMARY
%global godocs          README.md events/*.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Libraries, samples and tools to help Go developers develop AWS Lambda functions

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/urfave/cli/v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE LICENSE-LAMBDACODE LICENSE-SUMMARY
%doc README.md events/*.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 14:30:30 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.22.0-1
- Update to 1.22.0

* Thu Sep 03 23:50:05 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.19.1-1
- Initial package
