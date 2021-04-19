# Generated by go2rpm 1
%bcond_without check

# https://github.com/andybalholm/brotli
%global goipath         github.com/andybalholm/brotli
Version:                1.0.1

%gometa

%global common_description %{expand:
This package is a brotli compressor and decompressor implemented in Go. It was
translated from the reference implementation (https://github.com/google/brotli)
with the c2go tool at https://github.com/andybalholm/c2go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Pure Go Brotli encoder and decoder

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 02 20:55:48 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Fix CVE-2020-8927 (#1879225, #1879228)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 00:58:04 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat Aug 03 23:05:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190803gited0fd64
- Initial package
