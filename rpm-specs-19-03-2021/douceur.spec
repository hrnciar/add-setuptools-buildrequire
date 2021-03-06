# Generated by go2rpm
%bcond_without check

# https://github.com/aymerick/douceur
%global goipath         github.com/aymerick/douceur
Version:                0.2.0

%gometa

%global common_description %{expand:
A simple CSS parser and inliner in Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

%global godevelheader %{expand:
Obsoletes:      golang-github-aymerick-douceur-unit-test-devel < 0.2.0-7
}

Name:           douceur
Release:        11%{?dist}
Summary:        A simple CSS parser and inliner in Go

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
%{_bindir}/douceur

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-7
- Update to latest Go macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.2.0-5
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.0-2
- Require the correct devel subpackage for unit tests
- Fix unit tests subpackage Summary

* Wed Oct 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.0-1
- First package for Fedora
