# Generated by go2rpm
%bcond_without check

# https://github.com/benesch/cgosymbolizer
%global goipath         github.com/benesch/cgosymbolizer
%global commit          bec6fe6e597bfeb28b9d8c0b998772635fceea8b

%gometa

%global common_description %{expand:
Package cgosymbolizer teaches the Go runtime to include cgo frames in
backtraces.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Include cgo frames in backtraces

License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/ianlancetaylor/cgosymbolizer)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 18:58:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701gitbec6fe6
- Initial package
