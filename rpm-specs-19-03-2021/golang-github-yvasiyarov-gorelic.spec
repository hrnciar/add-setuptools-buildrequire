# Generated by go2rpm
%bcond_without check

# https://github.com/yvasiyarov/gorelic
%global goipath         github.com/yvasiyarov/gorelic
Version:                0.0.7

%gometa

%global common_description %{expand:
New Relic agent for Go runtime. It collect a lot of metrics about scheduler,
garbage collector and memory allocator and send them to NewRelic.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        New relic agent for Go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/yvasiyarov/go-metrics)
BuildRequires:  golang(github.com/yvasiyarov/newrelic_platform_go)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 22:05:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.7-1
- Update to 0.0.7

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 00:57:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.6-1.20190502git635ca60
- Release 0.0.6, commit 635ca6035f2355e29fc558effa613d0d5867aac8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gita9bba5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gita9bba5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gita9bba5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gita9bba5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gita9bba5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita9bba5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gita9bba5b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Fri Mar 04 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gita9bba5b
- First package for Fedora
  resolves: #1314978