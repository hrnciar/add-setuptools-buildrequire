%global collection_namespace community
%global collection_name mysql

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        MySQL collection for Ansible

License:        GPLv3+
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.mysql/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible >= 2.9.10

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n community.mysql-%{version}
rm -vr .github
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install
rm -vr %{buildroot}%{ansible_collection_files}/%{collection_name}/tests

%files
%license COPYING
%doc README.md changelogs/CHANGELOG.rst
%{ansible_collection_files}

%changelog
* Thu Mar 11 2021 Orion Poplawski <orion@nwra.com> - 1.3.0-1
- Initial package
