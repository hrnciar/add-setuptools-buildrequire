# Generated by go2rpm 1
%bcond_without check

# https://github.com/jcmturner/rpc
%global goipath         gopkg.in/jcmturner/rpc.v0
%global forgeurl        https://github.com/jcmturner/rpc
Version:                0.0.2

%gometa

%global common_description %{expand:
Remote Procedure Call libraries
(https://pubs.opengroup.org/onlinepubs/9629399/).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Remote Procedure Call libraries

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 20:43:58 EST 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.2-1
- Initial package
