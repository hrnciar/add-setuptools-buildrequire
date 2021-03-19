# Generated by go2rpm
%bcond_without check

# https://github.com/containerd/continuity
%global goipath         github.com/containerd/continuity
%global commit          180525291bb77dea7062ac4281fcd38e2a3d76c5

%gometa

%global common_description %{expand:
A transport-agnostic, filesystem metadata manifest system.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md sysx/README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Transport-agnostic, filesystem metadata manifest system

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(bazil.org/fuse)
BuildRequires:  golang(bazil.org/fuse/fs)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)

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
# TestCopyWithLargeFile: no space left on device
%gocheck -d fs
%endif

%files
%license LICENSE
%doc AUTHORS README.md sysx/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 14:52:45 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20210109git1805252
- Bump to commit 180525291bb77dea7062ac4281fcd38e2a3d76c5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 16:29:57 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200725gitefbc448
- Bump to commit efbc4488d8fe1bdc16bde3b2d2990d9b3a899165

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 16:31:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626gitaaeac12
- Initial package