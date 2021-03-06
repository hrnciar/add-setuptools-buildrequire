# Generated by go2rpm
%bcond_without check

# https://github.com/AudriusButkevicius/go-nat-pmp
%global goipath         github.com/AudriusButkevicius/go-nat-pmp
%global commit          452c97607362b2ab5a7839b8d1704f0396b640ca

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-AudriusButkevicius-go-nat-pmp-devel < 0-0.9
}

%global common_description %{expand:
A Go language client for the NAT-PMP internet protocol for port mapping and
discovering the external IP address of a firewall.

NAT-PMP is supported by Apple brand routers and open source routers like Tomato
and DD-WRT.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.14%{?dist}
Summary:        Go language client for the NAT-PMP internet protocol

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.10.20190703git452c976
- Add Obsoletes for old name

* Thu May 30 17:12:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20190703git452c976
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20160522git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.20160522git452c976
- Use forgeautosetup instead of gosetup.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20160522git452c976
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.git452c976
- First package for Fedora

