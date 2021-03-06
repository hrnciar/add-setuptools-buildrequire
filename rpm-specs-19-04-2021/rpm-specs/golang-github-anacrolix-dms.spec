# Generated by go2rpm
%bcond_without check

# https://github.com/anacrolix/dms
%global goipath         github.com/anacrolix/dms
Version:                1.2.0

%gometa

%global common_description %{expand:
dms is a UPnP DLNA Digital Media Server. It runs from the terminal, and serves
content directly from the filesystem from the working directory, or the path
given. The SSDP component will broadcast and respond to requests on all
available network interfaces.

dms advertises and serves the raw files, in addition to alternate transcoded
streams when it's able, such as mpeg2 PAL-DVD and WebM for the Chromecast.
It will also provide thumbnails where possible.

dms uses ffprobe/avprobe to get media data such as bitrate and duration,
ffmpeg/avconv for video transoding, and ffmpegthumbnailer for generating
thumbnails when browsing. These commands must be in the PATH given to dms or
the features requiring them will be disabled.}

%global golicenses      LICENSE
%global godocs          README.rst TODO

Name:           %{goname}
Release:        2%{?dist}
Summary:        UPnP DLNA Digital Media Server that includes basic video transcoding

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/nfnt/resize)
BuildRequires:  golang(golang.org/x/net/ipv4)

%description
%{common_description}

%gopkg

%prep
%goprep

# We remove dependencies to "github.com/anacrolix/ffprobe"
# which depends on ffmpeg
rm -rf dlna/dms play transcode

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 18:45:39 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Update to 1.2.0
- Close: rhbz#1909663

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 22:47:58 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 17:07:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Release 1.0.0

* Tue Apr 09 15:51:05 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190409git8af4925
- First package for Fedora
