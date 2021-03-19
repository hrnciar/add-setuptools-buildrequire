# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/marten-seemann/qtls-go1-16
%global goipath         github.com/marten-seemann/qtls-go1-16
Version:                0.1.0~beta.1.1

%gometa

%global extractdir      %(echo %{extractdir} | sed -e 's/~/-/g')
%global gosource        %(echo %{gosource} | sed -e 's/~/-/g')

%global common_description %{expand:
Go standard library TLS 1.3 implementation, modified for QUIC. For Go 1.16.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go standard library TLS 1.3 implementation, modified for QUIC. For Go 1.16

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/chacha20poly1305)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte)
BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/crypto/hkdf)
BuildRequires:  golang(golang.org/x/sys/cpu)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/golang/mock/gomock)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~beta.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 15:54:22 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-beta.1.1-1
- Initial package
