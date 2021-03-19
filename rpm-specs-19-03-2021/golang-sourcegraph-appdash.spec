# Generated by go2rpm
%bcond_without check

# https://github.com/sourcegraph/appdash
%global goipath         sourcegraph.com/sourcegraph/appdash
%global forgeurl        https://github.com/sourcegraph/appdash
%global commit          ebfcffb1b5c00031ce797183546746715a3cfe87

%gometa

%global common_description %{expand:
Appdash is an application tracing system for Go, based on Google's Dapper and
Twitter's Zipkin.

Appdash allows you to trace the end-to-end handling of requests and operations
in your application (for perf and debugging). It displays timings and
application-specific metadata for each step, and it displays a tree and timeline
for each request and its children.

To use appdash, you must instrument your application with calls to an appdash
recorder. You can record any type of event or operation. Recorders and schemas
for HTTP (client and server) and SQL are provided, and you can write your own.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md demo-annotations.md\\\
                        other-languages.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Application tracing system for Go, based on Google's Dapper

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/io)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/opentracing/basictracer-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/urfave/negroni)
BuildRequires:  golang(sourcegraph.com/sourcegraph/appdash-data)

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
# httptrace: needs network
%gocheck -d httptrace
%endif

%files
%license LICENSE
%doc examples CHANGELOG.md README.md demo-annotations.md other-languages.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 22:21:33 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20210113gitebfcffb
- Bump to commit ebfcffb1b5c00031ce797183546746715a3cfe87

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 01:18:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701gitd9ea5c5
- Initial package
