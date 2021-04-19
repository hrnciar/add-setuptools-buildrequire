# Generated by go2rpm 1
%bcond_with check

# https://github.com/ffuf/ffuf
%global goipath         github.com/ffuf/ffuf
Version:                1.0.2

%gometa

%global common_description %{expand:
Fast web fuzzer written in Go.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTORS.md README.md CHANGELOG.md

Name:           ffuf
Release:        3%{?dist}
Summary:        Fast web fuzzer written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/ffuf %{goipath}

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
%doc CONTRIBUTORS.md README.md CHANGELOG.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.2-1
- Initial package for Fedora