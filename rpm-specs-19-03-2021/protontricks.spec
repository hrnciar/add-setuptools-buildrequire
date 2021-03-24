%bcond_with tests

Name:       protontricks
Version:    1.4.4
Release:    1%{?dist}
Summary:    Simple wrapper that does winetricks things for Proton enabled games
BuildArch:  noarch

License:    GPLv3+
URL:        https://github.com/Matoking/protontricks

# GitHub tarball won't work for setuptools-scm
Source0:    %{pypi_source %{name}}

BuildRequires: python3-devel >= 3.5
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(vdf)
%if %{with tests}
BuildRequires: python3dist(pytest-cov) >= 2.10
BuildRequires: python3dist(pytest) >= 6.0
%endif

Requires:   winetricks

%description
A simple wrapper that does winetricks things for Proton enabled games,
requires Winetricks.

This is a fork of the original project created by sirmentio. The original
repository is available at Sirmentio/protontricks.


%prep
%autosetup -p1
sed -e '/\/usr\/bin\/env/d' -i src/%{name}/cli.py


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%{python3} -m pytest -v
%endif


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*.egg-info


%changelog
* Wed Feb 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.4-1
- build(update): 1.4.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.3-3
- build: polish to conform Fedora guidelines

* Mon Dec 28 2020 gasinvein <gasinvein@gmail.com> - 1.4.3-0.1
- Initial package
