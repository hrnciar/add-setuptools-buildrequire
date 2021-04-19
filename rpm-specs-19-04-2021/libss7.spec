Name:           libss7
Version:        2.0.0
Release:        7%{?dist}
%global so_version 2
Summary:        SS7 protocol services to applications

License:        GPLv2
URL:            https://www.asterisk.org/
%global src_base https://downloads.asterisk.org/pub/telephony/%{name}/releases
Source0:        %{src_base}/%{name}-%{version}.tar.gz
Source1:        %{src_base}/%{name}-%{version}.tar.gz.asc
# Keyring with developer signatures created on 2021-02-23 with:
#   workdir="$(mktemp --directory)"
#   gpg2 --with-fingerprint libss7-2.0.0.tar.gz.asc 2>&1 |
#     awk '$2 == "using" { print "0x" $NF }' |
#     xargs gpg2 --homedir="${workdir}" \
#         --keyserver=hkp://pool.sks-keyservers.net --recv-keys
#   gpg2 --homedir="${workdir}" --export --export-options export-minimal \
#       > libss7.gpg
#   rm -rf "${workdir}"
# Inspect keys using:
#   gpg2 --list-keys --no-default-keyring --keyring ./libss7.gpg
Source2:        %{name}.gpg

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2

%global _hardened_build 1

%description
%{name} is a userspace library that is used for providing SS7 protocol
services to applications. It has a working MTP2, MTP3, and ISUP for ITU and
ANSI style SS7, however it was written in a manner that will easily allow
support for other various national specific variants in the future.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q


%build
%set_build_flags
# The warnings here look like real problems, and should be reported upstream. A
# sample is below:
#
# In file included from /usr/include/string.h:519,
#                  from isup.c:32:
# In function 'strncpy',
#     inlined from 'isup_set_calling' at isup.c:2879:4,
#     inlined from 'isup_set_calling' at isup.c:2875:6:
# /usr/include/bits/string_fortified.h:91:10: error: 'strncpy' specified bound 64 equals destination size [-Werror=stringop-truncation]
#    91 |   return __builtin___strncpy_chk (__dest, __src, __len, __bos (__dest));
#       |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%if 0%{?epel} != 7
export CFLAGS="${CFLAGS} -Wno-error=stringop-truncation"
%endif
%make_build


%install
%make_install libdir=%{_libdir}
find %{buildroot} -name '*.a' -print -delete


%if 0%{?epel} && 0%{?epel} < 8
%ldconfig_scriptlets
%endif


%files
%license LICENSE
%doc ChangeLog
%doc NEWS*
%doc README
%doc %{name}-%{version}-summary.*

%{_libdir}/%{name}.so.%{so_version}*


%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so


%changelog
* Fri Feb 26 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-7
- Work around no -Werror=stringop-truncation on EPEL7

* Tue Feb 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-6
- Improve keyring generation instructions
- Reflow description text
- Whitespace changes according to personal preference
- Add release summary files to documentation
- Add %%_hardened_build macro, which still matters on EPEL

* Sun Feb 14 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-5
- Make dependency from -devel subpackage on main package arch-specific
- Use %%setup macro instead of %%setup0
- Remove obsolete %%ldconfig_scriptlets, except for EPEL7
- Use make macros
- Do not remove the buildroot in %%install
- Remove static libraries directly with find rather than calling rm
- Remove unnecessary README from -devel, since it is installed with the main
  package
- Correctly use the %%license macro
- Use tighter file globs; in particular, per the packaging guidelines, specify
  the current so-version so that a version bump in an update will not be missed
  so easily
- Switch URLs from HTTP to HTTPS
- Add source file signature verification
- Allow build to continue past string operation truncation warnings
- Remove obsolete commented-out manual symlink command

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Update to upstream 2.0.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.2-1
- Update to 1.0.2

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.1-3
- Don't forget to add spec file.

* Tue Oct  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.1-2
- Add LICENSE to docs

* Tue Aug  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.1-1
- Update to 1.0.1

* Tue Jul 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.0-1
- First version for Fedora
