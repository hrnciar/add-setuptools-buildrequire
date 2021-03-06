# Generated by go2rpm 1
%bcond_without check

# https://github.com/chris-ramon/douceur
%global goipath         github.com/chris-ramon/douceur
Version:                0.2.0
%global commit          f3463056cd52886eda904655e1940157bf323bd7

%gometa

%global common_description %{expand:
A simple CSS parser and inliner in Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Simple CSS parser and inliner in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gorilla/css/scanner)
BuildRequires:  golang(github.com/PuerkitoBio/goquery)
BuildRequires:  golang(golang.org/x/net/html)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/douceur %{goipath}

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
%doc CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 12:49:42 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1.20200910gitf346305
- Initial package