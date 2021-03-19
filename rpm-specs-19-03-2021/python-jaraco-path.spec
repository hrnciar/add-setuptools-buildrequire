Name:           python-jaraco-path
Version:        3.3.1
Release:        1%{?dist}
Summary:        Miscellaneous path functions

License:        MIT
URL:            https://github.com/jaraco/jaraco.path
Source0:        https://github.com/jaraco/jaraco.path/archive/v%{version}/jaraco.path-%{version}.tar.gz
# We do not have a correct version of singledispatch in Fedora that jaraco.path needs.
# Instead of backporting and updating singledispatch it is better to not to use
# it at all and use functools from the standard library with Python 3.7 and higher.
# Upstream PR: https://github.com/jaraco/jaraco.path/pull/1
Patch1:         https://github.com/jaraco/jaraco.path/pull/1.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pytest

%global _description %{expand:
jaraco.path provides cross platform hidden file detection}

%description %_description

%package -n     python3-jaraco-path
Summary:        %{summary}
Requires:       python3-jaraco

%description -n python3-jaraco-path %_description

%prep
%autosetup -p1 -n jaraco.path-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jaraco

%check
# When pytest collects tests, it ignores hidden directories by default,
# because the `.*` pattern is ignored.
# jaraco.path replaces this default by redefining norecursedirs without `.*`,
# thus hidden directories are not ignored.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1935212 for more info.
%pytest --ignore %_pyproject_builddir

%files -n python3-jaraco-path -f %{pyproject_files}
%license LICENSE
%doc README.rst
%exclude %dir %{python3_sitelib}/jaraco
%exclude %dir %{python3_sitelib}/jaraco/__pycache__
%pycached %exclude %{python3_sitelib}/jaraco/__init__.py

%changelog
* Tue Mar 02 2021 Tomas Hrnciar <thrnciar@redhat.com> - 3.3.1-1
- Initial package
