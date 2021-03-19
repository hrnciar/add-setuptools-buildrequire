# Generated by go2rpm 1
%bcond_without check

# Avoid noarch package built differently on different architectures
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/klauspost/cpuid\\)$

# https://github.com/minio/md5-simd
%global goipath         github.com/minio/md5-simd
Version:                1.1.1

%gometa

%global common_description %{expand:
Accelerate aggregated MD5 hashing performance up to 8x for AVX512 and 4x for
AVX2. Useful for server applications that need to compute many MD5 sums in
parallel.}

%global golicenses      LICENSE
%global godocs          README.md

%global godevelheader %{expand:
Requires:               golang(github.com/klauspost/cpuid)}

Name:           %{goname}
Release:        2%{?dist}
Summary:        Accelerate aggregated MD5 hashing performance up to 8x for AVX512 and 4x for AVX2

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/klauspost/cpuid)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 17:41:19 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Wed Jul 29 22:41:40 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Initial package