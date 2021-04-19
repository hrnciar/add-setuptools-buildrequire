# Generated by go2rpm 1
# Needs network access
%bcond_with check

# https://github.com/instrumenta/kubeval
%global goipath         github.com/instrumenta/kubeval
Version:                0.15.0
%global tag             0.15.0

%gometa

%global common_description %{expand:
Validate your Kubernetes configuration files, supports multiple Kubernetes
versions.}

%global golicenses      LICENSE
%global godocs          docs BUILDING.md CONDUCT.md README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Validate your Kubernetes configuration files

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(github.com/xeipuuv/gojsonschema)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/kubeval %{goipath}

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
%doc docs BUILDING.md CONDUCT.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 19:54:05 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.15.0-1
- Initial package
