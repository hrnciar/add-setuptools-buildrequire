%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           python-setuptools-rust
Version:        0.12.1
Release:        1%{?dist}
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        %{pypi_source setuptools-rust}
BuildArch:      noarch
ExclusiveArch:  %{rust_arches}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(semantic-version) >= 2.6
BuildRequires:  python3dist(toml) >= 0.9.0
%if 0%{?fedora}
BuildRequires:  python3dist(setuptools-scm) >= 3.4.3
BuildRequires:  python3dist(wheel)
BuildRequires:  rust-packaging >= 1.45
%else
# RHEL has rust-toolset and neither setuptools-scm nor wheel
BuildRequires:  rust-toolset >= 1.45
%endif
%if %{with tests}
BuildRequires:  rust-pyo3+default-devel
%endif

%description
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%package -n     python3-setuptools-rust
Summary:        %{summary}
%if 0%{?fedora}
Requires:       rust-packaging >= 1.45
%else
Requires:       rust-toolset >= 1.45
%endif

%description -n python3-setuptools-rust
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%prep
%autosetup -n setuptools-rust-%{version}
# Remove bundled egg-info
rm -rf setuptools-rust.egg-info

%if ! 0%{?fedora}
# RHEL doesn't have setuptools-scm
# remove setuptools-scm
rm pyproject.toml
sed -i 's/setup_requires.*//' setup.cfg

# create version.py without setuptools-scm
cat > setuptools_rust/version.py << EOF
version = '%{VERSION}'
version_tuple = ($(echo %{VERSION} | sed 's/\./, /g'))
EOF
%endif


%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{__python3} -c "from setuptools_rust import RustExtension, version"

%if %{with tests}
cd examples/tomlgen
%cargo_prep
sed -i 's/"0\.[0-9.]*"/"^0"/g' setup.cfg
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py build
cd ../..
%endif


%files -n python3-setuptools-rust
%doc README.md CHANGELOG.md
%license LICENSE
%{python3_sitelib}/setuptools_rust/
%{python3_sitelib}/setuptools_rust-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Mar 11 2021 Christian Heimes <cheimes@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Tue Mar 09 2021 Christian Heimes <cheimes@redhat.com> - 0.12.0-1
- Update to 0.12.0 (#1936679)
- Run tomlgen example as test case

* Thu Feb 11 2021 Christian Heimes <cheimes@redhat.com> - 0.11.6-4
- Fix RHEL build: remove wheel build requirements, use rust-toolset

* Thu Feb 11 2021 Christian Heimes <cheimes@redhat.com> - 0.11.6-3
- Add RHEL packaging support

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Christian Heimes <cheimes@redhat.com> - 0.11.6-1
- Initial package.
- Resolves: rhbz#1906490
