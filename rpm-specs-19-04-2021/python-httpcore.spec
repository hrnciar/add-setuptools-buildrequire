%global pypi_name httpcore

Name:           python-%{pypi_name}
Version:        0.12.3
Release:        1%{?dist}
Summary:        Minimal low-level HTTP client

License:        BSD
URL:            https://github.com/encode/httpcore
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 29 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.3-1
- Update to latest upstream release 0.12.2 (#1921813)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.2-1
- Enable dependency generator (#1897850)
- Update to latest upstream release 0.12.2 (#1895584)

* Sun Nov 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.1-1
- Update to latest upstream release 0.12.1 (#1895584)

* Fri Oct  9 16:39:18 -03 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.12.0-1
- Update to latest upstream release 0.12.0

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.1-1
- Update to latest upstream release 0.11.1 (#1883308)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-1
- Update to latest upstream release 0.11.0 (#1881374)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.2-1
- Update to latest upstream release 0.10.2 (#1875285)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Initial package for Fedora
