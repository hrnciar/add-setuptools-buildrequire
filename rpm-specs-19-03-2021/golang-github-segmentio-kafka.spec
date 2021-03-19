# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/segmentio/kafka-go
%global goipath         github.com/segmentio/kafka-go
Version:                0.4.8

%gometa

%global common_description %{expand:
Kafka-go provides both low and high level APIs for interacting with Kafka,
mirroring concepts and implementing interfaces of the Go standard library to
make it easy to use and integrate with existing software.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Kafka library in go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/klauspost/compress/zstd)
BuildRequires:  golang(github.com/pierrec/lz4)
BuildRequires:  golang(github.com/xdg/scram)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/eapache/go-xerial-snappy)
BuildRequires:  golang(golang.org/x/net/nettest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/mongodb/mongo-go-driver|go.mongodb.org/mongo-driver|' $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 12:44:54 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.8-1
- Update to 0.4.8
- Close: rhbz#1866990

* Sun Aug 02 17:14:57 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.7-1
- Update to 0.3.7

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 16:42:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Initial package