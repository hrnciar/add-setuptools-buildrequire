Name:           prewikka-updatedb
Version:        5.2.0
Release:        2%{?dist}
Summary:        Database update scripts for prewikka
# License justification: https://www.prelude-siem.org/projects/prelude/wiki/SourceOrganization
License:        GPLv2+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildArch:      noarch

%description
Database update scripts for prewikka.

%package -n python3-%{name}
Summary:        Database update scripts for prewikka
Requires:       python3-prewikka >= %{version}
Provides:       prewikka-updatedb = %{version}-%{release}

%description -n python3-%{name}
Database update scripts for prewikka.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{name}
%{python3_sitelib}/prewikkaupdatedb/
%{python3_sitelib}/prewikka_updatedb-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Thomas Andrejak <thomas.andrejak@gmail.com> 5.2.0-1
- Initial packaging
