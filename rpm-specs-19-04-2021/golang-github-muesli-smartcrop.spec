# Generated by go2rpm
%bcond_without check

# https://github.com/muesli/smartcrop
%global goipath         github.com/muesli/smartcrop
Version:                0.3.0

%gometa

%global common_description %{expand:
Smartcrop finds good image crops for arbitrary sizes. It is a pure Go
implementation, based on Jonas Wagner's smartcrop.js}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Find good image crops for arbitrary crop sizes

# While the package is licensed under MIT, images under the examples directory
# are licensed as CC-BY-SA
License:        MIT and CC-BY-SA
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/nfnt/resize)
BuildRequires:  golang(golang.org/x/image/draw)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 16:32:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Release 0.3.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5.20180220git1db4849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.20180220git1db4849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.0-3.20180220git1db4849
- Update to post release due to ABI changes

* Fri Feb 16 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.0-2
- Fix Release tag
- Add CC-BY-SA to license tag due to images in examples file

* Tue Feb 13 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.0-1
- First package for Fedora
