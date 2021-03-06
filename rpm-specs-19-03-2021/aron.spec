# Generated by go2rpm 1
%bcond_without check

# https://github.com/m4ll0k/Aron
%global goipath         github.com/m4ll0k/Aron
%global commit          7eade5895a950c97b00fa78b9b24fde52868be0b

%gometa

%global common_description %{expand:
Aron is a GO script for finding hidden GET & POST parameters.}

%global golicenses      LICENSE
%global godocs          README.md dict.txt

Name:           aron
Version:        0
Release:        0.3%{?dist}
Summary:        Tool to find hidden GET & POST parameters

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/Aron %{goipath}

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
%doc README.md dict.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200518git7eade58
- Initial package

