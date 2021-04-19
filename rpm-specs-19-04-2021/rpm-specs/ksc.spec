%global forgeurl https://github.com/RedHatOfficial/ksc
%global commitdate 20210216
%global commit 5955c6b2288353c5b093677221cc91a83a2c800c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%{?python_enable_dependency_generator}
%forgemeta -i

Name:		ksc
Version:	1.7
Release:	1%{?dist}
Summary:	Kernel source code checker
Group:		Development/Tools
AutoReqProv:	no
License:	GPLv2+
URL:		https://github.com/RedHatOfficial/ksc
BuildArch:	noarch
Requires:	kmod
Requires:	binutils
Requires:	kernel-devel
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Source0:	https://github.com/RedHatOfficial/ksc/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

%description
A kernel module source code checker to find usage of select symbols

%prep
%forgesetup

%build
%py3_build

%install
%py3_install
install -D ksc.1 %{buildroot}%{_mandir}/man1/ksc.1

%files
%license COPYING
%doc README PKG-INFO
%{_bindir}/ksc
%{_datadir}/ksc
%{_mandir}/man1/ksc.*
%config(noreplace) %{_sysconfdir}/ksc.conf
%{python3_sitelib}/ksc-%{version}*.egg-info

%changelog
* Tue Jan 05 2021 Čestmír Kalina <ckalina@redhat.com> - 1.7-1
- Initial Fedora commit.
