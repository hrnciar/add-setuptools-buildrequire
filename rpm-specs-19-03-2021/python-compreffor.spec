%global srcname compreffor

Name:           python-%{srcname}
Version:        0.5.0.post1
Release:        4%{?dist}
Summary:        CFF table subroutinizer for FontTools

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/googlei18n/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

%description
A CFF (Compact Font Format) table subroutinizer for FontTools.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-fonttools
BuildRequires:  python3-Cython
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description -n python3-%{srcname}
A CFF (Compact Font Format) table subroutinizer for FontTools.


%prep
%autosetup -n %{srcname}-%{version}
# removing shebangs from modules
sed -i '/#!\/usr\/bin\/env python/d' src/python/compreffor/*Compressor.py

# Remove the cythonized files in order to regenerate them during build.
rm $(grep -rl '/\* Generated by Cython')

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%dir %{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-*.egg-info
%{python3_sitearch}/%{srcname}/*.py
%{python3_sitearch}/%{srcname}/*.so
%{python3_sitearch}/%{srcname}/__pycache__
%{python3_sitearch}/%{srcname}/test
%{_bindir}/compreffor

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.post1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.post1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.post1-2
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5.0.post1-1
- Update version
- Use python auto-requires

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Charalampos Stratakis <cstratak@redhat.com> - 0.4.6-8
- Recythonize the sources

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.6-6
- Subpackage python2-compreffor has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-4
- Rebuilt for Python 3.7

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.4.6-3
- Include explicit BRs for gcc and gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.4.6-1
- Update version

* Thu Aug 24 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.4.5-1
- Update version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.4.4-1
- Initial package
