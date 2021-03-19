# Generated by go2rpm
%bcond_without check

# https://github.com/briandowns/spinner
%global goipath         github.com/briandowns/spinner
Version:                1.12.0

%gometa

%global common_description %{expand:
Spinner is a simple package to add a spinner / progress indicator to any
terminal application.}

%global golicenses      LICENSE
%global godocs          _example README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Go package providing a terminal spinner/progress indicator

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Disable TestRestart which fails with Go 1.16
# https://github.com/briandowns/spinner/issues/111
Patch0:         0001-Disable-failing-test.patch

BuildRequires:  golang(github.com/fatih/color)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 19:01:37 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-2
- Drop patch which wasn't fixing the race condition.
- Temporaly disabling test until upstream fixes the issue.

* Mon Nov 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.0-1
- Update to latest version (#1902535)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Harry Míchal <harrymichal@seznam.cz> - 1.11.1-1
- Update to 1.11.1

* Thu Mar 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.0-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.9.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.0-1
- Update to latest version

* Tue Sep 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.0-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 15:42:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.1-1
- Release 1.6.1

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6-1
- Update to latest version

* Mon Mar 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5-1
- Update to latest version

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4-1
- First package for Fedora
