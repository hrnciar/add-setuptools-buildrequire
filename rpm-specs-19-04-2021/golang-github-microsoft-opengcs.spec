# Generated by go2rpm
%bcond_without check

# https://github.com/Microsoft/opengcs
%global goipath         github.com/Microsoft/opengcs
Version:                0.3.9

%gometa

%global common_description %{expand:
Guest Compute Service for Linux Hyper-V Container.}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Guest Compute Service for Linux Hyper-V Container

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/containerd/containerd/sys)
BuildRequires:  golang(github.com/docker/docker/pkg/archive)
BuildRequires:  golang(github.com/docker/docker/pkg/symlink)
BuildRequires:  golang(github.com/linuxkit/virtsock/pkg/vsock)
BuildRequires:  golang(github.com/mattn/go-shellwords)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(github.com/vishvananda/netns)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|github.com/docker/containerd|github.com/containerd/containerd|" "{}" +;

%install
%gopkginstall

%if %{with check}
%check
# https://github.com/microsoft/opengcs/issues/309
%gocheck -d service/gcs/bridge -d service/gcs/core/gcs -d service/gcs/runtime/runc
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 18:42:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.9-1
- Initial package
