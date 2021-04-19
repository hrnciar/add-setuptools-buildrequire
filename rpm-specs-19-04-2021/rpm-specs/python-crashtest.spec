%global pypi_name crashtest

%global common_description %{expand:
Crashtest is a Python library that makes exceptions handling and
inspection easier.}

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        3%{?dist}
Summary:        Manage Python errors with ease
License:        MIT

URL:            https://github.com/sdispater/crashtest
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-2
- Build with poetry-core
- Run tests

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Initial package

