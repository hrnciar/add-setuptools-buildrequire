# Generated by go2rpm 1
%bcond_without check

# https://github.com/nrdcg/dnspod-go
%global goipath         github.com/nrdcg/dnspod-go
Version:                0.4.0

%gometa

%global common_description %{expand:
A Go client for the DNSPod API.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        DNSPod Go API client

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jan 26 18:02:03 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Initial package