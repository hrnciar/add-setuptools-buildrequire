# XXX 1: that they bundle one file in _plotly_utils: png.py, which is in the
# pypng module. However, it is unclear if they're actively tracking the
# upstream code so we just use their bundled copy.

# XXX 2: There are empty files in the _plotly_future directory but they are
# required and cannot be removed

# They do not include tests in the pypi tar, and they don't make GitHub
# releases only for the Python package---the GitHub tar also includes their JS
# etc. bits which we don't need here.
# Leave this here in case they do start including tests in their PyPi tar.
%bcond_with tests

%global pypi_name plotly

%global _description %{expand:
plotly.py is an interactive, open-source, and browser-based graphing library
for Python.

Built on top of plotly.js, plotly.py is a high-level, declarative charting
library. plotly.js ships with over 30 chart types, including scientific charts,
3D graphs, statistical charts, SVG maps, financial charts, and more.

plotly.py is MIT Licensed. Plotly graphs can be viewed in Jupyter notebooks,
standalone HTML files, or hosted online using Chart Studio Cloud.

Documentation is available at https://plotly.com/python/}

Name:           python-%{pypi_name}
Version:        4.14.3
Release:        1%{?dist}
Summary:        An open-source, interactive data visualization library

# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
License:        MIT
URL:            https://plotly.com/python/
Source0:        %pypi_source

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For jupyter configs etc.
Requires:       python-jupyter-filesystem
Recommends:     python3-notebook
# For tests, but see note at top of spec
# https://github.com/plotly/plotly.py/blob/master/.circleci/config.yml
# https://github.com/plotly/plotly.py/blob/6c463ee500960000341cc735b2d95680ac48e3ad/packages/python/plotly/tox.ini
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Fix one file
sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' _plotly_utils/png.py
chmod -x _plotly_utils/png.py

%build
%py3_build

%install
%py3_install

# Move to correct location
mkdir -p -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/jupyter/nbconfig/notebook.d/
mv -v $RPM_BUILD_ROOT/%{_prefix}/%{_sysconfdir}/jupyter/nbconfig/notebook.d/plotlywidget.json $RPM_BUILD_ROOT/%{_sysconfdir}/jupyter/nbconfig/notebook.d/plotlywidget.json
rm -rfv $RPM_BUILD_ROOT/%{_prefix}/%{_sysconfdir}/jupyter/nbconfig/notebook.d/

%check
%if %{with tests}
pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/_%{pypi_name}_utils
%{python3_sitelib}/_%{pypi_name}_future_
%{python3_sitelib}/%{pypi_name}widget
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/plotlywidget.json
%{_datadir}/jupyter/nbextensions/plotlywidget

%changelog
* Fri Apr 16 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.14.3-1
- Remove sphinx dep
- use macros

* Wed Apr 14 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.14.3-1
- Initial build
