# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/utils
%global goipath         k8s.io/utils
%global forgeurl        https://github.com/kubernetes/utils
%global commit          fddb29f9d0095a7a37582a1d86732ae83620f2e8

%gometa

%global common_description %{expand:
A set of Go libraries that provide low-level, kubernetes-independent packages
supplementing the Go standard libs.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md HOWTOMOVE.md README.md code-of-\\\
                        conduct.md

Name:           %{goname}
Version:        0
Release:        0.9%{?dist}
Summary:        Non-Kubernetes-specific utility libraries consumed by multiple projects

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(k8s.io/klog/v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/spf13/afero)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 21:59:33 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20210113gitfddb29f
- Bump to commit fddb29f9d0095a7a37582a1d86732ae83620f2e8

* Wed Sep 30 01:05:19 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7.20200930git4140de9
- Bump to commit 4140de9c8800f5b18f8fc59798e11862f2bb00cb

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 15:12:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200615gitc1c6865
- Bump to commit c1c6865ac45113491fd8207923d28d4bcff03a88

* Wed Feb 05 22:50:43 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200205git8619460
- Bump to commit 861946025e3491219eaccb1bf693e23df70c2fa8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 01:32:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190629git8fab8cb
- Initial package