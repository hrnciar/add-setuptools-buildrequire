Name:           python-pyev
Version:        0.9.0
License:        GPLv3+
Summary:        Python binding for the libev library
URL:            https://github.com/gabrielfalcao/pyev
#               https://code.google.com/archive/p/pyev/


%global         gituser         gabrielfalcao
%global         gitname         pyev
%global         gitdate         20130610
%global         commit          e31d13720916439038290d57d00ee3604298705f
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} >= 7 )
%global with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%endif

%if 0%{?fedora} <= 21
 %{!?py3_build:         %global py3_build       %{__python3} setup.py build --executable="%{__python3} -s"}
 %{!?py3_install:       %global py3_install     %{__python3} setup.py install -O1 --skip-build --root %{buildroot}}
%endif

# Build source is github release=1 or git commit=0
%global         build_release    0

%if 0%{?build_release}  > 0
Release:        13%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        0.13.%{gitdate}git%{shortcommit}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
%endif #build_release

# https://bugzilla.redhat.com/show_bug.cgi?id=1817984
Patch1:         python3.9.patch

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libev-devel

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif # if with_python3

# html doc generation


%description
Python binding for the libev library.
The libev is an event loop: you register interest in certain events (such
as a file descriptor being readable or a timeout occurring), and it will 
manage these event sources and provide your program with events.



%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{gitname}
Summary:        Python3 binding for the libev library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{gitname}}



%description -n python%{python3_pkgversion}-%{gitname}
The libev for Python3 wrapper - This is a Python extension that gives access
to libev library to be called from Python scripts.
%endif # with_python3

%prep
%if 0%{?build_release} > 0
# Build from git release version
%autosetup -p1 -n %{gitname}-%{version}

%else
# Build from git commit
%autosetup -p1 -n %{gitname}-%{commit}
%endif


%build

%if 0%{?with_python3}
%py3_build
%endif # with_python3



%install

%if 0%{?with_python3}
%py3_install
%endif # with_python3


#check


%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{gitname}
#license LICENSE
%doc README.md
%{python3_sitearch}/%{gitname}*
%endif # with_python3


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.13.20130610gite31d137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.12.20130610gite31d137
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.11.20130610gite31d137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.9.0-0.10.20130610gite31d137
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.9.20130610gite31d137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.9.0-0.8.20130610gite31d137
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.7.20130610gite31d137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.6.20130610gite31d137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.9.0-0.5.20130610gite31d137
- Don't BR python2

* Wed Oct 10 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.9.0-0.4.20130610gite31d137
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.3.20130610gite31d137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.9.0-0.2.20130610gite31d137
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Michal Ambroz <rebus at, seznam.cz> - 0.9.0-0.1
- initial package for Fedora

