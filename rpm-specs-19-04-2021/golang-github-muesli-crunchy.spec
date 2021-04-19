%bcond_without check
# Tests require network access
%bcond_with network

# https://github.com/muesli/crunchy
%global goipath         github.com/muesli/crunchy
Version:                0.4.0

%gometa

%global common_description %{expand:
Finds common flaws in passwords. Like cracklib, but written in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Finds common flaws in passwords

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/xrash/smetrics)

Recommends: words

%if %{with check}
# Tests
BuildRequires:  words
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with network}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-2
- Update requirements (#1893562)

* Sun Nov 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Initial package for Fedora