# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%bcond_without ikiwiki

Name:           git-annex
Version:        8.20210223
Release:        1%{?dist}
Summary:        Manage files with git, without checking their contents into git

License:        AGPLv3+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources
# These are missing from tarball, as it's a bit minimal.
Source2:        bash-completion.bash
Source3:        index.mdwn
Patch0:         %{name}-default-flags.patch

BuildRequires:  bash-completion
# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-DAV-static >= 1.0
BuildRequires:  ghc-IfElse-static
BuildRequires:  ghc-QuickCheck-static >= 2.8.2
BuildRequires:  ghc-SafeSemaphore-static
BuildRequires:  ghc-aeson-static
BuildRequires:  ghc-async-static
BuildRequires:  ghc-attoparsec-static
BuildRequires:  ghc-aws-static >= 0.9.2
BuildRequires:  ghc-base-static
BuildRequires:  ghc-blaze-builder-static
BuildRequires:  ghc-bloomfilter-static
BuildRequires:  ghc-byteable-static
BuildRequires:  ghc-bytestring-static
BuildRequires:  ghc-case-insensitive-static
BuildRequires:  ghc-clientsession-static
BuildRequires:  ghc-concurrent-output-static >= 1.6
BuildRequires:  ghc-conduit-static
BuildRequires:  ghc-connection-static
BuildRequires:  ghc-containers-static >= 0.5.7.1
BuildRequires:  ghc-crypto-api-static
BuildRequires:  ghc-cryptonite-static
BuildRequires:  ghc-data-default-static
BuildRequires:  ghc-dbus-static >= 0.10.7
BuildRequires:  ghc-deepseq-static
BuildRequires:  ghc-directory-static >= 1.2
BuildRequires:  ghc-disk-free-space-static
BuildRequires:  ghc-dlist-static
BuildRequires:  ghc-edit-distance-static
BuildRequires:  ghc-exceptions-static >= 0.6
BuildRequires:  ghc-fdo-notify-static
BuildRequires:  ghc-feed-static >= 0.3.9
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-filepath-bytestring-static
BuildRequires:  ghc-free-static
BuildRequires:  ghc-git-lfs-static
BuildRequires:  ghc-hinotify-static
BuildRequires:  ghc-hslogger-static
BuildRequires:  ghc-http-client-static
BuildRequires:  ghc-http-client-restricted-static
BuildRequires:  ghc-http-client-tls-static
BuildRequires:  ghc-http-conduit-static >= 2.0
BuildRequires:  ghc-http-types-static >= 0.7
BuildRequires:  ghc-magic-static
BuildRequires:  ghc-memory-static
BuildRequires:  ghc-microlens-static
BuildRequires:  ghc-monad-control-static
BuildRequires:  ghc-monad-logger-static
BuildRequires:  ghc-mountpoints-static
BuildRequires:  ghc-mtl-static >= 2
BuildRequires:  ghc-network-static >= 2.6
BuildRequires:  ghc-network-bsd-static
BuildRequires:  ghc-network-info-static
BuildRequires:  ghc-network-multicast-static
BuildRequires:  ghc-network-uri-static >= 2.6
BuildRequires:  ghc-old-locale-static
BuildRequires:  ghc-optparse-applicative-static >= 0.11.0
BuildRequires:  ghc-path-pieces-static >= 0.2.1
BuildRequires:  ghc-persistent-static
BuildRequires:  ghc-persistent-sqlite-static >= 2.1.3
BuildRequires:  ghc-persistent-template-static
BuildRequires:  ghc-process-static
BuildRequires:  ghc-random-static
BuildRequires:  ghc-regex-tdfa-static
BuildRequires:  ghc-resourcet-static
BuildRequires:  ghc-sandi-static
BuildRequires:  ghc-securemem-static
BuildRequires:  ghc-shakespeare-static >= 2.0.11
BuildRequires:  ghc-socks-static
BuildRequires:  ghc-split-static
BuildRequires:  ghc-stm-static
BuildRequires:  ghc-stm-chans-static
BuildRequires:  ghc-tagsoup-static
BuildRequires:  ghc-tasty-static >= 0.7
BuildRequires:  ghc-tasty-hunit-static
BuildRequires:  ghc-tasty-quickcheck-static
BuildRequires:  ghc-tasty-rerun-static
BuildRequires:  ghc-template-haskell-static
BuildRequires:  ghc-text-static
BuildRequires:  ghc-time-static
BuildRequires:  ghc-torrent-static >= 10000.0.0
BuildRequires:  ghc-transformers-static
BuildRequires:  ghc-unix-static
BuildRequires:  ghc-unix-compat-static
BuildRequires:  ghc-unliftio-core-static
BuildRequires:  ghc-unordered-containers-static
BuildRequires:  ghc-utf8-string-static
BuildRequires:  ghc-uuid-static >= 1.2.6
BuildRequires:  ghc-vector-static
BuildRequires:  ghc-wai-static
BuildRequires:  ghc-wai-extra-static
BuildRequires:  ghc-warp-static >= 3.2.8
BuildRequires:  ghc-warp-tls-static >= 3.2.2
BuildRequires:  ghc-yesod-devel >= 1.4.3
BuildRequires:  ghc-yesod-core-static >= 1.4.25
BuildRequires:  ghc-yesod-form-static >= 1.4.8
BuildRequires:  ghc-yesod-static-static >= 1.5.1
# End cabal-rpm deps
BuildRequires:  git
BuildRequires:  rsync
%if %{with ikiwiki}
BuildRequires:  ikiwiki
BuildRequires:  perl(Image::Magick)
%endif

