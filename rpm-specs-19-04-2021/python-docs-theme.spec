Name:           python-docs-theme
Version:        2020.12
Release:        1%{?dist}
Summary:        The Sphinx theme for the CPython docs and related projects

License:        Python
URL:            https://github.com/python/python-docs-theme/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description Python Docs Sphinx Theme is the theme for the Python documentation.

%description
%_description

%package -n     python3-docs-theme
Summary:        %{summary}

%description -n python3-docs-theme
%_description

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files python_docs_theme

%files -n python3-docs-theme -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Thu Mar 04 2021 Karolina Surma <ksurma@redhat.com> - 2020.12-1
- Initial package.
