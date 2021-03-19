# Generated by go2rpm 1
%bcond_without check

# https://gitlab.com/flimzy/testy
%global goipath         gitlab.com/flimzy/testy
Version:                0.3.2
%global tag             v0.3.2

%gometa

%global common_description %{expand:
Grab-bag of Go testing utilities.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go testing utilities

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/otiai10/copy)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# https://gitlab.com/flimzy/testy/-/issues/2
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 16:51:50 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Use GitLab macro (rhbz#1822191)
- Update to latest upstream release 0.2.1

* Wed Apr 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package

