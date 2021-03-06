%global git0 https://github.com/rootless-containers/%{name}
%global commit0 b156cc57195f05c4ffbde7e87b5d774d3d592cec
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Used for comparing with latest upstream tag
# to decide whether to autobuild and set download_url (non-rawhide only)
%define built_tag v1.1.9
%define built_tag_strip %(b=%{built_tag}; echo ${b:1})
%define download_url %{git0}/archive/%{built_tag}.tar.gz

Name: slirp4netns
Version: 1.1.9
Release: 1.dev.git%{shortcommit0}%{?dist}
# no go-md2man in ppc64
ExcludeArch: ppc64
Summary: slirp for network namespaces
License: GPLv2
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: git
BuildRequires: go-md2man
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: libslirp-devel
BuildRequires: make

%description
slirp for network namespaces, without copying buffers across the namespaces.

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%autosetup -Sgit -n %{name}-%{commit0}

%build
./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make} generate-man

%install
make DESTDIR=%{buildroot} install install-man

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon Mar 01 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.9-1.dev.gitb156cc5
- built commit b156cc5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3.dev.git6dc0186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.8-2.dev.git6dc0186
- bump to 1.1.8
- autobuilt 6dc0186

* Wed Nov 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.7-3.dev.git0bac994
- autobuilt 0bac994

* Wed Nov 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.7-2.dev.gitf266258
- bump to 1.1.7
- autobuilt f266258

* Wed Nov 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.6-6.dev.gitd0a8cf1
- autobuilt d0a8cf1

* Wed Nov 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.6-5.dev.git7ed048f
- autobuilt 7ed048f

* Wed Nov 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.6-4.dev.gite2e4eea
- autobuilt e2e4eea

* Wed Nov 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.6-3.dev.git4bce8d8
- autobuilt 4bce8d8

* Thu Nov  5 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.6-2.dev.git13ac4c2
- bump to 1.1.6
- autobuilt 13ac4c2

* Sat Oct  3 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.4-7.dev.git6767922
- autobuilt 6767922

* Tue Sep 29 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.4-6.dev.giteecccdb
- bump release tag

* Tue Sep 29 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.4-5.dev.giteecccdb
- bump release tag

* Tue Aug 04 08:10:13 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.4-4.dev.giteecccdb
- autobuilt eecccdb

* Tue Jul 28 06:09:58 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.4-3.dev.git6d002ad
- autobuilt 6d002ad

* Mon Jul 13 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.4-2.dev.git4c6befe
- bump to 1.1.4
- autobuilt 4c6befe

* Thu Jul 09 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.3-2.dev.git23ce219
- bump to 1.1.3
- autobuilt 23ce219

* Tue Jul 07 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.2-3.dev.git8bf8338
- autobuilt 8bf8338

* Mon Jul 06 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.2-2.dev.git4a30e56
- bump to 1.1.2
- autobuilt 4a30e56

* Fri Jul 03 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.1-6.dev.gitdd4af4f
- autobuilt dd4af4f

* Sun Jun 14 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.1-5.dev.git99e1516
- autobuilt 99e1516

* Fri Jun 12 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.1-4.dev.gita32a0d0
- autobuilt a32a0d0

* Mon Jun 08 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.1-3.dev.gitfcda5d9
- autobuilt fcda5d9

* Fri Jun 05 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.1-2.dev.git483e855
- bump to 1.1.1
- autobuilt 483e855

* Thu Jun 04 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.0-5.dev.git94bd97d
- autobuilt 94bd97d

* Wed May 27 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.0-4.dev.gitc2c87b9
- autobuilt c2c87b9

* Tue May 19 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.0-3.dev.git56941dd
- autobuilt 56941dd

* Sat May 16 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.1.0-2.dev.git3caa737
- bump to 1.1.0
- autobuilt 3caa737

* Tue May 05 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.1-3.dev.gitce56e0c
- autobuilt ce56e0c

* Fri Apr 24 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.1-2.dev.git4367de7
- bump to 1.0.1
- autobuilt 4367de7

* Tue Mar 31 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-9.0.dev.gitc48f4d7
- autobuilt c48f4d7

* Tue Mar 31 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-8.0.dev.gitbdcd9a7
- autobuilt bdcd9a7

* Mon Mar 30 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-7.0.dev.gitc0fef8d
- autobuilt c0fef8d

* Mon Mar 30 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-6.0.dev.gitcac9a34
- autobuilt cac9a34

* Wed Mar 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-5.0.dev.git4353fab
- autobuilt 4353fab

* Wed Mar 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-4.0.dev.gitb797921
- autobuilt b797921

* Tue Mar 24 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-3.0.dev.git38334c4
- autobuilt 38334c4

