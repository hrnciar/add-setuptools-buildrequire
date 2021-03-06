# Module Magic Number
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}

Name:           mod_md
Version:        2.4.0
Release:        1%{?dist}
Summary:        Certificate provisioning using ACME for the Apache HTTP Server
License:        ASL 2.0
URL:            https://icing.github.io/mod_md/
Source0:        https://github.com/icing/mod_md/releases/download/v%{version}/mod_md-%{version}.tar.gz
Patch1:         mod_md-2.0.8-state_dir.patch
Patch2:         mod_md-2.2.6-warnfix.patch
BuildRequires:  make, gcc
BuildRequires:  pkgconfig, httpd-devel >= 2.4.41, openssl-devel >= 1.1.0, jansson-devel, libcurl-devel, xmlto
Requires:       httpd-mmn = %{_httpd_mmn}, mod_ssl >= 1:2.4.41
Conflicts:      httpd < 2.4.39-7
Epoch:          1

%description
This module manages common properties of domains for one or more
virtual hosts. Specifically it can use the ACME protocol to automate
certificate provisioning.  Certificates will be configured for managed
domains and their virtual hosts automatically, including at renewal.

%prep
%autosetup -p1

%build
%configure --with-apxs=%{_httpd_apxs}
# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build V=1

%check
%make_build check

%install
%make_install
rm -rf %{buildroot}/etc/httpd/share/doc/

# remove links and rename SO files
rm -f %{buildroot}%{_httpd_moddir}/mod_md.so
mv %{buildroot}%{_httpd_moddir}/mod_md.so.0.0.0 %{buildroot}%{_httpd_moddir}/mod_md.so

# create configuration
mkdir -p %{buildroot}%{_httpd_modconfdir}
echo "LoadModule md_module modules/mod_md.so" > %{buildroot}%{_httpd_modconfdir}/01-md.conf

%files
%doc README.md ChangeLog AUTHORS
%license LICENSE
%config(noreplace) %{_httpd_modconfdir}/01-md.conf
%{_httpd_moddir}/mod_md.so
%{_bindir}/a2md
%{_mandir}/man1/*

%changelog
* Tue Mar  9 2021 Joe Orton <jorton@redhat.com> - 1:2.4.0-1
- update to 2.4.0

* Tue Feb  2 2021 Joe Orton <jorton@redhat.com> - 1:2.3.7-1
- update to 2.3.7 (beta)
- use autosetup macro

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Joe Orton <jorton@redhat.com> - 1:2.2.8-4
- update to 2.2.8

* Fri Aug 28 2020 Joe Orton <jorton@redhat.com> - 1:2.2.7-4
- use _httpd_apxs macro

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Alexander Bokovoy <abokovoy@redhat.com> - 1:2.2.7-2
- mod_md does not work with ACME server that does not provide revokeCert or
  keyChange resource (#1832841)

* Tue Feb 11 2020 Joe Orton <jorton@redhat.com> - 1:2.2.7-1
- update to 2.2.7

* Fri Feb  7 2020 Joe Orton <jorton@redhat.com> - 1:2.2.6-1
- update to 2.2.6 (#1799660)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Joe Orton <jorton@redhat.com> - 1:2.0.8-4
- require mod_ssl, update package description

* Fri Aug 30 2019 Joe Orton <jorton@redhat.com> - 1:2.0.8-3
- rebuild against 2.4.41

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Joe Orton <jorton@redhat.com> - 1:2.0.8-1
- update to 2.0.8

* Tue Jun 11 2019 Lubos Uhliarik <luhliari@redhat.com> - 2.0.3-1
- Initial import (#1719248).
