%global pypi_name matplotlib-scalebar

%global _description %{expand:
Provides a new artist for matplotlib to display a scale bar, aka micron bar. It
is particularly useful when displaying calibrated images plotted using
plt.imshow(…).  The artist supports customization either directly from the
ScaleBar object or from the matplotlibrc.}



Name:           python-%{pypi_name}
Version:        0.7.2
Release:        1%{?dist}
Summary:        Artist for matplotlib to display a scale bar

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source %{pypi_name}

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' matplotlib_scalebar/test*py

%build
%py3_build

%install
%py3_install

%check
%{pytest}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/matplotlib_scalebar-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/matplotlib_scalebar

%changelog
* Sat Jan 30 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2 (#1922612)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7.1-1
- Update to latest release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-3
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-1
- Update to new version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.1-1
- Update to latest release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-1
- Initial build
