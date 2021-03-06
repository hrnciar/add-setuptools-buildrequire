%global srcname pytest-astropy
%global sum The py.test astropy plugin

Name:           python-%{srcname}
Version:        0.8.0
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-arraydiff}
BuildRequires:  %{py3_dist pytest-astropy-header}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist pytest-doctestplus}
BuildRequires:  %{py3_dist pytest-filter-subpackage}
BuildRequires:  %{py3_dist pytest-openfiles}
BuildRequires:  %{py3_dist pytest-remotedata}
BuildRequires:  %{py3_dist hypothesis}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist setuptools_scm}

%description
This package provides a plugin for the pytest framework that is used for
testing Astropy and its affiliated packages. 


%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
This package provides a plugin for the pytest framework that is used for
testing Astropy and its affiliated packages. 


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{srcname}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 13:49:36 CET 2020 Christian Dersch <lupinix@fedoraproject.org> - 0.8.0-1
- new version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Christian Dersch <lupinix@fedoraproject.org> - 0.7.0-1
- new version

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.5.0-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.4.0-1
- new version

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.7

* Sat Mar 17 2018 Christian Dersch <lupinix@mailbox.org> - 0.2.0-1
- initial packaging effort

