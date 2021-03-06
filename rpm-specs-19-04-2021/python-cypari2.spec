%global	modname	cypari2
%global prerel	b1

Name:		python-%{modname}
Version:	2.1.2
Release:	0.3.%{prerel}%{?dist}
Summary:	A Python interface to the number theory library pari
License:	GPLv2+
URL:		https://github.com/sagemath/%{modname}
Source0:	https://github.com/sagemath/%{modname}/archive/%{version}%{?prerel}/%{modname}-%{version}%{?prerel}.tar.gz
# Previously sagemath-pari.patch
Patch0:		%{name}-pari.patch
# Fix building with cython language level 3
Patch1:		%{name}-cython.patch
# Adapt to python 3.10
# https://github.com/sagemath/cypari2/pull/103
Patch2:		%{name}-python310.patch

BuildRequires:	gcc
BuildRequires:	gmp-devel
BuildRequires:	make
BuildRequires:	pari-devel
BuildRequires:	pari-gp
BuildRequires:	python3-cysignals-devel >= 1.6.4
BuildRequires:	python3-devel
BuildRequires:	%{py3_dist cython}
BuildRequires:	%{py3_dist setuptools}
BuildRequires:	%{py3_dist six}
BuildRequires:	%{py3_dist sphinx}

%global _description \
A Python interface to the number theory library pari.

%description	%{_description}

%package	-n python3-%{modname}
Summary:	%{summary}

%description	-n python3-%{modname} %{_description}

%package	-n python3-%{modname}-devel
Summary:	Header files for the pari python interface
Requires:	python3-%{modname}

%description	-n python3-%{modname}-devel %{_description}

%package	doc
Summary:	Documentation for %{name}
Requires:	python3-%{modname}
BuildArch:	noarch
%description	doc
Documentation and examples for %{name}.

%prep
%autosetup -p0 -n %{modname}-%{version}%{?prerel}

# Build for python 3
sed -i '/language_level/s/2/3/' setup.py

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"
%py3_build

# Build the documentation
export PYTHONPATH=$PWD/$(ls -1d build/lib.*)
make -C docs html SPHINXBUILD="python3 -msphinx"
rst2html --no-datestamp README.rst README.html

%install
%py3_install

# Bug in version 1.3+ omits the automatically generated declarations
cp -p cypari2/auto_paridecl.pxd %{buildroot}%{python3_sitearch}/%{modname}

# Install the documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -farp docs/build/html %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo

%check
PATH=%{buildroot}%{_bindir}:$PATH
PYTHONPATH=%{buildroot}%{python3_sitearch}
export PATH PYTHONPATH
%{python3} tests/rundoctest.py || :

%files		-n python3-%{modname}
%license LICENSE
%doc README.html
%{python3_sitearch}/%{modname}
%{python3_sitearch}/%{modname}-*.egg-info
%exclude %{python3_sitearch}/%{modname}/*.h
%exclude %{python3_sitearch}/%{modname}/*.pxd

%files		-n python3-%{modname}-devel
%{python3_sitearch}/%{modname}/*.h
%{python3_sitearch}/%{modname}/*.pxd

%files		doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-0.3.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Jerry James <loganjerry@gmail.com> - 2.1.2-0.2.b1
- Add -python310 patch to adapt to python 3.10

* Mon Nov  9 2020 Jerry James <loganjerry@gmail.com> - 2.1.2-0.1.b1
- Update to 2.1.2b1 for pari 2.13.0 support
- Drop upstreamed -literal-block patch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.1.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Jerry James <loganjerry@gmail.com> - 2.1.1-5
- Add -literal-block and -cython patches
- Set cython language level to 3
- Ship the README as html instead of rst

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Update to 2.1.1 to guard against pari upgrades
- New URLs

* Mon Apr  8 2019 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Update to 2.1.0 for sagemath 8.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Update to 1.3.1 to get fix for print name collision
- Drop python2 subpackage

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Update to 1.2.1 for pari 2.11.0 (bz 1585285)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.1.4-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.1.4-1
- Update to 1.1.4 for sagemath 8.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.3-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Nov 10 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.3-5
- Add patch to correct pointer miscalculation (crashes on 32 bit glibc)
- Ignore one error that happens only on 32 bit %%check

* Fri Nov 10 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.3-4
- Add missing build requires for %%check

* Thu Nov 09 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.3-3
- Remove conditionals for doc package and %%check

* Thu Nov 09 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.3-2
- Correct Source URL
- Temporarily disable doc and check as need to update cysignals

* Thu Nov 09 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.3-1
- Update to 1.1.3
- Added doc subpackage and %%check section

* Wed Nov 08 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.0.0-1
- Initial python-cypari2 spec.
