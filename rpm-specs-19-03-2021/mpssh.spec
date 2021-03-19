%global commit	39b7ceece0e3daf675444ec711efd9fc534c100a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		mpssh
Version:	1.3.3
Release:	13%{?dist}
Summary:	Parallel ssh tool

License:	BSD
URL:		https://github.com/ndenev/%{name}
Source0:	https://github.com/ndenev/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:		mpssh-1.3.3.dont_override_cflags.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	openssh-clients
Requires:	openssh-clients

%description
mpssh is a parallel ssh tool. What it does is connecting to a number of hosts
specified in the hosts file and execute the same command on all of them


%prep
%setup -q -n %{name}-%{commit}
%patch0

%build
# No configure, so set compiler FLAGS manually
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
LDFLAGS="${LDFLAGS:-%?__global_ldflags}"; export LDFLAGS
make %{?_smp_mflags}
sed -i "s,/usr/local,%{_prefix},g" %{name}.1
cp debian/copyright .
gzip %{name}.1


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz


%files
%doc README
%if 0%{?rhel} <= 6
%doc copyright
%else
%license copyright
%endif
%{_bindir}/%{name}
%{_mandir}/*/%{name}.1.gz


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3.3-2
- Now works on epel5 and epel6
- Fixes for review request, bz #1230274

* Tue Jun 09 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3.3-1
- Initial package

