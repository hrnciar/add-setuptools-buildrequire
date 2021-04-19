%global srcname fissix

%bcond_without tests

Name:           python-%{srcname}
Version:        20.8.0
Release:        2%{?dist}
Summary:        Monkeypatches to override default behavior of lib2to3
License:        Python
URL:            https://github.com/jreese/fissix
Source0:        %{pypi_source}
Patch0:         %{srcname}-dont_ship_tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-test
BuildRequires:  %{py3_dist appdirs}
BuildRequires:  %{py3_dist pytest}
%endif


%global _description %{expand:
Backport of latest lib2to3, with enhancements.}


%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}
# not sure why but automatic requires don't work
Requires:       %{py3_dist appdirs}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i '1d' fissix/pgen2/token.py


%build
%py3_build


%install
%py3_install
cp -p fissix/*.txt %{buildroot}%{python3_sitelib}/%{srcname}/


%check
# mv fissix-tests fissix/tests
%{python3} -m pytest --verbose fissix/tests


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-1
- Initial package
