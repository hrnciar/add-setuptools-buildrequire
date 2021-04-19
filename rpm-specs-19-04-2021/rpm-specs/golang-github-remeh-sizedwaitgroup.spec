# Generated by go2rpm
%bcond_without check

# https://github.com/remeh/sizedwaitgroup
%global goipath         github.com/remeh/sizedwaitgroup
Version:                1.0.0

%gometa

%global common_description %{expand:
SizedWaitGroup has the same role and API as sync.WaitGroup but it adds a limit
of the amount of goroutines started concurrently.

SizedWaitGroup adds the feature of limiting the maximum number of concurrently
started routines. It could for example be used to start multiples routines
querying a database but without sending too much queries in order to not
overload the given database.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang WaitGroup with throttling

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 19:18:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 16:59:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190530git5e7302b
- Bump to commit 5e7302b12ccef91dce9fde2f5bda6d5c7ea5d2eb

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git5582a67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git5582a67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0-0.1.git5582a67
- Initial packaging