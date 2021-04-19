# FIXME: Test won't work offline
%bcond_with check

%global sysname bst_external

Name:           bst-external
Version:        0.21.0
Release:        3%{?dist}
Summary:        Additional BuildStream plugins

License:        LGPLv2+
URL:            https://gitlab.com/BuildStream/bst-external
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Switch from pytoml to toml
Patch1:         %{url}/-/merge_requests/131.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)
%if %{with check}
# FIXME: Packaged was retired in Fedora
# * https://bugzilla.redhat.com/show_bug.cgi?id=1839789
# * https://gitlab.com/BuildStream/bst-external/-/issues/44
#BuildRequires:  python3dist(pep8)
#BuildRequires:  python3dist(pytest-pep8)

#BuildRequires:  python3dist(pytest-env)
BuildRequires:  python3dist(buildstream)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-datafiles)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(ruamel.yaml)
%endif

%description
A collection of BuildStream plugins that don't fit in with the core plugins for
whatever reason.


%prep
%autosetup -p1
sed 's|coverage == 4.4.0|coverage|' -i setup.py


%build
%py3_build


%install
%py3_install


%if %{with check}
%check
export PATH=%{buildroot}%{_bindir}:${PATH} 
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{python3} -m pytest -v
%endif


%files
%license LICENSE
%doc README.rst NEWS MAINTAINERS
%{python3_sitelib}/%{sysname}/
%{python3_sitelib}/BuildStream_external-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Miro Hrončok <mhroncok@redhat.com> - 0.21.0-2
- Switch from pytoml to toml
- Fixes: rhbz#1899488

* Sat Oct  3 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.21.0-1
- Update to 0.21.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.0-2
- Adapt for Fedora packaging guidelines

* Sun Mar 01 2020 gasinvein <gasinvein@gmail.com> - 0.20.0-1
- new version

* Wed Nov 27 2019 gasinvein <gasinvein@gmail.com> - 0.19.1-1
- new version

* Fri Sep 27 2019 gasinvein <gasinvein@gmail.com> - 0.18.0-1
- new version

* Sat Jun  8 2019 gasinvein <gasinvein@gmail.com>
- Initial package
