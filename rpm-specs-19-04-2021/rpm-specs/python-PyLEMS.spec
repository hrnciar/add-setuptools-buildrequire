%global srcname PyLEMS
%global libname pylems

# Require network, so run locally on mock with --enable-network
%bcond_with tests

%global _description \
A LEMS (http://lems.github.io/LEMS) simulator written in Python which can be \
used to run NeuroML2 (http://neuroml.org/neuroml2.php) models.


Name:           python-%{srcname}
Version:        0.5.2
Release:        1%{?dist}
Summary:        LEMS interpreter implemented in Python

License:        LGPLv3

# Use github source. Pypi source does not include license and examples.
URL:            https://github.com/LEMS/%{libname}/
Source0:        %{url}/archive/v%{version}/%{libname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist lxml}
BuildRequires:  %{py3_dist setuptools}
Requires:  %{py3_dist lxml}
Requires:  %{py3_dist matplotlib}
Requires:  %{py3_dist numpy}
%if %{with tests}
BuildRequires:  %{py3_dist nose}
%endif
%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{_description}

%package doc
Summary: %{summary}

%description doc
%{_description}


%prep
%autosetup -n %{libname}-%{version}

# remove shebang
sed -i '1d' lems/dlems/exportdlems.py

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
# From test*sh scripts in the source and .travis.yml
# A lot of the tests use files from other software repositories, so we can't use them.
nosetests-3
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest2.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/loadtest.py
%endif

%files -n python3-%{srcname}
%license LICENSE.lesser
%doc README.md
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/lems
%{_bindir}/%{libname}

%files doc
%license LICENSE.lesser
%doc README.md examples

%changelog
* Thu Feb 18 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-1
- Update to 0.5.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-3
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-1
- Update to new release
- remove py2 bits

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.9.1-1
- Initial build
