%global srcname allpairspy

Name:      python-%{srcname}
Version:   2.5.0
Release:   1%{?dist}
Summary:   Pairwise test combinations generator

License:   MIT
URL:       https://github.com/thombashi/allpairspy
Source0:   %{pypi_source}

#https://github.com/thombashi/allpairspy/pull/9
Source1:   https://raw.githubusercontent.com/thombashi/allpairspy/v2.5.0/LICENSE.txt

BuildArch: noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-pytest

%description -n python3-%{srcname}
%{summary}.

%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

chmod -R -x+X .
install -m 644 %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{pytest}


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue Mar 16 2021 Jonny Heggheim <hegjon@gmail.com> - 2.5.0-1
- Initial package