# XXX: feature flag dependencies:
#Benchmark:
#  BuildRequires:  ghc-criterion-devel (unpackaged)
#  BuildRequires:  ghc-deepseq-devel

Requires:       git

%description
Git-annex allows managing files with git, without checking the file contents
into git. While that may seem paradoxical, it is useful when dealing with files
larger than git can currently easily handle, whether due to limitations in
memory, time, or disk space.

It can store large files in many places, from local hard drives, to a large
number of cloud storage services, including S3, WebDAV, and rsync, with a dozen
cloud storage providers usable via plugins. Files can be stored encrypted with
gpg, so that the cloud storage provider cannot see your data.
git-annex keeps track of where each file is stored, so it knows how many copies
are available, and has many facilities to ensure your data is preserved.

git-annex can also be used to keep a folder in sync between computers, noticing
when files are changed, and automatically committing them to git and
transferring them to other computers. The git-annex webapp makes it easy to set
up and use git-annex this way.

%if %{with ikiwiki}
%package docs
Summary:        %{summary}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name} in HTML format.
%endif


%prep
%autosetup -p1

cabal-tweak-drop-dep yesod-default
# https://bugzilla.redhat.com/show_bug.cgi?id=1907246
%ifarch armv7hl
cabal-tweak-flag Webapp False
%endif
cp %SOURCE2 .
cp %SOURCE3 doc/


%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build

LC_ALL=C TZ=UTC ikiwiki doc html -v --wikiname git-annex \
    --plugin=goodstuff \
    --no-usedirs --disable-plugin=openid --plugin=sidebar \
    --underlaydir=/dev/null --set deterministic=1 \
    --disable-plugin=shortcut --disable-plugin=smiley \
    --plugin=comments --set comments_pagespec="*" \
    --exclude='news/.*' --exclude='design/assistant/blog/*' \
    --exclude='bugs/*' --exclude='todo/*' --exclude='forum/*' \
    --exclude='users/*' --exclude='devblog/*' --exclude='thanks'


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install

bash_completion_dir=%{buildroot}$(pkg-config --variable=completionsdir bash-completion)
mkdir -p $bash_completion_dir
install -m 644 bash-completion.bash $bash_completion_dir/git-annex


%check
mkdir test
pushd test
PATH=%{buildroot}%{_bindir}:$PATH \
    git annex test
popd


%files
%license doc/license/AGPL doc/license/GPL
# Begin cabal-rpm files:
%license COPYRIGHT
%doc CHANGELOG NEWS README
%{_bindir}/%{name}
# End cabal-rpm files
%{_bindir}/%{name}-shell
%{_bindir}/git-remote-tor-annex
%{_mandir}/man1/git-annex*
%{_mandir}/man1/git-remote-tor-annex*
%{_datadir}/bash-completion/

