Name:           wfuzz
Version:        3.1.0
Release:        2%{?dist}
Summary:        Web fuzzer

License:        GPLv2
URL:            http://wfuzz.io
Source0:        https://github.com/xmendez/wfuzz/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-netaddr
BuildRequires:  python3-setuptools

%description
Wfuzz has been created to facilitate the task in web applications assessments
and it is based on a simple concept: it replaces any reference to the FUZZ
keyword by the value of a given payload.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-alabaster

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup
rm -rf %{name}.egg-info
# Remove shebang
sed -i -e '/^#!\//, 1d' src/wfuzz/wfuzz.py
# Remove release pinning 
sed -i -e 's/pyparsing>=2.4\*/pyparsing>=2.4/g' setup.py
# We don't need this as we have the whole documentation
sed -i -e '/data_files/d' setup.py

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wfencode
%{_bindir}/wfpayload
%{_bindir}/wfuzz
%{_bindir}/wxfuzz
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py*.egg-info/

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to new upstream release 3.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.5-4
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-3
- Fix changelog entries

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-2
- Create docs

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-1
- Initial package for Fedora
