# Generated by go2rpm
# Needs special permissions
%bcond_with check

# https://github.com/containerd/cgroups
%global goipath         github.com/containerd/cgroups
%global commit          4cbc285b33272039927a0b066d3412799db8de14

%gometa

%global common_description %{expand:
Go package for creating, managing, inspecting, and destroying cgroups.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Cgroups package for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cilium/ebpf)
BuildRequires:  golang(github.com/cilium/ebpf/asm)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/dbus)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/godbus/dbus/v5)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 14:07:41 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20210109git4cbc285
- Bump to commit 4cbc285b33272039927a0b066d3412799db8de14

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 14:24:41 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200725git318312a
- Bump to commit 318312a373405e5e91134d8063d04d59768a1bff

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 15:42:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git4994991
- Initial package