%if %{with ikiwiki}
%files docs
%license COPYRIGHT doc/license/AGPL doc/license/GPL
%doc html/
%endif


%changelog
* Thu Feb 25 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20210223-1
- update to 8.20210223

* Mon Feb  1 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20210127-1
- update to 8.20210127

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.20201129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20201129-1
- update to 8.20201129

* Mon Dec 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20201127-1
- update to 8.20201127
- Disable Webapp on armv7hl

* Fri Sep 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20200908-1
- update to 8.20200908

* Tue Sep 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20200810-1
- update to 8.20200810

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20200617-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20200617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Jens Petersen <petersen@redhat.com> - 8.20200617-1
- update to 8.20200617

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 8.20200522-1
- update to 8.20200522

* Sun May 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20200501-1
- update to 8.20200501

* Tue Mar 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20200330-1
- update to 8.20200330

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20200309-1
- update to 8.20200309

* Tue Mar 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.20200226-1
- update to 8.20200226

* Sat Feb 15 2020 Jens Petersen <petersen@redhat.com> - 7.20200204-1
- https://hackage.haskell.org/package/git-annex-7.20200204/changelog
- filepath-bytestring was packaged

* Sun Feb 02 2020 Jens Petersen <petersen@redhat.com> - 7.20191230-1
- update to 7.20191230
- refresh to cabal-rpm-2.0.2

