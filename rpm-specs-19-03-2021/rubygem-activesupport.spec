%global gem_name activesupport

#%%global prerelease 

Name: rubygem-%{gem_name}
Epoch: 1
Version: 6.1.3
Release: 1%{?dist}
Summary: A support libraries and Ruby core extensions extracted from the Rails framework
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# The activesupport gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/activesupport && git archive -v -o activesupport-6.1.3-tests.txz v6.1.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may get them like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-6.1.3-tools.txz v6.1.3 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz

# ruby package has just soft dependency on rubygem({bigdecimal,json}), while
# ActiveSupport always requires them.
Requires: rubygem(bigdecimal)
Requires: rubygem(json)

# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(dalli)
BuildRequires: (rubygem(i18n) >= 0.7 with rubygem(i18n) < 2)
BuildRequires: rubygem(minitest) >= 5.0.0
BuildRequires: rubygem(rack)
BuildRequires: rubygem(tzinfo) >= 2.0
BuildRequires: rubygem(listen)
BuildRequires: rubygem(redis)
BuildRequires: rubygem(rexml)
BuildRequires: memcached
BuildArch: noarch


%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/tools ..
mv %{_builddir}/test .

# These tests are really unstable, but they seems to be passing upstream :/
for f in \
  test/evented_file_update_checker_test.rb \
  test/cache/stores/redis_cache_store_test.rb # failed to require "redis/connection/hiredis"
do
  mv $f{,.disable}
done

# This seems to be unstable as well ...
# https://github.com/rails/rails/issues/25682
sed -i '/def test_iso8601_output_and_reparsing$/,/^  end$/ s/^/#/' test/core_ext/duration_test.rb

# Workaround TransformValuesTest#test_default_procs_do_not_persist_*_mapping
# test failures due to bug in Ruby 2.7.{0,1}.
# https://bugs.ruby-lang.org/issues/16498
sed -i '/assert_nil mapped\[:b\]/ s/^/#/' test/core_ext/hash/transform_values_test.rb

sed -i '/require .bundler./ s/^/#/' test/abstract_unit.rb

memcached &
mPID=$!
sleep 1
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
kill -15 $mPID
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Feb 18 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.3-1
- Update to activesupport 6.1.3.

* Mon Feb 15 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.2.1-1
- Update to activesupport 6.1.2.1.

* Wed Jan 27 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.1-1
- Update to activesupport 6.1.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 V??t Ondruch <vondruch@redhat.com> - 1:6.0.3.4-2
- Fix FTBFS due to Ruby 3.0 update.

* Thu Oct  8 10:45:37 CEST 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.4-1
- Update to activesupport 6.0.3.4.
  Resolves: rhbz#1886136

* Fri Sep 18 17:58:30 CEST 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.3-1
- Update to activesupport 6.0.3.3.
  Resolves: rhbz#1877502

* Thu Sep 10 08:42:03 GMT 2020 V??t Ondruch <vondruch@redhat.com> - 1:6.0.3.2-3
- Fix evaluator test from web-console.

* Tue Sep 01 2020 V??t Ondruch <vondruch@redhat.com> - 1:6.0.3.2-2
- Properly fix flaky `FileStoreTest#test_filename_max_size` test case.

* Mon Aug 17 04:41:17 GMT 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.2-1
- Update to activesupport 6.0.3.2.
  Resolves: rhbz#1742797

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Update to ActiveSupport 6.0.3.1.
  Resolves: rhbz#1742797

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 V??t Ondruch <vondruch@redhat.com> - 1:5.2.3-4
- Ruby 2.7 compatibility.
  Resolves: rhbz#1799093
- TZInfo 2.0 compatibility.
  Resolves: rhbz#1805531

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.3-1
- Update to Active Support 5.2.3.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.2.1-1
- Update to Active Support 5.2.2.1.

* Mon Feb 04 2019 V??t Ondruch <vondruch@redhat.com> - 1:5.2.2-3
- Fix Range and BigDecimal compatibility with Ruby 2.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.2-1
- Update to Active Support 5.2.2.

* Wed Nov 14 2018 V??t Ondruch <vondruch@redhat.com> - 1:5.2.1-2
- Update I18n fallbacks configuration to be compatible with i18n 1.1.0.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.1-1
- Update to Active Support 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.0-1
- Update to Active Support 5.2.0.

* Mon Apr 16 2018 V??t Ondruch <vondruch@redhat.com> - 1:5.1.5-3
- Fix test suite issue caused by fix of CVE-2018-6914 in Ruby.

* Wed Feb 21 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-2
- Allow rubygem-i18n ~> 1.0
  https://github.com/rails/rails/pull/31991

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-1
- Update to Active Support 5.1.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 V??t Ondruch <vondruch@redhat.com> - 1:5.1.4-2
- Fix MiniTest 5.11 compatibility.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.4-1
- Update to Active Support 5.1.4.

* Tue Aug 22 2017 V??t Ondruch <vondruch@redhat.com> - 1:5.1.3-2
- Explicitly require rubygem(json).
- Once again disable unstable test.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.3-1
- Update to Active Support 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.2-1
- Update to Active Support 5.1.2.
- Run tests that need memcached

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.1-1
- Update to Active Support 5.1.1.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.2-1
- Update to Active Support 5.0.2.

