%{?python_enable_dependency_generator}
%global srcname hs-dbus-signature

Name:           python-%{srcname}
Version:        0.07
Release:        4%{?dist}
Summary:        Hypothesis Strategy for Generating Arbitrary DBus Signatures

License:        MPLv2.0
URL:            https://github.com/stratis-storage/hs-dbus-signature
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This package contains a Hypothesis strategy for generating DBus signatures.\
\
The strategy is intended to be both sound and complete. That is, it should\
never generate an invalid DBus signature and it should be capable,\
modulo size constraints, of generating any valid DBus signature.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-hypothesis

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m unittest -v tests/test_deterministic.py

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/hs_dbus_signature/
%{python3_sitelib}/hs_dbus_signature-*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 mulhern <amulhern@redhat.com> - 0.07-3
- Restore python3-hypothesis to the list of packages required to build

* Wed Dec 02 2020 mulhern <amulhern@redhat.com> - 0.07-2
- Use python3 macro for python

* Wed Dec 02 2020 mulhern <amulhern@redhat.com> - 0.07-1
- Update to 0.07

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.06-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.06-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.06-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.06-1
- Update to 0.06

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.05-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.05-2
- Minor changes

* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.05-1
- Initial package
