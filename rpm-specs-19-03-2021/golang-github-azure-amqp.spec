# Generated by go2rpm 1
%bcond_without check

# https://github.com/Azure/go-amqp
%global goipath         github.com/Azure/go-amqp
Version:                0.13.1

%gometa

%global common_description %{expand:
github.com/Azure/go-amqp is an AMQP 1.0 client implementation for Go.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        SECURITY.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        AMQP 1.0 client library for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 05:03:07 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.13.1-2
- Update to 0.13.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 22:34:12 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.12.7-1
- Initial package
