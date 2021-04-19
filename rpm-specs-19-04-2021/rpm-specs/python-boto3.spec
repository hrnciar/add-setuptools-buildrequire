%global pypi_name boto3

Name:           python-%{pypi_name}
Version:        1.17.53
Release:        1%{?dist}
Summary:        The AWS SDK for Python

License:        ASL 2.0
URL:            https://github.com/boto/boto3
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Boto3 is the Amazon Web Services (AWS) Software Development
Kit (SDK) for Python, which allows Python developers to
write software that makes use of services like Amazon S3
and Amazon EC2.

%package -n     python3-%{pypi_name}
Summary:        The AWS SDK for Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Boto3 is the Amazon Web Services (AWS) Software Development
Kit (SDK) for Python, which allows Python developers to
write software that makes use of services like Amazon S3
and Amazon EC2.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove online tests
rm -rf tests/integration

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-*.egg-info/

%changelog
* Thu Apr 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.53-1
- 1.17.53

* Thu Apr 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.52-1
- 1.17.52

* Tue Apr 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.51-1
- 1.17.51

* Mon Apr 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.50-1
- 1.17.50

* Fri Apr 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.49-1
- 1.17.49

* Fri Apr 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.48-1
- 1.17.48

* Wed Apr 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.47-1
- 1.17.47

* Wed Apr 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.46-1
- 1.17.46

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.45-1
- 1.17.45

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.44-1
- 1.17.44

* Thu Apr 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.43-1
- 1.17.43

* Thu Apr 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.42-1
- 1.17.42

* Wed Mar 31 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.41-1
- 1.17.41

* Tue Mar 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.40-1
- 1.17.40

* Mon Mar 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.39-1
- 1.17.39

* Fri Mar 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.37-1
- 1.17.37

* Thu Mar 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.36-1
- 1.17.36

* Wed Mar 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.35-1
- 1.17.35

* Tue Mar 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.34-1
- 1.17.34

* Mon Mar 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.33-1
- 1.17.33

* Thu Mar 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.31-1
- 1.17.31

* Thu Mar 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.30-1
- 1.17.30

* Wed Mar 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.29-1
- 1.17.29

* Tue Mar 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.28-1
- 1.17.28

* Mon Mar 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.27-1
- 1.17.27

* Fri Mar 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.26-1
- 1.17.26

* Thu Mar 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.25-1
- 1.17.25

* Wed Mar 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.24-1
- 1.17.24

* Tue Mar 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.23-1
- 1.17.23

* Mon Mar 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.22-1
- 1.17.22

* Fri Mar 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.21-1
- 1.17.21

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.20-1
- 1.17.20

* Wed Mar 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.19-1
- 1.17.19

* Tue Mar 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.18-1
- 1.17.18

* Mon Mar 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.17-1
- 1.17.17

* Fri Feb 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.16-1
- 1.17.16

* Thu Feb 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.15-1
- 1.17.15

* Wed Feb 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.14-1
- 1.17.14

* Tue Feb 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.13-1
- 1.17.13

* Sat Feb 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.12-1
- 1.17.12

* Fri Feb 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.11-1
- 1.17.11

* Thu Feb 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.10-1
- 1.17.10

* Wed Feb 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.9-1
- 1.17.9

* Tue Feb 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.8-1
- 1.17.8

* Fri Feb 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.6-1
- 1.17.6

* Wed Feb 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.5-1
- 1.17.5

* Tue Feb 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.4-1
- 1.17.4

* Fri Feb 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.3-1
- 1.17.3

* Fri Feb 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.2-1
- 1.17.2

* Wed Feb 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.17.0-1
- 1.17.0

* Mon Feb 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.63-1
- 1.16.63

* Fri Jan 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.62-1
- 1.16.62

* Thu Jan 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.61-1
- 1.16.61

* Wed Jan 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.60-1
- 1.16.60

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.59-1
- 1.16.59

* Fri Jan 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.58-1
- 1.16.58

* Wed Jan 20 08:21:03 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.57-1
- 1.16.57

* Tue Jan 19 08:28:49 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.56-1
- 1.16.56

* Fri Jan 15 10:49:14 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.55-1
- 1.16.55

* Thu Jan 14 08:20:12 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.54-1
- 1.16.54

* Wed Jan 13 08:36:31 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.53-1
- 1.16.53

* Tue Jan 12 08:19:50 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.52-1
- 1.16.52

