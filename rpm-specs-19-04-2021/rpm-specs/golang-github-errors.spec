# Generated by go2rpm
%bcond_without check

# https://github.com/go-errors/errors
%global goipath         github.com/go-errors/errors
Version:                1.1.1

%gometa

%global common_description %{expand:
Package Errors adds stacktrace support to errors in Go.

This is particularly useful when you want to understand the state of execution
when an error was returned unexpectedly.

It provides the type *Error which implements the standard golang error
interface, so you can use this library interchangably with code that is
expecting a normal error return.}

%global golicenses      LICENSE.MIT
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Errors with stacktraces for Go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 16:36:39 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Jan 30 22:10:18 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-8
- Fix FTBFS by increasing error margin

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-5
- Add Obsoletes for old name

* Tue Apr 30 01:33:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-4
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Gianluca Sforna <giallu@gmail.com> - 1.0.1-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Gianluca Sforna <giallu@gmail.com> - 1.0.0-1
* upstream stable release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gita418503
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gita418503
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gita418503
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Gianluca Sforna <giallu@gmail.com> - 0-0.3.gita418503
- more macro clean up

* Wed Nov 16 2016 Gianluca Sforna <giallu@gmail.com> - 0-0.2.gita418503
- clean up el6 macros

* Fri Nov 04 2016 Gianluca Sforna <giallu@gmail.com> - 0-0.1.gita418503
- First package for Fedora