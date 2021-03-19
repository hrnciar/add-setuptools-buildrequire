# Generated by go2rpm 1
%bcond_without check

# https://github.com/zeebo/incenc
%global goipath         github.com/zeebo/incenc
%global commit          0d92902eec542dda12cf62dfbcdd8397d3c821f5

%gometa

%global common_description %{expand:
Incremental Encoding.}

%global golicenses      LICENSE

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Incremental Encoding

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/zeebo/errs)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 15:12:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200620git0d92902
- Initial package