# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/facebookincubator/ntp
%global goipath         github.com/facebookincubator/ntp
%global commit          81cb02c05f82f8c9cdf32e16f4ee02a3b05bfaf1

%gometa

%global common_description %{expand:
This package is a collection Facebook's NTP libraries and utilities. It
includes a protocol implementations for NTP, Chrony and ntpd.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Facebook's NTP libraries

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/jsimonetti/rtnetlink/rtnl)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%package -n ntpcheck
Summary:        CLI to perform various NTP-related tasks
%description -n ntpcheck
ntpcheck is a CLI to perform various NTP-related tasks:
- replacement for ntptime and ntpdate commands
- human-readable diagnostics for typical problems with NTP based on data
  from chrony/ntpd
- server stats and peer stats taken from chrony/ntpd with output in JSON

%package -n leaphash
Summary:        Utility for computing the leap second hash value
%description -n leaphash
leaphash is a utility for computing the hash value of the official
leap-second.list document

%package -n responder
Summary: Simple NTP server implementation with kernel timestamps support
%description -n responder
responder is a simple NTP server implementation with kernel timestamps
support, designed for scale and security.

%gopkg

%prep
%goprep

%build
for cmd in leaphash ntpcheck responder; do
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

%files -n ntpcheck
%license LICENSE
%doc README.md
%{_bindir}/ntpcheck

%files -n leaphash
%license LICENSE
%doc README.md
%{_bindir}/leaphash

%files -n responder
%license LICENSE
%doc README.md
%{_bindir}/responder

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 17:59:15 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20210109git81cb02c
- Bump to commit 81cb02c05f82f8c9cdf32e16f4ee02a3b05bfaf1

* Wed Nov 04 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 0-0.1.20201104git143e098
- Initial package
