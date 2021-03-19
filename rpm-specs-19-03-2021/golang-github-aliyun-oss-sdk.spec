# Generated by go2rpm
# Tests are FUBAR and I don't speak Chinese
%bcond_with check

# https://github.com/aliyun/aliyun-oss-go-sdk
%global goipath         github.com/aliyun/aliyun-oss-go-sdk
Version:                2.1.6

%gometa

%global common_description %{expand:
Alibaba Cloud OSS SDK for Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README-CN.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Alibaba Cloud OSS SDK for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/kms)
BuildRequires:  golang(golang.org/x/time/rate)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/baiyubin/aliyun-sts-go-sdk/sts)
BuildRequires:  golang(gopkg.in/check.v1)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 13:31:43 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.6-1
- Update to 2.1.6
- Close: rhbz#1915741

* Fri Dec 04 22:31:28 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.5-1
- Update to 2.1.5
- Close: rhbz#1860333

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 14:43:35 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 22:08:42 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 17:26:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.6-1
- Initial package
