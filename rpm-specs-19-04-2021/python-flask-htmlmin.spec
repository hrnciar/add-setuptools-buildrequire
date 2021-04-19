%global desc Minify flask text/html mime types responses. Just add MINIFY_PAGE = True to \
your deployment config to minify html and text responses of your flask \
application.

%global pkg_name flask-htmlmin
%global mod_name Flask-HTMLmin

Name:       python-%{pkg_name}
Version:    2.1.0
Release:    2%{?dist}
Summary:    Flask html response minifier
License:    BSD
URL:        https://github.com/hamidfzm/%{mod_name}
Source0:    https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-htmlmin
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest-runner

%description
%{desc}

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary:    %{summary}
BuildRequires:   python%{python3_pkgversion}-flask

Requires:  python%{python3_pkgversion}-flask
Requires:  python%{python3_pkgversion}-htmlmin

%py_provides python3-%{python3_pkgversion}-%{pkg_name}

%description -n python%{python3_pkgversion}-%{pkg_name}
%{desc}

%prep
%autosetup -n %{mod_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{pkg_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/flask_htmlmin/*.py
%{python3_sitelib}/flask_htmlmin/__pycache__/*.py*
%{python3_sitelib}/*.egg-info/

%changelog
* Sat Mar 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-2
- Cosmetic changes

* Mon Mar 08 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-1
- New version - 2.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.0.2-1
- 2.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-3
- Subpackage python2-flask-htmlmin has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 26 2018  Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.4.0-2
- include pytest-runner in builrequires

* Sun Aug 26 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.4.0-1
- 1.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.3.1-1
- Initial package
