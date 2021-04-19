# Generated by go2rpm
%bcond_without check

# https://github.com/klauspost/pgzip
%global goipath         github.com/klauspost/pgzip
Version:                1.2.5

%gometa

%global common_description %{expand:
Go parallel gzip compression/decompression. This is a fully gzip compatible drop
in replacement for "compress/gzip".

This will split compression into blocks that are compressed in parallel. This
can be useful for compressing big amounts of data. The output is a standard gzip
file.

The gzip decompression is modified so it decompresses ahead of the current
reader. This means that reads will be non-blocking if the decompressor can keep
ahead of your code reading from it. CRC calculation also takes place in a
separate goroutine.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go parallel gzip (de)compression

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/klauspost/compress/flate)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/klauspost/compress/gzip)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 02:31:50 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.5-1
- Update to 1.2.5
- Close: rhbz#1875033

* Tue Jul 28 19:31:50 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 01:00:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.1-1
- Initial package
