# Generated by go2rpm
%bcond_without check

# https://github.com/tinylib/msgp
%global goipath         github.com/tinylib/msgp
Version:                1.1.5

%gometa

%global common_description %{expand:
This is a code generation tool and serialization library for MessagePack.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go code generator for MessagePack
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/philhofer/fwd)
BuildRequires:  golang(github.com/ttacon/chalk)
BuildRequires:  golang(golang.org/x/tools/imports)

%description
%{common_description}

%package -n msgp
Summary:       %{summary}

%description -n msgp
%{common_description}

This package contains the msgp binary.

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/msgp %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
export GO111MODULE=off
export PATH=$PATH:%{buildroot}%{_bindir}
export GOPATH=%{_datadir}/gocode:%{buildroot}%{_datadir}/gocode
go generate ./msgp
go generate ./_generated
%gocheck
%endif

%files -n msgp
%license LICENSE
%doc README.md
%{_bindir}/msgp

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 04:21:15 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.5-1
- Update to 1.1.5
- Close: rhbz#1895539

* Mon Aug 03 18:35:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 23:17:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-2
- Update to new macros

* Sun Mar 03 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- First package for Fedora
