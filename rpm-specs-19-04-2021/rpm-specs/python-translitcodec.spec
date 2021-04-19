%global pypi_name translitcodec

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Unicode to 8-bit charset transliteration codec

License:        MIT
URL:            http://pypi.python.org/pypi/translitcodec/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
Best-effort representations using smaller coded character sets
(ASCII, ISO 8859, etc.).



%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Best-effort representations using smaller coded character sets
(ASCII, ISO 8859, etc.).


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Sun Mar 21 2021 Neal Gompa <ngompa13@gmail.com> - 0.6.0-1
- Initial package.
