%{?!_without_python2:%global with_python2 0%{?_with_python2:1} || !(0%{?rhel} >= 8 || 0%{?fedora} >= 32)}
%{?!_without_python3:%global with_python3 0%{?_with_python3:1} || !0%{?rhel} || 0%{?rhel} >= 7}

%global srcname rosdep

Name:           python-%{srcname}
Version:        0.20.1
Release:        1%{?dist}
Summary:        ROS System Dependency Installer

License:        BSD
URL:            http://ros.org/wiki/%{srcname}
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
rosdep is a command-line tool for installing system dependencies. For
end-users, rosdep helps you install system dependencies for software that
you are building from source. For developers, rosdep simplifies the problem
of installing system dependencies on different platforms. Instead of having to
figure out which Debian package on Ubuntu Oneiric contains Boost, you can just
specify a dependency on 'boost'.


%package doc
Summary:        HTML documentation for '%{name}'
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-catkin-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' python module


%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-catkin_pkg >= 0.4.0
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-pyyaml >= 3.1
BuildRequires:  python2-rosdistro >= 0.7.5
BuildRequires:  python2-rospkg >= 1.3.0
Requires:       python-srpm-macros
%{?python_provide:%python_provide python2-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python2-catkin_pkg >= 0.4.0
Requires:       python2-pyyaml >= 3.1
Requires:       python2-rosdistro >= 0.7.5
Requires:       python2-rospkg >= 1.3.0
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     python2-pip
Recommends:     python2-rpm
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python2-%{srcname}
rosdep is a command-line tool for installing system dependencies. For
end-users, rosdep helps you install system dependencies for software that
you are building from source. For developers, rosdep simplifies the problem
of installing system dependencies on different platforms. Instead of having to
figure out which Debian package on Ubuntu Oneiric contains Boost, you can just
specify a dependency on 'boost'.
%endif


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.4.0
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-PyYAML >= 3.1
BuildRequires:  python%{python3_pkgversion}-rosdistro >= 0.7.5
BuildRequires:  python%{python3_pkgversion}-rospkg >= 1.3.0
Requires:       python-srpm-macros
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.4.0
Requires:       python%{python3_pkgversion}-PyYAML >= 3.1
Requires:       python%{python3_pkgversion}-rosdistro >= 0.7.5
Requires:       python%{python3_pkgversion}-rospkg >= 1.3.0
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-pip
Recommends:     python%{python3_pkgversion}-rpm
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
rosdep is a command-line tool for installing system dependencies. For
end-users, rosdep helps you install system dependencies for software that
you are building from source. For developers, rosdep simplifies the problem
of installing system dependencies on different platforms. Instead of having to
figure out which Debian package on Ubuntu Oneiric contains Boost, you can just
specify a dependency on 'boost'.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

PYTHONPATH=$PWD/src %make_build -C doc man html SPHINXBUILD=sphinx-build-%{python3_version}
rm doc/_build/html/.buildinfo


%install
%if 0%{?with_python2}
%py2_install -- --install-scripts %{_bindir}/scripts

echo -n > py2_bins
for f in `ls %{buildroot}%{_bindir}/scripts`; do
    mv %{buildroot}%{_bindir}/scripts/$f %{buildroot}%{_bindir}/$f-%{python2_version}
    ln -s $f-%{python2_version} %{buildroot}%{_bindir}/$f-2
%if !(0%{?with_python3})
    ln -s $f-%{python2_version} %{buildroot}%{_bindir}/$f
    echo "%{_bindir}/$f" >> py2_bins
%endif
    echo -e "%{_bindir}/$f-2\n%{_bindir}/$f-%{python2_version}" >> py2_bins
done
%endif

%if 0%{?with_python3}
%py3_install -- --install-scripts %{_bindir}/scripts

echo -n > py3_bins
for f in `ls %{buildroot}%{_bindir}/scripts`; do
    mv %{buildroot}%{_bindir}/scripts/$f %{buildroot}%{_bindir}/$f-%{python3_version}
    ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f-3
    ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f
    echo -e "%{_bindir}/$f\n%{_bindir}/$f-3\n%{_bindir}/$f-%{python3_version}" >> py3_bins
done
%endif

rm -rf %{buildroot}%{_bindir}/scripts
install -D -p -m 0644 doc/man/rosdep.1 %{buildroot}%{_mandir}/man1/rosdep.1
install -D -p -m 0644 /dev/null %{buildroot}%{_sysconfdir}/ros/rosdep/sources.list.d/20-default.list


# Cannot currently run all of the tests because some need to query Github
%check
%if 0%{?with_python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} -m nose test \
    -e test_flake8 \
    -e test_rosdep_gbpdistro_support \
    -e test_rosdep_main \
    -e test_rosdep_pip \
    -e test_rosdep_rep3 \
    -e test_rosdep_source \
    -e test_rosdep_sources_list \
    %{nil}
%endif

%if 0%{?with_python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m nose test \
    -e test_flake8 \
    -e test_rosdep_gbpdistro_support \
    -e test_rosdep_main \
    -e test_rosdep_pip \
    -e test_rosdep_rep3 \
    -e test_rosdep_source \
    -e test_rosdep_sources_list \
    %{nil}
%endif


%files doc
%license LICENSE
%doc doc/_build/html

%if 0%{?with_python2}
%files -n python2-%{srcname} -f py2_bins
%license LICENSE
%doc README.md
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/%{srcname}2/
%{_mandir}/man1/%{srcname}.1.gz
%dir %{_sysconfdir}/ros/rosdep/
%dir %{_sysconfdir}/ros/rosdep/sources.list.d/
%ghost %{_sysconfdir}/ros/rosdep/sources.list.d/20-default.list
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname} -f py3_bins
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}2/
%{_mandir}/man1/%{srcname}.1.gz
%dir %{_sysconfdir}/ros/rosdep/
%dir %{_sysconfdir}/ros/rosdep/sources.list.d/
%ghost %{_sysconfdir}/ros/rosdep/sources.list.d/20-default.list
%endif


