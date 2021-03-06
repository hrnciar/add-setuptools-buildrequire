%global pypi_name pulsectl

Name:           python-%{pypi_name}
Version:        21.3.2
Release:        1%{?dist}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

License:        MIT
URL:            https://pypi.org/project/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/1a/a9/cdd1a19889f78ddd45775b9830045df2b4eb25f63911a2ddc3aaf8ec614f/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pulseaudio-libs

%description
Python (3.x and 2.x) high-level interface and ctypes-based bindings
for PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%package     -n python3-%{pypi_name}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

%description -n python3-%{pypi_name}
Python 3.x high-level interface and ctypes-based bindings for
PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%prep
%setup -n %{pypi_name}-%{version}


%build
%{py3_build}


%install
%{py3_install}


%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*egg-info/


%changelog
* Sat Mar  6 2021 Paul W. Frields <stickster@gmail.com> - 21.3.2-1
- New upstream release 21.3.2 (#1932817)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Paul W. Frields <stickster@gmail.com> - 20.5.1-2
- New upstream release 20.5.1 (#1837830)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.4.3-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Paul W. Frields <stickster@gmail.com> - 20.4.3-1
- New upstream release 20.4.3 (#1825597)

* Tue Mar  3 2020 Paul W. Frields <stickster@gmail.com> - 20.2.4-1
- New upstream release 20.2.4 (#1808016)

* Tue Feb 11 2020 Paul W. Frields <stickster@gmail.com> - 20.2.2-1
- New upstream release 20.2.2 (#1790078)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov  9 2019 Paul W. Frields <stickster@gmail.com> - 19.10.4-1
- Update to latest upstream 19.10.4 (#1759622)

* Mon Oct 14 2019 Paul W. Frields <stickster@gmail.com> - 19.10.0-1
- Update to latest upstream 19.10.0 (#1759622)

* Wed Sep 25 2019 Paul W. Frields <stickster@gmail.com> - 19.9.5-1
- Update to latest upstream 19.9.5 (#1754263)

* Wed Sep  4 2019 Paul W. Frields <stickster@gmail.com> - 18.12.5-1
- Initial RPM release
