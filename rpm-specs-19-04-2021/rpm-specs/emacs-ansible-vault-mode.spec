%global pkg ansible-vault-mode

Name:           emacs-%{pkg}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Minor mode for in place manipulation of ansible-vault

License:        GPLv3+
URL:            https://github.com/zellio/%{pkg}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
Requires:       ansible
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup -n %{pkg}-%{version}


%build
%{_emacs_bytecompile} ansible-vault.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 ansible-vault.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.1-1
- Initial RPM release