* Fri Jan  8 10:52:57 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.51-1
- 1.16.51

* Thu Jan  7 08:33:04 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.50-1
- 1.16.50

* Wed Jan  6 08:15:36 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.49-1
- 1.16.49

* Tue Jan  5 08:32:30 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.48-1
- 1.16.48

* Mon Jan  4 08:33:46 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.47-1
- 1.16.47

* Wed Dec 30 16:21:43 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.46-1
- 1.16.46

* Wed Dec 30 08:33:40 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.45-1
- 1.16.45

* Tue Dec 29 09:15:14 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.44-1
- 1.16.44

* Thu Dec 24 08:35:52 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.43-1
- 1.16.43

* Wed Dec 23 08:40:18 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.42-1
- 1.16.42

* Tue Dec 22 08:28:41 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.41-1
- 1.16.41

* Fri Dec 18 16:33:01 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.40-1
- 1.16.40

* Fri Dec 18 08:27:56 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.39-1
- 1.16.39

* Thu Dec 17 08:16:39 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.38-1
- 1.16.38

* Wed Dec 16 08:23:45 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.37-1
- 1.16.37

* Tue Dec 15 08:31:33 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.36-1
- 1.16.36

* Mon Dec 14 09:20:28 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.35-1
- 1.16.35

* Fri Dec 11 08:13:23 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.34-1
- 1.16.34

* Thu Dec 10 08:24:55 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.33-1
- 1.16.33

* Wed Dec  9 08:54:55 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.32-1
- 1.16.32

* Tue Dec  8 08:24:27 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.31-1
- 1.16.31

* Mon Dec  7 08:27:14 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.30-1
- 1.16.30

* Fri Dec  4 10:07:40 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.29-1
- 1.16.29

* Wed Dec  2 08:26:03 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.28-1
- 1.16.28

* Tue Dec  1 11:51:40 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.26-1
- 1.16.26

* Mon Nov 30 09:20:03 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.25-1
- 1.16.25

* Tue Nov 24 08:25:36 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.24-1
- 1.16.24

* Mon Nov 23 08:26:26 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.23-1
- 1.16.23

* Fri Nov 20 08:15:00 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.22-1
- 1.16.22

* Thu Nov 19 08:27:37 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.21-1
- 1.16.21

* Wed Nov 18 08:23:10 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.20-1
- 1.16.20

* Tue Nov 17 09:16:39 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.19-1
- 1.16.19

* Mon Nov 16 08:35:57 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.18-1
- 1.16.18

* Thu Nov 12 15:47:25 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.17-1
- 1.16.17

* Thu Nov 12 10:26:50 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.16-1
- 1.16.16

* Wed Nov 11 09:22:58 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.15-1
- 1.16.15

* Mon Nov  9 14:12:50 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.14-1
- 1.16.14

* Mon Nov  9 09:43:37 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.13-1
- 1.16.13

* Fri Nov  6 08:25:16 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.12-1
- 1.16.12

* Thu Nov  5 14:59:57 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.11-1
- 1.16.11

* Tue Nov  3 08:31:00 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.10-1
- 1.16.10

* Mon Nov  2 09:27:02 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.9-1
- 1.16.9

* Fri Oct 30 08:13:44 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.8-1
- 1.16.8

* Thu Oct 29 08:11:35 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.7-1
- 1.16.7

* Wed Oct 28 09:47:49 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.6-1
- 1.16.6

* Tue Oct 27 09:39:05 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.5-1
- 1.16.5

* Fri Oct 23 16:47:32 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.4-1
- 1.16.4

* Fri Oct 23 08:13:24 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.3-1
- 1.16.3

* Thu Oct 22 08:29:33 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.2-1
- 1.16.2

* Tue Oct 20 21:06:52 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.1-1
- 1.16.1

* Tue Oct 20 08:10:45 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.16.0-1
- 1.16.0

* Fri Oct 16 14:55:28 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.18-1
- 1.15.18

* Fri Oct 16 08:09:57 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.17-1
- 1.15.17

* Sat Oct 10 16:04:24 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.16-1
- 1.15.16

* Thu Oct  8 14:31:50 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.15-1
- 1.15.15

* Thu Oct  8 09:00:53 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.14-1
- 1.15.14

* Wed Oct  7 08:56:59 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.13-1
- 1.15.13

* Fri Oct  2 15:35:15 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.11-1
- 1.15.11

* Fri Oct  2 08:20:02 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.10-1
- 1.15.10

