Name:           smc-tools
Version:        1.5.0
Release:        1%{?dist}
Summary:        Shared Memory Communication Tools

License:        EPL
URL:            https://github.com/ibm-s390-linux/smc-tools
Source0:        https://github.com/ibm-s390-linux/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/ibm-s390-linux/smc-tools/commit/c3d1f45abff2433afefaea9d31cd9cda0a7408d3
Patch0:         smc-tools-1.5.0-makefile.patch
# https://github.com/ibm-s390-linux/smc-tools/issues/1
Patch1:         smc-tools-1.5.0-flags.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  bash-completion

%ifarch s390 s390x
# for smc_chk
Requires:       python3
Requires:       man
%endif


%description
The Shared Memory Communication Tools (smc-tools) package enables usage of SMC
sockets in Linux.

%prep
%autosetup


%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" V=1


%install
%make_install V=1


%files
%license LICENSE
%doc README.md
%{_bindir}/smcd
%{_bindir}/smcr
%{_bindir}/smc_dbg
%{_bindir}/smc_pnet
%{_bindir}/smc_run
%{_bindir}/smcss
%{_libdir}/libsmc-preload.so*
%{_mandir}/man7/af_smc.7*
%{_mandir}/man8/smcd*.8*
%{_mandir}/man8/smcr*.8*
%{_mandir}/man8/smc_pnet.8*
%{_mandir}/man8/smc_run.8*
%{_mandir}/man8/smcss.8*
%ifarch s390 s390x
%{_bindir}/smc_chk
%{_bindir}/smc_rnics
%{_mandir}/man8/smc_chk.8*
%{_mandir}/man8/smc_rnics.8*
%endif
%{_datadir}/bash-completion/


%changelog
* Wed Mar 17 2021 Dan Horák <dan@danny.cz> - 1.5.0-1
- update to 1.5.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Dan Horák <dan@danny.cz> - 1.3.1-1
- update to 1.3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Dan Horák <dan@danny.cz> - 1.2.0-1
- update to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Dan Horák <dan@danny.cz> - 1.1.0-1
- update to 1.1.0

* Mon Apr 16 2018 Dan Horák <dan@danny.cz> - 1.0.0-4
- fix LDFLAGS injection (#1567902)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Dan Horák <dan@danny.cz> - 1.0.0-2
- use make macro
- comment patches
- use distro LDFLAGS in build

* Mon Jan  8 2018 Dan Horák <dan@danny.cz> - 1.0.0-1
- initial Fedora version
