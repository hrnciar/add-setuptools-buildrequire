# Generated by go2rpm
%bcond_without check

# https://github.com/djherbis/nio
%global goipath         github.com/djherbis/nio
Version:                2.0.3

%gometa

%global common_description %{expand:
Package Nio provides a few buffered io primitives.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Concurrent Buffered IO in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/djherbis/buffer)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 00:30:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.3-1
- Initial package