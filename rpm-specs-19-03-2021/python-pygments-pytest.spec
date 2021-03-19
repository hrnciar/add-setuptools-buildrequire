%global pypi_name pygments_pytest
%global dash_name pygments-pytest

# this is BRed by pytest, so we need to run without tests when bootstrapping
# also pygments-ansi-color is not available in Fedora yet
%bcond_with tests

Name:           python-%{dash_name}
Version:        2.1.0
Release:        2%{?dist}
Summary:        A pygments lexer for pytest output
License:        MIT
URL:            https://github.com/asottile/pygments-pytest
Source0:        %{url}/archive/v%{version}/%{dash_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.

%package -n     python3-%{dash_name}
Summary:        %{summary}

%description -n python3-%{dash_name}
This library provides a pygments lexer called pytest.
This library also provides a sphinx extension.


%prep
%autosetup -n %{dash_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with tests}
%check
%pytest -v
%endif

%files -n python3-%{dash_name} -f %pyproject_files
%license LICENSE
%doc README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.1.0-1
- Update to 2.1.0 and convert to pyproject macros (rhbz#1856288)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-1
- Update to 2.0.0 (#1747425)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-1
- Initial package
