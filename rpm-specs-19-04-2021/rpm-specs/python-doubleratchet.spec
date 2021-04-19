Name:           python-doubleratchet
Version:        0.7.0~beta
Release:        3%{?dist}
Summary:        Python implementation of the Double Ratchet algorithm

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version_no_tilde}.tar.gz
# For files and directories
%global version_main %(c=%version; echo $c|cut -d~ -f1)

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-cryptography


%description
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.



%package     -n python3-doubleratchet
Summary:        Python implementation of the Double Ratchet algorithm

%description -n python3-doubleratchet
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.



%prep
%autosetup -n %{name}-%{version_no_tilde}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test



%files -n python3-doubleratchet
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/doubleratchet/
%{python3_sitelib}/DoubleRatchet-%{version_main}-py%{python3_version}.egg-info/



%changelog
* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0~beta-3
- Package Review RHBZ#1917089:
  - Fix the Version tag to match upstream version
  - Use %%{python3_version} in %%files section

* Mon Feb 08 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-2
- Remove upstream name variable used once: %%{srcname}
- Add more explicit description

* Sat Jan 16 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-1
- Initial package
