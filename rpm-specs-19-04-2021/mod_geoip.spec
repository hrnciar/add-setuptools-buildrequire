%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:     %{expand: %%global _httpd_moddir     %%{_libdir}/httpd/modules}}

Summary:	GeoIP module for the Apache HTTP Server
Name:		mod_geoip
Version:	1.2.10
Release:	13%{?dist}
License:	ASL 1.1
URL:		http://dev.maxmind.com/geoip/legacy/mod_geoip2/
Source0:	https://github.com/maxmind/geoip-api-mod_geoip2/archive/%{version}/geoip-api-mod_geoip2-%{version}.tar.gz
Source1:	10-geoip.conf
Source2:	geoip.conf
BuildRequires:	gcc, httpd-devel, GeoIP-devel >= 1.4.3
Requires:	GeoIP%{?_isa}, httpd-mmn = %{_httpd_mmn}

%description
mod_geoip is an Apache module to look up geolocation information for a
client as part of the HTTP request process. It uses the GeoIP library
and database to perform the lookup. It is free software, licensed under
the Apache license.

%prep
%setup -q -n geoip-api-mod_geoip2-%{version}

%build
%{_httpd_apxs} -Wc,-Wall -Wl,"-lGeoIP" -c %{name}.c

%install
install -D -p -m 755 .libs/%{name}.so $RPM_BUILD_ROOT%{_httpd_moddir}/%{name}.so

%if "%{_httpd_modconfdir}" == "%{_httpd_confdir}"
# httpd <= 2.2.x
cat %{SOURCE1} > unified.conf
echo >> unified.conf
cat %{SOURCE2} >> unified.conf
touch -c -r %{SOURCE1} unified.conf
install -D -p -m 644 unified.conf $RPM_BUILD_ROOT%{_httpd_confdir}/geoip.conf
%else
# httpd >= 2.4.x
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-geoip.conf
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_httpd_confdir}/geoip.conf
%endif

%files
%license LICENSE
%doc Changes INSTALL.md README.*
%{_httpd_moddir}/%{name}.so
%config(noreplace) %{_httpd_confdir}/geoip.conf
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/10-geoip.conf
%endif

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Robert Scheck <robert@fedoraproject.org> 1.2.10-1
- Upgrade to 1.2.10 (#1214493)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 1.2.7-4
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Robert Scheck <robert@fedoraproject.org> 1.2.7-1
- Upgrade to 1.2.7
- Updated spec file to match with Apache 2.4 policy (#809698)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Joe Orton <jorton@redhat.com> - 1.2.5-8
- fix config perms

* Wed Apr 04 2012 Jan Kaluza <jkaluza@redhat.com> - 1.2.5-7
- Fix compilation error with httpd-2.4 (#809698)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Fleming <mfleming+rpm@enlartenment.com> - 1.2.5-2
- Update setup macro

* Fri Aug 29 2008 Michael Fleming <mfleming+rpm@enlartenment.com> - 1.2.5-1
- Update to 1.2.5

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.4-3
- fix license tag

* Fri Jun 20 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.4-2
- New upstream update
- Minor spec tweaks

* Sun Apr 13 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.2-1
- New upstream update

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.0-2
- Autorebuild for GCC 4.3

* Wed Sep 5 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.2.0-1
- New upstream release
- Employ some macro sanity..

* Sun Sep 3 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.1.8-2
- Bump and rebuild

* Mon May 1 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.1.8-1
- New upstream release

* Sat Feb 18 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.1.7-2
- Small cleanups, including a saner Requires: for httpd
- Don't strip the binary

* Sun Feb 5 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.1.7-1
- Initial review package for Extras
