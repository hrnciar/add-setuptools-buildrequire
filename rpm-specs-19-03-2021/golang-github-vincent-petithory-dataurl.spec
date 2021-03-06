# Generated by go2rpm 1
%bcond_without check

# https://github.com/vincent-petithory/dataurl
%global goipath         github.com/vincent-petithory/dataurl
%global commit          d1553a71de50473073e188aa79cebf7f993f20fe

%gometa

%global common_description %{expand:
Data URL Schemes in Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Data URL Schemes in Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%package -n dataurl
Summary: Data URL encoder/decoder

%description
%{common_description}

%description -n dataurl
dataurl is a command-line data-scheme URL encoder and decoder written in Golang.

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%gopkgfiles

%files -n dataurl
%license LICENSE
%{_bindir}/dataurl

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 18:23:29 CST 2019 Benjamin Lowry <ben@ben.gmbh> - 0-0.1.20191224gitd1553a7
- Initial package

