# Generated by go2rpm
# Same issue as https://github.com/julienschmidt/httprouter/issues/263
%bcond_with check

# https://github.com/bouk/httprouter
%global goipath         github.com/bouk/httprouter
Version:                2.0

%gometa

%global common_description %{expand:
HttpRouter is a lightweight high performance HTTP request router (also called
multiplexer or just mux for short) for Go.

In contrast to the [default mux][http.ServeMux] of Go's net/http package, this
router supports variables in the routing pattern and matches against the request
method. It also scales better.

The router is optimized for high performance and a small memory footprint. It
scales well even with very long paths and a large number of routes. A
compressing dynamic trie (radix tree) structure is used for efficient
matching.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Lightweight high performance HTTP request router for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 16:23:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0-1
- Initial package