* Mon Feb 13 2017 Jun Aruga <jaruga@redhat.com> - 1:5.0.1-4
- Fix Fixnum/Bignum deprecated warning for Ruby 2.4.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jun Aruga <jaruga@redhat.com> - 1:5.0.1-2
- Fix Ruby 2.4.0 compatibility.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.1-1
- Update to Active Support 5.0.1.
  - Remove Patch0: rubygem-activesupport-5.0.0-Do-not-depend-on-Rails-git-repository-layout-in-Acti.patch; subsumed
- Fix warnings: Fixnum and Bignum are deprecated in Ruby trunk

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 1:5.0.0.1-1
- Update to Activesupport 5.0.0.1

* Wed Jul 27 2016 V??t Ondruch <vondruch@redhat.com> - 1:5.0.0-2
- Fix missing epoch in -doc subpackage.

* Fri Jul 01 2016 V??t Ondruch <vondruch@redhat.com> - 1:5.0.0-1
- Update to ActiveSupport 5.0.0.

* Fri Apr 08 2016 V??t Ondruch <vondruch@redhat.com> - 1:4.2.6-2
- Explicitly set rubygem(bigdecimal) dependency.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.6-1
- Update to activesupport 4.2.6

* Tue Mar 01 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.2-1
- Update to activesupport 4.2.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.1-1
- Update to activesupport 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 1:4.2.5-1
- Update to activesupport 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.4-1
- Update to activesupport 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.3-1
- Update to activesupport 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.2-1
- Update to activesupport 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-2
- Fix tests

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-1
- Update to activesupport 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.0-1
- Update to activesupport 4.2.0

* Tue Aug 19 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to activesupport 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.4-1
- Update to ActiveSupport 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.1-1
- Update to ActiveSupport 4.1.1

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-1
- Update to ActiveSupport 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.3-1
- Update to ActiveSupport 4.0.3

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-1
- Update to ActiveSupport 4.0.2

* Fri Aug 09 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-1
- Update to ActiveSupport 4.0.1

* Fri Aug 09 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-2
- Fix: add minitest to requires

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-1
- Update to ActiveSupport 4.0.0.

* Tue Mar 19 2013 V??t Ondruch <vondruch@redhat.com> - 1:3.2.13-1
- Update to ActiveSupport 3.2.13.

* Fri Mar 01 2013 V??t Ondruch <vondruch@redhat.com> - 1:3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 V??t Ondruch <vondruch@redhat.com> - 1:3.2.12-1
- Update to ActiveSupport 3.2.12.

* Wed Jan 09 2013 V??t Ondruch <vondruch@redhat.com> - 1:3.2.11-1
- Update to ActiveSupport 3.2.11.

* Thu Jan 03 2013 V??t Ondruch <vondruch@redhat.com> - 1:3.2.10-1
- Update to ActiveSupport 3.2.10.

* Mon Aug 13 2012 V??t Ondruch <vondruch@redhat.com> - 1:3.2.8-1
- Update to ActiveSupport 3.2.8.

* Mon Jul 30 2012 V??t Ondruch <vondruch@redhat.com> - 1:3.2.7-1
- Update to ActiveSupport 3.2.7.

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-1
- Update to ActiveSupport 3.2.6.
- Removed unneeded BuildRoot tag.
- Tests no longer fail with newer versions of Mocha, remove workaround.

* Fri Jun 15 2012 V??t Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Update to ActiveSupport 3.0.15.

* Fri Jun 01 2012 V??t Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Update to ActiveSupport 3.0.13.

* Wed Apr 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-5
- Add the bigdecimal dependency to gemspec.

* Fri Mar 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-4
- The CVE patch name now contains the CVE id.

* Mon Mar 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-3
- Patch for CVE-2012-1098

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActiveSupport 3.0.11.

* Mon Aug 22 2011 V??t Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActiveSupport 3.0.10

* Fri Jul 01 2011 V??t Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActiveSupport 3.0.9
- Changed %%define into %%global
- Removed unnecessary %%clean section

* Thu Jun 16 2011 Mo Morsi <mmorsi@redhat.com> - 1:3.0.5-3
- Reverting accidental change adding a few gem flags

* Thu Jun 16 2011 Mo Morsi <mmorsi@redhat.com> - 1:3.0.5-2
- Include fix for CVE-2011-2197

* Thu Mar 24 2011 V??t Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Update to ActiveSupport 3.0.5
- Remove Rake dependnecy

* Mon Feb 14 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-4
- fix bad dates in the spec changelog

* Thu Feb 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-3
- include i18n runtime dependency

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- update to rails 3

* Wed Aug 25 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- bumped version

* Wed Aug 04 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8
- Added check section with rubygem-mocha dependency
- Added upsteam Rakefile and test suite to run tests

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Mon Sep 7 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4 (bug 520843, CVE-2009-3009)

* Sun Jul 26 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.3-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.2.2-1
- New upstream version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Wed Nov 28 2007 David Lutterkort <dlutter@redhat.com> - 1.4.4-3
- Fix buildroot

* Tue Nov 13 2007 David Lutterkort <dlutter@redhat.com> - 1.4.4-2
- Install README and CHANGELOG in _docdir

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.4.4-1
- Initial package
