%{?python_enable_dependency_generator}
%global forgeurl https://github.com/Yubico/yubikey-manager/
%global commit ea268d5c067417a81db5e66b4149779b7053335f

Name:           yubikey-manager
Version:        4.0.0p1

%forgemeta

Release:        1%{?dist}
Summary:        Python library and command line tool for configuring a YubiKey
License:        BSD
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.rpmlintrc

BuildArch:      noarch
BuildRequires:  swig pcsc-lite-devel ykpers pyproject-rpm-macros
BuildRequires:  python3-devel tox
BuildRequires:  %{py3_dist six pyscard pyusb click cryptography pyopenssl}
BuildRequires:  %{py3_dist tox-current-env poetry-core setuptools}
BuildRequires:  %{py3_dist fido2} >= 0.9.0

Requires:       python3-%{name} python3-setuptools u2f-hidraw-policy

%description
Command line tool for configuring a YubiKey.

%generate_buildrequires
%pyproject_buildrequires

%package -n python3-%{name}
Summary:        Python library for configuring a YubiKey
Requires:       ykpers pcsc-lite

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python library for configuring a YubiKey.

%prep
%forgesetup
%autosetup -n %{archivename}

%build
%pyproject_wheel

%install
%pyproject_install

# Remove tests temporarily for early alpha code
# Rawhide / F34 code only
# check
# tox

%files -n python3-%{name}
%license COPYING
%doc NEWS
%{python3_sitelib}/*

%files
%{_bindir}/ykman

%changelog
* Tue Mar 02 2021 Gerald Cox <gbcox@fedoraproject.org> - 4.0.0p1
- Upstream release rhbz#1921519

* Tue Mar 02 2021 Gerald Cox <gbcox@fedoraproject.org> - 4.0.0
- Upstream release rhbz#1921519

* Thu Feb 18 2021 Gerald Cox <gbcox@fedoraproject.org> - 4.0.0a3
- Upstream release rhbz#1921519

* Wed Feb 10 2021 Gerald Cox <gbcox@fedoraproject.org> - 4.0.0a1
- Upstream release rhbz#1921519

* Wed Feb 03 2021 Gerald Cox <gbcox@fedoraproject.org> - 4.0.0a1
- Upstream release rhbz#1921519

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Gerald Cox <gbcox@fedoraproject.org> - 3.1.2.1
- Upstream release rhbz#1919027

* Mon Oct 05 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.1.1.4.git87dd1d8
- BuildRequire python3-setuptools explicitly

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3.git87dd1d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-2.git87dd1d8
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.1.1-1.git87dd1d8
- Upstream release rhbz#1796504

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8.git1f22620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Gerald Cox <gbcox@fedoraproject.org - 3.0.0-7.git1f22620
- PCSC Exceptions - rhbz#1684945

* Thu Oct 24 2019 Gerald Cox <gbcox@fedoraproject.org - 3.0.0-6.gitcfa1907
- PCSC Exceptions - rhbz#1684945 rhbz#1737264

* Mon Oct 21 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-5.gitcfa1907
- Require python3-setuptools explicitly

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-4.gitcfa1907
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3.gitcfa1907
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.0.0-2.gitcfa1907
- Upstream release - rhbz#1737243

* Sun Aug 04 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.0.0-1.gitcfa1907
- Upstream release - rhbz#1737243

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3.gitb44d719
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.0-2.gitb44d719
- Upstream release - rhbz#1703827

* Sun Apr 28 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.0-1.gitb44d719
- Upstream release - rhbz#1703827

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4.gite17b3de
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.0.0-3.gite17b3de
- Upstream release - rhbz#1655888

* Tue Jan 01 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-2.git1c707b2
- Enable python dependency generator

* Mon Dec 31 2018 Gerald Cox <gbcox@fedoraproject.org> - 2.0.0-1.git1c707b2
- Upstream release - rhbz#1655888

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.7

* Mon May 7 2018 Seth Jennings <sethdjennings@gmail.com> - 0.6.0-2
- add u2f-host as dependency

* Wed May 2 2018 Seth Jennings <sethdjennings@gmail.com> - 0.6.0-1
- Upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 9 2017 Seth Jennings <sethdjennings@gmail.com> - 0.4.0-1
- New package
- Upstream release
