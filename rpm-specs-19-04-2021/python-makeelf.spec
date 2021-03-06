%global pypi_name makeelf

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        4%{?dist}
Summary:        ELF reader-writer library

License:        GPLv3+
URL:            https://github.com/v3l0c1r4pt0r/makeelf
Source0:        %{pypi_source}
BuildArch:      noarch

%description
MakeELF is a Python library to parse, modify and create ELF binaries. It
provides following features:

- easy to use, standard Python interface
- reading existing ELF files to Python representation
- modification of every aspect of ELF format structures
- ability to skip any validation to test other parsers for potential errors
- creating new valid ELF files with just one step

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MakeELF is a Python library to parse, modify and create ELF binaries. It
provides following features:

- easy to use, standard Python interface
- reading existing ELF files to Python representation
- modification of every aspect of ELF format structures
- ability to skip any validation to test other parsers for potential errors
- creating new valid ELF files with just one step

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebang
sed -i -e '/^#!\//, 1d' {*/*.py,*/*/*.py}
# Fix encoding
sed -i "s|\r||g" README.txt

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-1
- Initial package for Fedora
