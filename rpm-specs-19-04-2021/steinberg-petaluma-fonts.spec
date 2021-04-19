# Upstream has not yet tagged any releases, so build from git
%global commit            c7a3e8edba148915e5d1af8a5d4a50e5da4e0ea2
%global date              20190129
%global forgeurl          https://github.com/steinbergmedia/petaluma

# The Scripts font has a different version from the other two
%global petalumaver       1.055
%global petalumascriptver 1.10

Version:        %{petalumaver}
Release:        2%{?dist}
URL:            https://www.smufl.org/fonts/

%forgemeta

%global foundry          steinberg
%global fontlicense      OFL
%global fontlicenses     redist/OFL*.txt
%global fontdocs         README.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description %{expand:
Petaluma is a Unicode typeface designed by Steinberg for its Dorico music
notation and scoring application.  It is compliant with version 1.3 of
the Standard Music Font Layout (SMuFL), a community-driven standard for
how music symbols should be laid out in the Unicode Private Use Area
(PUA) in the Basic Multilingual Plane (BMP) for compatibility between
different scoring applications.}

%global fontfamily0      Petaluma
%global fontsummary0     Petaluma music font
%global fonts0           redist/otf/Petaluma.otf
%global fontconfs0       %{SOURCE1}
%global fontdescription0 %{expand:%{common_description}

This package contains the Petaluma font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

%global fontfamily1      PetalumaText
%global fontsummary1     Petaluma text font
%global fonts1           redist/otf/PetalumaText.otf
%global fontconfs1       %{SOURCE2}
%global fontdescription1 %{expand:%{common_description}

This package contains the Petaluma Text font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

%global fontfamily2      PetalumaScript
%global fontsummary2     Petaluma script font
%global fonts2           redist/otf/PetalumaScript.otf
%global fontconfs2       %{SOURCE3}
%global fontdescription2 %{expand:%{common_description}
%global fontpkgheader2   %{expand:
Version:        %{petalumascriptver}
}

This package contains the Petaluma Script font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

Source0:        %{forgesource}
Source1:        65-%{fontpkgname0}.conf
Source2:        65-%{fontpkgname1}.conf
Source3:        65-%{fontpkgname2}.conf

%fontpkg -a

# We cannot use %%fontmetapkg, because it doesn't know how to deal with a
# different version number for the Scripts font.
%package        all
Summary:        All the font packages generated from %{name}
Version:        %{petalumaver}
Requires:       %{name} = %{petalumaver}-%{release}
Requires:       steinberg-petalumatext-fonts = %{petalumaver}-%{release}
Requires:       steinberg-petalumascript-fonts = %{petalumascriptver}-%{release}

%description    all
This meta-package installs all the font packages generated from the
%{name} source package.

%prep
%forgesetup

%build
%fontbuild -a

%install
%fontinstall -a

# Install the SMuFL metadata
install -m 0644 -p redist/petaluma_metadata.json \
        %{buildroot}%{_fontdir}/metadata.json

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck -a
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%fontfiles -z 0
%{_fontdir}/metadata.json

%fontfiles -z 1

%fontfiles -z 2

%files          all

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.055-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Jerry James <loganjerry@gmail.com> - 1.055-1.20190129gitc7a3e8e
- Initial RPM
