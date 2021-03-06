%global collection_namespace netbox
%global collection_name netbox

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Netbox modules for Ansible

License:        GPLv3+
URL:            %{ansible_collection_url}
Source:         https://github.com/netbox-community/ansible_modules/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible_modules-%{version}
sed -i -e '1{\@^#!.*@d}' plugins/modules/*.py
rm -vr .{github,gitignore,readthedocs.yml} tests/integration

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%changelog
* Thu Feb 04 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.2.0-3
- Rebuild against new ansible-generator and allow to be used by ansible-base-2.10.x

* Wed Dec 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-2
- Drop runtime dependencies

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sun Apr 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Wed Mar 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Initial package
