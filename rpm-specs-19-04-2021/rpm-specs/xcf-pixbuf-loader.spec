%global commit b037c59

Name:		xcf-pixbuf-loader
Version:	0.0.1
Release:	28.20120530git%{commit}%{?dist}
Summary:	XCF (GIMP) image loader for GTK+ applications

License:	LGPLv2+
URL:		http://gitorious.org/xcf-pixbuf-loader/mainline.git
Source0:	https://gitorious.org/xcf-pixbuf-loader/mainline?a=snapshot;h=%{commit};sf=tgz#/xcf-pixbuf-loadermainline-%{commit}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:	gdk-pixbuf2-devel glib2-devel
BuildRequires:	bzip2-devel
BuildRequires:	autoconf automake libtool

%define		loaders_dir	gdk-pixbuf-2.0/2.10.0/loaders
Requires:	gdk-pixbuf2%{?_isa}

%description
xcf-pixbuf-loader contains a plugin to load XCF images, as created by
the GIMP, in GTK+ applications.

%prep
%setup -q -n xcf-pixbuf-loadermainline-%{commit}

%build
autoreconf -v --force --install
%configure
make %{?_smp_mflags}

%install
install -m0755 -D .libs/libioxcf.so $RPM_BUILD_ROOT/%{_libdir}/%{loaders_dir}/libioxcf.so

%postun
%if 0%{?fedora} < 24
    /usr/bin/gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache &> /dev/null || :
%endif

%post
%if 0%{?fedora} < 24
if [ $1 -eq 1 ] ; then
    # For upgrades, the cache will be regenerated by the new package's %%postun
    /usr/bin/gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache &> /dev/null || :
fi
%endif

%files
%doc NEWS README
%{_libdir}/%{loaders_dir}/*.so

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-28.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-27.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-26.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-25.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-24.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-23.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-22.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-21.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-20.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-19.20120530gitb037c59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.0.1-18.20120530gitb037c59
- Fix post/postun conditionals

* Mon Sep 19 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.0.1-17.20120530gitb037c59
- Updated snapshot
- Drop post/postun scriptlets for F24

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-16.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.1-15.8af913d1
- Use post/postun scripts from Packaging:ScriptletSnippets (#668159)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-14.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-13.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-12.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-11.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-10.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-9.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-8.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0.1-7.8af913d1
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-6.8af913d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 Bastien Nocera <bnocera@redhat.com> 0.0.1-5.8af913d1
- Use a gdk-pixbuf2 requires, instead of requiring a particular file

* Mon Jul 19 2010 Bastien Nocera <bnocera@redhat.com> 0.0.1-4.8af913d1
- Rebuild against gdk-pixbuf2

* Thu Mar 04 2010 Bastien Nocera <bnocera@redhat.com> 0.0.1-3.8af913d1
- Bump release for upgrades

* Wed Feb 17 2010 Bastien Nocera <bnocera@redhat.com> 0.0.1-2.8af913d1
- Update to 8af913d1 commit
- Update with review comments

* Tue Oct 13 2009 Bastien Nocera <bnocera@redhat.com> 0.0.1-1.e5ce761
- First version