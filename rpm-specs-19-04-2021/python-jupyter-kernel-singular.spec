%global srcname jupyter-kernel-singular
%global upname  jupyter_kernel_singular

Name:           python-%{srcname}
Version:        0.9.9
Release:        5%{?dist}
Summary:        Jupyter kernel for Singular

License:        GPLv2+
URL:            https://github.com/sebasguts/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist pysingular}

%global _description %{expand:
This package contains a Jupyter kernel for Singular, to enable using
Jupyter as the front end for Singular.}

%description %_description

%package     -n python3-%{srcname}
Summary:        Jupyter kernel for Singular
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist jupyter-client}
Requires:       %{py3_dist pysingular}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{upname}-%{version}

%build
%py3_build

%install
%py3_install

# We want /etc, not /usr/etc
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%files       -n python3-%{srcname}
%doc README.md
%license COPYING GPLv2 LICENSE
%{python3_sitelib}/%{upname}*
%{_datadir}/jupyter/kernels/singular/
%{_datadir}/jupyter/nbextensions/singular-mode/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/singular-mode.json

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 0.9.9-1
- Initial RPM
