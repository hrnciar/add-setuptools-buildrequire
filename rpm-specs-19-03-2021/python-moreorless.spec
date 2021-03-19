%global srcname moreorless

%bcond_without tests

Name:           python-%{srcname}
Version:        0.3.0
Release:        2%{?dist}
Summary:        Python diff wrapper
License:        MIT
URL:            https://github.com/thatch/moreorless/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist setuptools_scm}
%if %{with tests}
BuildRequires:  %{py3_dist click}
BuildRequires:  %{py3_dist coverage}
BuildRequires:  %{py3_dist parameterized}
BuildRequires:  %{py3_dist volatile}
%endif


%global _description %{expand:
This is a thin wrapper around difflib.unified_diff that Does The Right Thing for
"No newline at eof". The args are also simplified compared to difflib.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%{python3} -m coverage run -m moreorless.tests
%endif


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%exclude %{python3_sitelib}/%{srcname}/py.typed
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.3.0-1
- Initial package
