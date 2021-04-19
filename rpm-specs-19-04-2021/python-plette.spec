Name:           python-plette
Version:        0.2.3
Release:        1%{?dist}

License:        ISC
URL:            https://github.com/sarugaku/plette
Source0:        https://github.com/sarugaku/plette/archive/%{version}/plette-%{version}.tar.gz

Summary:        Pipfle and Pipfile.lock parsers, generators and validators

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest

%global _description %{expand:
Plette implements Pipfle and Pipfile.lock parsers, generators, and optional
validators to let the user work with them in a structured manner.

Validation support is provided by the extra package 'python3-plette+validation'.
}

%description %_description

%package -n python3-plette
Summary:        %{summary}

%description -n python3-plette %_description

%pyproject_extras_subpkg -n python3-plette validation

%prep
%autosetup -p1 -n plette-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files plette


%check
%pytest -v tests


%files -n python3-plette -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Thu Jan 28 2021 Petr Viktorin <pviktori@redhat.com> - 0.2.3-1
- Update to 0.2.3
- Switch to pyproject macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.8

* Sun May 12 2019 Patrik Kopkan <pkopkan@redhat.com> 0.2.2-1
- initial package
