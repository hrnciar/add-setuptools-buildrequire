# Generated by go2rpm 1
%bcond_without check

# https://github.com/rolieup/golie
%global goipath         github.com/rolieup/golie
Version:        0.2.1

%gometa

%global common_description %{expand:
A client/server implementation of ROLIE written in GO.}

%global golicenses      LICENSE LICENSE.NIST
%global godocs          examples README.md

Name:           golie
Release:        2%{?dist}
Summary:        A client/server implementation of ROLIE written in GO

# Upstream license specification: CC0-1.0
License:        CC0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gocomply/scap/pkg/scap/constants)
BuildRequires:  golang(github.com/gocomply/scap/pkg/scap/scap_document)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)

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
%license LICENSE LICENSE.NIST
%doc examples README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Šimon Lukašík <slukasik@redhat.com> - 0.2.1-1
- new version

* Fri Aug 21 2020 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-2
- rebuilt

* Fri Aug 21 2020 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-1
- new version

* Thu Jul 30 2020 Šimon Lukašík <slukasik@redhat.com> - 0.1.2-1
- new version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 14:42:42 CEST 2020 Šimon Lukašík <slukasik@redhat.com> - 0.1.1-1
- Update to the latest upstram release

* Thu Jul 02 19:38:12 CEST 2020 Šimon Lukašík <slukasik@redhat.com> - 0-0.1.20200702git9dd93d8
- Initial package
