%global pypi_name nudatus

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        1%{?dist}
Summary:        Strip comments from Python scripts

License:        MIT
URL:            https://github.com/zanderbrown/nudatus
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# test requirements mixed with coverage upstream, BRing pytest manually is easier
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros

%description
Nudatus is a tool to remove comments from python scripts. It's created for use
in uflash to help squeeze longer programs onto the micro:bit but it should be
suitable for various environments with restricted storage.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Provides:       %{pypi_name} == %{version}-%{release}

%description -n python3-%{pypi_name}
Nudatus is a tool to remove comments from python scripts. It's created for use
in uflash to help squeeze longer programs onto the micro:bit but it should be
suitable for various environments with restricted storage.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -vvv tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/nudatus

%changelog
* Mon Apr 12 2021 Karolina Surma <ksurma@redhat.com> - 0.0.5-1
- Update to 0.0.5
Resolves rhbz#1924644

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0.0.4-1
- Update to 0.0.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-1
- Update to 0.0.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-1
- Initial package.
