%global collection_namespace community
%global collection_name general

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Modules and plugins supported by Ansible community

# plugins/module_utils/_mount.py: Python Software Foundation License version 2
# plugins/module_utils/_netapp.py: BSD 2-clause "Simplified" License
# plugins/module_utils/compat/ipaddress.py: Python Software Foundation License version 2
# plugins/module_utils/identity/keycloak/keycloak.py: BSD 2-clause "Simplified" License
License:        GPLv3+ and BSD and Python
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.general/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible >= 2.9.10

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n community.general-%{version}
rm -vr .github .azure-pipelines
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install
rm -vr %{buildroot}%{ansible_collection_files}/%{collection_name}/tests

%files
%license COPYING
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%changelog
* Thu Feb 04 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.3.1-2
- Rebuild against new ansible-generator and allow usage by ansible-base-2.10.x

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
