# Generated by go2rpm 1
%bcond_without check

# https://github.com/go-playground/assert/v2
%global goipath         github.com/go-playground/assert/v2
Version:                2.0.1

%gometa

%global goaltipaths     gopkg.in/go-playground/assert.v2

%global common_description %{expand:
Basic Assertion Library used along side native go testing, with building blocks
for custom assertions.}

Name:           %{goname}
Release:        2%{?dist}
Summary:        Basic Assertion Library used along side native go testing

License:        MIT
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jul 26 19:03:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-1
- Initial package