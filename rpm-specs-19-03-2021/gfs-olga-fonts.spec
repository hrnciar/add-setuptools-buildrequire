# SPDX-License-Identifier: MIT
Version: 20160509
Release: 8%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Olga
%global fontsummary       GFS Olga, a 20th century oblique Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
In Greece the terms italic and oblique have the same meaning since they are
borrowed from the Latin typographic practice without any real historical
equivalent in Greek history. Until the end of the 19th century Greek typefaces
were cut and cast independently, not as members of a font family. The
mechanization of type cutting allowed the transformation of upright Greek
typefaces to oblique designs. Nonetheless, the typesetting practice of a
cursive Greek font to complement an upright one did not survive the 19th
century.

The experimental font GFS Olga (1995) attempts to revive this lost tradition.
The typeface was designed and digitized by George Matthiopoulos, based on the
historical Porson Greek type (1803) with the intention to be the companion of
the upright GFS Didot font whenever there is a need for an italic alternative.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

%fontmeta

%global source_files %{expand:
Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml
}

%fontpkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc *.pdf

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20160509-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20160509-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20160509-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20160509-3
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20160509-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20160509-1
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20060908-1
✅ Initial packaging
