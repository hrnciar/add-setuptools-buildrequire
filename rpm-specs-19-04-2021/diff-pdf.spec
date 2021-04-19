Name:           diff-pdf
Version:        0.5
Release:        1%{?dist}
Summary:        A simple tool for visually comparing two PDF files

License:        GPLv2+ and LGPLv2+
URL:            http://vslavik.github.io/diff-pdf/
Source0:        https://github.com/vslavik/diff-pdf/archive/v%{version}/diff-pdf-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  wxGTK3-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  make

%description
%{summary}.

%prep
%autosetup

%build
aclocal ${wx+-I} $wx -I admin
autoconf
automake --add-missing --copy --foreign
%configure --disable-silent-rules
%make_build


%install
%make_install


%files
%license COPYING COPYING.icons
%doc AUTHORS README.md
%{_bindir}/%{name}


%changelog
* Mon Mar 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5-1
- Update to 0.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Marek Kasik <mkasik@redhat.com> - 0.4.1-5
- Do not require poppler-cairo
- It is not needed and drags in explicit dependency on poppler base library

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 09 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4.1-3
- Disable silent make rules, thanks Orion Poplawski

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Thu Jan 09 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4-1
- Update to 0.4

* Fri Nov 15 2019 Vasiliy Glazov <vascom2@gmail.com> - 0.3-1
- Initial release
