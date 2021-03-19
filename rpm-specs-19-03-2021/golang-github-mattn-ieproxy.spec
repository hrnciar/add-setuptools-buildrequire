# Generated by go2rpm 1
%bcond_without check

# https://github.com/mattn/go-ieproxy
%global goipath         github.com/mattn/go-ieproxy
Version:                0.0.1

%gometa

%global common_description %{expand:
Go package to detect the proxy settings on Windows platform.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Detect the proxy settings on Windows platform

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 20:19:39 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- Update to 0.0.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 11:35:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190729git6dee0af
- Initial package