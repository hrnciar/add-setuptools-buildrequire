# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/cri-api
%global goipath         k8s.io/cri-api
%global forgeurl        https://github.com/kubernetes/cri-api
Version:                1.20.1
%global tag             kubernetes-1.20.1
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Container Runtime Interface (CRI) – a plugin interface which enables kubelet to
use a wide variety of container runtimes.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md code-of-conduct.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Plugin interface which enables kubelet to use container runtimes

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)

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
* Thu Jan 28 2021 Olivier Lemasle <o.lemasle@gmail.com> - 1.20.1.1
- Update to 1.20.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 15:56:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.9-1
- Update to 1.18.9

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 17:59:24 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Wed Apr 01 2020 Olivier Lemasle <o.lemasle@gmail.com> - 1.17.2-1
- Update to 1.17.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 15:12:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Initial package