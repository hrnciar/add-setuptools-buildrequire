%global modname pynetdicom

%global _description %{expand:
pynetdicom is a pure Python package that implements the DICOM
networking protocol. Working with pydicom, it allows the easy creation of 
DICOM Service Class Users (SCUs) and Service Class Providers (SCPs).}

Name:           python-%{modname}
Version:        1.5.6
Release:        1%{?dist}
Summary:        A Python implementation of the DICOM networking protocol

License:        MIT and (BSD or ASL 2.0)
URL:            https://github.com/pydicom/%{modname}
Source0:        https://github.com/pydicom/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command
BuildRequires:  make
BuildRequires:  %{py3_dist setuptools} %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx} %{py3_dist sphinx-rtd-theme} %{py3_dist sphinx-issues}
BuildRequires:  %{py3_dist pydicom} >= 2
BuildRequires:  %{py3_dist sqlalchemy}
BuildRequires:  %{py3_dist pyfakefs}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

export PYTHONPATH=../
make -C docs SPHINXBUILD=sphinx-build-3 html 
rm -rf docs/_build/html/{.doctrees,.buildinfo,.nojekyll} -vf

%install
%py3_install

%check
# test_tls_yes_server_yes_client and test_tls_transfer are disabled. Upstream is investigating.
# https://github.com/pydicom/pynetdicom/issues/406 and https://github.com/pydicom/pynetdicom/issues/364
# PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest -k "not test_tls_yes_server_yes_client and not test_tls_transfer"

# tests in the apps/ part not reliable, upstream advice to disable them
# https://github.com/pydicom/pynetdicom/issues/498
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest --deselect=pynetdicom/apps/tests -vvv

%files -n python3-%{modname}
%license LICENCE.txt
%doc README.rst
%{python3_sitelib}/%{modname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modname}

%files doc
%license LICENCE.txt
%doc docs/_build/html

%changelog
* Thu Jan 28 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.6-1
- Update to 1.5.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.5-1
- Update to 1.5.5

* Thu Dec 17 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.4-1
- Update to 1.5.4

* Mon Aug 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.3-2
- Re-enable test_fsm in pytest

* Mon Aug 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.3-1
- 1.5.3 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.2-1
- 1.5.2 release

* Wed Jun 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.1-1
- 1.5.1 release

* Fri Jun 05 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.0-2
- Fixed dependecy with pydicom

* Mon Jun 01 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.0-1
- 1.5.0 release

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Alessio <alciregi AT fedoraproject DOT org> - 1.4.1-1
- Initial package
