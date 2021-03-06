# Generated by go2rpm 1
%bcond_without check

# https://github.com/s-rah/onionscan
%global goipath         github.com/s-rah/onionscan
Version:                0.2
%global tag             OnionScan-0.2

%gometa

%global common_description %{expand:
OnionScan is a free and open source tool for investigating the Dark Web.}

%global golicenses      LICENSE
%global godocs          doc CONTRIBUTING.md README.md design/000-onionscan.md\\\
                        design/001-database.md

Name:           onionscan
Release:        3%{?dist}
Summary:        Tool for investigating the Dark Web

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/HouzuoGuo/tiedot/db)
BuildRequires:  golang(github.com/rwcarlsen/goexif/exif)
BuildRequires:  golang(github.com/rwcarlsen/goexif/tiff)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/proxy)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/onionscan %{goipath}

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
%doc doc CONTRIBUTING.md README.md design/000-onionscan.md
%doc design/001-database.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-1
- Initial package for Fedora

