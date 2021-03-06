%global realname cf
%global upstream project-fifo

Name:     erlang-%{realname}
Version:  0.3.1
Release:  7%{?dist}
BuildArch:noarch
Summary:  Terminal color helper
License:  BSD
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://github.com/%{upstream}/%{realname}/archive/v%{version}.tar.gz#/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-rebar

%description
%{summary}.

%prep
%autosetup -n %{realname}-%{version}

%build
%{erlang_compile}

%install
%{erlang_install}

%check
%{erlang_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Lemenkov <lemenkov@gmail.com> - 0.3.1-6
- Drop unnecessary dependency
- Make it noarch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Timothée Floure <fnux@fedoraproject.org> - 0.3.1-1
- Update to latest upstream release

* Sat Jul 14 2018 Timothée Floure <fnux@fedoraproject.org> - 0.2.2-1
- Let there be package
