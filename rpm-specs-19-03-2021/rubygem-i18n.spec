%global gem_name i18n

%bcond_without tests

Name: rubygem-%{gem_name}
Version: 1.8.7
Release: 2%{?dist}
Summary: New wave Internationalization support for Ruby
# `BSD or Ruby` due to header of lib/i18n/gettext/po_parser.rb
License: MIT and (BSD or Ruby)
URL: https://github.com/ruby-i18n/i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Since 1.8.2 tests are not shipped with the gem, but can be checked like
# git clone --no-checkout https://github.com/ruby-i18n/i18n
# cd i18n && git archive -v -o i18n-1.8.7-tests.txz v1.8.7 test
Source1: %{gem_name}-%{version}-tests.txz
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if %{with tests}
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(test_declarative)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(activesupport)
%endif
BuildArch: noarch

%description
Ruby Internationalization and localization solution.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{with tests}
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# Bundler just complicates everything in our case, remove it.
sed -i -e "/require 'bundler\/setup'/ s/^/#/" test/test_helper.rb

# Tests are failing without LANG environment is set.
# https://github.com/svenfuchs/i18n/issues/115
LANG=C.utf8 ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Pavel Valena <pavel.valena@email.com> - 1.8.7-1
- Update to i18n 1.8.7.
  Resolves: rhbz#1911952

* Fri Oct 30 16:58:04 CET 2020 Pavel Valena <pvalena@redhat.com> - 1.8.5-1
- Update to i18n 1.8.5.
  Resolves: rhbz#1844286

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 V??t Ondruch <vondruch@redhat.com> - 1.8.2-1
- Update to i18n 1.8.2.
  Resolves: rhbz#1788714

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Pavel Valena <pvalena@redhat.com> - 1.7.0-1
- Update to i18n 1.7.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.1-2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Nov 13 2018 V??t Ondruch <vondruch@redhat.com> - 1.1.1-1
- Update to i18n 1.1.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 1.0.0-1
- Update to i18n 1.0.0.
  Requires rubygem(concurrent-ruby)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 V??t Ondruch <vondruch@redhat.com> - 0.7.0-1
- Update to i18n 0.7.0.

* Tue Jul 22 2014 Josef Stribny <jstribny@redhat.com> - 0.6.11-1
- Update to i18n 0.6.11

* Wed Jun 18 2014 Josef Stribny <jstribny@redhat.com> - 0.6.9-4
- Fix test suite compatibility with minitest 5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Josef Stribny <jstribny@redhat.com> - 0.6.9-2
- Fix license: Ruby is now licensed under BSD or Ruby

* Mon Dec 09 2013 V??t Ondruch <vondruch@redhat.com> - 0.6.9-1
- Update to i18n 0.6.9.
  - Fix CVE-2013-4491.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Josef Stribny <jstribny@redhat.com> - 0.6.4-1
- Update to i18n 0.6.4.

* Tue Feb 26 2013 V??t Ondruch <vondruch@redhat.com> - 0.6.1-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 V??t Ondruch <vondruch@redhat.com> - 0.6.1-1
- Update to I18n 0.6.1.

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-1
- Update to I18n 0.6.0.
- Removed unneeded %%defattr usage.

* Thu Jan 19 2012 V??t Ondruch <vondruch@redhat.com> - 0.5.0-3
- Rebuilt for Ruby 1.9.3.
- Enabled test suite.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 V??t Ondruch <vondruch@redhat.com> - 0.5.0-1
- Update to i18n 0.5.0.
- Documentation moved into subpackage.
- Removed unnecessary cleanup.
- Preparetion for test suite execution during build.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Jozef Zigmund <jzigmund@redhat.com> - 0.4.2-2
- Add GPLv2 or Ruby License
- Files MIT-LICENSE, geminstdir/lib/i18n.rb are non executable now

* Thu Nov 11 2010 Jozef Zigmund <jzigmund@redhat.com> - 0.4.2-1
- Initial package
