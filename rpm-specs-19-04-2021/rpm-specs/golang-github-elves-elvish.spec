# Generated by go2rpm 1
%bcond_without check

# https://github.com/elves/elvish
%global goipath         github.com/elves/elvish
Version:                0.15.0

%gometa

%global common_description %{expand:
Friendly Interactive Shell and Expressive Programming Language.}

%global golicenses      LICENSE
%global godocs          README.md CONTRIBUTING.md examples

Name:           %{goname}
Release:        1%{?dist}
Summary:        Friendly Interactive Shell and Expressive Programming Language

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/xiaq/persistent/hash)
BuildRequires:  golang(github.com/xiaq/persistent/hashmap)
BuildRequires:  golang(github.com/xiaq/persistent/vector)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/kr/pty)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# gopkginstall wants to install some examples to docs
# and seems to expect them at repo_root/examples
mv cmd/examples examples
# These actually aren't commands for end users; and
# confuse gopkginstall here.
rm -rf cmd

%build
%gobuild -o %{gobuilddir}/bin/elvish %{goipath}

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
%doc CONTRIBUTING.md website/README.md examples
%{_bindir}/*
%gopkgfiles

%changelog
* Sat Jan 30 12:04:00 EDT 2021 Jan Blackquill <uhhadd@gmail.com> - 0.15.0-1
- Initial package

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 19:37:01 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 16:11:15 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.0-1
- Update to 0.14.0

* Tue May 19 21:36:38 EDT 2020 Carson Black <uhhadd@gmail.com> - 0.13.1-1
- Initial package
