# Generated by go2rpm 1
%bcond_without check

# https://github.com/google/go-dap
%global goipath         github.com/google/go-dap
Version:                0.4.0

%gometa

%global common_description %{expand:
Go implementation of the Debug Adapter Protocol.}

%global golicenses      LICENSE
%global godocs          docs README.md cmd/gentypes/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of the Debug Adapter Protocol

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

# Fix an overflows 32bit int
# https://github.com/google/go-dap/pull/52
Patch0: fix-overflow-32bit.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

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
%gocheck
%endif

%files
%license LICENSE
%doc docs README.md cmd/gentypes/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Feb 11 2021 Alejandro Sáez <asm@redhat.com> - 0.4.0-1
- Bump up to version 0.4.0
- Add Patch0

* Thu Sep 03 12:10:56 CEST 2020 Alejandro Sáez <asm@redhat.com> - 0.2.0-1
- Initial package
