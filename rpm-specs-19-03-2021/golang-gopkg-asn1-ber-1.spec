# Generated by go2rpm
%bcond_without check

# https://github.com/go-asn1-ber/asn1-ber
%global goipath         gopkg.in/asn1-ber.v1
%global forgeurl        https://github.com/go-asn1-ber/asn1-ber
Version:                1.5.3

%gometa

%global goaltipaths     github.com/go-asn1-ber/asn1-ber

%global common_description %{expand:
Asn1 ber encoding / decoding library for the Go programming language.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Asn1 ber encoding / decoding library for the Go programming language

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 11:04:41 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.3-1
- Update to 1.5.3
- Close: rhbz#1906716

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5.1-1
- Update to version 1.5.1.
- Fixes RHBZ#1846577

* Fri Jun 12 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-1
- Update to version 1.5.0.

* Sat Feb 15 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.1-1
- Update to version 1.4.1.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.4-1
- Update to version 1.4.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 16:31:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3-4
- Add alternative import path

* Wed Apr 17 09:09:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3-3
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3-1
- Update to version 1.3.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2-2
- Use autosetup instead of gosetup.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2-1
- Initial package for fedora.

