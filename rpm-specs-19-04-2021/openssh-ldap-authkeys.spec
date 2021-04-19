%global commit aee4c4660818e51c8bde81a3921ca9db4bd914d0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20200205

Name:		openssh-ldap-authkeys
Version:	0.1.0%{?commitdate:~git%{commitdate}.%{shortcommit}}
Release:	2%{?dist}
Summary:	Python script to generate SSH authorized_keys files using an LDAP directory

License:	MIT
URL:		https://github.com/fuhry/%{name}
Source0:	%{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:	noarch

%if 0%{?el7}
BuildRequires:	systemd
%else
BuildRequires:	systemd-rpm-macros
%endif

BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools

Requires(pre):	%{_sbindir}/groupadd
Requires(pre):	%{_sbindir}/useradd

# This is only for cases that we don't have a dependency generator active...
%if ! (%{defined python_enable_dependency_generator} || %{defined python_disable_dependency_generator})
Requires:	python%{python3_pkgversion}-ldap
Requires:	python%{python3_pkgversion}-dns
Requires:	python%{python3_pkgversion}-yaml
%endif


%description
openssh-ldap-authkeys is an implementation of AuthorizedKeysCommand for
OpenSSH 6.9 and newer that allows SSH public keys to be retrieved from
an LDAP source. It's provided for situations where a solution other
than 1:1 mapping is needed for users.

With SSH keys stored centrally in LDAP, revocation of a compromised
key is a quick and painless exercise for the user or IT department.

openssh-ldap-authkeys allows shared accounts to be fully auditable as
to who used them.


%prep
%if %{defined commitdate}
%autosetup -n %{name}-%{commit} -p1
%else
%autosetup -p1
%endif


%build
%py3_build


%install
%py3_install

# Make ghost entries for config files
touch %{buildroot}%{_sysconfdir}/%{name}/olak.yml
touch %{buildroot}%{_sysconfdir}/%{name}/authmap

# Delete example files, we'll docify them later
rm %{buildroot}%{_sysconfdir}/%{name}/*.example


%files
%license COPYING
%doc README.md
%doc *.example
%{python3_sitelib}/ldapauthkeys/
%{python3_sitelib}/openssh_ldap_authkeys*egg-info/
%{_bindir}/openssh-ldap-authkeys
%dir %{_sysconfdir}/%{name}
%ghost %config(noreplace) %{_sysconfdir}/%{name}/olak.yml
%ghost %config(noreplace) %{_sysconfdir}/%{name}/authmap
%{_tmpfilesdir}/openssh-ldap-authkeys.tmpfiles.conf

%pre
getent group olak >/dev/null || groupadd -r olak
getent passwd olak >/dev/null || \
    useradd -r -g olak -d /dev/null -s /bin/false \
    -c "System account for %{name} to run as" olak
exit 0


%changelog
* Tue Apr 06 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.0~git20200205.aee4c46-2
- Correctly guard out manual dependencies

* Mon Apr 05 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.0~git20200205.aee4c46-1
- Build pre-release snapshot
