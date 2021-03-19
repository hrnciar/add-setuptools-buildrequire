%global srcname ncclient

Name:           python-ncclient
Version:        0.6.10
Release:        2%{?dist}
%global forgeurl https://github.com/%{srcname}/%{srcname}/
%forgemeta
Summary:        Python library for the NETCONF protocol

License:        ASL 2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

# https://github.com/ncclient/ncclient/pull/483
# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock
Patch0:         %{srcname}-0.6.10-use-mock-from-stdlib-unittest.patch
# https://github.com/ncclient/ncclient/pull/484
# https://fedoraproject.org/wiki/Changes/DeprecateNose
Patch1:         %{srcname}-0.6.10-allow-running-tests-without-nose.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global common_description %{expand:
%{srcname} is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol. %{srcname} was
developed by Shikar Bhushan.net). It is now maintained by Leonidas Poulopoulos
(@leopoul) and Einar Nilsen-Nygaard (@einarnn).

Docs: http://%{srcname}.readthedocs.org

PyPI: https://pypi.python.org/pypi/%{srcname}}

%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}


%package doc
Summary:        Documentation and examples for %{name}

BuildRequires:  make
# docs/requirements.txt
BuildRequires:  python3dist(sphinx) >= 3.2.0

%description doc
The %{name}-doc package contains detailed documentation and examples
for %{name}.


%generate_buildrequires
%pyproject_buildrequires -t


%prep
%autosetup -n %{srcname}-%{version} -p1
%py3_shebang_fix examples
# Do not install nose; it is deprecated, and is no longer a hard requirement
# for the tests:
sed -r -i '/^nose$/d' test-requirements.txt


%build
%pyproject_wheel

%make_build -C docs html SPHINXOPTS='%{?_smp_mflags}'
rm -vf docs/build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%tox

 
%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE


%files doc
%license LICENSE
%doc Changelog
%doc NOTICE
%doc README.md
%doc README.rst
%doc docs/build/html
%doc examples


%changelog
* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.6.10-2
- Patch out BR on deprecated python3-mock
- Patch out BR on deprecated python3-nose

* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.6.10-1
- Update to 0.16.10
- Drop python-ncclient-0.6.9-shebangs.patch, now upstreamed
- Drop python3dist(setuptools) BR, redundant with pyproject-rpm-macros

* Tue Mar 02 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.6.9-2
- Rebuild for fixed RHBZ#1925963 in pyproject-rpm-macros-0-38
- Enable parallel Sphinx build

* Fri Jan  1 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.6.9-1
- Prepare for unretirement
- New upstream version 0.6.9
- Migrate from Python 2 to Python 3
- Use new macros for source URL and build/install/test sections, and drop old
  macros like python_provide
- Use generated Requires and BuildRequires
- Split documentation and examples into a separate -doc subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.7-5
- Python 2 binary package renamed to python2-ncclient
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 08 2016 Ihar Hrachyshka <ihrachys@redhat.com> 0.4.7-1.el7
- Update to 0.4.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec  5 2014 Ihar Hrachyshka <ihrachys@redhat.com> - 0.4.2-2
- Added missing python-setuptools as a build dependency.
- Include documentation and examples.
- Run unit tests on build.
- Rebuild egg file.
- Added python2 macros needed for el6.
- Made python macros more specific (python -> python2).
- Made python2_sitelib file inclusion wildcard a bit more strict.

* Thu Dec  4 2014 Ihar Hrachyshka <ihrachys@redhat.com> - 0.4.2-1
- Updated to upstream 0.4.2 version

* Thu Aug  7 2014 Ihar Hrachyshka <ihrachys@redhat.com> - 0.4.1-1
- Initial package for Fedora
