# Generated by go2rpm 1
%bcond_without check

# https://github.com/subfinder/goaltdns
%global goipath         github.com/subfinder/goaltdns
%global commit          2b3e8a30b8cf333be47885687ca92794d8f485fa

%gometa

%global common_description %{expand:
A permutation generation tool written in Golang.}

%global golicenses      LICENSE
%global godocs          README.md words2.txt words.txt

Name:           goaltdns
Version:        0
Release:        0.4%{?dist}
Summary:        Permutation generation tool

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/bobesa/go-domain-util/domainutil)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/goaltdns %{goipath}

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
%doc README.md words2.txt words.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200524git2b3e8a3
- Initial package

