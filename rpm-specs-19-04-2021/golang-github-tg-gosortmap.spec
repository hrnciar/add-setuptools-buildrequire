# Generated by go2rpm
%bcond_without check

# https://github.com/tg/gosortmap
%global goipath         github.com/tg/gosortmap
%global commit          4b9ddc7c3a61652b569b7cc4368bbcde539392ce

%gometa

%global common_description %{expand:
Sort maps in Go by keys or values. Works with most built-in types; own
comparator can be provided to support custom types and ordering.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Sort maps in Go

License:        MIT
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 01:47:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20190523git4b9ddc7
- Bump to commit 4b9ddc7c3a61652b569b7cc4368bbcde539392ce

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git2901ada
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Gabe <redhatrises@gmail.com> - 0-0.1.20180814git2901ada
- First package for Fedora