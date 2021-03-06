# Generated by go2rpm
%bcond_without check

# Depends on github.com/vmware/vmw-guestinfo/bdoor only available for i686 and x86_64
%ifarch %{ix86} x86_64
%bcond_without binary
%endif

# https://github.com/vmware/govmomi
%global goipath         github.com/vmware/govmomi
Version:                0.24.0

%gometa

%global common_description %{expand:
A Go library for interacting with VMware vSphere APIs (ESXi and/or vCenter).}

%global golicenses      LICENSE.txt
%global godocs          examples CONTRIBUTING.md CONTRIBUTORS README.md\\\
                        CHANGELOG.md examples README-govc.md\\\
                        CHANGELOG-govc.md USAGE-govc.md README-toolbox.md\\\
                        README-vcsim.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go library for the VMware vSphere API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/davecgh/go-xdr/xdr2)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/vmware/vmw-guestinfo/message)
BuildRequires:  golang(github.com/vmware/vmw-guestinfo/vmcheck)

%description
%{common_description}

%gopkg

%prep
%goprep
mv govc/README.md README-govc.md
mv govc/CHANGELOG.md CHANGELOG-govc.md
mv govc/USAGE.md USAGE-govc.md
mv toolbox/README.md README-toolbox.md
mv vcsim/README.md README-vcsim.md

%if %{with binary}
%build
for cmd in govc toolbox/toolbox vcsim; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mv %{gobuilddir}/bin/toolbox %{gobuilddir}/bin/govmomi-toolbox
%endif

%install
%gopkginstall
%if %{with binary}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{with check}
%check
# toolbox: needs network
%gocheck -t toolbox -d simulator
%endif

%if %{with binary}
%files
%license LICENSE.txt
%doc examples CONTRIBUTING.md CONTRIBUTORS README.md CHANGELOG.md examples
%doc README-govc.md CHANGELOG-govc.md USAGE-govc.md README-toolbox.md
%doc README-vcsim.md
%{_bindir}/*
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 06:00:28 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.24.0-1
- Update to 0.24.0
- Close: rhbz#1909913

* Tue Aug 04 17:25:08 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.23.1-1
- Update to 0.23.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 12:48:56 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.21.0-1
- Release 0.21.0 (#1742303)
- Rename toolbox to govmomi-toolbox (#1755694)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 17:00:57 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.20.0-1
- Initial package
