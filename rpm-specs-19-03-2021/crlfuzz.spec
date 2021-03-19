# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/dwisiswant0/crlfuzz
%global goipath         github.com/dwisiswant0/crlfuzz
Version:                1.4.0

%gometa

%global common_description %{expand:
A fast tool to scan CRLF vulnerability written in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           crlfuzz
Release:        2%{?dist}
Summary:        Tool to scan CRLF vulnerability

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/logrusorgru/aurora)
BuildRequires:  golang(github.com/projectdiscovery/gologger)

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
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Initial package