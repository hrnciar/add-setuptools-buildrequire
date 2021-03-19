Name:           ubu-keyring
Version:        2020.06.17.1
Release:        3%{?dist}
Summary:        GnuPG keys of the Ubuntu archive

License:        Public Domain
URL:            https://launchpad.net/ubuntu-keyring
Source0:        https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-keyring_%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  keyrings-filesystem
Requires:       keyrings-filesystem

%description
The Ubuntu project digitally signs its Release files. This package contains the
archive keys used for that, in a minimal form for use in the installer.

%prep
%autosetup -p1 -n ubuntu-keyring-%{version}


%build


%install
install -d %{buildroot}%{_keyringsdir}
[ ! -s keyrings/ubuntu-archive-removed-keys.gpg ] && rm keyrings/ubuntu-archive-removed-keys.gpg
cp -a keyrings/* %{buildroot}%{_keyringsdir}


%files
%doc README
%{_keyringsdir}/*.gpg


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Sandro Mani <manisandro@gmail.com> - 2020.06.17.1-1
- Update to 2020.06.17.1

* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 2020.02.11.2-1
- Update to 2020.02.11.2

* Tue Feb 11 2020 Sandro Mani <manisandro@gmail.com> - 2020.02.11.1-1
- Update to 2020.02.11.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.09.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.09.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.09.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Sandro Mani <manisandro@gmail.com> - 2018.09.18.1-
- Update to 2018.09.18.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Sandro Mani <manisandro@gmail.com> - 2018.02.28-1
- Update to 2018.02.28

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.10.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.10.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.10.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Sandro Mani <manisandro@gmail.com> - 2016.10.27-1
- Update to 2016.10.27

* Mon Sep 05 2016 Sandro Mani <manisandro@gmail.com> - 2016.09.01-1
- Update to 2016.09.01

* Thu May 19 2016 Sandro Mani <manisandro@gmail.com> - 2016.05.13-1
- Update to 2016.05.13

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2012.05.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.05.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.05.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 15 2013 Sandro Mani <manisandro@gmail.com> - 2012.05.19-2
- Remove empty file

* Thu Oct 10 2013 Sandro Mani <manisandro@gmail.com> - 2012.05.19-1
- Initial package
