# Generated by go2rpm
%bcond_without check
# lower memory usage on 32-bit
%ifarch armv7hl i686
%global gotestflags -short %{gotestflags}
%endif

# https://github.com/klauspost/compress
%global goipath         github.com/klauspost/compress
Version:                1.11.7

%gometa

%global common_description %{expand:
This package is based on an optimized Deflate function, which is used by
gzip/zip/zlib packages.

It offers slightly better compression at lower compression settings, and up to
3x faster encoding at highest compression level.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Optimized compression packages

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.11.7-1
- update to 1.11.7 (#1916508)

* Fri Jan  8 00:18:08 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.11.6-1
- Update to 1.11.6
- Close: rhbz#1913944

* Sun Jan  3 11:30:56 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.11.4-1
- Update to 1.11.4
- Close: rhbz#1909545

* Mon Nov 16 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.11.3-1
- update to 1.11.3 (#1897991)

* Mon Nov 02 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.11.2-1
- update to 1.11.2 (#1892279)

* Mon Oct 05 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.11.1-1
- update to 1.11.1 (#1884436)

* Thu Sep 10 2020 Dominik Mierzejewski <dominik@greysector.net> - 1.11.0-1
- update to 1.11.0 (#1876973)

* Wed Aug 19 2020 Dominik Mierzejewski <dominik@greysector.net> - 1.10.11-1
- update to 1.10.11 (#1868730)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Dominik Mierzejewski <dominik@greysector.net> - 1.10.10-1
- update to 1.10.10 (#1850299)

* Wed Jun 17 2020 Dominik Mierzejewski <dominik@greysector.net> - 1.10.9-1
- update to 1.10.9 (#1838747)

* Thu Apr 30 2020 Dominik Mierzejewski <dominik@greysector.net> - 1.10.5-1
- update to 1.10.5 (#1826957)

* Thu Apr 09 2020 Dominik Mierzejewski <dominik@greysector.net> - 1.10.4-1
- update to 1.10.4 (#1804486)

* Sun Feb 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.0-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Dominik Mierzejewski <dominik@greysector.net> - 1.9.4-1
- update to 1.9.4 (#1765428)
- drop upstream patch (merged)
- use upstream-suggested flags for gotest to lower memory usage

* Wed Dec 04 2019 Dominik Mierzejewski <dominik@greysector.net> - 1.9.3-1
- update to 1.9.3 (#1765428)
- fix failing test on i686

* Thu Oct 10 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.8.6-1
- Update to 1.8.6 (#1760526)

* Wed Oct 02 2019 Dominik Mierzejewski <dominik@greysector.net> - 1.8.5-1
- update to 1.8.5 (#1757636)
- drop obsolete patches

* Fri Sep 27 2019 Dominik Mierzejewski <dominik@greysector.net> - 1.8.4-1
- update to 1.8.4 (#1742049)
- backport upstream patch for 32-bit arches
- increase zstd encoder_test timeout (times out on ARM)

* Wed Jul 24 23:24:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.2-1
- Release 1.7.2

* Mon Apr 29 01:02:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.0-1
- Release 1.7.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.2.1-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 11 2018 Dominik Mierzejewski <dominik@greysector.net> - 1.2.1-2
- fix end-of-line encoding in README.md
- build as archful due to assembly usage on x86_64

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 1.2.1-1
- initial package for Fedora