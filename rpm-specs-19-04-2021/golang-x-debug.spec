# Generated by go2rpm
%bcond_without check

# https://github.com/golang/debug
%global goipath         golang.org/x/debug
%global forgeurl        https://github.com/golang/debug
%global commit          c934e1b37329c7060a7a2578f9c2ca870a085bf7

%gometa

%global common_description %{expand:
This repository holds utilities and libraries for debugging Go programs.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        Go debugging tools

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/chzyer/readline)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(golang.org/x/sys/unix)

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
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 01:45:58 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20210123gitc934e1b
- Bump to commit c934e1b37329c7060a7a2578f9c2ca870a085bf7

* Fri Aug 07 19:06:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20200807git66ec140
- Bump to commit 66ec140f2f72d15dc6133502edd2bb7238b1740c

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 22:11:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190602git621e2d3
- Bump to commit 621e2d3f35dac46daf912f8d9d2fabd57d022520

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git7fa577e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git7fa577e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180421git7fa577e
- First package for Fedora
