# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/insomniacslk/termhook
%global goipath         github.com/insomniacslk/termhook
%global commit          a267c978e590d0e84c40b76dbf79393eabed254a

%gometa

%global common_description %{expand:
termhook is a small library that attaches to a terminal, serial console or
other similar device, and lets you attach your own hook on terminal output.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Simple terminal that allows attaching hooks

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/term)
BuildRequires:  golang(github.com/pkg/term/termios)
BuildRequires:  golang(golang.org/x/sys/unix)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmds/termhook; do
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
%license COPYING
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Apr 06 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0-0.1.20210406gita267c97
- Initial package
