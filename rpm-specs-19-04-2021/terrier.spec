# Generated by go2rpm 1
%bcond_without check

# https://github.com/heroku/terrier
%global goipath         github.com/heroku/terrier
Version:                0.0.2
%global tag             0.0.2

%gometa

%global common_description %{expand:
Terrier is a Image and Container analysis tool that can be used to scan Images
and Containers to identify and verify the presence of specific files according
to their hashes.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           terrier
Release:        3%{?dist}
Summary:        Image and Container analysis tool

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep
chmod -x README.md LICENSE

%build
%gobuild -o %{gobuilddir}/bin/terrier %{goipath}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.2-1
- Initial package

