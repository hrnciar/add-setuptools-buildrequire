%global pypi_name hashID

Name:           hashid
Version:        3.1.4
Release:        9%{?dist}
Summary:        Tool to identify different types of hashes

License:        GPLv3+
URL:            https://github.com/psypanda/hashID
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Identify the different types of hashes used to encrypt data and especially
passwords. hashID is a tool which supports the identification of over 220
unique hash types using regular expressions.

It is able to identify a single hash, parse a file or read multiple files in
a directory and identify the hashes within them.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' hashid.py

%build
%py3_build

%install
%py3_install
install -Dp -m 0644 doc/man/%{name}.7 %{buildroot}%{_mandir}/man7/%{name}.7

%files
%doc README.rst doc/CHANGELOG
%license doc/LICENSE
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.4-7
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.4-1
- Initial package for Fedora
