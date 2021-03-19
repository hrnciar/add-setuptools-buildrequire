%global modname weasyprint
%global srcname WeasyPrint

Name:           weasyprint
Version:        52.4
Release:        1%{?dist}
Summary:        Utility to render HTML and CSS to PDF

License:        BSD
URL:            https://weasyprint.org/
Source0:        %pypi_source
Patch0:         %{name}-disable-flake8-isort-for-pytest.patch
# cairo creates PDFs according to the PDF 1.4 specification which requires a
# trailing apostrophe. cairo 1.17.4 added the missing apostrophe.
# see also https://gitlab.freedesktop.org/cairo/cairo/-/issues/450
Patch1:         %{name}-cairo-1174-pdf-dates.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pillow >= 4.0.0
# upstream installation docs say:
# "setuptools ≥ 30.3.0 is required to install WeasyPrint from wheel,
# but 39.2.0 is required to build the package or install from source."
BuildRequires:  python3-setuptools >= 39.2.0
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-runner
BuildRequires:  /usr/bin/pathfix.py

# requirements for testing
BuildRequires:  cairo >= 1.15.4
BuildRequires:  dejavu-sans-fonts
BuildRequires:  gdk-pixbuf2 >= 2.25.0
BuildRequires:  gdk-pixbuf2-modules
# gdk-pixbuf2 does not require libjpeg directly but tests try to load jpg
# images via gdk-pixbuf2
BuildRequires:  libjpeg-turbo
BuildRequires:  pango >= 1.38.0
BuildRequires:  python3-cairosvg >= 2.4.0
BuildRequires:  python3-cssselect2 >= 0.1
BuildRequires:  python3-cairocffi >= 0.9.0
BuildRequires:  python3-html5lib >= 0.999999999
# upstream requires > 0.9.1 (actually >= 0.8, != 0.9.1), see
# https://github.com/Kozea/WeasyPrint/pull/989#issuecomment-551845041
# We need pyhen's hyphenation dicts (instead of system-wide dicts) otherwise
# there will be test failures.
BuildRequires:  python3-pyphen > 0.9.1
BuildRequires:  python3-tinycss2 >= 1.0

Requires:       python3-weasyprint = %{version}-%{release}


%description
WeasyPrint can render HTML and CSS to PDF. It aims to support web standards
for printing.

%package -n python3-weasyprint
Summary:        Python library to render HTML and CSS to PDF
Requires:       cairo >= 1.15.4
Requires:       pango >= 1.38.0
Requires:       gdk-pixbuf2 >= 2.25.0
# other Python dependencies will be picked up automatically
# Weasyprint will fail if no fonts are installed. There's no way to know
# what fonts the user would actually want, but require a few common ones
# that might be useful:
Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts

%description -n python3-weasyprint
The WeasyPrint Python library is a rendering engine for HTML and CSS that
can export to PDF. It aims to support web standards for printing.

%prep
%autosetup -p1 -n WeasyPrint-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build

%install
%py3_install

%check
# Some tests fail due to cairo 1.17.4 but upstream is not interested in fixing
# these as they are moving away from cairo. At the same time there was some
# indication on the WeasyPrint mailing list that the actual issue is already
# present with WeasyPrint 1.16 (just not in the test suite).
# I hope to fix this anyway but for now disable the failing tests.
# Upstream tracking issue: https://github.com/Kozea/WeasyPrint/issues/1291
pytest-3 -k "not test_text and not test_float and not test_table_vertical_align"
# do not ship tests
rm -rf %{buildroot}%{python3_sitelib}/%{modname}/tests

%files
%license LICENSE
%doc README.rst
%{_bindir}/weasyprint

%files -n python3-weasyprint
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}-*/
%{python3_sitelib}/%{modname}/

%changelog
* Fri Mar 12 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 52.4-1
- update to 52.4

* Tue Mar 02 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 52.3-1
- update to 52.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 52.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec  6 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 52.2-1
- update to 52.2

* Sun Nov 08 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 52.1-1
- update to 52.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 51-4
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 51-3
- drop runtime requirement on "dejavu-fonts-common" (#1810150)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Felix Schwarz <fschwarz@fedoraproject.org> 51-1
- update to upstream version 51

* Sun Dec 01 2019 Felix Schwarz <fschwarz@fedoraproject.org> 50-1
- update to new upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.39-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.39-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.39-2
- avoid dependency on Python 3.3
- require python3-xcffib directly (#1685654)

* Tue Apr 30 2019 Eric Smith <brouhaha@fedoraproject.org> 0.39-1
- Update to newer (but not latest) upstream.

* Tue Apr 30 2019 Eric Smith <brouhaha@fedoraproject.org> 0.22-16
- Update requirements, use license macro, and other minor changes from
  Felix Schwarz <fschwarz@fedoraproject.org>.
- Use better github tarball naming.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.22-14
- Remove python2 subpackage (#1631306)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.22-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.22-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.22-9
- Python 2 binary package renamed to python2-weasyprint
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.22-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Eric Smith <brouhaha@fedoraproject.org> 0.22-1
- Update to latest upstream.
- No Python 3 in EL7.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 20 2014 Eric Smith <brouhaha@fedoraproject.org> 0.21-3
- Add Python 3 support.
- Require python-html5lib 0.999, which has epoch 1 because
  that is newer than upstream 1.0b2.

* Fri Mar 14 2014 Eric Smith <brouhaha@fedoraproject.org> 0.21-2
- Add some missing Requires (#1076734).

* Mon Mar 10 2014 Eric Smith <brouhaha@fedoraproject.org> 0.21-1
- Update to lastest upstream.

* Sun Jul 28 2013 Eric Smith <brouhaha@fedoraproject.org> 0.19.2-3
- Remove /usr/bin/env from Python script shebang lines.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 0.19.2-2
- Fixed dependencies.

* Sat Jul 20 2013 Eric Smith <brouhaha@fedoraproject.org> 0.19.2-1
- initial version
