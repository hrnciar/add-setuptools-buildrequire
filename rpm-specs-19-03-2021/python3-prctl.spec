%global srcname python-prctl
Name:           python3-prctl
Version:        1.6.1
Release:        12%{?dist}
Summary:        Python(ic) interface to the linux prctl syscall

License:        GPLv3+
URL:            https://pythonhosted.org/python-prctl/
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/seveas/python-prctl/master/COPYING

BuildRequires:  libcap-devel
BuildRequires:  glibc-devel
BuildRequires:  python3-devel
BuildRequires:  gcc

%description
Control process attributes through prctl


%prep
%autosetup -n %{srcname}-%{version}
cp -p %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files
%doc README
%license COPYING
%{python3_sitearch}/prctl.py
%{python3_sitearch}/__pycache__/prctl*
%{python3_sitearch}/_prctl*
%{python3_sitearch}/python_prctl*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Kushal Das <kushal@fedoraproject.org> 1.6.1-2
- Fixes from review

* Tue Oct 04 2016 Kushal Das <kushal@fedoraproject.org> 1.6.1-1
- Initial package
