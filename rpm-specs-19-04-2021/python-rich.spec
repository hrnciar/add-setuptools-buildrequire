# Created by pyp2rpm-3.3.4
%global pypi_name rich

Name:           python-%{pypi_name}
Version:        10.1.0
Release:        1%{?dist}
Summary:        Render rich text and beautiful formatting in the terminal

License:        MIT
URL:            https://github.com/willmcgugan/rich
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Apr 07 2021 Parag Nemade <pnemade AT redhat DOT com> - 10.1.0-1
- Update to 10.1.0 version (#1945988)

* Wed Mar 31 2021 Parag Nemade <pnemade AT redhat DOT com> - 10.0.1-1
- Update to 10.0.1 version (#1944804)

* Sat Mar 27 2021 Parag Nemade <pnemade AT redhat DOT com> - 10.0.0-1
- Update to 10.0.0 version (#1943805)

* Mon Mar 08 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.13.0-1
- Update to 9.13.0 version (#1936085)

* Thu Mar 04 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.12.4-1
- Update to 9.12.4 version (#1933882)

* Sun Feb 28 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.12.3-1
- Update to 9.12.3 version (#1933478)

* Sun Feb 28 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.12.2-1
- Update to 9.12.2 version (#1931063)

* Tue Feb 16 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.11.0-1
- Update to 9.11.0 version (#1928971)

* Tue Feb  2 14:22:24 IST 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.10.0-1
- Update to 9.10.0 version (#1921301)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 08:37:21 IST 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.9.0-1
- Update to 9.9.0 version (#1915923)

* Tue Jan 12 14:05:31 IST 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.8.0-1
- Update to 9.8.0 version (#1913979)

* Sat Jan  2 21:51:00 IST 2021 Parag Nemade <pnemade AT redhat DOT com> - 9.6.1-1
- Update to 9.6.1 version (#1911840)

* Thu Dec 31 22:12:44 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 9.6.0-1
- Update to 9.6.0 version (#1911672)

* Tue Dec 22 20:05:06 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 9.5.1-1
- Update to 9.5.1 version (#1909212)

* Fri Dec 18 13:36:15 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 9.4.0-1
- Update to 9.4.0 version (#1907029)

* Thu Dec  3 15:11:46 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 9.3.0-1
- Update to 9.3.0 version (#1903254)

* Fri Nov 13 12:18:46 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 9.2.0-1
- Update to 9.2.0 version (#1895694)

* Sat Oct 24 12:47:42 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 9.1.0-1
- Update to 9.1.0 version (#1889145)

* Sun Oct 18 16:38:50 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 8.0.0-1
- Update to 8.0.0 version (#1884915)

* Thu Oct  1 08:41:03 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 7.1.0-1
- Update to 7.1.0 version (#1882733)

* Wed Aug 26 2020 Parag Nemade <pnemade AT redhat DOT com> - 6.0.0-1
- Initial package.
