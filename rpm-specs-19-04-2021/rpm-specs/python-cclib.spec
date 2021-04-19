%global pname cclib

%bcond_without check

%global _description %{expand:
cclib is a Python library that provides parsers for output
files of computational chemistry packages.
It also provides a platform for computational chemists to
implement algorithms in a platform-independent way.

The goals of cclib are centered around the reuse of data obtained
from these programs and contained in output files, specifically:

- extract (parse) data from the output files generated by multiple programs
- provide a consistent interface to the results of computational chemistry
  calculations, particularly those results that are useful for
  algorithms or visualization
- facilitate the implementation of algorithms that are not specific to a
  particular computational chemistry package
- to maximize interoperability with other open source computational
  chemistry and cheminformatic software libraries}

Name:           python-%{pname}
Version:        1.7
Release:        1%{?dist}
Summary:        Parsers for output files of computational chemistry packages
License:        BSD and LGPLv2+
URL:            https://cclib.github.io/
Source0:        https://github.com/cclib/cclib/archive/v%{version}/%{pname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{_description}.

%package -n python%{python3_pkgversion}-%{pname}
Summary: Parsers for output files of computational chemistry packages

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-scipy
BuildRequires:  python%{python3_pkgversion}-periodictable
BuildRequires:  python%{python3_pkgversion}-biopython
BuildRequires:  python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-periodictable
Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-PyQt4
Requires:       python%{python3_pkgversion}-vtk
Requires:       python%{python3_pkgversion}-scipy
Requires:       python%{python3_pkgversion}-biopython
Requires:       python%{python3_pkgversion}-packaging
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pname}}

%description -n python%{python3_pkgversion}-%{pname}
%{_description}.

%prep
%autosetup -n %{pname}-%{version}

rm -rf  cclib.egg-info

%build
%py3_build

%install
%py3_install

# Remove shebangs
for lib in %{buildroot}%{python3_sitelib}/cclib/scripts/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m test.test_data
%endif

%files -n python%{python3_pkgversion}-%{pname}
%license LICENSE
%doc CHANGELOG ANNOUNCE THANKS
%{python3_sitelib}/*egg-info/
%{python3_sitelib}/%{pname}/
%{_bindir}/ccframe
%{_bindir}/ccget
%{_bindir}/ccwrite
%{_bindir}/cda

%changelog
* Sat Jan 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.7-1
- Release 1.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.4-1
- Release 1.6.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-6
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-5
- Make patch unconditioned

* Mon Mar 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-4
- Extend patch0 to Python-3.10

* Sun Mar 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-3
- Fix rhbz#1818598

* Fri Mar 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-2
- Remove shabangs from scripts
- Add PyQt4 and vtk runtime dependencies

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.6.2-1
- Release 1.6.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.2-3
- Temporarily disable tests for fixing FTBFS
- Fixes bug #1307899

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.2-1
- Update to maintenance update 1.3.2
- re-enable python3 tests (fixed upstream)

* Sun Nov 15 2015 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.1-5
- Move binaries to the right package
- Remove deprecated tags and replace deprecated macros
- Build python2 and python3 packages in the same directory
- Use %%license macro

* Sat Nov 14 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-4
- Disable python3 tests temporarily
- upstream issue filed

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 14 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-1
- Update to version 1.3.1

* Thu Jan 22 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3-1
- Update to version 1.3

* Sun Jul 13 2014 Mukundan Ragavan <nonamedotc@gmail.com> - 1.2-2
- Added python3 package

* Fri Jun 13 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2-1
- Updated to 1.2
- Changed URL and Source0 to github links
- Added sed lines to add file encoding for compiling under python-2.7

* Fri Jun 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1-1
- Update to 1.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 15 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 24 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-2
- Workaround bad permissions in tarball causing FTBFS

* Fri Mar 12 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-1
- Update to 1.0

* Wed Feb 24 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0a-1
- Update to 1.0a

* Sun Feb 14 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.91-7
- Bump release

* Fri Jul 31 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.91-6
- Drop extra requires by request of upstream

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 02 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.91-4
- Put everything in main package instead

* Fri Apr 24 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.91-3
- Branched supplementary Requires metapackage

* Thu Apr 23 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.91-2
- Added BR: numpy and Requires: numpy
- Removed test/ from %%doc

* Thu Apr 23 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.91-1
- First release
