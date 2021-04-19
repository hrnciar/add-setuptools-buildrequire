# Generated by go2rpm
%bcond_without check

# https://github.com/client9/gospell
%global goipath         github.com/client9/gospell
%global commit          90dfc71015dfebd3a7274f1ad2756c1dbf09e250

%gometa

%global common_description %{expand:
Pure golang spelling based on Hunspell dictionaries.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        Pure golang spelling based on Hunspell dictionaries

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/client9/plaintext)
BuildRequires:  golang(github.com/naoina/toml)
BuildRequires:  golang(github.com/ryanuber/go-glob)
BuildRequires:  golang(golang.org/x/net/html)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/gospell %{goipath}/cmd/gospell

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
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 17:47:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190524git90dfc71
- Update to new macro

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git90dfc71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git90dfc71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0-0.1.git90dfc71
- Initial packaging