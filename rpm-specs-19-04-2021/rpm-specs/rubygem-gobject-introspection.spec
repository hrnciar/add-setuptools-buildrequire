%global	header_dir	%{ruby_vendorarchdir}

%global	gem_name	gobject-introspection
%global	gem_so_name	gobject_introspection

%global	glib_min_ver	3.1.8

%undefine        _changelog_trimtime

Summary:	Ruby binding of GObjectIntrospection
Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:	3%{?dist}

# lib/gobject-introspection.rb and so on
License:	LGPLv2+
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	gcc
Requires:	ruby(rubygems) 
Requires:	ruby
BuildRequires:	rubygems-devel 
BuildRequires:	rubygem-glib2-devel >= %{glib_min_ver}
BuildRequires:	gobject-introspection-devel
# %%check
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Ruby/GObjectIntrospection is a Ruby binding of 
GObjectIntrospection.

%package	devel
Summary:	Ruby/GdkPixbuf2 development environment
Requires:	%{name}%{?isa} = %{version}-%{release}
Requires:	ruby-devel%{?isa}
Requires:	rubygem-glib2-devel%{?isa}
Requires:	gobject-introspection-devel%{?isa}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}

%prep
%setup -q -c -T
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# Patches

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 3\.4\.3|>= 3.4.3|' %{gem_name}.gemspec

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
mkdir -p .%{gem_dir}

export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror-implicit-function-declaration'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/

# Cleanups
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd

%check
pushd .%{gem_instdir}

# Kill unneeded make process
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd

sed -i test/run-test.rb -e ':loop; N; $!b loop; s|true,\n|true,|'
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
ruby -Ilib:test:ext/%{gem_name} ./test/run-test.rb
popd

%files
%dir	%{gem_instdir}/
%dir	%{gem_instdir}/lib/
%doc	%{gem_instdir}/COPYING.LIB
%doc	%{gem_instdir}/README.md
%{gem_instdir}/lib/%{gem_name}.rb
%{gem_instdir}/lib/gi.rb
%dir	%{gem_instdir}/lib/%{gem_name}/
%{gem_instdir}/lib/%{gem_name}/*.rb

%{gem_extdir_mri}/

%exclude %{gem_cache}
%exclude %{gem_instdir}/*gemspec
%{gem_spec}

%files	devel
%{header_dir}/rb-gobject-introspection.h
%{_libdir}/pkgconfig/ruby-gobject-introspection.pc

%files		doc
%doc	%{gem_docdir}/
%exclude	%{gem_instdir}/Rakefile
%exclude	%{gem_instdir}/test/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-2
- F-34: rebuild against ruby 3.0

* Wed Aug 12 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-1
- 3.4.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-2
- F-32: rebuild against ruby27

* Wed Dec  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Sat Oct 12 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Thu Oct  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.8-1
- 3.3.8

* Wed Sep  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Sun Feb 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-2
- F-30: rebuild against ruby26

* Wed Nov 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.9-1
- 3.2.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-1
- 3.2.7

* Thu May  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.5-1
- 3.2.5

* Wed Apr 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-1
- 3.2.4

* Mon Feb 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-5
- Fix 32bit overflow

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.2.1-3
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-2
- F-28: rebuild for ruby25

* Tue Nov 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Sat Oct 21 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Tue Jul 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Tue Jun  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-2
- Enable test failure check on i686, arm again

* Tue Jun  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
- 3.1.6

* Thu May  4 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Tue Jan 10 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-2
- F-26: rebuild for ruby24

* Tue Nov 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Wed Aug 31 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-2
- Fix how to pass return value to libffi
  - https://bugzilla.redhat.com/show_bug.cgi?id=1331726
  - https://github.com/ruby-gnome2/ruby-gnome2/issues/758

* Sun Aug 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Thu May  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.8-2
- Apply the upstream int32[] issue patch (github 758),
  which may fix RHBZ 1331726

* Tue Apr 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-2
- F-24: rebuild against ruby23

* Sun Oct 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-1
- 3.0.7

* Wed Sep 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Tue Sep 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.4-1
- 3.0.4

* Sun Sep 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.5-2
- gobject-introspection 244 patch should be for F-22+

* Wed Apr 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.5-1
- 2.2.5

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-2
- F-22: Rebuild for ruby 2.2

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-1
- 2.2.4

* Sun Nov 23 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-2
- Patch to fix test failure on clutter

* Wed Nov  5 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-1
- 2.2.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-2
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Fri Apr 11 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Mon Jan 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Yet more test failure fix

* Sun Jan 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-2
- Fix test failure, patch from upstream

* Thu Jan 16 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-1
- 2.1.0

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-1
- 2.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-1
- 1.2.6

* Thu Apr  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-1
- 1.2.5

* Tue Mar 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-1
- 1.2.4

* Wed Mar 20 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Sun Mar  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-2
- F-19: Rebuild for ruby 2.0.0

* Mon Feb 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Sat Jan 05 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.9-1
- Initial package
