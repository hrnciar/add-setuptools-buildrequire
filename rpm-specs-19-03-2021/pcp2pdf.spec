Name:           pcp2pdf
Version:        0.3
Release:        22%{?dist}
Summary:        Utility to create PDF reports from PCP archives

License:        GPLv2+
URL:            https://github.com/performancecopilot/pcp2pdf
Source0:        https://github.com/performancecopilot/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-spurious-python-interpreter.patch

Requires:       python3-reportlab
Requires:       python3-matplotlib
Requires:       python3-pcp

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Utility to create PDF reports from Performance Co-Pilot archives. It allows to
choose sampling rate, custom graphs, custom labels and selection of which
metrics should appear in the report.

%prep
%setup -q
%patch0 -p1 -b .orig

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 man/pcp2pdf.1 $RPM_BUILD_ROOT%{_mandir}/man1
# FIXME: bash completion is not yet there
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/pcp/pcp2pdf
# Note that when this lands it should go in {_datadir}/bash-completion/completions/
# and not in {_sysconfdir}/bash_completion.d
%{_bindir}/%{name}
%{_mandir}/*/*
%{_datadir}/%{name}/*
# For noarch packages: sitelib
%{python3_sitelib}/*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Michele Baldessari <michele@acksyn.org> - 0.3-21
- Add python3-setuptools BR

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-19
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3-12
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3-8
- Rebuild for Python 3.6

* Tue Sep 27 2016 Lukas Berk <lberk@redhat.com> - 0.3-7
- Rebuild for broken python3-matplotlib dependency

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Michele Baldessari <michele@acksyn.org> - 0.3-3
- Own /usr/share/pcp2pdf
* Wed Jun 03 2015 Michele Baldessari <michele@acksyn.org> - 0.3-2
- Incorporate suggestions from Fedora review (remove buildroot, defattr,
  remove a spurios /usr/bin/python line, do not use macros when not needed) 
* Mon Jun 01 2015 Michele Baldessari <michele@acksyn.org> - 0.3-1
- New upstream
* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.2-1
- New upstream
* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.1-3
- Fix URLs
* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.1-2
- Port to Python 3
* Tue Oct 28 2014 Michele Baldessari <michele@redhat.com> - 0.1-1
- Initial release