* Thu Oct  1 08:15:53 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.9-1
- 1.15.9

* Wed Sep 30 09:04:06 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.8-1
- 1.15.8

* Tue Sep 29 09:14:56 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.7-1
- 1.15.7

* Mon Sep 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.6-1
- 1.15.6

* Fri Sep 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.5-1
- 1.15.5

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.4-1
- 1.15.4

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.3-1
- 1.15.3

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.2-1
- 1.15.2

* Fri Sep 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.1-1
- 1.15.1

* Fri Sep 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.0-1
- 1.15.0

* Wed Sep 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.63-1
- 1.14.63

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.62-1
- 1.14.62

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.61-1
- 1.14.61

* Mon Sep 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.60-1
- 1.14.60

* Fri Sep 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.59-1
- 1.14.59

* Thu Sep 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.58-1
- 1.14.58

* Wed Sep 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.57-1
- 1.14.57

* Tue Sep 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.56-1
- 1.14.56

* Fri Sep 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.55-1
- 1.14.55

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.54-1
- 1.14.54

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.53-1
- 1.14.53

* Tue Sep 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.52-1
- 1.14.52

* Mon Aug 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.51-1
- 1.14.51

* Fri Aug 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.50-1
- 1.14.50

* Thu Aug 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.49-1
- 1.14.49

* Tue Aug 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.48-1
- 1.14.48

* Fri Aug 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.47-1
- 1.14.47

* Wed Aug 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.46-1
- 1.14.46

* Wed Aug 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.45-1
- 1.14.45

* Tue Aug 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.44-1
- 1.14.44

* Mon Aug 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.43-1
- 1.14.43

* Fri Aug 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.42-1
- 1.14.42

* Thu Aug 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.41-1
- 1.14.41

* Wed Aug 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.40-1
- 1.14.40

* Tue Aug 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.39-1
- 1.14.39

* Mon Aug 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.38-1
- 1.14.38

* Thu Aug 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.37-1
- 1.14.37

* Thu Aug 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.36-1
- 1.14.36

* Wed Aug 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.35-1
- 1.14.35

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.34-1
- 1.14.34

* Fri Jul 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.33-1
- 1.14.33

* Fri Jul 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.32-1
- 1.14.32

* Thu Jul 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.31-1
- 1.14.31

* Wed Jul 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.30-1
- 1.14.30

* Tue Jul 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.29-1
- 1.14.29

* Fri Jul 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.28-1
- 1.14.28

* Fri Jul 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.27-1
- 1.14.27

* Thu Jul 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.26-1
- 1.14.26

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.25-1
- 1.14.25

* Tue Jul 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.24-1
- 1.14.24

* Mon Jul 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.23-1
- 1.14.23

* Fri Jul 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.22-1
- 1.14.22

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.21-1
- 1.14.21

* Fri Jul 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.20-1
- 1.14.20

* Thu Jul 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.19-1
- 1.14.19

* Wed Jul 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.18-1
- 1.14.18

* Tue Jul 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.17-1
- 1.14.17

* Fri Jul 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.16-1
- 1.14.16

* Thu Jul 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.15-1
- 1.14.15

* Wed Jul 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.14-1
- 1.14.14

* Tue Jun 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.13-1
- 1.14.13

* Sat Jun 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.12-1
- 1.14.12

* Fri Jun 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.11-1
- 1.14.11

* Thu Jun 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.10-1
- 1.14.10

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.9-1
- 1.14.9

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.8-1
- 1.14.8

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.7-1
- 1.14.7

* Fri Jun 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.6-1
- 1.14.6

* Thu Jun 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.5-1
- 1.14.5

* Wed Jun 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.4-1
- 1.14.4

* Tue Jun 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.3-1
- 1.14.3

* Sat Jun 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.2-1
- 1.14.2

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.1-1
- 1.14.1

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.0-1
- 1.14.0

* Sat Jun 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.24-1
- 1.13.24

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.23-1
- 1.13.23

* Thu Jun 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.22-1
- 1.13.22

* Tue Jun 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.20-1
- 1.13.20

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.19-1
- 1.13.19

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.16-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.16-1
- 1.13.16

* Thu May 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.15-1
- 1.13.15

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.14-1
- 1.13.14

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.11-1
- 1.13.11

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.10-1
- 1.13.10

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.9-1
- 1.13.9

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.8-1
- 1.13.8

* Tue May 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.7-1
- 1.13.7

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.6-1
- 1.13.6

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.5-1
- 1.13.5

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.4-1
- 1.13.4