* Thu Mar 19 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 1.0.0-2.0.dev.git735fcd7
- bump to 1.0.0
- autobuilt 735fcd7

* Wed Mar 18 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.3-8.0.dev.git7560ba4
- autobuilt 7560ba4

* Tue Mar 17 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.3-7.0.dev.git7ba0c6f
- autobuilt 7ba0c6f

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6.0.dev.gita8414d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.3-5.0.dev.gita8414d1
- autobuilt a8414d1

* Wed Dec 18 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.3-4.0.dev.gite6b31fe
- autobuilt e6b31fe

* Fri Dec 13 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.3-3.0.dev.gitdad442a
- autobuilt dad442a

* Thu Dec 12 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.3-2.0.dev.gite14da48
- bump to 0.4.3
- autobuilt e14da48

* Wed Dec 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.2-6.0.dev.git1fea75f
- autobuilt 1fea75f

* Thu Nov 21 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.2-5.0.dev.git21fdece
- autobuilt 21fdece

* Mon Nov 04 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.2-4.0.dev.git0186bac
- autobuilt 0186bac

* Thu Oct 31 2019 Jindrich Novy <jnovy@redhat.com> - 0.4.2-3.0.dev.git3527c98
- add BR: libseccomp-devel

* Fri Oct 18 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.2-2.0.dev.git3527c98
- bump to 0.4.2
- autobuilt 3527c98

* Wed Oct 02 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.4.1-3.0.dev.gite8759b9
- autobuilt e8759b9

* Fri Aug 30 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.1-2.0.dev.gitf9503fe
- bump to 0.4.1
- autobuilt f9503fe

* Fri Aug 30 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-25.1.dev.gitd2e449b
- autobuilt d2e449b

* Thu Aug 29 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-24.1.dev.git1a96e26
- autobuilt 1a96e26

* Sun Aug 25 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-23.1.dev.git29db6bd
- autobuilt 29db6bd

* Fri Aug 23 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-22.1.dev.git4e51172
- autobuilt 4e51172

* Wed Aug 21 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-21.1.dev.git56c8370
- autobuilt 56c8370

* Sun Aug 04 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-20.1.dev.gitbbd6f25
- autobuilt bbd6f25

* Thu Aug 01 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-19.1.dev.gited51817
- autobuilt ed51817

* Tue Jul 30 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-18.1.dev.gitaacef69
- autobuilt aacef69

* Tue Jul 30 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-17.1.dev.git1dfc6f6
- autobuilt 1dfc6f6

* Sun Jul 28 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-16.1.dev.git96ff33c
- autobuilt 96ff33c

* Sat Jul 27 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-15.1.dev.gitb911c9a
- autobuilt b911c9a

* Sat Jul 27 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-14.1.dev.gitd23723e
- autobuilt d23723e

* Fri Jul 26 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-13.1.dev.git10c0ee5
- autobuilt 10c0ee5

* Thu Jul 25 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-12.1.dev.git87a4bf7
- autobuilt 87a4bf7

* Wed Jul 24 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-11.1.dev.git85efff0
- autobuilt 85efff0

* Wed Jul 24 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-10.1.dev.git4f5a083
- autobuilt 4f5a083

* Tue Jul 23 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.4.0-9.1.dev.git62cbdd3
- bump to 0.4.0
- autobuilt 62cbdd3

* Tue Jul 23 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.3.0-8.1.dev.gitbf199bb
- autobuilt bf199bb

* Thu Jul 18 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.3.0-7.1.dev.git2f857ec
- autobuilt 5c690f7
- autobuilt 2f857ec

* Thu Jul 18 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.3.0-6.1.dev.gitd34e916
- autobuilt 5c690f7
- autobuilt d34e916

* Thu Jul 18 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.3.0-5.1.dev.git6612517
- autobuilt 5c690f7
- autobuilt 6612517

* Thu Jul 18 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.3.0-4.1.dev.gitf34ad90
- autobuilt 5c690f7
- autobuilt f34ad90

* Sun Jul 14 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.3.0-3.1.dev.git5c690f7
- autobuilt 5c690f7

* Wed Jul 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.3.0-2.1.dev.git4889f52
- built 4889f52
- hook up to autobuild

* Wed May 15 2019 Dan Walsh <dwalsh@fedoraproject.org> - v0.3.0-2
- Update to released version

* Wed Feb 27 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.3.0-1.alpha.2
- make version tag consistent with upstream

* Sun Feb 17 2019 Dan Walsh <dwalsh@fedoraproject.org> - v0.3.0-alpha.2
- Latest release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3.dev.git0037042
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-2.dev.git0037042
- built 0037042

* Fri Jul 27 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-1.dev.gitc4e1bc5
- Resolves: #1609595 - initial upload
- First package for Fedora
