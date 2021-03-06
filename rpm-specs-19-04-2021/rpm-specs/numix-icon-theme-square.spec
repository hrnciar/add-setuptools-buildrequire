%global forgeurl    https://github.com/numixproject/numix-icon-theme-square
%global tag         %{version}

%forgemeta

Name:           numix-icon-theme-square
Summary:        Numix Project square icon theme
Version:        20.09.19
Release:        2%{?dist}
License:        GPLv3

URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
Requires:       numix-icon-theme

%description
Numix Square is a modern icon theme for Linux from the Numix project.

%prep
%forgesetup

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -pr Numix-Square %{buildroot}%{_datadir}/icons/Numix-Square
cp -pr Numix-Square-Light %{buildroot}%{_datadir}/icons/Numix-Square-Light

%post
touch -c %{_datadir}/icons/Numix-Square &>/dev/null || :
touch -c %{_datadir}/icons/Numix-Square-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch -c %{_datadir}/icons/Numix-Square &>/dev/null
    touch -c %{_datadir}/icons/Numix-Square-Light &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/Numix-Square &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/Numix-Square-Light &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/Numix-Square &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/Numix-Square-Light &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Numix-Square
%{_datadir}/icons/Numix-Square-Light

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.09.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Brendan Early <mymindstorm@evermiss.net> - 20.09.19-1
- Update to release 20.09.19

* Thu Aug 06 2020 Brendan Early <mymindstorm@evermiss.net> - 20.07.11-1
- Update to release 20.07.11
- Switch to forge marcos

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13.20191227.git6702bc0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12.20191227.git6702bc0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-11.20191227.git6702bc0
- Update to release 19.12.27

* Tue Nov 12 2019 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-10.20191106.gitbb3ee41
- Update to release 19.11.06

* Fri Sep 27 2019 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-9.20190920.git7a63a68
- Update to release 19.09.20

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8.20190415.git7b1574f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-6.20190415.git7b1574f
- Update to release 19.04.15

* Sun Feb 24 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-6.20190222.git3c95740
- Update to release 19.02.22

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5.20190124.gitb37c7e4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-4.20190124.gitb37c7e4
- Update to release 19.01.24

* Fri Jan 18 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-3.20181201.git70711c2
- Update to release 18.12.01

* Wed Aug 29 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-2.20180829.git307e742
- Update to release 18.08.29

* Sun Jul 22 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-2.20180717.git9fc27a9
- Accept new git tag date format

* Mon Jan 01 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-1.20171225.git084e0ae
- Initial packaging
