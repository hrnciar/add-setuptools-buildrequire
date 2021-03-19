# Generated from ruby-dbus-0.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-dbus

Name: rubygem-%{gem_name}
Version: 0.16.0
Release: 4%{?dist}
Summary: Ruby module for interaction with D-Bus
# MIT: lib/dbus/core_ext/*
License: LGPLv2+ and MIT
URL: https://github.com/mvidner/ruby-dbus
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Add 'rexml' dependency to fix Ruby 3.0 compatibility.
# https://github.com/mvidner/ruby-dbus/pull/87
Patch0: ruby-dbus-0.16.0-Add-dependency-rexml.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rexml)
BuildRequires: %{_bindir}/dbus-daemon
BuildArch: noarch

%description
Pure Ruby module for interaction with D-Bus IPC system.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1
%gemspec_add_dep -g rexml

# Rakefile should not be executable.
sed -i '1d' Rakefile
chmod a-x Rakefile

# Fix shebangs.
find {examples,spec} -type f -executable -exec sed -i 's|env ||' '{}' \;
find {examples,spec} -type f -executable -exec sed -r -i 's|#!.?/bin|#!/usr/bin|' '{}' \;

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
COVERAGE=false spec/tools/test_env rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/NEWS.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/VERSION
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/examples
%{gem_instdir}/ruby-dbus.gemspec
%{gem_instdir}/spec

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Vít Ondruch <vondruch@redhat.com> - 0.16.0-3
- Add REXML dependecy to fix Ruby 3.0 compatibility.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Vít Ondruch <vondruch@redhat.com> - 0.16.0-1
- Update to ruby-dubs 0.16.0.
  Resolves: rhbz#1336069

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Vít Ondruch <vondruch@redhat.com> - 0.11.0-1
- Update to ruby-dubs 0.11.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.0-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.0-1
- Update to 0.9.0.
- Don't run tests by default (fail on Koji because of no networking).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.0-1
- Update to 0.8.0.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.0-3
- Bump release to allow getting 0.7.0-3 into F16 (stupid mistake).

* Tue Feb 28 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.0-2
- Simplified the test running.
- Properly obsolete ruby-dbus.
- Applied the patch that unbundles files from activesupport (accepted by upstream).

* Tue Feb 28 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.0-1
- Initial package
