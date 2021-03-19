# Generated by go2rpm 1
%bcond_without check

# https://github.com/projectdiscovery/naabu
%global goipath         github.com/projectdiscovery/naabu
Version:                1.1.4

%gometa

%global common_description %{expand:
A fast port scanner written in go with focus on reliability and simplicity.
Designed to be used in combination with other tools for attack surface
discovery in bug bounties and pentests.}

%global golicenses      LICENSE
%global godocs          THANKS.md README.md

Name:           naabu
Release:        3%{?dist}
Summary:        Fast port scanner

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/gopacket)
BuildRequires:  golang(github.com/google/gopacket/layers)
BuildRequires:  golang(github.com/google/gopacket/pcap)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/phayes/freeport)
BuildRequires:  golang(github.com/projectdiscovery/gologger)
BuildRequires:  golang(github.com/remeh/sizedwaitgroup)
BuildRequires:  golang(golang.org/x/net/icmp)
BuildRequires:  golang(golang.org/x/net/ipv4)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc THANKS.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> -  1.1.4-1
- Update to new upstream release 1.1.4

* Sun Jun 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-1
- Update to latest upstream release 1.1.3

* Sat May 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Initial package

