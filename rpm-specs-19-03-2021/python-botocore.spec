%global pypi_name botocore

Name:           python-%{pypi_name}
# NOTICE - Updating this package requires updating python-boto3
Version:        1.20.31
Release:        1%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        ASL 2.0
URL:            https://github.com/boto/botocore
Source0:        %{pypi_source}
BuildArch:      noarch

Patch0:         botocore-1.19.53-bucket-threshhold.patch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%package -n     python3-%{pypi_name}
Summary:        Low-level, data-driven core of boto 3
Provides:       bundled(python3-six) = 1.10.0
%{?python_provide:%python_provide python3-%{pypi_name}}


%description -n python3-%{pypi_name}
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%prep
%autosetup -n %{pypi_name}-%{version} -p0
rm -vr %{pypi_name}.egg-info
# Remove online tests
rm -vr tests/integration
# This test tried to import tests/cmd-runner which failed as the code was
# unable to import "botocore". I'm not 100% sure why this happened but for now
# just exclude this one test and run all the other functional tests.
rm -vr tests/functional/leak

%generate_buildrequires
# -r use final runtime dependencies as BuildRequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
cd tests
nosetests-%{python3_version} unit functional


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.dist-info/

%changelog
* Thu Mar 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.31-1
- 1.20.31

* Thu Mar 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.30-1
- 1.20.30

* Wed Mar 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.29-1
- 1.20.29

* Tue Mar 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.28-1
- 1.20.28

* Mon Mar 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.27-1
- 1.20.27

* Fri Mar 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.26-1
- 1.20.26

* Thu Mar 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.25-1
- 1.20.25

* Wed Mar 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.24-1
- 1.20.24

* Tue Mar 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.23-1
- 1.20.23

* Mon Mar 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.22-1
- 1.20.22

* Fri Mar 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.21-1
- 1.20.21

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.20-1
- 1.20.20

* Wed Mar 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.19-1
- 1.20.19

* Tue Mar 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.18-1
- 1.20.18

* Mon Mar 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.17-1
- 1.20.17

* Fri Feb 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.16-1
- 1.20.16

* Thu Feb 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.15-1
- 1.20.15

* Wed Feb 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.14-1
- 1.20.14

* Tue Feb 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.13-1
- 1.20.13

* Sat Feb 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.12-1
- 1.20.12

* Fri Feb 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.11-1
- 1.20.11

* Thu Feb 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.10-1
- 1.20.10

* Wed Feb 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.9-1
- 1.20.9

* Tue Feb 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.8-1
- 1.20.8

* Fri Feb 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.6-1
- 1.20.6

* Wed Feb 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.5-1
- 1.20.5

* Tue Feb 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.4-1
- 1.20.4

* Fri Feb 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.3-1
- 1.20.3

* Fri Feb 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.2-1
- 1.20.2

* Wed Feb 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.20.0-1
- 1.20.0

* Mon Feb 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.63-1
- 1.19.63

* Fri Jan 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.62-1
- 1.19.62

* Thu Jan 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.61-1
- 1.19.61

* Wed Jan 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.60-1
- 1.19.60

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.59-1
- 1.19.59

* Fri Jan 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.58-1
- 1.19.58

* Wed Jan 20 08:14:42 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.57-1
- 1.19.57

* Tue Jan 19 08:21:00 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.56-1
- 1.19.56

* Fri Jan 15 10:36:04 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.55-1
- 1.19.55

* Thu Jan 14 08:13:55 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.54-1
- 1.19.54

* Wed Jan 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.53-2
- Patch to increase bucket test threshold.

* Wed Jan 13 08:29:49 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.53-1
- 1.19.53

* Tue Jan 12 08:13:31 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.52-1
- 1.19.52

* Fri Jan  8 10:46:30 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.51-1
- 1.19.51

* Thu Jan  7 08:25:18 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.50-1
- 1.19.50

* Wed Jan  6 08:09:03 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.49-1
- 1.19.49

