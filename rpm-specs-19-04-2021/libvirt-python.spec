# -*- rpm-spec -*-

# This spec file assumes you are building on a Fedora or RHEL version
# that's still supported by the vendor. It may work on other distros
# or versions, but no effort will be made to ensure that going forward
%define min_rhel 7
%define min_fedora 29

%if (0%{?fedora} && 0%{?fedora} >= %{min_fedora}) || (0%{?rhel} && 0%{?rhel} >= %{min_rhel})
    %define supported_platform 1
%else
    %define supported_platform 0
%endif

Summary: The libvirt virtualization API python3 binding
Name: libvirt-python
Version: 7.2.0
Release: 1%{?dist}
Source0: http://libvirt.org/sources/python/%{name}-%{version}.tar.gz
Url: http://libvirt.org
License: LGPLv2+
BuildRequires: libvirt-devel == %{version}
BuildRequires: python3-devel
%if 0%{?rhel} == 7
BuildRequires: python36-nose
BuildRequires: python36-lxml
%else
BuildRequires: python3-nose
BuildRequires: python3-lxml
%endif
BuildRequires: gcc

# Don't want provides for python shared objects
%{?filter_provides_in: %filter_provides_in %{python3_sitearch}/.*\.so}
%{?filter_setup}

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%package -n python3-libvirt
Summary: The libvirt virtualization API python3 binding
Url: http://libvirt.org
License: LGPLv2+
%{?python_provide:%python_provide python3-libvirt}
Provides: libvirt-python3 = %{version}-%{release}
Obsoletes: libvirt-python3 <= 3.6.0-1%{?dist}

%description -n python3-libvirt
The python3-libvirt package contains a module that permits applications
written in the Python 3.x programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep
%setup -q

# Unset execute bit for example scripts; it can introduce spurious
# RPM dependencies, like /usr/bin/python3
# for the -python3 package
find examples -type f -exec chmod 0644 \{\} \;

%build
%if ! %{supported_platform}
echo "This RPM requires either Fedora >= %{min_fedora} or RHEL >= %{min_rhel}"
exit 1
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%py3_build
%else
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
%endif

%install
%if 0%{?fedora} || 0%{?rhel} >= 8
%py3_install
%else
%{__python3} setup.py install --skip-build --root=%{buildroot}
%endif

%check
%{__python3} setup.py test

%files -n python3-libvirt
%doc ChangeLog AUTHORS README COPYING COPYING.LESSER examples/
%{python3_sitearch}/libvirt.py*
%{python3_sitearch}/libvirtaio.py*
%{python3_sitearch}/libvirt_qemu.py*
%{python3_sitearch}/libvirt_lxc.py*
%{python3_sitearch}/__pycache__/libvirt.cpython-*.py*
%{python3_sitearch}/__pycache__/libvirt_qemu.cpython-*.py*
%{python3_sitearch}/__pycache__/libvirt_lxc.cpython-*.py*
%{python3_sitearch}/__pycache__/libvirtaio.cpython-*.py*
%{python3_sitearch}/libvirtmod*
%{python3_sitearch}/*egg-info


%changelog
* Mon Apr 05 2021 Cole Robinson <crobinso@redhat.com> - 7.2.0-1
- Update to version 7.2.0

* Mon Mar 01 2021 Cole Robinson <crobinso@redhat.com> - 7.1.0-1
- Update to version 7.1.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Cole Robinson <crobinso@redhat.com> - 7.0.0-1
- Update to version 7.0.0

* Tue Dec 01 2020 Cole Robinson <crobinso@redhat.com> - 6.10.0-1
- Update to version 6.10.0

* Tue Nov 03 2020 Cole Robinson <crobinso@redhat.com> - 6.9.0-1
- Update to version 6.9.0

* Thu Oct 15 2020 Daniel P. Berrangé <berrange@redhat.com> - 6.8.0-2
- Fix regression with snapshot handling (rhbz #1888709)

* Fri Oct 02 2020 Cole Robinson <crobinso@redhat.com> - 6.8.0-1
- Update to version 6.8.0

* Wed Sep 02 2020 Cole Robinson <crobinso@redhat.com> - 6.7.0-1
- Update to version 6.7.0

* Tue Aug 04 2020 Cole Robinson <crobinso@redhat.com> - 6.6.0-1
- Update to version 6.6.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Cole Robinson <crobinso@redhat.com> - 6.5.0-1
- Update to version 6.5.0

* Tue Jun 02 2020 Cole Robinson <crobinso@redhat.com> - 6.4.0-1
- Update to version 6.4.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.3.0-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Cole Robinson <crobinso@redhat.com> - 6.3.0-1
- Update to version 6.3.0

* Thu Apr 02 2020 Cole Robinson <crobinso@redhat.com> - 6.2.0-1
- Update to version 6.2.0

* Wed Mar 04 2020 Cole Robinson <crobinso@redhat.com> - 6.1.0-1
- Update to version 6.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Cole Robinson <crobinso@redhat.com> - 6.0.0-1
- Update to version 6.0.0
