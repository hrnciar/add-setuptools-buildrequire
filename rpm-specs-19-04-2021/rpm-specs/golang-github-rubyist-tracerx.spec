# Generated by go2rpm
%bcond_without check

# https://github.com/rubyist/tracerx
%global goipath         github.com/rubyist/tracerx
%global commit          787959303086f44a8c361240dfac53d3e9d53ed2

%gometa

%global common_description %{expand:
Package Tracerx implements a simple tracer function that uses environment
variables to control the output. It is a generalized package inspired by git's
GIT_TRACE mechanism.

By default, Tracerx will look for the TRACERX_TRACE environment variable. The
default can by changed by setting the DefaultKey. }

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        12%{?dist}
Summary:        Output tracing information in your Go app based on environment variables

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 17:27:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-8.20190524git7879593
- Bump to commit 787959303086f44a8c361240dfac53d3e9d53ed2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.gitd7bcc0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-1.gitd7bcc0b
- Initial package
