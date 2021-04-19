# Generated by go2rpm
%bcond_without check

# https://github.com/smartystreets/go-aws-auth
%global goipath         github.com/smartystreets/go-aws-auth
Version:                1.0.0
%global tag             1.0.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-smartystreets-go-aws-auth-devel < 0-0.12
Obsoletes:      golang-github-smartystreets-go-aws-auth-unit-test < 0-0.12
}

%global common_description %{expand:
Go-AWS-Auth is a comprehensive, lightweight library for signing requests to
Amazon Web Services.

It's easy to use: simply build your HTTP request and call awsauth.Sign(req)}

%global golicenses      LICENSE.md
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Signs requests to Amazon Web Services

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/assertions)
BuildRequires:  golang(github.com/smartystreets/assertions/should)
BuildRequires:  golang(github.com/smartystreets/gunit)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-2
- Add Obsoletes for old names

* Fri Apr 26 23:13:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Release 1.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git1f0db8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git1f0db8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git1f0db8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git1f0db8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git1f0db8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git1f0db8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git1f0db8c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git1f0db8c
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git1f0db8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git1f0db8c
- Update spec file to spec-2.0
  resolves: 1250510

* Thu Apr 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git1f0db8c
- First package for Fedora
  resolves: #1214892
