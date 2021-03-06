# Generated by go2rpm
%bcond_without check

# https://github.com/inconshreveable/go-vhost
%global goipath         github.com/inconshreveable/go-vhost
%global commit          06d84117953b22058c096b49a429ebd4f3d3d97b

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-inconshreveable-go-vhost-devel < 0-0.4
Obsoletes:      golang-github-inconshreveable-go-vhost-unit-test-devel < 0-0.4
}

%global common_description %{expand:
Go-vhost is a simple library that lets you implement virtual hosting
functionality for different protocols (HTTP and TLS so far). Go-vhost has a
high-level and a low-level interface. The high-level interface lets you wrap
existing net.Listeners with "muxer" objects. You can then Listen() on a muxer
for a particular virtual host name of interest which will return to you a
net.Listener for just connections with the virtual hostname of interest.

The lower-level Go-vhost interface are just functions which extract the
name/routing information for the given protocol and return an object
implementing net.Conn which works as if no bytes had been consumed.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        HTTP/TLS hostname multiplexing library for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/inconshreveable/go-vhost/pull/7
Patch0:         mux_test-missing-format-string.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.5.20160627git06d8411
- Add Obsoletes for old name

* Fri May 10 14:37:58 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0-0.4.20160627git06d8411
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20160627git06d8411
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160627git06d8411
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Jiri Kucera <jkucera@redhat.com> - 0-0.1.20160627git06d8411
- First package for Fedora
  resolves #1540726
  patch `mux_test-missing-format-string.patch` is needed to resolve https://github.com/inconshreveable/go-vhost/pull/7
