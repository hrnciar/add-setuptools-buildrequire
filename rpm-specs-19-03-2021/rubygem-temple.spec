# Generated from temple-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name temple

Name: rubygem-%{gem_name}
Version: 0.8.2
Release: 2%{?dist}
Summary: Template compilation framework in Ruby
License: MIT
URL: https://github.com/judofyr/temple
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Replace Erubi by Erubis.
# https://github.com/judofyr/temple/pull/132
Patch0: rubygem-temple-0.8.2-Use-Erubi-instead-of-Erubis.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/bacon
BuildRequires: rubygem(erubi)
BuildRequires: rubygem(tilt)
BuildArch: noarch

%description
Temple is an abstraction and a framework for compiling templates to pure Ruby.
It's all about making it easier to experiment, implement and optimize template
languages. If you're interested in implementing your own template language,
or anything else related to the internals of a template engine: You've come
to the right place.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
bacon -Itest -a
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/EXPRESSIONS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/temple.gemspec
%{gem_instdir}/test

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Vít Ondruch <vondruch@redhat.com> - 0.8.2-1
- Update to Temple 0.8.2.
  Resolves: rhbz#1684883
- Use Erubi instead of Erubis.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 02 2017 Vít Ondruch <vondruch@redhat.com> - 0.8.0-1
- Update to Temple 0.8.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Vít Ondruch <vondruch@redhat.com> - 0.7.7-1
- Update to Temple 0.7.7.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 20 2014 Vít Ondruch <vondruch@redhat.com> - 0.6.7-1
- Update to Temple 0.6.7.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Josef Stribny <jstribny@redhat.com> - 0.6.3-1
- Updated to version 0.6.3.

* Thu Feb 28 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.2-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Updated to version 0.6.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.0-1
- Initial package
