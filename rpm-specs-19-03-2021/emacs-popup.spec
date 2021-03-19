%global pkg popup

Name:           emacs-%{pkg}
Version:        0.5.8
Release:        2%{?dist}
Summary:        Visual Popup Interface Library for Emacs

License:        GPLv3+
URL:            https://github.com/auto-complete/%{pkg}-el/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
Emacs.popup.el is a visual popup user interface library for Emacs. This provides
a basic API and common UI widgets such as popup tooltips and popup menus.


%prep
%autosetup -n %{pkg}-el-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc README.md
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.8-1
- Initial RPM release
