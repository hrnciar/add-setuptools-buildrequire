%global srcname matrix-nio

Name:           python-%{srcname}
Version:        0.15.2
Release:        5%{?dist}
Summary:        A Matrix client library

License:        ISC and ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
nio is a multilayered Matrix client library. The underlying base layer doesn't
do any network IO on its own, but on top of that is a full fledged
batteries-included asyncio layer using aiohttp. File IO is only done if you
enable end-to-end encryption (E2EE).}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
Requires:       python3-crypto

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
# Update BRs
sed \
    -e 's/aiofiles.*/aiofiles = "*"/' \
    -e 's/h11.*/h11 = "*"/' \
    -e 's/h2.*/h2 = "*"/' \
    -e 's/pycryptodome.*/pycryptodomex = "*"/' \
    -i pyproject.toml
# Remove backup file
rm -fv nio/events/room_events.py.orig


%generate_buildrequires
%pyproject_buildrequires -x e2e

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files nio

%check

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}  -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
* Sat Apr 17 2021 Michael Scherer <misc@fedoraproject.org> - 0.15.2-5
- Add missing requires python3-crypto (#1925689)

* Mon Feb 08 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.2-4
- Manually merge Miro's pyproject packaging improvements to resolve merge conflict

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.2-2
- Remove extra file to fix build

* Mon Jan 18 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.2-2
- Bump for rebuild

* Fri Nov 20 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.2-1
- Initial rpm
