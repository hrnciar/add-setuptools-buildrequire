# Generated by go2rpm
%bcond_without check
# Avoid noarch package built differently on different architectures
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(golang.org/x/sys/cpu\\)$

# https://github.com/aead/chacha20
%global goipath         github.com/aead/chacha20
%global commit          8b13a72661dae6e9e5dea04f344f0dc95ea29547

%gometa

%global godevelheader %{expand:
Requires:       golang(golang.org/x/sys/cpu)}

%global common_description %{expand:
ChaCha is a stream cipher family created by Daniel J. Bernstein. The most common
ChaCha variant is ChaCha20 (20 rounds). ChaCha20 is standardized in RFC 7539.

This package provides implementations of three ChaCha versions:

 - ChaCha20 with a 64 bit nonce (can en/decrypt up to 2^64 * 64 bytes for one
   key-nonce combination)
 - ChaCha20 with a 96 bit nonce (can en/decrypt up to 2^32 * 64 bytes ~ 256 GB
   for one key-nonce combination)
 - XChaCha20 with a 192 bit nonce (can en/decrypt up to 2^64 * 64 bytes for one
   key-nonce combination)

Furthermore the chacha sub package implements ChaCha20/12 and ChaCha20/8. These
versions use 12 or 8 rounds inste -d of 20. But it's recommended to use ChaCha20
(with 20 rounds) - it will be fast enough for almost all purposes.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        ChaCha20 and XChaCha20 stream ciphers

License:        MIT
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 18:00:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190523git8b13a72
- Bump to commit 8b13a72661dae6e9e5dea04f344f0dc95ea29547

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gite253874
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gite253874
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180517gite253874
- First package for Fedora