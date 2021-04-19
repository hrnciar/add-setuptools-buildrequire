# Generated by go2rpm
%bcond_without check

# https://github.com/rwcarlsen/goexif
%global goipath         github.com/rwcarlsen/goexif
%global commit          9e8deecbddbd4989a3e8d003684b783412b41e7a

%gometa

%global common_description %{expand:
This package provides decoding of basic exif and tiff encoded data.}

%global golicenses      LICENSE
%global godocs          README.md README-exif.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Decode embedded EXIF meta data from image files

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
mv exif/README.md README-exif.md

%build
for cmd in exif exifstat; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mv %{gobuilddir}/bin/exif %{gobuilddir}/bin/goexif
mv %{gobuilddir}/bin/exifstat %{gobuilddir}/bin/goexifstat

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
%doc README.md README-exif.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20191017git9e8deec
- Update to latest commit

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190626git41dad3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 22:27:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git41dad3a
- Initial package
