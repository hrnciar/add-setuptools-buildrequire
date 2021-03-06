# Generated by go2rpm 1.3
# Fails, dead upstream.
%bcond_with check

# https://github.com/alicebob/gopher-json
%global goipath         github.com/alicebob/gopher-json
%global commit          a9ecdc9d1d3afa52b1f21db0ed0b568152d74cab

%gometa

%global common_description %{expand:
Package Json is a simple JSON encoder/decoder for gopher-lua.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A fork of layeh.com/gopher-json for use in miniredis

License:        Unlicense
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/yuin/gopher-lua)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 17:14:14 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20210110gita9ecdc9
- Initial package
