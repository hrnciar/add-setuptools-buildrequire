%global pkg dash

Name:           emacs-%{pkg}
Version:        2.18.1
Release:        1%{?dist}
Summary:        A modern list library for Emacs

License:        GPLv3+
URL:            https://github.com/magnars/%{pkg}.el/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup -n %{pkg}.el-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Sun Mar 21 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.18.1-1
- Update to 2.18.1

* Tue Feb 16 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.18.0-1
- Update to 2.18.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.17.0-1
- Initial RPM release
