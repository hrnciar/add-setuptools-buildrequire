# Generated by go2rpm 1
%bcond_without check

# https://github.com/NetSPI/goddi
%global goipath         github.com/NetSPI/goddi
Version:                1.2

%gometa

%global common_description %{expand:
Goddi (go dump domain info) dumps Active Directory domain information.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           goddi
Release:        4%{?dist}
Summary:        Dumper for Active Directory domain information

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/ldap.v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/goddi %{goipath}

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
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Initial package

