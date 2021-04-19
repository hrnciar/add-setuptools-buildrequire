%bcond_without check

# https://github.com/R4yGM/netscanner
%global goipath         github.com/R4yGM/netscanner
%global commit          8baab364210e664c0f3e58f625a2cd4cc1e18bbb

%gometa

%global common_description %{expand:
A TCP/UDP scanner to find open or closed ports.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           netscanner
Version:        0
Release:        0.2%{?dist}
Summary:        TCP/UDP scanner to find open or closed ports

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's/\r$//' README.md

%build
%gobuild -o %{gobuilddir}/bin/netscanner %{goipath}

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20201029git8baab36
- Initial package for Fedora