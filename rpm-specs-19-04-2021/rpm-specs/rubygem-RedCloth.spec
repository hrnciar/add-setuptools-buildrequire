# Generated from RedCloth-4.1.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name RedCloth

Name: rubygem-%{gem_name}
Version: 4.3.2
Release: 17%{?dist}
Summary: Textile parser for Ruby
License: MIT
URL: http://redcloth.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fixes failing tests on ARM which defaults to use unsigned char
# http://jgarber.lighthouseapp.com/projects/13054-redcloth/tickets/236-test-failure-on-armelpowerpc
Patch0: rubygem-redcloth-4.2.9-unsigned-char-fix.patch
# Fix Ruby 2.5 compatibility.
# https://github.com/jgarber/redcloth/pull/38/commits/00b55ace17ed408b1b6129e1ba6c90fd4f0a6d2c
Patch1: rubygem-RedCloth-4.3.2-Replace-deprecated-YAML-load_documents.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
#BuildRequires: rubygem(rspec) < 3
#BuildRequires: rubygem(rspec-core) < 3
#BuildRequires: rubygem(rspec-mocks) < 3
#BuildRequires: rubygem(rspec-expectations) < 3
BuildRequires: ruby-devel
BuildRequires: gcc

%description
Textile parser for Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch0 -p1
%patch1 -p1

%build
gem build %{gem_name}.gemspec

%gem_install

# To create debuginfo file corretly (workaround for
# "#line" directive)
pushd .%{gem_instdir}/ext/redcloth_scan
mkdir ext
ln -sf .. ext/redcloth_scan
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check 
pushd .%{gem_instdir}
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/redcloth
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING
%{gem_instdir}/bin
%exclude %{gem_instdir}/redcloth.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/spec
%{gem_instdir}/tasks

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 11:59:45 CET 2021 V??t Ondruch <vondruch@redhat.com> - 4.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Thu Oct 22 2020 V??t Ondruch <vondruch@redhat.com> - 4.3.2-15
- Relax RSpec dependency.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 V??t Ondruch <vondruch@redhat.com> - 4.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 V??t Ondruch <vondruch@redhat.com> - 4.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Fri Jul 27 2018 V??t Ondruch <vondruch@redhat.com> - 4.3.2-8
- Add "BR: gcc" to fix FTBFS (rhbz#1606150).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Bj??rn Esser <besser82@fedoraproject.org> - 4.3.2-6
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 V??t Ondruch <vondruch@redhat.com> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 V??t Ondruch <vondruch@redhat.com> - 4.3.2-1
- Update to RedCloth 4.3.2.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 V??t Ondruch <vondruch@redhat.com> - 4.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 V??t Ondruch <vondruch@redhat.com> - 4.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Use RSpec 2.x for test suite.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 V??t Ondruch <vondruch@redhat.com> - 4.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Josef Stribny <jstribny@redhat.com> - 4.2.9-5
- Patch for ARM which doesn't use signed chars as a default

* Thu Mar 07 2013 Josef Stribny <jstribny@redhat.com> - 4.2.9-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.9-1
- Rebuilt for Ruby 1.9.3.
- Update to RedCloth 4.2.9.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 03 2010 Michael Stahnke <stahnma@fedoraproject.org> - 4.2.3-1
- Version update 

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> - 4.2.2-1
- Commented out the piece of set the executable status on files.
- Release 4.2.2 of RedCloth.

* Thu Jul 30 2009 Darryl L. Pierce <dpierce@redhat.com> - 4.1.9-7
- Resolves: rhbz#505589 - rubygem-RedCloth-debuginfo created from stripped binaries

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Darryl L. Pierce <dpierce@redhat.com> - 4.1.9-5
- Resolves: rhbz#505589 - rubygem-RedCloth-debuginfo created from stripped binaries

* Fri May  1 2009 Darryl L. Pierce <dpierce@redhat.com> - 4.1.9-4
- First official build for Fedora.

* Thu Apr 30 2009 Darryl L. Pierce <dpierce@redhat.com> - 4.1.9-3
- Changed mv to cp for binaries.
- Removed redundant %%doc entries.

* Thu Apr 30 2009 Darryl L. Pierce <dpierce@redhat.com> - 4.1.9-2
- Added BuildRequires: ruby-devel to fix koji issues.

* Thu Apr 23 2009 Darryl L. Pierce <dpierce@redhat.com> - 4.1.9-1
- Initial package
