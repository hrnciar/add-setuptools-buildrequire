Name:       js-jquery-prettyphoto
Version:    3.1.6
Release:    9%{?dist}
BuildArch:  noarch

License:    GPLv2
Summary:    PrettyPhoto is a jQuery based lightbox clone
URL:        https://github.com/scaron/prettyphoto
Source0:    %{url}/archive/%{version}.tar.gz

BuildRequires: web-assets-devel

Requires:      js-jquery
Requires:      web-assets-filesystem


%description
The prettyPhoto library provides a jQuery based lightbox clone. Not only
does it support images, it also add support for videos, flash, YouTube,
iFrames. It’s a full blown media lightbox. The setup is easy and quick,
plus the script is compatible in every major browser. 


%prep
%autosetup -n prettyphoto-%{version}

# https://github.com/scaron/prettyphoto/pull/170
chmod 0644 README


%install
install -d -m 0755 %{buildroot}/%{_webassetdir}
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto/css
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto/images
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto/js

install -D -p -m 0644 css/*.css %{buildroot}/%{_webassetdir}/jquery-prettyphoto/css
cp -a images/* %{buildroot}/%{_webassetdir}/jquery-prettyphoto/images
install -D -p -m 0644 js/jquery.prettyPhoto.js %{buildroot}/%{_webassetdir}/jquery-prettyphoto/js


%files
# Upstream has no license file, but https://github.com/scaron/prettyphoto/pull/169 is proposed.
%doc README
%{_webassetdir}/jquery-prettyphoto


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.6-1
- Initial release.