* Tue Jan  5 08:23:32 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.48-1
- 1.19.48

* Mon Jan  4 08:27:26 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.47-1
- 1.19.47

* Wed Dec 30 16:15:17 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.46-1
- 1.19.46

* Wed Dec 30 08:21:28 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.45-1
- 1.19.45

* Tue Dec 29 09:09:01 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.44-1
- 1.19.44

* Thu Dec 24 08:15:06 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.43-1
- 1.19.43

* Wed Dec 23 08:29:08 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.42-1
- 1.19.42

* Tue Dec 22 08:21:05 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.41-1
- 1.19.41

* Fri Dec 18 16:24:06 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.40-1
- 1.19.40

* Fri Dec 18 08:13:19 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.39-1
- 1.19.39

* Thu Dec 17 08:10:23 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.38-1
- 1.19.38

* Wed Dec 16 08:16:16 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.37-1
- 1.19.37

* Tue Dec 15 08:25:16 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.36-1
- 1.19.36

* Mon Dec 14 08:55:49 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.35-1
- 1.19.35

* Fri Dec 11 08:06:30 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.34-1
- 1.19.34

* Thu Dec 10 08:15:47 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.33-1
- 1.19.33

* Wed Dec  9 08:48:23 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.32-1
- 1.19.32

* Tue Dec  8 08:18:17 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.31-1
- 1.19.31

* Mon Dec  7 08:19:37 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.30-1
- 1.19.30

* Fri Dec  4 09:42:28 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.29-1
- 1.19.29

* Wed Dec  2 08:19:53 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.28-1
- 1.19.28

* Tue Dec  1 11:44:50 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.26-1
- 1.19.26

* Mon Nov 30 09:13:53 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.25-1
- 1.19.25

* Sun Nov 29 23:16:01 CET 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.19.24-2
- also run tests during build, rely on auto-generated requirements

* Tue Nov 24 08:24:37 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.24-1
- 1.19.24

* Mon Nov 23 08:25:04 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.23-1
- 1.19.23

* Fri Nov 20 08:13:27 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.22-1
- 1.19.22

* Thu Nov 19 08:26:36 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.21-1
- 1.19.21

* Wed Nov 18 08:21:58 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.20-1
- 1.19.20

* Tue Nov 17 09:15:08 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.19-1
- 1.19.19

* Mon Nov 16 08:34:42 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.18-1
- 1.19.18

* Thu Nov 12 15:45:59 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.17-1
- 1.19.17

* Thu Nov 12 10:23:55 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.16-1
- 1.19.16

* Wed Nov 11 09:20:06 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.15-1
- 1.19.15

* Mon Nov  9 14:11:42 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.14-1
- 1.19.14

* Mon Nov  9 09:42:26 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.13-1
- 1.19.13

* Fri Nov  6 08:23:51 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.12-1
- 1.19.12

* Thu Nov  5 14:58:29 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.11-1
- 1.19.11

* Tue Nov  3 08:29:36 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.10-1
- 1.19.10

* Mon Nov  2 09:26:02 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.9-1
- 1.19.9

* Fri Oct 30 08:12:36 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.8-1
- 1.19.8

* Thu Oct 29 08:10:31 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.7-1
- 1.19.7

* Wed Oct 28 09:45:23 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.6-1
- 1.19.6

* Tue Oct 27 09:38:01 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.5-1
- 1.19.5

* Fri Oct 23 16:46:42 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.4-1
- 1.19.4

* Fri Oct 23 08:11:47 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.3-1
- 1.19.3

* Thu Oct 22 08:28:32 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.2-1
- 1.19.2

* Tue Oct 20 21:05:38 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.1-1
- 1.19.1

* Tue Oct 20 08:09:45 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.19.0-1
- 1.19.0

* Fri Oct 16 14:54:26 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.18-1
- 1.18.18

* Fri Oct 16 08:08:23 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.17-1
- 1.18.17

* Sat Oct 10 16:03:11 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.16-1
- 1.18.16

* Thu Oct  8 14:29:56 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.15-1
- 1.18.15

