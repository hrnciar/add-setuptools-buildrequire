# Generated by go2rpm
%bcond_without check

# https://github.com/paulrosania/go-charset
%global goipath         github.com/paulrosania/go-charset
%global commit          55c9d7a5834c4d034b34bf042103dbc646887f4f

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-paulrosania-go-charset-devel < 0-0.4
Obsoletes:      golang-github-paulrosania-go-charset-unit-test-devel < 0-0.4
}

%global common_description %{expand:
A fork of go-charset, which itself is a port of inferno's convcs for Go, which
supports conversion to and from UTF-8.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.9%{?dist}
Summary:        Character set conversion for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# Changes /usr/local/lib/go-charset/datafiles to /usr/share/go-charset/datafiles
Patch0:         charsetdir-fedora-fix.patch

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.5.20190703git55c9d7a
- Add Obsoletes for old name

* Tue May 28 16:04:16 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190703git55c9d7a
- Bump to commit 55c9d7a5834c4d034b34bf042103dbc646887f4f

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20151028git621bb39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20151028git621bb39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Jiri Kucera <jkucera@redhat.com> - 0-0.1.20151028git621bb39
- First package for Fedora
  this package is required by golang-github-elazarl-goproxy package, which is
  a dependency of bettercap 2.0.0 (resolves #1540726);
  patch charsetdir-fedora-fix.patch changes /usr/local/lib/go-charset/datafiles
  to /usr/share/go-charset/datafiles to met the Fedora Packaging Guidelines
  requirements;
  patch sprintf-fatalf-invalid-args-fix.patch fixes ill-formed format string
  in fmt.Sprintf (charset/ascii.go)  and  forgotten  t.Fatalf  arguments
  (charset/charset_test.go)
