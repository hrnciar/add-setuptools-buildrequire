%global	majorver	2.14.5
#%%global	preminorver	.rc6
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}

%global	fedorarel	10

%global	gem_name	rspec-expectations
%global	rpmgem_name	rspec2-expectations

# It is too dangerous to use minitest >= 5 on rspec-expections-2.14.x...
# e5102884716f8bc1b4e8f0fe0b2b7c4dd1d04734 ... too big
%global	gem_minitest	rubygem(minitest4)


# %%check section needs rspec-core, however rspec-core depends on rspec-expectations
# runtime part of rspec-expectaions does not depend on rspec-core
%global	need_bootstrap_set	0

%{!?need_bootstrap:	%global	need_bootstrap	%{need_bootstrap_set}}

Summary:	Rspec 2 expectations (should and matchers)
Name:		rubygem-%{rpmgem_name}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{fedorarel}%{?preminorver:%{rpmminorver}}%{?dist}.7

License:	MIT
URL:		http://github.com/rspec/rspec-expectations
Source0:	https://rubygems.org/gems/%{gem_name}-%{fullver}.gem
# Backport temporarily be_truthy matchers and so on
Patch0:	rubygem-rspec-expectations-2.14.5-be_truthy-alias.patch
# Test suite fix for ruby24 wrt integer unification
Patch1:	rubygem-rspec-expectations-2.14.5-ruby24.patch

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
%if 0%{?need_bootstrap} < 1
BuildRequires:	rubygem(rspec2)
BuildRequires:	%gem_minitest
BuildRequires:	rubygem(test-unit)
%endif
Provides:		rubygem(%{rpmgem_name}) = %{version}-%{release}
Obsoletes:		rubygem-rspec-expectations < 2.14.5-5
BuildArch:		noarch

%description
rspec-expectations adds `should` and `should_not` to every object and includes
RSpec::Matchers, a library of standard matchers.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
Obsoletes:		rubygem-rspec-expectations-doc < 2.14.5-5

%description	doc
This package contains documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch0 -p2
%patch1 -p1
sed -i -e "s@\(require 'test/unit'\)@gem 'minitest', '~> 4' ;\1@" \
	spec/spec_helper.rb

gem specification %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# cleanups
rm -f %{buildroot}%{gem_instdir}/{.document,.gitignore,.travis.yml,.yardopts}

%if 0%{?need_bootstrap} < 1
%check
LANG=C.UTF-8
pushd .%{gem_instdir}
ruby -rrubygems -Ilib/ -S rspec2 spec/
popd
%endif

%files
%dir	%{gem_instdir}

%license	%{gem_instdir}/License.txt
%doc	%{gem_instdir}/*.md
%{gem_instdir}/lib/

%exclude	%{gem_cache}
%{gem_spec}

%files	doc
%{gem_docdir}
%{gem_instdir}/features/
%exclude	%{gem_instdir}/spec/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-10.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-10.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-10.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-10.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-10.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 2.14.5-10.2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-10
- ruby 2.5 no longer supports -rubygems, drop it

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-9
- F-26: adjust for ruby24

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-8
- BR: rubygem(test-unit)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.5-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-7
- Enable tests

* Wed Sep 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-6
- Change summary a bit

* Thu Aug 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-5
- Rename to rspec2-expectations, cleanup

* Thu Aug 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-4
- Clearner way to specify minitest 4.x

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-3
- Backport temporarily be_truthy matchers and so on

* Thu Jun 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-2
- Force to use minitest 4.x, 5.x is too dangerous now

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-1
- 2.14.5

* Mon Nov 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.4-1
- 2.14.4

* Fri Sep 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-1
- 2.14.3

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.2-2
- Enable test suite again

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.2-1
- 2.14.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.0-2
- Enable test suite again

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.0-1
- 2.13.0

* Wed Feb 20 2013 V??t Ondruch <vondruch@redhat.com> - 2.12.1-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.1-2
- Enable test suite again

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.1-1
- 2.12.1

* Thu Oct 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.11.3-1
- 2.11.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.0-2
- Require (diff-lcs) again

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.0-1
- 2.8.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-1
- 2.6.0

* Tue May 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-0.3.rc6
- 2.6.0 rc6

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- And enable check on rawhide

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-0.1.rc4
- 2.6.0 rc4

* Sat Feb 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- And enable check on rawhide

* Sat Feb 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.5.0-2
- Cleanups

* Thu Feb 17 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-1
- 2.5.0

* Fri Nov 05 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-1
- Initial package
