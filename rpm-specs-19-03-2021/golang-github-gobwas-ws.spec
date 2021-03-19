# Generated by go2rpm 1
%bcond_without check

# https://github.com/gobwas/ws
%global goipath         github.com/gobwas/ws
Version:                1.0.4

%gometa

%global common_description %{expand:
Tiny WebSocket library for Go.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Tiny WebSocket library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gobwas/httphead)
BuildRequires:  golang(github.com/gobwas/pool)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in autobahn; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
rm -rf %{gobuilddir}/usr/share/gocode/src/github.com/gobwas/ws/server_test.s

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
%doc example README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.4-1
- Update to latest version

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.3-1
- Initial package
