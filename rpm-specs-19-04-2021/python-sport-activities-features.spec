%bcond_without tests

%global pypi_name sport-activities-features
%global pretty_name sport_activities_features

%global _description %{expand:
A minimalistic toolbox for extracting features 
from sport activity files written in Python}

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        2%{?dist}
Summary:        Extracting features from sport activity files

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  make

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires: %{py3_dist lockfile}
BuildRequires: %{py3_dist packaging}
BuildRequires: %{py3_dist pep517}
BuildRequires: %{py3_dist poetry}

#For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

BuildRequires: %{py3_dist tcxreader}
BuildRequires: %{py3_dist niaaml}
BuildRequires: %{py3_dist geopy}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version} -S git
rm -rf %{pretty_name}.egg-info
rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%pyproject_install
%pyproject_save_files sport_activities_features

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/LICENSE
rm -rf %{buildroot}/%{python3_sitelib}/CHANGELOG.md

%check	
%if %{with tests}
%{python3} -m pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%files doc
%license LICENSE
%doc docs/_build/html
%doc examples/

%changelog
* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-2
- Install additional files

* Thu Apr 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-1
- Initial package
