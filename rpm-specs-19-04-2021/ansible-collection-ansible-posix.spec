%global collection_namespace ansible
%global collection_name posix

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        1.1.1
Release:        3%{?dist}
Summary:        Ansible Collection targeting POSIX and POSIX-ish platforms

# plugins/module_utils/mount.py: Python Software Foundation License version 2
License:        GPLv3+ and Python
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/ansible.posix/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible >= 2.9.10

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible.posix-%{version}
rm -vr tests/{integration,utils} .github changelogs/fragments/.keep {test-,}requirements.txt shippable.yml
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license COPYING
%doc README.md
%{ansible_collection_files}

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.1.1-2
- Rebuild against new ansible-generator and allow to be used by ansible-base-2.10.x

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
