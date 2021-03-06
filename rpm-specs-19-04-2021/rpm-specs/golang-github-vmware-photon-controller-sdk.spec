# Generated by go2rpm
%bcond_without check

# https://github.com/vmware/photon-controller-go-sdk
%global goipath         github.com/vmware/photon-controller-go-sdk
%global commit          e3620ad3ad39dcb965dee64917d8880475a95e77

%gometa

%global common_description %{expand:
Photon Controller GO SDK.}

%global golicenses      LICENSE LICENSE-SSPI.txt
%global godocs          DEVELOP.md README.md README-SSPI.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Photon Controller GO SDK

# Upstream license specification: Apache-2.0 and BSD-3-Clause
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv SSPI/LICENSE.txt LICENSE-SSPI.txt
mv SSPI/README.md README-SSPI.md

%install
%gopkginstall

%if %{with check}
%check
# https://github.com/vmware/photon-controller-go-sdk/issues/5
%gocheck -d photon
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 23:06:37 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702gite3620ad3
- Initial package

