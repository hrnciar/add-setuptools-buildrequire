# Generated by go2rpm 1
%bcond_without check

# https://github.com/d5/tengo
%global goipath         github.com/d5/tengo/v2
Version:                2.6.2

%gometa

%global common_description %{expand:
A fast script language for Go.}

%global golicenses      LICENSE
%global godocs          docs examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Fast script language for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/tengo %{goipath}/cmd/tengo

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
%doc docs examples README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 19:02:26 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.6.2-1
- Update to 2.6.2

* Tue Sep 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-1
- Update to latest upstream release 2.6.1

* Tue Sep 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.0-2
- Rename package and adjust path
- Limit binary part (rhbz#1872583)

* Wed Aug 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.0-1
- Initial package