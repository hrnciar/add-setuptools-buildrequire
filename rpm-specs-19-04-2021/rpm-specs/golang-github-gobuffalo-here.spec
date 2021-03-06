# Generated by go2rpm 1.3
# Needs go modules
%bcond_with check

# https://github.com/gobuffalo/here
%global goipath         github.com/gobuffalo/here
Version:                0.6.2

%gometa

%global common_description %{expand:
Here will get you accurate Go information about the directory of package
requested.}

%global golicenses      LICENSE
%global godocs          README.md SHOULDERS.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Get you accurate Go information about the directory of package requested

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

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
%license LICENSE
%doc README.md SHOULDERS.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 23:40:19 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.2-1
- Initial package
