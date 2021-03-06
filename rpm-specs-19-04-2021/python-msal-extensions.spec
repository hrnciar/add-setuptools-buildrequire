%global srcname msal-extensions
%global _description %{expand:The Microsoft Authentication Extensions for Python offers secure mechanisms for
client applications to perform cross-platform token cache serialization and
persistence. It gives additional support to the Microsoft Authentication Library
for Python (MSAL).

MSAL Python supports an in-memory cache by default and provides the
SerializableTokenCache to perform cache serialization. You can read more about
this in the MSAL Python documentation. Developers are required to implement
their own cache persistance across multiple platforms and Microsoft
Authentication Extensions makes this simpler.}

Name:           python-%{srcname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Microsoft Authentication extensions for MSAL Python

License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-extensions-for-python/
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       libsecret
Requires:       %{py3_dist pygobject}
%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n microsoft-authentication-extensions-for-python-%{version}

# Remove bundled egg-info
rm -rf *.egg-info

# Remove DOS line endings
sed "s|\r||g" README.md >README.md.new && \
touch -r README.md README.md.new && \
mv README.md.new README.md


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/msal_extensions/
%{python3_sitelib}/msal_extensions-*.egg-info/


%changelog
* Sat Feb 13 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-1
- Initial RPM release
