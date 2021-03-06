# Generated by go2rpm 1
%bcond_without check

# https://github.com/Azure/azure-amqp-common-go
%global goipath         github.com/Azure/azure-amqp-common-go
Version:                3.1.0

%gometa

%global goaltipaths     github.com/Azure/azure-amqp-common-go/v3

%global common_description %{expand:
Azure AMQP abstractions for Golang contains common types and interfaces for use
in Service Bus and Event Hubs.

This project contains reusable components for AMQP based services like Event Hub
and Service Bus. You will find abstractions over authentication, claims-based
security, connection string parsing and RPC for AMQP.}

%global golicenses      LICENSE
%global godocs          README.md changelog.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Common types and interfaces for Service Bus and Event Hubs

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Azure/go-amqp)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/devigned/tab)
BuildRequires:  golang(golang.org/x/crypto/pkcs12)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 07:27:34 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.0-1
- Update to 3.1.0
- Close: rhbz#1867014

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 21:59:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-3
- Add alternative import path

* Tue Jan 28 22:29:17 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 19:53:56 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- Initial package
