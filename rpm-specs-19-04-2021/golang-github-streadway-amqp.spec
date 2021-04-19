# Generated by go2rpm
%bcond_without check

# https://github.com/streadway/amqp
%global goipath         github.com/streadway/amqp
Version:                1.0.0

%gometa

%global common_description %{expand:
Package Amqp is an AMQP 0.9.1 client with RabbitMQ extensions.}

%global golicenses      LICENSE
%global godocs          _examples CONTRIBUTING.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go client for AMQP 0.9.1

# Upstream license specification: BSD-2-Clause
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 02 21:55:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 00:55:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20190515git75d898a
- Bump to commit 75d898a42a940fbc854dfd1a4199eabdc00cf024

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170926gitcefed15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170926gitcefed15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170926gitcefed15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170926gitcefed15
- First package for Fedora
