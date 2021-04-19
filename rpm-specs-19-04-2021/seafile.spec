%global _hardened_build 1

Name:           seafile
Version:        7.0.10
Release:        2%{?dist}
Summary:        Cloud storage cli client

License:        GPLv2
URL:            http://seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(libsearpc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel
BuildRequires:  vala


%description
Seafile is a next-generation open source cloud storage system with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
sed -i -e /\(DESTDIR\)/d lib/libseafile.pc.in


%build
./autogen.sh
%configure --disable-static --with-python3
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name 'seafile.desktop' -exec rm -f {} ';'

%ldconfig_scriptlets


%files
%doc README.markdown
%license LICENSE.txt
%{python3_sitearch}/%{name}/
%{_libdir}/lib%{name}.so.0*
%{_bindir}/seaf-cli
%{_bindir}/seaf-daemon
%{_mandir}/man1/*.1.*


%files devel
%doc README.markdown
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 7.0.10-1
- Update to 7.0.10
- Spec cleanup: remove unused deps, update for current guidelines

* Tue Sep 29 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.4-5
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Julien Enselme <jujens@jujens.eu> - 7.0.4-1
- Update to 7.0.4
- Make this package compatible with Python3

* Tue Aug 20 2019 Julien Enselme <jujens@jujens.eu> - 7.0.2-1
- Update to 7.0.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Julien Enselme <jujens@jujens.eu> - 6.2.11-1
- Update to 6.2.11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Julien Enselme <jujens@jujens.eu> - 6.2.5-1
- Update to 6.2.5

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 6.2.3-2
- Correct ccnet requirement

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 6.2.3-1
- Update to 6.2.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Julien Enselme <jujens@jujens.eu> - 6.1.6-1
- Update to 6.1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Julien Enselme <jujens@jujens.eu> - 6.1.4-1
- Update to 6.1.4

* Mon Nov 06 2017 Julien Enselme <jujens@jujens.eu> - 6.1.3-1
- Update to 6.1.3

* Thu Aug 10 2017 Julien Enselme <jujens@jujens.eu> - 6.1.0-1
- Update to 6.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.6-1
- Update to 6.0.6
- Build with openSSL 1.0

* Tue Mar 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.4-2
- Correct name of the python package

* Tue Mar 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.4-1
- Update to 6.0.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Julien Enselme - 6.0.0-2
- Compile against compat-openssl10 until it is compatible with OpenSSL 1.1

* Sun Oct 30 2016 Julien Enselme - 6.0.0-1
- Update to 6.0.0
- Unretire package

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 31 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.2-3
- Fix license

* Fri May 27 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.2-2
- Fix shared libraries

* Tue May 17 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2
- Add missing requiremnts
- Add missing license file from subpackage
- Add tests

* Mon Feb 08 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5

* Wed Sep 16 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- Hardened build

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Thu Aug 28 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
