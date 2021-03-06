%global realname erlware_commons
%global upstream erlware

Name:     erlang-%{realname}
Version:  1.3.1
Release:  6%{?dist}
Summary:  Extension to Erlang's standard library
License:  MIT
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://repo.hex.pm/tarballs/%{realname}-%{version}.tar
# The "color" test does not play well with Fedora's build system
Patch0:   erlang-erlware_commons-disable-color_test.patch
BuildArch:     noarch
BuildRequires: erlang-rebar
BuildRequires: erlang-cf

%description
%{summary}.

%prep
%setup -c -q
tar xzf contents.tar.gz # contained in source0
%patch0

%build
%{erlang_compile}

%install
%{erlang_install}
cp -arv priv/ %{buildroot}%{erlang_appdir}/

%check
%{erlang_test}

%files
%doc README.md
%{erlang_appdir}/

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-5
- Don't list deps explicitly

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Timothée Floure <fnux@fedoraproject.org> - 1.3.1-1
- New upstream release
- Use source archive from hex.pm since upstream did not provide 'github release'
- Switch to noarch (Changes/TrueNoarchErlangPackages)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Timothée Floure <fnux@fedoraproject.org> - 1.2.0-1
- Let there be package
