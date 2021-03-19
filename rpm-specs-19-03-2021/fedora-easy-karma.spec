Name:           fedora-easy-karma
Version:        0
Release:        0.46.20200427git6fc0f39%{?dist}
Summary:        Fedora update feedback made easy
License:        GPLv2+
URL:            https://fedoraproject.org/wiki/Fedora_Easy_Karma

# git clone https://pagure.io/fedora-easy-karma.git
# cd fedora-easy-karma
# git rev-parse --short HEAD
# git checkout 56f1e97
# git archive --format=tar.gz --prefix=fedora-easy-karma-56f1e97/ HEAD > \
#     ../fedora-easy-karma-56f1e97.tar.gz
Source0:        fedora-easy-karma-6fc0f39.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires: make

Requires:       python3-bodhi-client
Requires:       python3-dnf
Requires:       python3-fedora


%description
Fedora-easy-karma helps you to easily and fast provide feedback for all testing
updates that you have currently installed.


%prep
%autosetup -p1 -n fedora-easy-karma-6fc0f39
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" fedora-easy-karma.py
sed -i 's,useragent="Fedora Easy Karma/GIT",useragent="Fedora Easy Karma/%{version}-%{release}",' fedora-easy-karma.py


%install
%make_install prefix=%{_prefix}


%files
%license gpl-2.0.txt gpl-3.0.txt
%doc README.md
%{_bindir}/fedora-easy-karma


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.46.20200427git6fc0f39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.45.20200427git6fc0f39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 0-0.44.20200427git6fc0f39
- Fix wrong password handling (RHBZ#1818453)
- Support for oraculum endpoint

* Tue Mar 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 0-0.43.20191206git56f1e97
- Proper Bodhi 4 Support
- Legacy code cleanup (drop yum, py2 and old bodhi support)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.43.20181206gitb6d97e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.42.20181206gitb6d97e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.41.20181206gitb6d97e0
- Apply workarounds from pull requests

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.40.20181206gitb6d97e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.39.20181206gitb6d97e0
- Switch to Python 3 (#1650648)

* Thu Aug 09 2018 Till Maas <opensource@till.name> - 0-0.38.20171129gita8fe9cbc
- Update Bodhi dependency for Fedora 29 and newer

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.37.20171129gita8fe9cbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.20171129gita8fe9cbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Till Maas <opensource@till.name> - 0-0.35.20171129gita8fe9cbc
- Update to new release to limit number of updates requested from Bodhi to 25

* Thu Oct 19 2017 Till Maas <opensource@till.name> - 0-0.34.20171019gitbc16e916
- Update to new release to limit number of updates requested from Bodhi

* Sat Sep 30 2017 Till Maas <opensource@till.name> - 0-0.33.20170930git0c81432c
- Depend on python2-fedora

* Sat Sep 30 2017 Till Maas <opensource@till.name> - 0-0.32.20170930git0c81432c
- Add hard dependencies on dnf or yum (#1270600)
- Use bodhi bindings if available (#1494644)
- Update to new pagure upstream
- Adjust dependencies
- Cleanup spec file

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20160408gitb5cdbc7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20160408gitb5cdbc7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 08 2016 Till Maas <opensource@till.name> - 0-0.29.20160408gitb5cdbc7f
- Update to recent snapshot to fix support on RHEL

* Thu Mar 24 2016 Till Maas <opensource@till.name> - 0-0.28.20150921gitc932687a
- Add python2-dnf recommendation for F23 and newer (https://bugzilla.redhat.com/show_bug.cgi?id=1270600)
- Use https in comments

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20150921gitc932687a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Till Maas <opensource@till.name> - 0-0.26.20150921gitc932687a
- Update to new snapshot with Bodhi2 support (Red Hat Bugzilla #1255452)
- Drop yum dependency (Red Hat Bugzilla #1249303)
- Use %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.25.20150508gitc8e437c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Till Maas <opensource@till.name> - 0-0.25.20150508gitc8e437c0
- Update to new snapshot

* Fri Sep 05 2014 Till Maas <opensource@till.name> - 0-0.23.20140905git5fb5b77a
- Update to new snapshot

* Sun Aug 31 2014 Till Maas <opensource@till.name> - 0-0.22.20140831git1ae921a8
- Update to new snapshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.21.20130707git121694f6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.20.20130707git121694f6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Till Maas <opensource@till.name> - 0-0.19.20130707git121694f6
- Update to new snapshot

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.18.20110825git36efb338
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.17.20110825git36efb338
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.16.20110825git36efb338
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Till Maas <opensource@till.name> - 0-0.15.20110825git36efb338
- Update to new release

* Wed Aug 24 2011 Till Maas <opensource@till.name> - 0-0.14.20110824gitb3e2f900
- Update to new release

* Tue Aug 23 2011 Till Maas <opensource@till.name> - 0-0.13.20110823gitb0706146
- Update to new release
- Fix Red Hat Bug #732610

* Fri Aug 19 2011 Till Maas <opensource@till.name> - 0-0.12.20110819gitadba3055
- Update to new release
- Fix Red Hat Bug #718446

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20101123gitf70e9b6d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Till Maas <opensource@till.name> - 0-0.10.20101123gitf70e9b6d
- Add accidentally removed distag

* Tue Nov 23 2010 Till Maas <opensource@till.name> - 0-0.9.20101123gitf70e9b6d
- Update to new snapshot
- Fix Red Hat Bug #656273

* Mon Nov 22 2010 Till Maas <opensource@till.name> - 0-0.8.20101122git07665f93.1
- Reduce dependencies: fedora-cert is now a separate package

* Mon Nov 22 2010 Till Maas <opensource@till.name> - 0-0.8.20101122git07665f93
- Update to new snapshot
- Fix Red Hat Bug #637349

* Fri Jul 09 2010 Till Maas <opensource@till.name> - 0-0.7.20100709git561718c8
- Update to new snapshot

* Tue Jun 29 2010 Till Maas <opensource@till.name> - 0-0.6.20100629git0e80f096
- Update to new snapshot

* Mon Mar 15 2010 Till Maas <opensource@till.name> - 0-0.5.20100315gitacf8b834
- Update to new snapshot

* Mon Mar 08 2010 Till Maas <opensource@till.name> - 0-0.4.20100308git1d2e3a85
- Update to new snapshot
- Set useragent

* Sat Mar 06 2010 Till Maas <opensource@till.name> - 0-0.3.20100306git00fc20aa
- Use short githash
- Update to new snapshot

* Sat Mar 06 2010 Till Maas <opensource@till.name> - 0-0.2.20100306git668cdcf9a6c7effd2b9e3394f207b71aa1395983
- Use fedpkg-vcs to manage snapshots
- Update to new snapshot

* Fri Mar 05 2010 Till Maas <opensource@till.name> - 0-0.1.20100305
- initial spec for Fedora
