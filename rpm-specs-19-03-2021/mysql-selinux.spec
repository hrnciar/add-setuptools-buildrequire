# defining macros needed by SELinux
%global selinuxtype targeted
%global moduletype contrib
%global modulename mysql

Name:           mysql-selinux
Version:        1.0.2
Release:        2%{?dist}

License:        GPLv3
URL:            https://github.com/devexp-db/mysql-selinux
Summary:        SELinux policy modules for MySQL and MariaDB packages

Source0:        mysql-selinux-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  selinux-policy-devel
Requires(post): policycoreutils
%{?selinux_requires}

%description
SELinux policy modules for MySQL and MariaDB packages.

%prep
%setup -q -n %{name}-%{version}

%pre
%selinux_relabel_pre -s %{selinuxtype}

%build
make

%install
# install policy modules
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages

%check

%post
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp.bz2 || :

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename} || :
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype} || :

%files
%defattr(-,root,root,0755)
%attr(0644,root,root) %{_datadir}/selinux/packages/%{modulename}.pp.bz2
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%license COPYING

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Michal Schorm <mschorm@redhat.com> - 1.0.2-1
- Rebase to 1.0.2 release
  Added context for "*mariadb*" named executables

* Tue Dec 01 2020 Michal Schorm <mschorm@redhat.com> - 1.0.1-1
- Rebase to 1.0.1 release
  This release is just a sync-up with upstream selinux-policy
- URL changed to a new upstream repository

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Kevin Fenzi <kevin@scrye.com> - 1.0.0-7
- Also make sure posttrans does not fail.

* Thu Jan 10 2019 Kevin Fenzi <kevin@scrye.com> - 1.0.0-6
- Add Requires(post) on policycoreutils for semodule and make sure post/postun cannot fail

* Thu Dec 06 2018 Jakub Janco <jjanco@redhat.com> - 1.0.0-5
- Sync with upstream

* Wed Aug 29 2018 Jakub Janco <jjanco@redhat.com> - 1.0.0-4
- Allow mysqld sys_nice capability

* Mon Aug 20 2018 Jakub Janco <jjanco@redhat.com> - 1.0.0-3
- reflect latest changes of mysql policy

* Fri Jul 27 2018 Jakub Janco <jjanco@redhat.com> - 1.0.0-2
- reflect latest changes of Independent Product Policy

* Wed Jul 18 2018 Jakub Janco <jjanco@redhat.com> - 1.0.0-1
- First Build

