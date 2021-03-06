# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/buengese/sgzip
%global goipath         github.com/buengese/sgzip
Version:                0.1.1

%gometa

%global common_description %{expand:
Experiments for a seekable gzip for use in rclone. Based on pgzip.}

%global golicenses      LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        Experiments for a seekable gzip for use in rclone

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
* Sat Mar 06 08:11:28 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Initial package
