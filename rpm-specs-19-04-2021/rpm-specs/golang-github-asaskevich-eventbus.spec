# Generated by go2rpm 1
%bcond_without check

# https://github.com/asaskevich/EventBus
%global goipath         github.com/asaskevich/EventBus
%global commit          49d423059eefd67a7243331db83e16d347139b4a

%gometa

%global common_description %{expand:
Lightweight eventbus with async compatibility for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Lightweight eventbus

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 22:15:22 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20210108git49d4230
- Bump to commit 49d423059eefd67a7243331db83e16d347139b4a

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 18:28:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20200723git4fc0642
- Bump to commit 4fc0642a29f392d9caa94cdb7503d2b676e3f442

* Fri Apr 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200410gitd46933a
- Initial package