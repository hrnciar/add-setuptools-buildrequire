# Generated by go2rpm
%bcond_without check

# https://github.com/pact-foundation/pact-go
%global goipath         github.com/pact-foundation/pact-go
Version:                1.5.1

%gometa

%global common_description %{expand:
Pact Go enables consumer driven contract testing, providing a mock service and
DSL for the consumer project, and interaction playback and verification for the
service provider project.}

%global golicenses      LICENSE
%global godocs          examples RELEASING.md CHANGELOG.md CONTRIBUTING.md\\\
                        README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Contract testing framework for HTTP APIs and non-HTTP messaging systems for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gin-gonic/gin)
BuildRequires:  golang(github.com/hashicorp/go-version)
BuildRequires:  golang(github.com/hashicorp/logutils)
BuildRequires:  golang(github.com/spf13/cobra)

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
%gobuild -o %{gobuilddir}/bin/pact %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# dsl: needs network
%gocheck -d dsl -d command
%endif

%files
%license LICENSE
%doc examples RELEASING.md CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 10:26:56 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.1-1
- Update to 1.5.1
- Close: rhbz#1868942

* Thu Jul 30 20:24:22 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.3-1
- Update to 1.4.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 02:34:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1.beta.3
- Initial package