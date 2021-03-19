# Generated by go2rpm
%bcond_without check

# https://github.com/dgryski/go-bitstream
%global goipath         github.com/dgryski/go-bitstream
%global commit          3522498ce2c8ea06df73e55df58edfbfb33cfdd6

%gometa

%global common_description %{expand:
Read and write bits from io.Reader and io.Writer streams.}

%global golicenses      LICENSE
%global godocs          README

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Read and write bits from io.Reader and io.Writer streams
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 22:37:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190307git3522498
- Update to new macros

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190307git3522498
- First package for Fedora
