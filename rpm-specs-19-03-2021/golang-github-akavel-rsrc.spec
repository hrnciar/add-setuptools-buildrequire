# Generated by go2rpm
%bcond_without check

# https://github.com/akavel/rsrc
%global goipath         github.com/akavel/rsrc
Version:                0.10.1

%gometa

%global common_description %{expand:
Tool for embedding binary resources in Go programs.}

%global golicenses      LICENSE.txt
%global godocs          AUTHORS README.txt

Name:           %{goname}
Release:        2%{?dist}
Summary:        Tool for embedding .ico & manifest resources in Go programs

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/rsrc %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.txt
%doc AUTHORS README.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 04:17:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.1-1
- Update to 0.10.1
- Close: rhbz#1906676

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 09:32:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 23:05:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-1
- Initial package