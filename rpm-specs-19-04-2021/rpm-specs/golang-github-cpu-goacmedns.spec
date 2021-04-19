# Generated by go2rpm
%bcond_without check

# https://github.com/cpu/goacmedns
%global goipath         github.com/cpu/goacmedns
Version:                0.1.1

%gometa

%global common_description %{expand:
A Go library to handle acme-dns client communication and persistent account
storage.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go library to handle acme-dns client communication

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

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
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 16:30:57 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Update to 0.1.1
- Close: rhbz#1913150

* Fri Jan  1 21:59:35 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Update to 0.1.0
- Close: rhbz#1911548

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 19:23:59 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.3-1
- Update to 0.0.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 18:38:58 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-3
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Carl George <carl@george.computer> - 0.0.1-1
- Initial package