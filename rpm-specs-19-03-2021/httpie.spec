Name:           httpie
Version:        2.3.0
Release:        3%{?dist}
Summary:        A Curl-like tool for humans

License:        BSD
URL:            https://httpie.org/
Source0:        https://pypi.python.org/packages/source/h/httpie/httpie-%{version}.tar.gz
BuildArch:      noarch


BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sed

# Needed so we can build the manpage with help2man without fataling.
BuildRequires:  %{py3_dist pygments}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist requests-toolbelt}
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires:  %{py3_dist requests[socks]}
%endif

BuildRequires:  help2man

Obsoletes:      python2-httpie <= 0.9.4-3
Obsoletes:      python3-httpie <= 0.9.4-3

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%prep
%autosetup
sed -i '/#!\/usr\/bin\/env/d' %{name}/__main__.py

%build
%py3_build

%install
%py3_install

export PYTHONPATH=%{buildroot}%{python3_sitelib}

# Generate man pages for everything
mkdir -p %{buildroot}/%{_mandir}/man1
help2man %{buildroot}/%{_bindir}/http > %{buildroot}/%{_mandir}/man1/http.1
help2man %{buildroot}/%{_bindir}/https > %{buildroot}/%{_mandir}/man1/https.1


%files
%doc README.rst
%license LICENSE
%{_mandir}/man1/http.1*
%{_mandir}/man1/https.1*
%{_bindir}/http
%{_bindir}/https

%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Nils Philippsen <nils@tiptoe.de> - 2.3.0-2
- use macros for Python dependencies
- add missing Python dependencies needed for running help2man
- remove manual Python dependencies
- discard stderr when running help2man

* Thu Dec 24 2020 Nils Philippsen <nils@tiptoe.de> - 2.3.0-1
- version 2.3.0
- Python 2 is no more
- use %%autosetup and Python build macros
- remove EL7-isms
- explicitly require sed for building

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Rick Elrod <relrod@redhat.com> - 1.0.3-1
- Latest upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-15
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-8
- Fix help2man usage with python3.
  https://bugzilla.redhat.com/show_bug.cgi?id=1430733

* Mon Feb 27 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-7
- Fix missing Requires.  https://bugzilla.redhat.com/show_bug.cgi?id=1417730

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 2 2017 Ricky Elrod <relrod@redhat.com> - 0.9.4-5
- Add missing Obsoletes.

* Mon Jan 2 2017 Ricky Elrod <relrod@redhat.com> - 0.9.4-4
- Nuke python-version-specific subpackages. Just use py3 if we can.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 05 2016 Ricky Elrod <relrod@redhat.com> - 0.9.4-1
- Update to latest upstream.

* Fri Jun 03 2016 Ricky Elrod <relrod@redhat.com> - 0.9.3-4
- Add proper Obsoletes for rhbz#1329226.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.9.3-2
- Modernize python macros and subpackaging.
- Move LICENSE to %%license macro.
- Make python3 the default on modern Fedora.

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.9.3-1
- new version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Ricky Elrod <relrod@redhat.com> - 0.9.2-1
- Latest upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Jan 31 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.8.0-1
- Latest upstream release.

* Fri Oct 4 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.2-2
- Add in patch to work without having python-requests 2.0.0.

* Sat Sep 28 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.2-1
- Latest upstream release.

* Thu Sep 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-7
- Only try building the manpage on Fedora, since RHEL's help2man doesn't
  have the --no-discard-stderr flag.

* Thu Sep 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-6
- Loosen the requirement on python-pygments.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 2 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-4
- python-requests 1.2.3 exists in rawhide now.

* Sun Jun 30 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-3
- Patch to use python-requests 1.1.0 for now.

* Sat Jun 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-2
- Update to latest upstream release.

* Mon Apr 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-2
- Fix changelog messup.

* Mon Apr 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-1
- Update to latest upstream release.

* Mon Apr 8 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-3
- Fix manpage generation by exporting PYTHONPATH.

* Tue Mar 26 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-2
- Include Python3 support, and fix other review blockers.

* Mon Mar 11 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-1
- Update to latest upstream release

* Thu Jul 19 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.5-1
- Initial build.