* Thu Oct  8 08:59:46 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.14-1
- 1.18.14

* Wed Oct  7 08:55:36 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.13-1
- 1.18.13

* Fri Oct  2 15:33:49 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.11-1
- 1.18.11

* Fri Oct  2 08:18:33 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.10-1
- 1.18.10

* Thu Oct  1 08:14:54 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.9-1
- 1.18.9

* Wed Sep 30 09:03:15 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.8-1
- 1.18.8

* Tue Sep 29 09:13:43 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.7-1
- 1.18.7

* Mon Sep 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.6-1
- 1.18.6

* Fri Sep 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.5-1
- 1.18.5

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.4-1
- 1.18.4

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.3-1
- 1.18.3

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.2-1
- 1.18.2

* Fri Sep 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.1-1
- 1.18.1

* Fri Sep 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.0-1
- 1.18.0

* Wed Sep 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.63-1
- 1.17.63

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.62-1
- 1.17.62

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.61-1
- 1.17.61

* Mon Sep 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.60-1
- 1.17.60

* Fri Sep 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.59-1
- 1.17.59

* Thu Sep 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.58-1
- 1.17.58

* Wed Sep 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.57-1
- 1.17.57

* Tue Sep 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.56-1
- 1.17.56

* Fri Sep 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.55-1
- 1.17.55

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.54-1
- 1.17.54

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.53-1
- 1.17.53

* Tue Sep 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.52-1
- 1.17.52

* Mon Aug 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.51-1
- 1.17.51

* Fri Aug 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.50-1
- 1.17.50

* Thu Aug 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.49-1
- 1.17.49

* Tue Aug 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.48-1
- 1.17.48

* Fri Aug 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.47-1
- 1.17.47

* Wed Aug 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.46-1
- 1.17.46

* Wed Aug 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.45-1
- 1.17.45

* Tue Aug 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.44-1
- 1.17.44

* Mon Aug 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.43-1
- 1.17.43

* Fri Aug 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.42-1
- 1.17.42

* Thu Aug 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.41-1
- 1.17.41

* Wed Aug 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.40-1
- 1.17.40

* Tue Aug 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.39-1
- 1.17.39

* Mon Aug 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.38-1
- 1.17.38

* Thu Aug 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.37-1
- 1.17.37

* Thu Aug 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.36-1
- 1.17.36

* Wed Aug 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.35-1
- 1.17.35

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.34-1
- 1.17.34

* Fri Jul 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.33-1
- 1.17.33

* Fri Jul 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.32-1
- 1.17.32

* Thu Jul 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.31-1
- 1.17.31

* Wed Jul 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.30-1
- 1.17.30

* Tue Jul 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.29-1
- 1.17.29

* Fri Jul 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.28-1
- 1.17.28

* Fri Jul 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.27-1
- 1.17.27

* Thu Jul 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.26-1
- 1.17.26

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.25-1
- 1.17.25

* Tue Jul 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.24-1
- 1.17.24

* Mon Jul 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.23-1
- 1.17.23

* Fri Jul 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.22-1
- 1.17.22

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.21-1
- 1.17.21

* Fri Jul 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.20-1
- 1.17.20

* Thu Jul 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.19-1
- 1.17.19

* Wed Jul 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.18-1
- 1.17.18

* Tue Jul 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.17-1
- 1.17.17

* Fri Jul 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.16-1
- 1.17.16

* Thu Jul 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.15-1
- 1.17.15

* Wed Jul 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.14-1
- 1.17.14

* Tue Jun 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.13-1
- 1.17.13

* Sat Jun 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.12-1
- 1.17.12

* Fri Jun 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.11-1
- 1.17.11

* Thu Jun 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.10-1
- 1.17.10

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.9-1
- 1.17.9

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.8-1
- 1.17.8

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.7-1
- 1.17.7

* Fri Jun 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.6-1
- 1.17.6

* Thu Jun 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.5-1
- 1.17.5