* Wed May 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.3-1
- 1.13.3

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.2-1
- 1.13.2

* Sat May 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.1-1
- 1.13.1

* Fri May 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.0-1
- 1.13.0

* Thu Apr 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.49-1
- 1.12.49

* Wed Apr 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.48-1
- 1.12.48

* Tue Apr 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.47-1
- 1.12.47

* Sat Apr 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.46-1
- 1.12.46

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.45-1
- 1.12.45

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.44-1
- 1.12.44

* Wed Apr 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.43-1
- 1.12.43

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.42-1
- 1.12.42

* Sun Apr 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.41-1
- 1.12.41

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.40-1
- 1.12.40

* Thu Apr 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.39-1
- 1.12.39

* Wed Apr 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.38-1
- 1.12.38

* Tue Apr 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.37-1
- 1.12.37

* Mon Apr 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.36-1
- 1.12.36

* Fri Apr 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.35-1
- 1.12.35

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.34-1
- 1.12.34

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.33-1
- 1.12.33

* Mon Mar 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.32-1
- 1.12.32

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.31-1
- 1.12.31

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.30-1
- 1.12.30

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.29-1
- 1.12.29

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.28-1
- 1.12.28

* Tue Mar 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.27-1
- 1.12.27

* Sat Mar 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.26-1
- 1.12.26

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.25-1
- 1.12.25

* Thu Mar 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.24-1
- 1.12.24

* Wed Mar 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.23-1
- 1.12.23

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.22-1
- 1.12.22

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.21-1
- 1.12.21

* Fri Mar 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.20-1
- 1.12.20

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.19-1
- 1.12.19

* Wed Mar 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.18-1
- 1.12.18

* Tue Mar 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.17-1
- 1.12.17

* Sun Mar 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.16-1
- 1.12.16

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.15-1
- 1.12.15

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.14-1
- 1.12.14

* Wed Mar 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.13-1
- 1 12.13

* Tue Mar 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.12-1
- 1.12.12

* Fri Feb 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.9-1
- 1.12.9

* Thu Feb 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.12.8-1
- Update to 1.12.8

* Wed Feb 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.7-1
- 1.12.7

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.6-1
- 1.12.6

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.5-1
- 1.12.5

* Fri Feb 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.4-1
- 1.12.4

* Thu Feb 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.3-1
- 1.12.3

* Wed Feb 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.11.17-1
- 1.11.17

* Fri Feb 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.11.12-1
- Update to 1.11.12

* Wed Jan 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.11.9-1
- Update to 1.11.9

* Fri Jan 17 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.11.4-1
- Update to 1.11.4 (rhbz#1677949)

* Mon Jan 13 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.11.0-1
- Update to 1.11.0 (rhbz#1677949)

* Wed Nov 20 2019 Orion Poplawski <orion@nwra.com> - 1.10.22-1
- Update to 1.10.21

* Mon Sep 09 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.9.225-1
- Update to 1.9.225 (rhbz#1677949)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.101-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.101-1
- Update to 1.9.101

* Fri Feb 15 2019 Kevin Fenzi <kevin@scrye.com> - 1.9.96-1
- Update to 1.9.96. Fixes bug #1667629

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.15-3
- Enable python dependency generator

* Thu Dec 20 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.15-2
- Subpackage python2-boto3 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Oct 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.9.15-1
- Update to 1.9.15

* Wed Jul 18 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 1.7.41-1
- Upstream 1.7.41 (Fix compat with botocore 1.10.41)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 28 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.19-1
- Update to 1.5.19

* Sat Jan 20 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.18-1
- Update to 1.5.18

* Tue Jan 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.15-1
- Update to 1.5.15

* Wed Jan 10 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.12-1
- Update to 1.5.12

* Wed Jan 03 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.7-1
- Update to 1.5.7

* Sun Aug 13 2017 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.6-1
- Update to 1.4.6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.4-1
- Update to 1.4.4

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.3-1
- Update to 1.4.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuild for Python 3.6

* Sat Dec 03 2016 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.2-1
- Update to 1.4.2

* Mon Oct 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Aug 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.0-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.1-1
- New upstream release

* Tue Mar 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.0-1
- New upstream release

* Fri Feb 19 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.2.4-1
- New upstream release

* Thu Feb 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.2.3-3
- Fix python2- subpackage to require python-future

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.2.3-1
- Initial package.
