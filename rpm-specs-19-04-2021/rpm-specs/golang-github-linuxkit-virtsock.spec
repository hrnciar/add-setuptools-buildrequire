# Generated by go2rpm
%bcond_without check

# https://github.com/linuxkit/virtsock
%global goipath         github.com/linuxkit/virtsock
%global commit          f8cee7dfc7a3a337738ff3c1852fafe193a4f5d3

%gometa

%global common_description %{expand:
This package contains Go bindings and sample code for Hyper-V sockets and virtio
sockets(VSOCK).}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Go bindings for virtio and Hyper-V sockets

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(golang.org/x/sys/unix)

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

* Sun Jan 10 11:56:22 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20210110gitf8cee7d
- Bump to commit f8cee7dfc7a3a337738ff3c1852fafe193a4f5d3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 18:00:48 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627git8e79449
- Initial package
