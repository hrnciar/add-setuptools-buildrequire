# Generated by go2rpm
%bcond_without check

# https://github.com/iij/doapi
%global goipath         github.com/iij/doapi
%global commit          0bbf12d6d7dfbba49740730208c418ece866a22b

%gometa

%global common_description %{expand:
Golang binding for DO API.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Golang binding for DO API

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/sirupsen/logrus)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 21:55:04 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20210109git0bbf12d
- Bump to commit 0bbf12d6d7dfbba49740730208c418ece866a22b

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 21:17:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190502git8803795
- Initial package
