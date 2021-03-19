# Generated by go2rpm 1
%bcond_without check
# Avoid noarch package built differently on different architectures
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(golang.org/x/sys/cpu\\)$

# https://github.com/marten-seemann/chacha20
%global goipath         github.com/marten-seemann/chacha20
Version:                0.2.0

%gometa

%global godevelheader %{expand:
Requires:       golang(golang.org/x/sys/cpu)}

%global common_description %{expand:
Copy of ChaCha20.}

%global godocs          README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        ChaCha20 in Go

# https://github.com/marten-seemann/chacha20/issues/1
# BSD: main library
# OpenSSL: asm_ppc64le.s
License:        BSD and OpenSSL

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/cpu)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 23:47:47 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
