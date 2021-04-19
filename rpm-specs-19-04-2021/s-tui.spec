%global sys_name s_tui

Name:       s-tui
Version:    1.1.1
Release:    1%{?dist}
Summary:    Terminal-based CPU stress and monitoring utility
BuildArch:  noarch

License:    GPLv2+
URL:        https://github.com/amanusk/s-tui
Source0:    %{pypi_source}
Source1:    https://raw.githubusercontent.com/amanusk/%{name}/master/LICENSE

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)

Recommends: stress-ng

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and
utilization in a graphical way from the terminal.

What it does

  * Monitoring your CPU temperature/utilization/frequency/power
  * Shows performance dips caused by thermal throttling
  * Requires no X-server
  * Built in options for stressing the CPU (stress/stress-ng/FIRESTARTER)}


%prep
%autosetup -p1

# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%py3_build


%install
%py3_install
install -Dpm0644 %{SOURCE1} -t %{buildroot}%{_licensedir}/%{name}/

# Remove shebang from Python libraries
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%files

# Provide license file on PyPI
# https://github.com/amanusk/s-tui/issues/172
%license LICENSE

%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{sys_name}/


%changelog
* Tue Mar 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.1-1
- Initial package
