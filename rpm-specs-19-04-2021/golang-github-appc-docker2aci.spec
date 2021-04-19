# Generated by go2rpm
%bcond_without check

# https://github.com/appc/docker2aci
%global goipath         github.com/appc/docker2aci
Version:                0.17.2

%gometa

%global common_description %{expand:
Docker2aci is a small library and CLI binary that converts Docker images to ACI.
It takes as input either a file generated by "docker save" or a Docker registry
URL. It gets all the layers of a Docker image and squashes them into an ACI
image. Optionally, it can generate one ACI for each layer, setting the correct
dependencies.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md Documentation

Name:           %{goname}
Release:        5%{?dist}
Summary:        Library and CLI tool to convert Docker images to ACIs

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Update to opencontainers/image-spec v1.0.1
# https://github.com/woofwoofinc/docker2aci/commit/d4e8e83bfaff27a65d6f7ff4657bcc66a21d0e0f
# https://github.com/appc/docker2aci/issues/257#issuecomment-363477582
Patch0:         0001-Update-to-opencontainers-image-spec-v1.0.1.patch

BuildRequires:  golang(github.com/appc/spec/aci)
BuildRequires:  golang(github.com/appc/spec/pkg/acirenderer)
BuildRequires:  golang(github.com/appc/spec/schema)
BuildRequires:  golang(github.com/appc/spec/schema/types)
BuildRequires:  golang(github.com/coreos/ioprogress)
BuildRequires:  golang(github.com/coreos/pkg/progressutil)
BuildRequires:  golang(github.com/docker/distribution/reference)
BuildRequires:  golang(github.com/klauspost/pgzip)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%build
%gobuild -o %{gobuilddir}/bin/docker2aci %{goipath}

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
%doc CHANGELOG.md README.md Documentation
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 14:07:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.2-1
- Initial package