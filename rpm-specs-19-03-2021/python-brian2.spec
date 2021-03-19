%bcond_with tests

%global srcname brian2
%global pretty_name Brian2

# Documents disabled for the moment
%bcond_with docs

%global desc %{expand: \
Brian2 is a simulator for spiking neural networks available on almost all
platforms. The motivation for this project is that a simulator should not only
save the time of processors, but also the time of scientists.

It is the successor of Brian1 and shares its approach of being highly flexible
and easily extensible. It is based on a code generation framework that allows
to execute simulations using other programming languages and/or on different
devices.

Please report issues to the github issue tracker
(https://github.com/brian-team/brian2/issues) or to the brian support mailing
list (http://groups.google.com/group/briansupport/)

Documentation for Brian2 can be found at http://brian2.readthedocs.org}

Name:           python-%{srcname}
Version:        2.4.2
Release:        2%{?dist}
Summary:        A clock-driven simulator for spiking neural networks


License:        CeCILL
URL:            https://pypi.python.org/pypi/%{pretty_name}
Source0:        %pypi_source %{pretty_name}
Patch0:         0001-Brian2-2.2-remove-crosscompiling.patch

BuildRequires:  gcc-c++ gcc
BuildRequires:  gsl-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython} >= 0.18
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist nose}
%if %{with docs}
BuildRequires:  %{py3_dist sphinx}
%endif
BuildRequires:  %{py3_dist numpy} >= 1.10
BuildRequires:  %{py3_dist sympy} >= 0.7.6
BuildRequires:  %{py3_dist pyparsing}
BuildRequires:  %{py3_dist jinja2}
BuildRequires:  %{py3_dist py-cpuinfo}

# For code generation
Requires:       %{py3_dist Cython} >= 0.18
Requires:       %{py3_dist numpy} >= 1.10
Requires:       %{py3_dist sympy} >= 0.7.6
Requires:       %{py3_dist pyparsing}
Requires:       %{py3_dist jinja2}
Requires:       %{py3_dist py-cpuinfo}

Suggests:       %{py3_dist ipython}
%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{desc}

%package doc
Summary:    %{summary}
BuildArch:  noarch

%description doc
Documentation and examples for %{name}.


%prep
%autosetup -n %{pretty_name}-%{version}

# Remove unnecessary files
find . -name ".gitignore" -print -delete
rm -rvf %{pretty_name}.egg-info
rm -f brian2/synapses/cythonspikequeue.cpp
# Remove this since it is only an issue on Windows systems
sed -i 's|, !=4.0.0||' setup.py

# Correct shebang for examples
find examples -name "*.py" -print -exec sed -i 's|^#!/usr/bin/env python|#!/usr/bin/python3|' '{}' \;


%build
%py3_build
%if %{with docs}
# Build documentation
PYTHONPATH=.
sphinx-build-3 docs_sphinx html
%endif

%install
%py3_install

%check
%if %{with tests}
# We cannot use the local build because the codebase is still py2 and uses 2to3
# to convert to py3 during the build process and install the converted bits, so
# we *must* point to the installed version for tests
# https://github.com/brian-team/brian2/issues/1027
export PYTHONDONTWRITEBYTECODE=1
# remove since we dont want it to use this version
rm -rf %{srcname}
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitearch}/ %{__python3} -c 'import brian2; brian2.test()'
%endif

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%doc README.rst

%files doc
%license LICENSE
%doc examples
%if %{with docs}
%doc html
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4.2-1
- Update to 2.4.2

* Tue Sep 29 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4.1-1
- Update to 2.4.1

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-1
- Update to 2.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0.2-2
- Rebuilt for Python 3.9

* Tue Apr 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.3.0.2-1
- Update to latest release

* Sat Apr 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.3.0.1-1
- Update to latest upstream release

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.3-1
- Update to latest release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.2.2.1-1
- Update to latest upstream release
- Remove AUTHORS, tutorials that are no longer included in tar

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.2-1
- Initial build
