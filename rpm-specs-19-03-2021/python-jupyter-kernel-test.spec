%global srcname jupyter-kernel-test
%global srcname_ jupyter_kernel_test

Name:           python-%{srcname}
Version:        0.3
Release:        17%{?dist}
Summary:        Machinery for testing Jupyter kernels via the messaging protocol

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/jupyter/%{srcname_}/archive/%{version}/%{srcname}-%{version}.tar.gz

# https://github.com/jupyter/jupyter_kernel_test/issues/42
Patch0:         https://github.com/jupyter/jupyter_kernel_test/commit/0b78c2835fad5df3be182ddd5013a73a63c4f81e.patch
# flit 3.0.0 expects pyproject.toml file instead of flit.ini.
# When a new version of jupyter_kernel_test is released
# this patch can be removed.
Patch1:         0001-Replace-flit.ini-file-with-pyproject.toml.patch

BuildArch:      noarch

# No support for Python 2.
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  python3-ipykernel

%description
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol
(currently 5.0).


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3-traitlets
Requires:       python3-jupyter-client
Requires:       python3-nose

%description -n python3-%{srcname}
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol
(currently 5.0).

%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup -n %{srcname_}-%{version} -p1


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname_}

%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    %{__python3} test_ipykernel.py


# Note that there is no %%files section for the unversioned python module if we
# are building for several python runtimes
%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING.md
%doc README.rst


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 02 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0.3-16
- Backport patch to replace flit.ini with pyproject.toml needed by flit 3.0.0
- Convert spec to use pyproject-rpm-macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.3-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.3-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.3-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.3-7
- Rebuilt for Python 3.7

* Thu Apr 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-6
- Fix build against latest flit.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-4
- Fix license tag.

* Sun Oct 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-3
- Use new method of skipping flit network usage.
- Simplify spec against latest template.

* Mon Jul 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-2
- Use new py3_install_wheel macro.

* Mon Jul 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-1
- Update to latest version.

* Sun Mar 12 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Initial package release.
