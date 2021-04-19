Name:           tldr
Version:        1.2.1
Release:        1%{?dist}
Summary:        Simplified and community-driven man pages

License:        MIT
URL:            https://github.com/tldr-pages/tldr-python-client
Source0:        https://github.com/tldr-pages/tldr-python-client/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-colorama 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six
BuildRequires:  python3-termcolor
# dependencies for %%check
BuildRequires:  python3-argcomplete
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner

Requires:       python3-colorama
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-termcolor

%description
A Python command line client for tldr - Simplified and community-driven
man pages http://tldr-pages.github.io/.

%prep
%autosetup -n %{name}-python-client-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -k "not test_error_message"

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/*.pyc
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Apr 02 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.2.1-1
- Update to 1.2.1

* Mon Feb 01 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.2.0-1
- Update to 1.2.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.1.0-1
- Update to 1.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5-2
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Lumír Balhar <lbalhar@redhat.com> - 0.5-1
- Update to 0.5 (#1800511)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Lumír Balhar <lbalhar@redhat.com> - 0.4.4-1
- New upstream version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Lumir Balhar <lbalhar@redhat.com> - 0.4.2-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Lumir Balhar <lbalhar@redhat.com> - 0.4.1-1
- Initial package.
