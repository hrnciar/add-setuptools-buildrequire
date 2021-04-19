Name:           python-fastjsonschema
Version:        2.15.0
Release:        1%{?dist}
Summary:        Fastest Python implementation of JSON schema

License:        BSD
URL:            https://github.com/horejsek/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
fastjsonschema implements validation of JSON documents by JSON schema.
The library implements JSON schema drafts 04, 06 and 07.
The main purpose is to have a really fast implementation.}

%description %_description

%package -n     python3-fastjsonschema
Summary:        %{summary}

%description -n python3-fastjsonschema %_description

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fastjsonschema

%check
%tox

%files -n python3-fastjsonschema -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Thu Feb  4 09:47:59 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.15.0-1
- Update 2.15.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.14.5-1
- Initial package
