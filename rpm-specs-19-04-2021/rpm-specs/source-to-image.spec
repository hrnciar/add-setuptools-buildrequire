# github.com/containers/image/v5 is not yet packaged
%global with_devel 0
%global with_bundled 1

%global goipath github.com/openshift/source-to-image
Version:        1.3.1

%gometa

%global common_description %{expand:
Source-to-Image (S2I) is a toolkit and workflow for building reproducible 
container images from source code. S2I produces ready-to-run images by 
injecting source code into a container image and letting the container prepare 
that source code for execution. By creating self-assembling builder images, 
you can version and control your build environments exactly like you use 
container images to version your runtime environments.}

%global golicenses LICENSE

Name:           source-to-image
Release:        1%{?dist}
Summary:        A tool for building artifacts from source and injecting into docker images
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

# for github.com/containers/storage, a dependency of github.com/containers/image/v5
%if 0%{?fedora}
BuildRequires:  btrfs-progs-devel
%endif
BuildRequires:  device-mapper-devel
%if ! 0%{?with_bundled}
#BuildRequires:  golang(github.com/containers/image/v5/transports/alltransports)
#BuildRequires:  golang(github.com/containers/image/v5/types)
BuildRequires:  golang(github.com/docker/distribution/reference)
BuildRequires:  golang(github.com/docker/docker/api/types)
BuildRequires:  golang(github.com/docker/docker/api/types/container)
BuildRequires:  golang(github.com/docker/docker/api/types/network)
BuildRequires:  golang(github.com/docker/docker/api/types/strslice)
BuildRequires:  golang(github.com/docker/docker/cli/config)
BuildRequires:  golang(github.com/docker/docker/client)
BuildRequires:  golang(github.com/docker/docker/pkg/jsonmessage)
BuildRequires:  golang(github.com/docker/docker/pkg/stdcopy)
BuildRequires:  golang(github.com/docker/go-connections/tlsconfig)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/parser)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(k8s.io/klog/v2)
%endif
# for tests
BuildRequires:  git-core
%if ! 0%{?with_devel}
Obsoletes: %{name}-devel < %{version}-%{release}
Obsoletes: %{name}-unit-test < %{version}-%{release}
%endif

Recommends:    docker
Requires:      git
Requires:      tar

Provides:      s2i = %{version}-%{release}

%description
%{common_description}

%if 0%{?with_devel}
%godevelpkg

Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-unit-test = %{version}-%{release}
Obsoletes: %{name}-devel < %{version}-%{release}
Obsoletes: %{name}-unit-test < %{version}-%{release}
%endif

%prep
%if 0%{?with_bundled}
%goprep -k
%else
%goprep
%endif

%build
%if 0%{?rhel}
export BUILDTAGS="$BUILDTAGS exclude_graphdriver_btrfs "
%endif
export LDFLAGS="$LDFLAGS -X %{goipath}/pkg/version.versionFromGit=v%{version} "
%gobuild -o %{gobuilddir}/bin/s2i %{goipath}/cmd/s2i

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 %{gobuilddir}/bin/s2i %{buildroot}%{_bindir}

%if 0%{?with_devel}
%godevelinstall
%endif

%check
export LDFLAGS="$LDFLAGS -X %{goipath}/pkg/version.versionFromGit=v%{version} "
%gocheck -d pkg/docker

%files
%license LICENSE
%doc README.md CONTRIBUTING.md AUTHORS
%{_bindir}/s2i

%if 0%{?with_devel}
%gopkgfiles
%endif

%changelog
* Mon Feb 22 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 1.3.1-1
- Update to v1.3.1
- Overhaul to conform to Go packaging guidelines

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Jan Chaloupka <jchaloup@redhat.com> - 1.1.7-5
- Remove unneeded dependency on github.com/fsouza/go-dockerclient
  resolves: #1676016

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1.7-1
- Update to v1.1.7
  resolves: #1510476

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Till Maas <opensource@till.name> - 1.0.9-5
- Do not build on ppc64 (does not contain docker)

* Mon May 15 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.9-4
- Fix go-1.8 -X importpath/name=value syntax

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sat May 21 2016 jchaloup <jchaloup@redhat.com> - 1.0.9-1
- Update to v1.0.9
  resolves: #1273677

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- New upstream release
- https://github.com/openshift/source-to-image/releases/tag/v1.0.4

* Thu Oct 22 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-2
- Rebase to new upstream version
- Package now provides s2i
- Disable tests removed by upstream

* Thu Sep 17 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-4
- Fix dependencies
- Remove -devel sub package

* Tue Sep 15 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-2
- Build the right directory

* Mon Sep 14 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git00d1cb3
- First package for Fedora


