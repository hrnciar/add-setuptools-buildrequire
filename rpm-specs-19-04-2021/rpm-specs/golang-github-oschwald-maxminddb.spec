# Generated by go2rpm
%bcond_without check

# https://github.com/oschwald/maxminddb-golang
%global goipath         github.com/oschwald/maxminddb-golang
Version:                1.8.0
# test data for the non-exported git submodule
%global dataurl https://github.com/maxmind/MaxMind-DB
%global dataref c46c33c3c598c648013e2aa7458f8492f4ecfcce

%gometa

%global common_description %{expand:
This is a Go reader for the MaxMind DB format. Although this can be used to read
GeoLite2 and GeoIP2 databases, geoip2 provides a higher-level API for doing so.}

%global golicenses      LICENSE LICENSE-test-data
%global godocs          README.md test-data/MaxMind-DB-spec.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        MaxMind DB Reader for Go

# Code: ISC; Test data: CC-BY-SA 3.0
License:        ISC and CC-BY-SA
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{dataurl}/archive/%{dataref}/MaxMind-DB-%{dataref}.tar.gz

BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# extract test data to the right location
pushd test-data
tar -xzf %{SOURCE1}
mv MaxMind-DB-%{dataref}/* ./
rm -r MaxMind-DB-%{dataref}
popd
mv test-data/LICENSE LICENSE-test-data

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 09:32:14 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.0-1
- Update to 1.8.0
- Close: rhbz#1900901

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Fabio Valentini <decathorpe@gmail.com> - 1.7.0-1
- Update to version 1.7.0.
- Fixes: RHBZ#1846912

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6.0-1
- Update to version 1.6.0.

* Sat Sep 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-1
- Update to version 1.5.0.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 1.4.0-1
- Update to version 1.4.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-2
- Add Obsoletes for old name

* Thu May 23 17:08:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-1
- Release 1.3.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-4
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-3
- Update to use spec 3.0 and enable tests.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Update to version 1.3.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-1
- Update to version 1.2.1.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-1
- Update to version 1.2.0.

* Mon Mar 13 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1.git697da80
- First package for Fedora

