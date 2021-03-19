# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/nanomsg/mangos
%global goipath         go.nanomsg.org/mangos/v3
%global forgeurl        https://github.com/nanomsg/mangos
Version:                3.1.3

%gometa

%global common_description %{expand:
Mangos is a pure Golang implementation of nanomsg's "Scalablilty Protocols".}

%global golicenses      LICENSE
%global godocs          examples AUTHORS CODE_OF_CONDUCT.md README.adoc\\\
                        macat/README.md macat/macat.txt

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang implementation of nanomsg's "Scalablilty Protocols"

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gdamore/optopia)
BuildRequires:  golang(github.com/gorilla/websocket)

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf examples/websocket/.gitignore

%build
for cmd in macat/macat perf; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%ifnarch aarch64
%if %{with check}
%check
%gocheck
%endif
%endif

%files
%license LICENSE
%doc examples AUTHORS CODE_OF_CONDUCT.md README.adoc macat/README.md
%doc macat/macat.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.3-1
- Initial package for Fedora