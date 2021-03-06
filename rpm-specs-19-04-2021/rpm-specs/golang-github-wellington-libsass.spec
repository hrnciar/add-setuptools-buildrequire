# Generated by go2rpm
%bcond_without check

# https://github.com/wellington/go-libsass
%global goipath         github.com/wellington/go-libsass
Version:                0.9.2
%global commit          f870eaa15594bb64b1908df39d0812704f0ceb8f

%gometa

%global godevelheader %{expand:
Requires:       libsass-devel >= 3.5.4}

%global common_description %{expand:
Go wrapper for libsass, the only Sass 3.5 compiler for Go.}

%global golicenses      LICENSE
%global godocs          examples README.md docs

Name:           %{goname}
Release:        8%{?dist}
Summary:        Go wrapper for libsass, the only Sass 3.5 compiler for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  gcc-c++
BuildRequires:  libsass-devel >= 3.5.4

%description
%{common_description}

%gopkg

%prep
%goprep

# Remove bundled libsass.
rm -rf libsass-build
rm libs/wrap_main.go
for f in $(find -iname '*_dev.go'); do
    sed -e '/ +build dev/, 1d' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 15:41:42 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.2-4.20190528gitf870eaa
- Bump to commit f870eaa15594bb64b1908df39d0812704f0ceb8f

* Fri Jun 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.2-3
- Add gcc-c++ to Requires

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.2-2
- Remove unused file causing extra (auto) dependencies

* Sun Feb 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.2-1
- First package for Fedora
