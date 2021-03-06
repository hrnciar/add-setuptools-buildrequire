# Generated by go2rpm 1
%bcond_without check

# https://github.com/chifflier/nfqueue-go
%global goipath         github.com/chifflier/nfqueue-go
%global commit          61ca646babef3bd4dea1deb610bfb0005c0a1298

%gometa

%global common_description %{expand:
nfqueue-go is a wrapper library for libnetfilter-queue. The goal is to
provide a library to gain access to packets queued by the kernel packet
filter.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Go wrapper library for libnetfilter-queue

License:        GPLv2

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/gopacket)

Requires:       libnetfilter_queue

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20200404git61ca646
- Bump release to avoid confusion (rhbz#1820891)

* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200404git61ca646
- Initial package

