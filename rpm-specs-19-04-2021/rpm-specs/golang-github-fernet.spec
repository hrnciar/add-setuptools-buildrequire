# Generated by go2rpm
%bcond_without check

# https://github.com/fernet/fernet-go
%global goipath         github.com/fernet/fernet-go
%global commit          eff2850e60014b3643d850a51c69482d3a8352b1

%gometa

%global common_description %{expand:
Fernet takes a user-provided *message* (an arbitrary sequence of bytes), a key
(256 bits), and the current time, and produces a token, which contains the
message in a form that can't be read or altered without the key.}

%global golicenses      License
%global godocs          Readme

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Generate and verify HMAC-based authentication tokens

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
%doc Readme
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 17:21:47 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200726giteff2850
- Bump to commit eff2850e60014b3643d850a51c69482d3a8352b1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 23:56:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190628git9eac43b
- Initial package
