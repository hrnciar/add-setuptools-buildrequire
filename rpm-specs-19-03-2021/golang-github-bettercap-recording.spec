# Generated by go2rpm 1
%bcond_without check

# https://github.com/bettercap/recording
%global goipath         github.com/bettercap/recording
%global commit          3ce1dcf032e391eb321311b34cdf31c6fc9523f5

%gometa

%global common_description %{expand:
This package allows reading and writing bettercap's session recordings.}

%global golicenses      LICENSE.md
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Allows reading and writing bettercap's session recordings

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/evilsocket/islazy/fs)
BuildRequires:  golang(github.com/kr/binarydist)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200404git3ce1dcf
- Initial package