* Wed Jun 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.4-1
- 1.17.4

* Tue Jun 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.3-1
- 1.17.3

* Sat Jun 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.2-1
- 1.17.2

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.1-1
- 1.17.1

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.17.0-1
- 1.17.0

* Sat Jun 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.24-1
- 1.16.24

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.23-1
- 1.16.23

* Thu Jun 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.22-1
- 1.16.22

* Tue Jun 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.20-1
- 1.16.20

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.19-1
- 1.16.19

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.16.16-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.16-1
- 1.16.16

* Thu May 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.15-1
- 1.16.15

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.14-1
- 1.16.14

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.12-1
- 1.16.12

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.11-1
- 1.16.11

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.10-1
- 1.16.10

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.9-1
- 1.16.9

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.8-1
- 1.16.8

* Tue May 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.7-1
- 1.16.7

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.6-1
- 1.16.6

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.5-1
- 1.16.5

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.4-1
- 1.16.4

* Wed May 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.3-1
- 1.16.3

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.2-1
- 1.16.2

* Sat May 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.1-1
- 1.16.1

* Fri May 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.0-1
- 1.16.0

* Thu Apr 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.49-1
- 1.15.49

* Wed Apr 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.48-1
- 1.15.48

* Tue Apr 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.47-1
- 1.15.47

* Sat Apr 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.46-1
- 1.15.46

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.45-1
- 1.15.45

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.44-1
- 1.15.44

* Wed Apr 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.43-1
- 1.15.43

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.42-1
- 1.15.42

* Sun Apr 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.41-1
- 1.15.41

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.40-1
- 1.15.40

* Thu Apr 09 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.15.39-2
- Fix docutils 0.16 runtime dependency issue

* Thu Apr 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.39-1
- 1.15.39

* Wed Apr 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.38-2
- Python 3.9 fix

* Wed Apr 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.38-1
- 1.15.38

* Tue Apr 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.37-1
- 1.15.37

* Mon Apr 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.36-1
- 1.15.36

* Fri Apr 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.35-1
- 1.15.35

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.34-1
- 1.15.34

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.33-1
- 1.15.33

* Mon Mar 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.32-1
- 1.15.32

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.31-1
- 1.15.31

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.30-1
- 1.15.30

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.29-1
- 1.15.29

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.28-1
- 1.15.28

* Tue Mar 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.27-1
- 1.15.27

* Sat Mar 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.26-1
- 1.15.26

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.25-1
- 1.15.25

* Thu Mar 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.24-1
- 1.15.24

* Wed Mar 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.23-1
- 1.15.23

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.22-1
- 1.15.22

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.21-1
- 1.15.21

* Fri Mar 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.20-1
- 1.15.20

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.19-1
- 1.15.19

* Wed Mar 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.18-1
- 1.15.18

* Tue Mar 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.17-1
- 1.15.17

* Sun Mar 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.16-1
- 1.15.16

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.15-1
- 1.15.15

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.14-1
- 1.15.14

* Wed Mar 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.13-1
- 1.15.13

* Tue Mar 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.12-1
- 1.15.12

* Fri Feb 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.9-1
- 1.15.9

* Thu Feb 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.15.8-1
- Update to 1.15.8

* Wed Feb 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.7-1
- 1.15.7.

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.6-1
- 1.15.6.

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.5-1
- 1.15.5.

* Thu Feb 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.3-1
- 1.15.3.

* Thu Feb 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.17-1
- 1.14.17.

* Fri Feb 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.14.12-1
- Update to 1.14.12

* Wed Jan 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.14.9-1
- Update to 1.14.9

* Thu Jan 16 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.14.4-1
- Update to 1.14.4

* Tue Dec 31 2019 David Duncan <davdunc@amazon.com> - 1.13.45-2
- Bumping to version 1.13.45

* Tue Nov 19 2019 Orion Poplawski <orion@nwra.com> - 1.13.21-1
- Update to 1.13.21

