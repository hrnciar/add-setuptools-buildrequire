%{?drupal7_find_provides_and_requires}

%global module link

Name:          drupal7-%{module}
Version:       1.7
Release:       5%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Defines simple link field types

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# link.info
#     <none>
# phpcompatinfo (computed from version 1.7)
#     <none>

%description
The link module can be count to the top 50 modules in Drupal installations and
provides a standard custom content field for links. With this module links can
be added easily to any content types and profiles and include advanced
validating and different ways of storing internal or external links and URLs.
It also supports additional link text title, site wide tokens for titles and
title attributes, target attributes, CSS class attribution, static repeating
values, input conversion, and many more.

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7-3
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7-1
- Update to 1.7 (RHBZ #1772459)
- Add .info file to repo

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6-1
- Update to 1.6 (RHBZ #1547794 / SA-CONTRIB-2019-020 / SA-CORE-2019-003)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.4.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.2.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5-0.1.beta2
- Updated to 1.5-beta2 (RHBZ #1475049)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 31 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4-1
- Updated to 1.4 (BZ #1298909)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3-1
- Updated to 1.3 (BZ #1155470)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Peter Borsa <peter.borsa@gmail.com> - 1.2-1
- Update to upstream 1.2 release for bugfixes
- Upstream changelog for this release is available at https://drupal.org/node/2143271

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-2
- Updated for drupal7-rpmbuild 7.22-5

* Mon Apr 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1
- Initial package
