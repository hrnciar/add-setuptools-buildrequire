# Generated from slim-1.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name slim

Name: rubygem-%{gem_name}
Version: 4.1.0
Release: 3%{?dist}
Summary: Slim is a template language
License: MIT
URL: http://slim-lang.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# These are to revert dependency on sprocket-rails and slim-rails, because:
# 1) It is not really clear what the dependencies actually fix (there is no
#    test error without them).
# 2) We don't want the sprockets-rails and slim-rails dependency.
# https://github.com/slim-template/slim/commit/14a845a75047fd564acdc940c25f9bab599bbb9c
Patch0: rubygem-slim-4.1.0-see-if-this-fixes-the-unknown-line-indicator.patch
# https://github.com/slim-template/slim/pull/844
Patch1: rubygem-slim-4.1.0-Fix-build-for-Rails.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(activemodel)
BuildRequires: rubygem(rails-controller-testing)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(kramdown)
BuildRequires: rubygem(sassc)
BuildRequires: rubygem(temple)
BuildRequires: rubygem(tilt)
BuildArch: noarch

%description
Slim is a template language whose goal is reduce the syntax to the essential
parts without becoming cryptic.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch1 -p1 -R
%patch0 -p1 -R

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ruby -Ilib:test/core -rostruct -e 'Dir.glob "./test/core/**/test_*.rb", &method(:require)'
ruby -Ilib:test/core -e 'Dir.glob "./test/include/**/test_*.rb", &method(:require)'
ruby -Ilib:test/literate test/literate/run.rb
ruby -Ilib:test/core -e 'Dir.glob "./test/logic_less/**/test_*.rb", &method(:require)'
ruby -Ilib -e 'Dir.glob "./test/rails/**/test_*.rb", &method(:require)'
ruby -Ilib -e 'Dir.glob "./test/sinatra/**/test_*.rb", &method(:require)'
ruby -Ilib:test/core -e 'Dir.glob "./test/smart/**/test_*.rb", &method(:require)'
ruby -Ilib:test/core -e 'Dir.glob "./test/translator/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/slimrb
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%lang(ja) %doc %{gem_instdir}/README.jp.md
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/README.md
%{gem_instdir}/benchmarks/
%{gem_instdir}/Rakefile
%dir %{gem_instdir}/doc
%doc %{gem_instdir}/doc/*.md
%lang(ja) %doc %{gem_instdir}/doc/jp
%{gem_instdir}/slim.gemspec
%{gem_instdir}/test

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Vít Ondruch <vondruch@redhat.com> - 4.1.0-1
- Update to Slim 4.1.0.
  Resolves: rhbz#1833182

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Vít Ondruch <vondruch@redhat.com> - 3.0.9-1
- Update to Slim 3.0.9.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Vít Ondruch <vondruch@redhat.com> - 3.0.8-1
- Update to Slim 3.0.8.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Vít Ondruch <vondruch@redhat.com> - 3.0.7-1
- Update to Slim 3.0.7.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 20 2014 Vít Ondruch <vondruch@redhat.com> - 2.0.2-1
- Update to Slim 2.0.2.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Josef Stribny <jstribny@redhat.com> - 1.3.8-2
- Fix runtime requirement of temple version

* Mon Apr 15 2013 Josef Stribny <jstribny@redhat.com> - 1.3.8-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to slim 1.3.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012  <mzatko@redhat.com> - 1.2.2-8
- Excluded gem cache
- Check goes after install section

* Wed Oct 17 2012  <mzatko@redhat.com> - 1.2.2-7
- Split prep to prep and build sections
- Made nonexecutable scripts executable
- Owning whole test/ directory

* Tue Oct 16 2012  <mzatko@redhat.com> - 1.2.2-6
- Fixed markdown test

* Thu Oct 11 2012  <mzatko@redhat.com> - 1.2.2-5
- Now owning test and benchmarks directories

* Wed Oct 10 2012  <mzatko@redhat.com> - 1.2.2-4
- Added deps for rails tests. Runs tests.

* Mon Oct 08 2012  <mzatko@redhat.com> - 1.2.2-3
- Moved tests to doc, removed unnecessary files, some minor corrections
- Not running tests (missing deps)

* Mon Sep 03 2012  <mzatko@redhat.com> - 1.2.2-2
- Removed unnecessary files & corrected license

* Wed Jul 11 2012  <mzatko@redhat.com> - 1.2.2-1
- Initial package
