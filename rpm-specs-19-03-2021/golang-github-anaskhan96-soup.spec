# Generated by go2rpm 1
%bcond_without check

# https://github.com/anaskhan96/soup
%global goipath         github.com/anaskhan96/soup
Version:                1.2.4

%gometa

%global common_description %{expand:
Web Scraper in Go, similar to BeautifulSoup.}

%global golicenses      license
%global godocs          examples README.md CHANGELOG.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Web Scraper in Go, similar to BeautifulSoup

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/charset)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 13:54:00 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 01:56:19 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2-1
- Update to 1.2

* Wed Oct 02 03:03:58 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.1-1
- Initial package
