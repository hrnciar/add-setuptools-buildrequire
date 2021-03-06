Version: 1.00
Release: 8%{?dist}
URL:     https://www.businesswire.com/news/home/20100608005491/en/Monotype-Imaging-Contributes-Simplified-Chinese-Font-%E2%80%9CMYuppy%E2%80%9D

%global foundry           Symbian
%global fontlicense       EPL-1.0

%global fontlicenses      *.TXT

%global fontfamily        M Yuppy GB
%global fontsummary       M Yuppy GB, a Chinese font family with a unique, modern feel
%global fonts             %{SOURCE0}
%global fontconfngs       %{SOURCE2}

%global fontdescription   %{expand:
Designed to appeal to young urban professionals, M Yuppy is a font family with
a unique, modern feel. The design combines elements of handwriting with classic
letter-form characteristics, such as open shapes and proper proportions that
help the typeface retain legibility.}

%fontmeta

%global source_files %{expand:
Source0: https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium.ttf
Source1: https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium_README.TXT
Source2: 65-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q -c -T
cp %{SOURCE1} .
%linuxtext *TXT

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-1
✅ Initial packaging
