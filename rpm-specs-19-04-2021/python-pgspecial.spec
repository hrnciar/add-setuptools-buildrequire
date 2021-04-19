%global srcname pgspecial

Name:           python-%{srcname}
Version:        1.12.1
Release:        5%{?dist}
Summary:        Meta-commands handler for Postgres Database

License:        BSD
URL:            https://www.dbcli.com
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Manual BR’s for testing:
BuildRequires:  python3dist(pytest)
# From requirements-dev.txt, and required for tests, but missing from tox.ini:
BuildRequires:  python3dist(configobj) >= 5.0.6

%global common_description %{expand:
This package provides an API to execute meta-commands AKA “special”, or
“backslash commands”) on PostgreSQL.}

%description %{common_description}


%generate_buildrequires
%pyproject_buildrequires -r


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info
# Remove obsolete mock dependency, which is not required in practice
sed -r -i '/^[[:blank:]]*mock[[:blank:]]*$/d' tox.ini


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# Note that most tests will be skipped since there is not a postgres database
# we can connect to.
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license License.txt
%doc README.rst
%doc changelog.rst
%doc DEVELOP.rst


%changelog
* Sat Apr 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.1-5
- Drop workarounds for Fedora 32

* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.1-4
- Drop python3dist(setuptools) BR, redundant with pyproject-rpm-macros

* Tue Mar 02 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.1-3
- Use pyproject-rpm-macros, including generated BR’s

* Tue Mar 02 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.1-2
- Add version and comment for python3dist(configobj) dependency

* Tue Mar 02 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.12.1-1
- New upstream release 1.12.1
- Add changelog to doc-files

* Tue Mar 02 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.11.10-5
- Use srcname instead of pypi_name
- Add common_description macro
- Drop obsolete python_provide macro
- Drop scripts/README.rst from doc-files, and add DEVELOP.rst
- Use %%pytest macro
- Drop explicit/manual Requires, which are redundant with automatic Python
  dependency generation

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.10-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.11.10-1
- Initial package.
