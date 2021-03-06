# Generated by go2rpm
%bcond_without check

# https://github.com/soheilhy/cmux
%global goipath         github.com/soheilhy/cmux
Version:                0.1.4

%gometa

%global common_description %{expand:
Cmux is a generic Go library to multiplex connections based on their payload.
Using cmux, you can serve gRPC, SSH, HTTPS, HTTP, Go RPC, and pretty much any
other protocol on the same TCP listener.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTORS README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Connection multiplexer for Go: serve different services on the same port

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/hpack)

%description
%{common_description}

%gopkg

%prep
%goprep
rm example_test.go

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 15:44:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.4-2
- Update to new macros

* Thu Mar 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.4-1
- First package for Fedora
