# Generated by go2rpm
%bcond_without check

# https://github.com/PuerkitoBio/purell
%global goipath         github.com/PuerkitoBio/purell
Version:                1.1.1

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-PuerkitoBio-purell-devel < 1.1.1-2
Obsoletes:      golang-github-PuerkitoBio-purell-unit-test-devel < 1.1.1-2
}

%global common_description %{expand:
Purell is a tiny Go library to normalize URLs. It returns a pure URL.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Tiny Go library to normalize URLs

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/PuerkitoBio/urlesc)
BuildRequires:  golang(golang.org/x/net/idna)
BuildRequires:  golang(golang.org/x/text/unicode/norm)
BuildRequires:  golang(golang.org/x/text/width)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-3
- Add Obsoletes for old name

* Thu May 09 21:57:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-2
- Update to new repos

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-5
- Include cvs revision information for golang tools

* Tue Mar 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-4
- Run all tests
- Remove empty conditionals
- Fix GOPATH in %%check
- Improve Source URL

* Sun Mar 12 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-3
- Remove package name from summary
- Use dist tag

* Sun Feb 26 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-2
- Use different version of urlesc

* Sun Feb 26 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-1
- Update version

* Sun Nov 13 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-1
- Initial package
