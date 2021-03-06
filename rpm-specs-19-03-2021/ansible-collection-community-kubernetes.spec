%global collection_namespace community
%global collection_name kubernetes

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        1.1.1
Release:        4%{?dist}
Summary:        Kubernetes Collection for Ansible

License:        GPLv3+
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.kubernetes/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n %{collection_namespace}.%{collection_name}-%{version}
rm -vr tests/integration molecule .github .yamllint codecov.yml setup.cfg
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.1.1-3
- Rebuild against new ansible-generator and allow to be used by ansible-base-2.10.x

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-2
- Drop unneeded dependency

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
