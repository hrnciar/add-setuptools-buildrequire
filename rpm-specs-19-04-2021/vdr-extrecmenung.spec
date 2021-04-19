%global pname   extrecmenung
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

Name:           vdr-%{pname}
Version:        2.0.11
Release:        1%{?dist}
Summary:        Powerful next generation recordings menu replacement plugin for VDR

License:        GPLv2+
URL:            https://gitlab.com/kamel5/extrecmenung
Source0:        https://gitlab.com/kamel5/extrecmenung/-/archive/v%{version}/extrecmenung-v%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 2.4.6-6
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin provides a powerful replacement for VDR's default
recordings menu entry.  It looks like the standard recordings menu, but
adds several functions, such as additional commands for "rename" and "move"
This is the next generation version based on the original "extrecmenu"

%prep
%setup -q -n %{pname}-v%{version}
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build
%make_build AUTOCONFIG=0

%install
%make_install

install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%license COPYING
%doc HISTORY
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/*.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Tue Feb 02 2021 Peter Bieringer <pb@bieringer.de> - 2.0.11-1
- Update to 2.0.11 incl. dependency to vdr >= 2.4.6-6 to enable rename features based on EPG

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Peter Bieringer <pb@bieringer.de> - 2.0.10-1
- Update to 2.0.10

* Thu Jan 14 2021 Peter Bieringer <pb@bieringer.de> - 2.0.9-1
- Update to 2.0.9

* Tue Dec 29 2020 Peter Bieringer <pb@bieringer.de> - 2.0.5-3
- Remove %%defattr

* Tue Dec 29 2020 Peter Bieringer <pb@bieringer.de> - 2.0.5-2
- Add UTF-8 conversion for HISTORY

* Sun Dec 20 2020 Peter Bieringer <pb@bieringer.de> - 2.0.5-1
- First build