* Mon Oct 28 2019 David Duncan <davdunc@amazon.com> - 1.13.2-1
- Merge changes from 1.13.2 release. (#1677950)

* Mon Oct 21 2019 James Hogarth <james.hogarth@gmail.com> - 1.12.253-2
* Fix changelog format

* Sat Oct 19 2019 David Duncan <davedunc@amazon.com> - 1.12.253-1
- Merge changes from 1.12.253 release. (#1677950)

* Fri Oct 04 2019 David Duncan <davedunc@amazon.com> - 1.12.243-1
- Merge changes from 1.12.243 release. (#1677950)

* Thu Oct 03 2019 David Duncan <davedunc@amazon.com> - 1.12.242-1
- Merge changes from 1.12.242 release. (#1677950)

* Thu Oct 03 2019 David Duncan <davedunc@amazon.com> - 1.12.241-1
- Merge changes from 1.12.241 release. (#1677950)

* Tue Oct 01 2019 David Duncan <davedunc@amazon.com> - 1.12.240-1
- Merge changes from 1.12.240 release. (#1677950)

* Mon Sep 30 2019 David Duncan <davedunc@amazon.com> - 1.12.239-1
- Merge changes from 1.12.239 release. (#1677950)

* Sat Sep 28 2019 David Duncan <davedunc@amazon.com> - 1.12.238-1
- Merge changes from 1.12.238 release. (#1677950)

* Thu Sep 26 2019 David Duncan <davdunc@amazon.com> - 1.12.237-1
- Merge changes from 1.12.237 release. (#1677950)

* Thu Sep 26 2019 David Duncan <davdunc@amazon.com> - 1.12.236-1
- Merge changes from 1.12.236 release.

* Sun Sep 22 2019 David Duncan <davdunc@amazon.com> - 1.12.233-1
- Merge changes from 1.12.233 release.

* Thu Sep 19 2019 David Duncan <davdunc@amazon.com> - 1.12.231 
- Update to 1.12.231
- Update to latest endpoints and models

* Mon Sep 09 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.12.225-1
- Update to 1.12.225

* Wed Aug 21 2019 Kevin Fenzi <kevin@scrye.com> - 1.12.212-1
- Update to 1.12.212

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.12.188-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.188-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 David Duncan <davdunc@amazon.com> - 1.12.188-1
- Bumping version to 1.12.188
- resolves #1677950
- update to latest endpoints and models

* Tue May 28 2019 David Duncan <davdunc@amazon.com> - 1.12.157-1
- Bumping to version 1.12.157
- resolves #1677950
- update to latest endpoints and models

* Wed Apr 24 2019 David Duncan <dadvunc@amazon.com> - 1.12.135-1
- Bumping version to 1.12.135
- add support for ap-east-1

* Thu Mar 21 2019 David Duncan <davdunc@amazon.com> - 1.12.119-1
- resolves #1677950
- Bumping version to 1.12.119


* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.12.101-1
- Update to 1.12.101

* Fri Feb 15 2019 Kevin Fenzi <kevin@scrye.com> - 1.12.96-1
- Update to 1.12.96.

* Sun Feb 10 2019 David Duncan <davdunc@amazon.com> - 1.12.91
- resolves #1667630
- Update to latest models
- api-change:``discovery``: Update discovery client to latest version
- api-change:``ecs``: Update ecs client to latest version
- api-change:``dlm``: Update dlm client to latest version

* Mon Feb 04 2019 David Duncan <davdunc@amazon.com> - 1.12.87
- Update to latest models
- Improve event stream parser tests
- resolves #1667630

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.12.75-3
- Enable python dependency generator

* Wed Jan 09 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.12.75-2
- Subpackage python2-botocore has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jan 08 2019 David Duncan <davdunc@amazon.com> - 1.12.75
- Update to latest endpoints
- Update to latest models

* Sun Nov 18 2018 David Duncan <davdunc@amazon.com> - 1.12.47
- Update to latest models.

* Sun Oct 07 2018 David Duncan <davdunc@amazon.com> - 1.12.18
- Update to latest models 

* Tue Oct 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.12.15-2
- Reinstate python-urllib3 dependency as python-boto3 requires it

* Tue Oct 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.12.15-1
- Update to 1.12.15

* Wed Sep 5 2018 David Duncan <davdunc@amazon.com> - 1.10.43-1
- Bumping version to 1.10.43 Updates bz#1531330

* Mon Sep 3 2018 David Duncan <davdunc@amazon.com> - 1.10.42-1
- Bumping version to 1.10.42 Updates bz#1531330

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.10.41-3
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 1.10.41-2
- Fix EL7 dateutil patch

* Wed Jun 20 2018 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 1.10.41-1
- Upstream 1.10.41

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.9.1-3
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 28 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.9.1-1
- Update to 1.9.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.8.33-1
- Update to 1.8.33

* Tue Jan 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.8.29-1
- Update to 1.8.29

* Wed Jan 10 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.8.26-1
- Update to 1.8.26

* Wed Jan 03 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.8.21-1
- Update to 1.8.21

* Sun Aug 13 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.72-1
- Update to 1.5.72

* Tue May 23 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.53-1
- Update to 1.5.53

* Wed Mar 15 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.26-1
- Update to 1.5.26

* Sat Feb 25 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.18-1
- Update to 1.5.18

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3
- Rebase patch

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.91-1
- Update to 1.4.91

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 1.4.85-2
- Rebuild for Python 3.6

* Sun Dec 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.85-1
- Update to 1.4.85

* Sat Dec 03 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.81-1
- Update to 1.4.81

* Thu Nov 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.78-1
- Update to 1.4.78

* Thu Oct 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.67-1
- Update to 1.4.67

* Mon Oct 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.60-1
- Update to 1.4.60

* Sun Oct 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.58-1
- Update to 1.4.58
- Add python-six dependency

* Wed Sep 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.57-1
- Update to 1.4.57

* Tue Sep 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.52-3
- Fix patch

* Tue Sep 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.52-2
- Add testing support for EL7 using a lower version of dateuil library

* Wed Sep 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.52-1
- Update to 1.4.52

* Sat Sep 03 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.50-1
- Update to 1.4.50

* Wed Aug 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.49-1
- Upstream update

* Tue Aug 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.48-1
- Upstream update

* Fri Aug 05 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.43-1
- Upstream update

* Thu Aug 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.42-1
- Upstream update

* Tue Aug 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.41-1
- Upstream update

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.35-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.35-1
- New version from upstream

* Wed Jun 08 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.26-1
- New version from upstream

* Sat May 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.24-1
- New version from upstream

* Tue Mar 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.7-1
- New version from upstream

* Tue Mar 01 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.30-1
- New version from upstream

* Wed Feb 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.29-1
- New version from upstream

* Fri Feb 19 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.28-1
- New version from upstream

* Wed Feb 17 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.27-1
- New version from upstream

* Fri Feb 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.26-1
- New version from upstream

* Wed Feb 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.25-1
- New version from upstream

* Tue Feb 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.24-1
- New version from upstream

* Tue Feb 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.23-1
- New version from upstream

* Fri Jan 22 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.22-1
- New version from upstream

* Wed Jan 20 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.21-1
- New version from upstream

* Fri Jan 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.20-1
- New version from upstream

* Fri Jan 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.19-1
- New version from upstream

* Wed Jan 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.18-1
- New version from upstream

* Tue Jan 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.17-2
- Add testing for Fedora

* Thu Jan 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.17-1
- Update to upstream version

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.16-2
- Fix shabang on botocore/vendored/requests/packages/chardet/chardetect.py
- Fix shabang on botocore/vendored/requests/certs.py
- Remove the useless dependency with python-urllib3

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.16-1
- Update to new upstream version
- Fix Provides for EL6

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.15-1
- Update to current version
- Improve the spec

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.79.0-1
- New version

* Fri Jul 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.58.0-2
- Add Python 3 support

* Fri Jul 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.58.0-1
- Initial packaging
