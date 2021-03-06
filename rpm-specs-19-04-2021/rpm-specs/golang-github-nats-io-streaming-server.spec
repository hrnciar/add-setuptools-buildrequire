# Generated by go2rpm
%bcond_without check

# https://github.com/nats-io/nats-streaming-server
%global goipath         github.com/nats-io/nats-streaming-server
Version:                0.20.0

%gometa

%global common_description %{expand:
NATS Streaming is an extremely performant, lightweight reliable streaming
platform built on NATS.}

%global golicenses      LICENSE
%global godocs          CODE-OF-CONDUCT.md GOVERNANCE.md MAINTAINERS.md\\\
                        TODO.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        NATS Streaming System Server

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/hashicorp/go-hclog)
BuildRequires:  golang(github.com/hashicorp/go-msgpack/codec)
BuildRequires:  golang(github.com/hashicorp/raft)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/nats-io/nats-server/v2/conf)
BuildRequires:  golang(github.com/nats-io/nats-server/v2/logger)
BuildRequires:  golang(github.com/nats-io/nats-server/v2/server)
BuildRequires:  golang(github.com/nats-io/nats.go)
BuildRequires:  golang(github.com/nats-io/nuid)
BuildRequires:  golang(github.com/nats-io/stan.go/pb)
BuildRequires:  golang(github.com/prometheus/procfs)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(golang.org/x/crypto/chacha20poly1305)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/nats-io/nats-server/v2/test)
BuildRequires:  golang(github.com/nats-io/stan.go)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/nats-streaming-server %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# logger, stores: need network
%gocheck -d server -d logger -d stores
%endif

%files
%license LICENSE
%doc CODE-OF-CONDUCT.md GOVERNANCE.md MAINTAINERS.md TODO.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 18:38:13 CET 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.20.0-1
- Update to 0.20.0
- Close: rhbz#1914489

* Mon Dec 21 08:04:48 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.19.0-1
- Update to 0.19.0
- Close: rhbz#1893912

* Thu Jul 30 07:18:45 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 22:00:36 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 01:34:47 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.14.1-1
- Initial package
