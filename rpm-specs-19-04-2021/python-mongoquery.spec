%global srcname mongoquery

Name:           python-%{srcname}
Version:        1.3.6
Release:        6%{?dist}
Summary:        Python implementation of mongodb queries

License:        Unlicense
URL:            https://github.com/kapouille/%{srcname}
Source0:        %{url}}/%{srcname}/archive/%{version}.tar.gz
BuildArch:      noarch

%description
A utility library that provides a MongoDB-like query language for querying
Python collections. It's mainly intended to parse objects structured as
fundamental types in a similar fashion to what is produced by JSON or YAML
parsers. It follows the specification of queries for MongoDB version 3.2.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A utility library that provides a MongoDB-like query language for querying
Python collections. It's mainly intended to parse objects structured as
fundamental types in a similar fashion to what is produced by JSON or YAML
parsers. It follows the specification of queries for MongoDB version 3.2.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.6-5
- Clean-up spec file

* Wed Aug 05 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.6-4
- BuildRequires python3-setuptools, fix RHBZ#1850951

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-2
- Rebuilt for Python 3.9

* Mon Feb 03 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.6-1
- Release 1.3.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.5-1
- Update to latest upstream: 1.3.5
- Drop Python 2 support

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.3-1
- Update to latest upstream: 1.3.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuild for Python 3.6

* Thu Jun 02 2016 Josef Skladanka <jskladan@redhat.com> - 1.1.0-1
- initial packaging
