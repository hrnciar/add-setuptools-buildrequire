%global	majorver	2.14.6
#%%global	preminorver	.rc6
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}

%global	fedorarel	6

%global	gem_name	rspec-mocks
%global	rpmgem_name	rspec2-mocks


# %%check section needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core
%global	need_bootstrap_set	0

Summary:	Rspec 2 doubles (mocks and stubs)
Name:		rubygem-%{rpmgem_name}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{fedorarel}%{?preminorver:%{rpmminorver}}%{?dist}.6

License:	MIT
URL:		http://github.com/rspec/rspec-mocks
Source0:	https://rubygems.org/gems/%{gem_name}-%{fullver}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
%if 0%{?need_bootstrap_set} < 1
BuildRequires:	rubygem(rspec2)
%endif
Provides:	rubygem(%{rpmgem_name}) = %{version}-%{release}
Obsoletes:	rubygem-rspec-mocks < 2.14.6-2
BuildArch:	noarch

%description
rspec-mocks provides a test-double framework for Rspec including support
for method stubs, fakes, and message expectations.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	rubygem-rspec-mocks-doc < 2.14.6-2

%description	doc
This package contains documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

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

%if 0%{?need_bootstrap_set} < 1
%check
pushd .%{gem_instdir}
sed -i.yaml spec/rspec/mocks/serialization_spec.rb \
	-e '\@::YAML::ENGINE.yamler@d'
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 9
# ruby 2.5 changed toplevel constant behavior, disabling no longer applicable test
sed -i.toplevel spec/rspec/mocks/mutate_const_spec.rb \
	-e '\@expect.TestClass::Hash.@d'
%endif
ruby -rrubygems -Ilib/ -S rspec2 spec/
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Merlin Mathesius <mmathesi@redhat.com> - 2.14.6-6.5
- Minor conditional fix for ELN

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.6-6
- F-28: remove tests no longer valid on ruby 2.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-5.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-5.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.6-5
- Only test Psych, ::YAML::ENGINE.yamler is no longer supported

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.6-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.6-4
- Enable tests

* Wed Sep 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.6-3
- Modify summary, description a bit
- Kill redundant macro
- Fix BR to use rspec2, not rspec

* Thu Aug 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.6-2
- Rename to rspec2-mocks, cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.6-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.6-1
- 2.14.6

* Tue Feb  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.5-1
- 2.14.5

* Thu Oct 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.4-1
- 2.14.4

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-2
- Enable test suite again

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.3-1
- 2.14.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.1-1
- 2.13.1

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.0-2
- Enable test suite again

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.0-1
- 2.13.0

* Wed Feb 20 2013 V??t Ondruch <vondruch@redhat.com> - 2.12.2-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.2-1
- 2.12.2

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.1-2
- Enable test suite again

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.1-1
- 2.12.1

* Thu Oct 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.11.3-1
- 2.11.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

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
