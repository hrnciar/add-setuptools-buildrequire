%global srcname pathvalidate

Name:      python-%{srcname}
Version:   2.3.2
Release:   2%{?dist}
Summary:   Library to sanitize/validate a string such as file-names/file-paths/etc

License:   MIT
URL:       https://github.com/thombashi/pathvalidate
Source0:   %{pypi_source}
BuildArch: noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-allpairspy
BuildRequires:  python3-click

%description -n python3-%{srcname}
%{summary}.

%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

# https://github.com/thombashi/pathvalidate/issues/17
chmod -R -x+X .


%build
%py3_build

%install
%py3_install

%check
%{pytest}


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Mar 19 2021 Jonny Heggheim <hegjon@gmail.com> - 2.3.2-2
- Enabled unit tests

* Fri Mar 05 2021 Jonny Heggheim <hegjon@gmail.com> - 2.3.2-1
- Initial package
