%bcond_without tests

%global pypi_name rdflib-jsonld

%global _description %{expand:
This is an implementation of JSON-LD for RDFLib. JSON-LD is a lightweight
Linked Data format. It is easy for humans to read and write. It is based on
the already successful JSON format and provides a way to help JSON data
inter operate at Web-scale.

This implementation will:
- Read in an JSON-LD formatted document and create an RDF graph
- Serialize an RDF graph to JSON-LD formatted output}

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Python rdflib extension adding JSON-LD parser and serializer

License:        BSD
URL:            https://github.com/RDFLib/rdflib-jsonld
Source0:        %{pypi_source}

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist rdflib}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist flake8}
%endif

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}
BuildRequires:	%{py3_dist sphinx}

%description doc %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

# Build documentation
PYTHONPATH=. sphinx-build-%{python3_version} docs html
rm -rvf html/.buildinfo
rm -rvf html/.doctrees

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=. pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/rdflib_jsonld/
%{python3_sitelib}/rdflib_jsonld-%{version}-py%{python3_version}.egg-info/

%files doc
%license LICENSE.md
%doc html

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.5.0-1
- Initial build
