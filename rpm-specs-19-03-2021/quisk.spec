Name:           quisk
Version:        4.1.80
Release:        1%{?dist}
Summary:        Software Defined Radio (SDR) software

License:        GPLv2 and BSD
URL:            http://james.ahlstrom.name/quisk/
Source0:        https://files.pythonhosted.org/packages/source/q/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-wxpython4
BuildRequires:  fftw-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  dos2unix
BuildRequires:  libsoundio-devel
Requires:       python3-wxpython4
Suggests:       codec2-devel

%description
QUISK is a Software Defined Radio (SDR) which can control various
radio hardware. QUISK supports CW, SSB, and AM.

%prep
%setup -q

dos2unix afedrinet/sdr_control.py

# remove binaries, etc
find . -name \*.pyc -exec rm {} \;
find . -name \*.pyd -exec rm {} \;
find . -name \*.so -exec rm {} \;
find . -name \*.dll -exec rm {} \;

# remove execute permissions from everything
find . -type f -exec chmod a-x {} \;

# fix shebangs
sed -i 's|#!\s*/usr/bin/python|#!/usr/bin/python3|;s|#!\s*/usr/bin/env\s\+python|#!/usr/bin/python3|' \
  quisk.py quisk_vna.py portaudio.py n2adr/startup.py \
  afedrinet/sdr_control.py afedrinet/afedri.py

%build
CFLAGS="%{optflags}" %{__python3} setup.py build_ext --inplace
%py3_build

%install
%py3_install
# make Python scripts with shebangs executable
for f in `find %{buildroot}%{python3_sitearch}/%{name} -name \*.py`
do
    grep -E -q '^#!' $f && chmod a+x $f
done

%files
%license license.txt
%doc docs.html defaults.html
%doc help.html help_conf.html help_vna.html
%{_bindir}/%{name}{,_vna}
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Feb 22 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.80-1
- New version
  Resolves: rhbz#1931081

* Thu Feb 18 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.79-1
- New version
  Resolves: rhbz#1930349

* Tue Feb 16 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.78-1
- New version
  Resolves: rhbz#1928278

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.77-1
- New version
  Resolves: rhbz#1918484

* Thu Jan 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.76-1
- New version
  Resolves: rhbz#1916497

* Tue Dec 22 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.75-1
- New version
  Resolves: rhbz#1909830

* Wed Dec  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.74-1
- New version
  Resolves: rhbz#1906161

* Wed Nov 11 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.73-1
- New version
  Resolves: rhbz#1896889

* Wed Sep 23 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.72-1
- New version
  Resolves: rhbz#1880465

* Tue Sep  8 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.71-1
- New version
  Resolves: rhbz#1875953

* Sun Aug 30 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.70-1
- New version
  Resolves: rhbz#1873818

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.69-1
- New version
  Resolves: rhbz#1871976

* Sat Aug 15 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.68-1
- New version
  Resolves: rhbz#1868941

* Fri Jul 31 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.67-1
- New version
  Resolves: rhbz#1862424

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.66-1
- New version
  Resolves: rhbz#1858527

* Thu Jul  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.65-1
- New version
  Resolves: rhbz#1854984

* Wed Jul  8 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.64-2
- Enabled libsoundio support

* Thu Jul  2 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.64-1
- New version
  Resolves: rhbz#1853315

* Sun Jun 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.63-1
- New version
  Related: rhbz#1851600

* Sun Jun 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.62-1
- New version
  Resolves: rhbz#1851600

* Fri Jun 26 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.61-1
- New version
  Resolves: rhbz#1851441

* Tue Jun 23 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.60-1
- New version
  Resolves: rhbz#1849989

* Mon Jun 22 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.59-1
- New version
  Resolves: rhbz#1849289

* Wed Jun 17 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.58-1
- New version
  Resolves: rhbz#1847630

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.57-2
- Rebuilt for Python 3.9

* Thu May  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.57-1
- New version
  Resolves: rhbz#1833089

* Fri Apr 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.56-1
- New version
  Resolves: rhbz#1822719

* Mon Apr  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.55-1
- New version
  Resolves: rhbz#1820661

* Wed Apr  1 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.54-1
- New version
  Resolves: rhbz#1819225

* Fri Mar 27 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.53-1
- New version
  Resolves: rhbz#1818091

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.52-1
- New version
  Resolves: rhbz#1783705

* Sun Nov 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.51-1
- New version
  Resolves: rhbz#1775966

* Thu Nov 21 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.50-1
- New version
  Resolves: rhbz#1774760

* Fri Nov 15 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.49-1
- New version
  Resolves: rhbz#1772608

* Fri Nov  8 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.48-2
- Switched to Python 3
  Resolves: rhbz#1737848

* Wed Nov  6 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.48-1
- New version
  Resolves: rhbz#1769036

* Thu Oct 31 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.47-1
- New version
  Resolves: rhbz#1767463

* Tue Oct 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.46-1
- New version
  Resolves: rhbz#1764201

* Mon Sep 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.45-2
- Fixed CTCSS tone generation
- Fixed traceback on systems with unicode pulseaudio device names

* Tue Sep 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.45-1
- New version
  Resolves: rhbz#1751364

* Fri Aug 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.43-1
- New version
  Resolves: rhbz#1747002

* Fri Aug 23 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.42-1
- New version
  Resolves: rhbz#1744610

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.41-1
- New version
  Resolves: rhbz#1723961

* Mon Jun 10 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.40-1
- New version
  Resolves: rhbz#1718590

* Fri May 10 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.39-1
- New version
  Resolves: rhbz#1708747

* Thu Apr 18 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.38-1
- New version
  Resolves: rhbz#1701354

* Wed Apr 10 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.37-1
- New version
  Resolves: rhbz#1698049

* Fri Mar 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.36-1
- Updated to latest upstream
  Resolves: rhbz#1632940
  Resolves: rhbz#1632941
- Added weak dependency on codec2-devel for FreeDV support
  Resolves: rhbz#1633195

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Eric Smith <brouhaha@fedoraproject.org> 4.1.17-1
- Updated to latest upstream.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Eric Smith <brouhaha@fedoraproject.org> 4.1.10-1
- Updated to latest upstream.
- Spec changes per package review (#1443429).

* Wed Apr 19 2017 Eric Smith <brouhaha@fedoraproject.org> 4.1.3-1
- Initial version.