%changelog
* Fri Apr 16 2021 Scott K Logan <logans@cottsay.net> - 0.20.1-1
- Update to 0.20.1 (rhbz#1950541)

* Thu Feb 04 2021 Scott K Logan <logans@cottsay.net> - 0.20.0-1
- Update to 0.20.0 (rhbz#1897764)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.19.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.19.0-1
- Update to 0.19.0 (rhbz#1774738)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.17.1-1
- Update to 0.17.1 (rhbz#1763367)
- Add a weak pip dependency

* Fri Oct 04 2019 Scott K Logan <logans@cottsay.net> - 0.16.1-2
- Add dependency on python-srpm-macros to resolve %%{python3_pkgversion}
- Add weak dependencies for RHEL 8
- Make doc subpackage dependency weaker

* Thu Sep 19 2019 Scott K Logan <logans@cottsay.net> - 0.16.1-1
- Update to 0.16.1
- Drop Python 2 subpackage from f32+ (rhbz#1740997)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Scott K Logan <logans@cottsay.net> - 0.15.2-1
- Update to 0.15.2 (rhbz#1711473)
- Handle automatic dependency generation (f30+)
- Switch to Python 3 sphinx

* Tue Feb 19 2019 Scott K Logan <logans@cottsay.net> - 0.15.1-1
- Update to 0.15.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Scott K Logan <logans@cottsay.net> - 0.15.0-1
- Update to 0.15.0 (rhbz#1669292)
- Add executable links with Python version numbers

* Mon Jan 14 2019 Scott K Logan <logans@cottsay.net> - 0.14.0-1
- Update to 0.14.0

* Wed Nov 07 2018 Scott K Logan <logans@cottsay.net> - 0.13.0-1
- Update to 0.13.0
- Conditional python2 package
- Use python3_pkgversion
- Create a separate 'doc' package
- Co-own man page and sources directories among python2 and python3

* Fri Sep 14 2018 Scott K Logan <logans@cottsay.net> - 0.12.2-1
- Update to 0.12.2 (rhbz#1476259)
- Fix missing infrastructure files after making python 3 the default
- Enable at least SOME tests
- Make python-rpm recommended (will fall back to RPM CLI if not present)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-12
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Jan Beran <jberan@redhat.com> - 0.11.4-11
- Fix of missing Python 3 executables (rhbz #1432570)

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11.4-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-6
- Rebuild for Python 3.6

* Mon Oct 24 2016 Rich Mattes <richmattes@gmail.com> - 0.11.4-5
- Update package to comply with python_provide guideline

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Oct 18 2015 Rich Mattes <richmattes@gmail.com> - 0.11.4-1
- Update to release 0.11.4
- Remove upstream patches

* Sun Sep 13 2015 Scott K Logan <logans@cottsay.net> - 0.11.2-4
- Add upstream patches for DNF

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Rich Mattes <richmattes@gmail.com> - 0.11.2-2
- Make sure scripts in bindir use python2 instead of python3

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 0.11.2-1
- Update to release 0.11.2
- Update to latest github guidelines
- Use license macro for license file
- Added python3 package

* Tue Dec 30 2014 Rich Mattes <richmattes@gmail.com> - 0.11.0-1
- Update to release 0.11.0

* Mon Nov 24 2014 Scott K Logan <logans@cottsay.net> - 0.10.33-1
- Update to release 0.10.33

* Sat Oct 18 2014 Scott K Logan <logans@cottsay.net> - 0.10.32-1
- Update to release 0.10.32

* Thu Jul 31 2014 Scott K Logan <logans@cottsay.net> - 0.10.30-1
- Update to release 0.10.30

* Mon Jul 28 2014 Scott K Logan <logans@cottsay.net> - 0.10.29-1
- Update to release 0.10.29

* Tue Jul 01 2014 Scott K Logan <logans@cottsay.net> - 0.10.28-1
- Update to release 0.10.28

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Scott K Logan <logans@cottsay.net> - 0.10.27-2
- Fix for F19 release name in exceptions
- Update python macros to packaging spec
- Remove pythonpip patch, which is not needed for F19+

* Sat Apr 12 2014 Rich Mattes <richmattes@gmail.com> - 0.10.27-1
- Update to release 0.10.27
- Build html documentation

* Sat Feb 08 2014 Rich Mattes <richmattes@gmail.com> - 0.10.25-1
- Update to release 0.10.25

* Mon Aug 19 2013 Rich Mattes <richmattes@gmail.com> - 0.10.21-1
- Update to release 0.10.21
- Depend on python-catkin_pkg (rhbz#975896)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.18-2.20130601git91fb685
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Rich Mattes <richmattes@gmail.com> - 0.10.18-1.20130601git91fb6852
- Update to release 0.10.18
- Update github source url

* Mon Mar 18 2013 Rich Mattes <richmattes@gmail.com> - 0.10.14-1.20130318git76a8fef
- Update to release 0.10.14
- Fix installer to look for python-pip instead of pip (rhbz922296)
- Move rosdep cache to /var/cache instead of /etc

* Sun Oct 28 2012 Rich Mattes <richmattes@gmail.com> - 0.10.7-1.20121028gita9d29d2
- Update to 0.10.7
- Depend on /etc/ros from ros-release
- Separate build and install steps

* Mon Sep 17 2012 Rich Mattes <richmattes@gmail.com> - 0.9.7-1.20120917git5e1ecef
- Update to 0.9.7

* Sat Jun 16 2012 Rich Mattes <richmattes@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Sun Apr 29 2012 Rich Mattes <richmattes@gmail.com> - 0.9.3-1
- Initial package
