%global srcname uamqp
%global _description %{expand:An AMQP 1.0 client library for Python.}

Name:           python-%{srcname}
Version:        1.2.15
Release:        1%{?dist}
Summary:        AMQP 1.0 client library for Python

License:        MIT
URL:            https://github.com/Azure/azure-uamqp-python/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fix build with GCC 11
Patch0:         %{name}-1.2.14-gcc11.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist setuptools}
# Required for tests
BuildRequires:  %{py3_dist certifi}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist six}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n azure-uamqp-python-%{version} -p0

# Remove bundled egg-info
rm -rf *.egg-info


%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=strict-aliasing"
export CXXFLAGS=$CFLAGS
VERBOSE=1 %py3_build


%install
%py3_install

rm $RPM_BUILD_ROOT%{python3_sitearch}/%{srcname}/*.c


%check
%pytest tests/


%files -n python3-%{srcname}
%doc HISTORY.rst README.rst
%license LICENSE
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info/


%changelog
* Sun Mar 21 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15

* Sat Feb 13 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.14-1
- Update to 1.2.14

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Fri Dec 11 2020 Jeff Law <law@redhat.com> - 1.2.11-2
- Fix prototype/definition mismatch caught by gcc-11

* Fri Oct 02 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.11-1
- Update to 1.2.11

* Tue Aug 18 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.10-1
- Update to 1.2.10

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9

* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.8-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.8-1
- Initial RPM release
