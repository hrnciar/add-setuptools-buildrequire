# Generated by go2rpm
%bcond_without check

# https://github.com/facebookarchive/structtag
%global goipath         github.com/facebookarchive/structtag
%global commit          217e25fb96916cc60332e399c9aa63f5c422ceed

%gometa

%global goaltipaths     github.com/facebookgo/structtag

%global common_description %{expand:
Package structtag provides parsing of the defacto struct tag style.}

%global golicenses      license
%global godocs          readme.md

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        Package providing parsing of the defacto struct tag style
License:        BSD
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 14:23:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190321git217e25fb
- Update to new macros

* Mon Apr 29 2019 Mark Goodwin <mgoodwin@redhat.com> - 0-0.3.20190321git217e25fb
- bump to rebuild the subpackage for the non-archived import path

* Thu Mar 28 2019 Nathan Scott <nathans@redhat.com> - 0-0.2.20190321git217e25fb
- Add a subpackage for the non-archived import path as well

* Thu Mar 21 2019 Mark Goodwin <mgoodwin@redhat.com> - 0-0.1.20190321git217e25fb
- First package for Fedora
