%global common_configure --disable-unity --with-gnome-shell=3.30 --srcdir=..

%global common_desc							\
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and	\
Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments	\
like Gnome, Cinnamon, Budgie, Pantheon, XFCE, Mate, etc.


Name:		arc-theme
Version:	20210127
Release:	1%{?dist}
Summary:	Flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/jnsh/%{name}
Source0:	%{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:		support_xed.patch

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fdupes
BuildRequires:	gtk3-devel
BuildRequires:	gtk-murrine-engine
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	sassc
BuildRequires:	cinnamon
BuildRequires: make

Requires:	filesystem
Requires:	gnome-themes-standard
Requires:	gtk-murrine-engine

%description
%{common_desc}


%package plank
Summary:	Arc-theme for Plank dock

Requires:	%{name} == %{version}-%{release}

%if 0%{?fedora}
Requires:	plank
Supplements:	(%{name} and plank)
%endif

%description plank
%{common_desc}

This package contains the %{summary}.


%prep
%autosetup -p 1
%{_bindir}/autoreconf -fiv


%build
%{__mkdir} -p regular solid
pushd regular
%{__ln_s} -f ../configure configure
%configure %{common_configure}
popd

pushd solid
%{__ln_s} -f ../configure configure
%configure --disable-transparency %{common_configure}
popd

%make_build -C regular
%make_build -C solid


%install
%make_install -C regular
%make_install -C solid

# Install Plank-theme.
%{__mkdir} -p %{buildroot}/%{_datadir}/plank/themes/{Arc{,-solid},Arc-Lighter{,-solid},Arc-Darker{,-solid},Arc-Dark{,-solid}}
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Lighter/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Lighter/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Lighter-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Lighter-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Dark/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Dark/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Dark-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Dark-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Darker/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Darker/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Darker-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Darker-solid/

# cleanup plank theme files from main package
rm -fvr %{buildroot}/%{_datadir}/themes/{Arc{,-solid},Arc-Lighter{,-solid},Arc-Darker{,-solid},Arc-Dark{,-solid}}/plank

# Link duplicate files.
%fdupes -s %{buildroot}%{_datadir}


%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*

%files plank
%if 0%{?fedora}
%{_datadir}/plank/themes/*
%else
%{_datadir}/plank
%endif


%changelog
* Mon Feb 22 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 20210127-1
- Update to 20210127

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 20201013-1
- Update to 20201013
- Changed to new upstream

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181022-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181022-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 20181022-1
- New upstream release
- Adds recent support for newer gnome-shell and cinnamon versions

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170302-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170302-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Björn Esser <besser82@fedoraproject.org> - 20170302-8
- Remove Requires: plank on EPEL and properly own the directory

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 20170302-7
- Add several patches from upstream

* Mon Aug 28 2017 Björn Esser <besser82@fedoraproject.org> - 20170302-6
- Use Supplements on recent distros only

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170302-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Leigh Scott <leigh123linux@googlemail.com> - 20170302-4
- Add patch to fix OSD

* Sun May 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 20170302-3
- remove margin:auto as it's not supported

* Mon May 01 2017 Björn Esser <besser82@fedoraproject.org> - 20170302-2
- Add Supplements: (%%{name} and plank) for Plank-theme addon-package

* Fri Mar 03 2017 Björn Esser <besser82@fedoraproject.org> - 20170302-1
- New upstream release (rhbz#1428616)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161119-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Björn Esser <besser82@fedoraproject.org> - 20161119-3
- Build a 'solid'-version of the theme, too (rhbz#1415364)
- Symlink all duplicate files to save disk-space

* Sun Jan 29 2017 Björn Esser <besser82@fedoraproject.org> - 20161119-2
- Add Patch0: fix missing gradient warning

* Tue Jan 10 2017 Björn Esser <bjoern.esser@gmail.com> - 20161119-1
- Initial rpm-release (rhbz#1411438)

* Mon Jan 09 2017 Björn Esser <bjoern.esser@gmail.com> - 20161119-0.2
- Add plank-subpkg and require Plank (rhbz#1411438)

* Mon Jan 09 2017 Björn Esser <bjoern.esser@gmail.com> - 20161119-0.1
- Initial package (rhbz#1411438)