* Sat Feb  1 2020 Jens Petersen <petersen@redhat.com> - 7.20191114-3
- fix FTBFS on armv7hl using non-Production build (#1797176)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.20191114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20191114-1
- update to 7.20191114

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20191106-1
- update to 7.20191106

* Sat Oct 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20191024-1
- update to 7.20191024

* Fri Oct 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20191017-1
- update to 7.20191017

* Wed Oct 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20191009-1
- update to 7.20191009

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190912-1
- update to 7.20190912

* Fri Aug 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190819-1
- update to 7.20190819

* Fri Aug 09 2019 Jens Petersen <petersen@redhat.com> - 7.20190730-1
- update to 7.20190730

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 7.20190708-3
- rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.20190708-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190708-1
- update to 7.20190708

* Wed Jun 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190626-1
- update to 7.20190626

* Sun Jun 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190615-1
- update to 7.20190615

* Wed May 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190507-1
- update to 7.20190507

* Sun May 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190503-1
- update to 7.20190503

* Thu Mar 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190322-1
- update to 7.20190322

* Wed Feb 27 2019 Jens Petersen <petersen@redhat.com> - 7.20190219-2
- rebuild

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190219-1
- update to 7.20190219

* Wed Feb 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.20190129-1
- update to 7.20190129

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.20181011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20181011-1
- update to 6.20181011

* Tue Oct 23 2018 Jens Petersen <petersen@redhat.com> - 6.20180913-2
- rebuild for static executable

* Thu Sep 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20180913-1
- update to 6.20180913

* Sat Aug 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20180807-1
- update to 6.20180807

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 6.20180719-1
- update to 6.20180719

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.20180626-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20180626-1
- update to 6.20180626
- Fix CVE-2018-10857 and CVE-2018-10859 (#1595634)

* Fri Apr 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20180409-1
- update to 6.20180409

* Fri Apr 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20180316-1
- update to 6.20180316

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.20180112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20180112-1
- Update to latest version.

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 6.20171214-1
- update to 6.20171214

* Thu Nov 30 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20171124-1
- Update to latest version.

* Tue Nov 28 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-6.fc27
- Enable S3 support.
- Enable WebDAV support.

* Wed Nov 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-8.fc28
- Enable TestSuite.

* Fri Nov 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-7.fc28
- Enable Webapp and Pairing support.

* Wed Nov 15 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-6.fc28
- Enable S3 support.

* Wed Nov 15 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-5.fc27
- Add minimum versions to dependencies.
- Enable use of concurrent-output library.
- Enable use of libmagic for file identification.
- Enable TorrentParser for parsing torrents.

* Wed Nov 15 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-5.fc28
- Add minimum versions to dependencies.
- Enable use of concurrent-output library.
- Enable use of libmagic for file identification.
- Enable TorrentParser for parsing torrents.
- Enable WebDAV support.

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-4
- rebuilt

* Sat Nov 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-3
- rebuilt

* Mon Oct 23 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.20170925-2
- rebuilt

* Fri Sep 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 6.20170925-1
- Update to 6.20170925.
- Add rsync BuildRequires.
- Fix documentation packaging.
- Add and install bash-completion.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.20140717-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.20140717-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.20140717-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Jens Petersen <petersen@redhat.com> - 5.20140717-12
- need network-uri
- patch for ambiguous createPipe in Utility.Process
- patch for ambiguous defaultTimeLocale
- disable quvi and tahoe for build with ghc8

* Tue Mar  8 2016 Jens Petersen <petersen@redhat.com> - 5.20140717-11
- rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.20140717-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 08 2015 Ben Boeckel <mathstuf@gmail.com> - 5.20140717-8
- rebuild for ghc-edit-distance and ghc-bloomfilter

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.20140717-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Richard W.M. Jones <rjones@redhat.com> - 5.20140717-6
- Bump release and rebuild because of ghc-dbus dependency.

* Thu Mar  5 2015 Jens Petersen <petersen@redhat.com> - 5.20140717-5
- rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@redhat.com> - 5.20140717-4
- cblrpm refresh

* Fri Sep  5 2014 Jens Petersen <petersen@redhat.com> - 5.20140717-3
- rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.20140717-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Ben Boeckel <mathstuf@gmail.com> - 5.20140717-1
- Update to 5.20140717
- disable DesktopNotify until fdo-notify packaged

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.20140221-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Ben Boeckel <mathstuf@gmail.com> - 5.20140221-2
- Rebuild for dbus rebuild

* Tue Feb 25 2014 Jens Petersen <petersen@redhat.com> - 5.20140221-1
- update to 5.20140221
- BR cryptohash

* Fri Feb 07 2014 Jens Petersen <petersen@redhat.com> - 5.20140116-1
- update to 5.20140116

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 5.20140108-2
- rebuild

* Tue Jan 14 2014 Jens Petersen <petersen@redhat.com> - 5.20140108-1
- update to 5.20140108

* Tue Jan 14 2014 Jens Petersen <petersen@redhat.com> - 4.20130827-2
- enable dbus

* Wed Sep 04 2013 Jens Petersen <petersen@redhat.com> - 4.20130827-1
- update to 4.20130827
- update deps and default flags
- build with regex-tdfa

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20130207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Jens Petersen <petersen@redhat.com> - 3.20130207-1
- update to 3.20130207
- requires SafeSemaphore

* Thu Jun  6 2013 Jens Petersen <petersen@redhat.com> - 3.20121009-5
- IfElse is now in Fedora

* Fri Mar 22 2013 Jens Petersen <petersen@redhat.com> - 3.20121009-4
- rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20121009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Jens Petersen <petersen@redhat.com> - 3.20121009-2
- create manpages when no ikiwiki

* Tue Nov 06 2012 Jens Petersen <petersen@redhat.com> - 3.20121009-1
- update to 3.20121009

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20120615-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Jens Petersen <petersen@redhat.com> - 3.20120615-2
- fix doc file symlinks
- BR ImageMagick-perl
- make docs subpackage noarch

* Sat Jun 23 2012 Ben Boeckel <mathstuf@gmail.com> - 3.20120615-1
- Update to 3.20120615

* Tue May 22 2012 Jens Petersen <petersen@redhat.com> - 3.20120522-1
- create git-annex-shell symlink
- build and include manpages and docs in a subpackage

* Sat Apr 21 2012 Ben Boeckel <mathstuf@gmail.com> - 3.20120418-1
- Update to 3.20120418

* Fri Mar 02 2012 Ben Boeckel <mathstuf@gmail.com> - 3.20120229-1
- Update to 3.20120229

* Fri Mar  2 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4
