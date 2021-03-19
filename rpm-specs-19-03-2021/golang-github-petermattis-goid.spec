# Generated by go2rpm
%bcond_without check

# https://github.com/petermattis/goid
%global goipath         github.com/petermattis/goid
%global commit          b0b1615b78e5ee59739545bb38426383b2cda4c9

%gometa

%global common_description %{expand:
Programatically retrieve the current goroutine's ID.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.17%{?dist}
Summary:        Programatically retrieve the current goroutine's ID

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 23:56:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.13.20180902gitb0b1615
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20180202gitb0b1615
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.11.20180202gitb0b1615
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.10.20180202gitb0b1615
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20180202.gitb0b1615
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180202.gitb0b1615
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.20180202.gitb0b1615
- Bump to commit b0b1615.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.git176e84a
- Bump to commit 176e84a.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.git3db12eb
- Bump to commit 3db12eb.

* Sat Aug 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.4.git0ded858
- Bump to commit 0ded858, which adds support for go 1.9.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitcaab644
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitcaab644
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.gitcaab644
- First package for Fedora
