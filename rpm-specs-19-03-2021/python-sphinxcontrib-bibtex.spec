%global srcname sphinxcontrib-bibtex

Name:           python-%{srcname}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Sphinx extension for BibTeX style citations

License:        BSD
URL:            https://github.com/mcmtroffaes/sphinxcontrib-bibtex
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python-sphinx-doc
BuildRequires:  %{py3_dist pybtex}
BuildRequires:  %{py3_dist pybtex-docutils}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx}

%global common_desc %{expand:
This package contains a Sphinx extension for BibTeX style citations.

This extension allows BibTeX citations to be inserted into documentation
generated by Sphinx, via a bibliography directive, and a cite role,
which work similarly to LaTeX's thebibliography environment and \\cite
command.

For formatting, the extension relies on pybtex, written by Andrey
Golovizin.}

%description %common_desc

%package -n python3-%{srcname}
Summary:        Sphinx extension for BibTeX style citations
Provides:       bundled(jquery)
Provides:       bundled(js-underscore)

%description -n python3-%{srcname} %common_desc

%package doc
Summary:        Documentation for python-%{srcname}

%description doc
Documentation for python-%{srcname}.

%prep
%autosetup -p0 -n %{srcname}-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -e "s|\('http://www\.sphinx-doc\.org/en/master/', \)None|\1'%{_docdir}/python-sphinx-doc/html/objects.inv'|" \
    -i doc/conf.py

%build
%py3_build

# Build documentation
PYTHONPATH=$PWD sphinx-build doc html
rm -fr html/{.buildinfo,.doctrees}
rst2html --no-datestamp LICENSE.rst LICENSE.html

%install
%py3_install

%check
PYTHONPATH=$PWD pytest

%files -n python3-%{srcname}
%license LICENSE.html
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_bibtex*

%files doc
%doc html/*

%changelog
* Fri Mar  5 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Version 2.2.0
- Drop upstreamed -sphinx3.5 patch

* Fri Feb 19 2021 Jerry James <loganjerry@gmail.com> - 2.1.4-3
- Add -sphinx3.5 patch to fix FTBFS with Sphinx 3.5 (bz 1930799)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Jerry James <loganjerry@gmail.com> - 2.1.4-1
- Version 2.1.4

* Fri Jan  1 2021 Jerry James <loganjerry@gmail.com> - 2.1.3-1
- Version 2.1.3

* Wed Dec 30 2020 Jerry James <loganjerry@gmail.com> - 2.1.2-1
- Version 2.1.2

* Tue Dec 29 2020 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Version 2.1.1
- Drop orderedset dependency and patch

* Tue Dec 22 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 1.0.0-2
- Use the pyproject macros
- Fix documentation cross-references

* Fri Sep 20 2019 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- New upstream version

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0~a0.20170423git5fa80ec5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~a0.20170423git5fa80ec5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0~a0.20170423git5fa80ec5-1
- Update to git snapshot 5fa80ec5 for Sphinx 2 compatibility (#1698477)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 0.4.2-1
- New upstream version
- Drop upstreamed -bibliography patch

* Sat Dec  8 2018 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- New upstream version

* Thu Oct 25 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-4
- Subpackage python2-sphinxcontrib-bibtex has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.7

* Thu Apr 19 2018 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Jerry James <loganjerry@gmail.com> - 0.3.6-1
- New upstream version
- Drop upstreamed python 3.6 fix

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jerry James <loganjerry@gmail.com> - 0.3.5-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-2
- Rebuild for Python 3.6

* Mon May 23 2016 Jerry James <loganjerry@gmail.com> - 0.3.4-1
- New upstream version

* Thu Feb 25 2016 Jerry James <loganjerry@gmail.com> - 0.3.3-1
- Initial RPM
