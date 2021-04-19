# Created by pyp2rpm-3.3.5
%global pypi_name nbclient

%global _description %{expand:
NBClient, a client library for programmatic notebook execution, is a tool for 
running Jupyter Notebooks in different execution contexts. NBClient was spun 
out of nbconvert (formerly ExecutePreprocessor). NBClient lets you execute notebooks.
}

Name:           python-%{pypi_name}
Version:        0.5.3
Release:        1%{?dist}
Summary:        A client library for executing notebooks

License:        BSD
URL:            https://jupyter.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(traitlets) >= 4.2
BuildRequires:  python3dist(jupyter-client) >= 5.3.4
BuildRequires:  python3dist(nbformat) >= 5
BuildRequires:  python3dist(async-generator)
BuildRequires:  python3dist(nest-asyncio)

%bcond_without check

%if %{with check}
# for testing
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(ipywidgets)
BuildRequires:  python3dist(nbconvert)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(testpath)
BuildRequires:  python3dist(xmltodict)
%endif

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}

Requires:  python3dist(traitlets) >= 4.2
Requires:  python3dist(jupyter-client) >= 5.3.4
Requires:  python3dist(nbformat) >= 5
Requires:  python3dist(async-generator)
Requires:  python3dist(nest-asyncio)

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
# disable test_many_parallel_notebooks
# This should be fixed in a future version
# https://github.com/jupyter/nbclient/pull/74#issuecomment-635929953
%pytest -v -k 'not test_many_parallel_notebooks'
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun Feb 28 2021 Lumír Balhar <lbalhar@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 17:08:21 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.5.1-3
- Bootstrap for Python 3.10

* Sat Nov 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.1-2
- Change pytest invocation
- use py_provides macro

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.5.1-1
- Initial package.
