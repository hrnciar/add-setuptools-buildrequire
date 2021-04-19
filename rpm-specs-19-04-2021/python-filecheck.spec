%bcond_without check
%global pypi_name filecheck
%global commit 65c0d93c98024b3e7656d4e44bebd8381178951d
%global shortcommit %%(c=%{commit}; echo ${c:0:7})

%global desc Python port of LLVM's FileCheck, flexible pattern matching file verifier.

Name: python-%{pypi_name}
Version: 0.0.17
Release: 2%{?dist}
Summary: Flexible pattern matching file verifier
License: ASL 2.0
URL: https://github.com/mull-project/FileCheck.py
Source0: https://github.com/mull-project/FileCheck.py/archive/%{commit}/%{pypi_name}-%{shortcommit}.tar.gz
# upstream testsuite includes only x86_64 reference binaries and Fedora llvm9.0 package doesn't include FileCheck
# https://bugzilla.redhat.com/show_bug.cgi?id=1939414
Patch0: %{name}-tests-x86_64.patch
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-poetry
BuildRequires: sed
%if %{with check}
BuildRequires: %{_bindir}/invoke
BuildRequires: %{_bindir}/lit
BuildRequires: %{_bindir}/python
BuildRequires: gcc
%endif

%description -n python3-%{pypi_name}
%{desc}

%prep
%setup -q -n FileCheck.py-%{commit}
%patch0 -p1 -b .orig
sed -i -e '/#!.*python3/d' filecheck/FileCheck.py

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with check}
%check
# lit seems to overwrite PYTHONPATH, so inject the buildroot paths directly
if ! grep -q %{buildroot} tests/integration/tests/examples/lit-and-filecheck/lit.local.cfg ; then
cat << __EOF__ >> tests/integration/tests/examples/lit-and-filecheck/lit.local.cfg

config.environment['PYTHONPATH'] = '%{buildroot}%{python3_sitelib}'
config.environment['PATH'] = '${PATH}:%{buildroot}%{_bindir}'
__EOF__
fi
%{_bindir}/invoke -e test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Mon Mar 15 2021 Dominik Mierzejewski <dominik@greysector.net> 0.0.17-2
- enable testsuite
- drop shebang from module source
- run testsuite only on x86_64

* Sun Jan 24 2021 Dominik Mierzejewski <dominik@greysector.net> 0.0.17-1
- initial build
