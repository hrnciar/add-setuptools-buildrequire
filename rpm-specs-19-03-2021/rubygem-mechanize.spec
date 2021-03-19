# Initially Generated from mechanize-0.8.5.gem by gem2rpm -*- rpm-spec -*-

%global	majorver		2.7.7
%undefine	preminorver	
%global	rpmminorver		.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver		%{majorver}%{?preminorver}

%global	fedorarel		1

%global	gem_name		mechanize

%global	gem_instdir	%{gem_dir}/gems/%{gem_name}-%{version}%{?preminorver}

Summary:	A handy web browsing ruby object
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{fedorarel}%{?preminorver:%{rpmminorver}}%{?dist}
License:	MIT
URL:		http://mechanize.rubyforge.org/
Source0:	https://rubygems.org/gems/%{gem_name}-%{fullver}.gem
# Kill ntlm-http support
# https://github.com/sparklemotion/mechanize/issues/282
Patch0:	rubygem-mechanize-2.6.0-disable-ntlm-http.patch
Patch1:	rubygem-mechanize-2.6.0-disable-ntlm-http-test.patch

BuildRequires:	ruby(release)
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
# For %%check
BuildRequires:	rubygem(domain_name)
BuildRequires:	rubygem(http-cookie)
BuildRequires:	rubygem(mime-types)
BuildRequires:	rubygem(net-http-digest_auth)
BuildRequires:	rubygem(net-http-persistent)
BuildRequires:	rubygem(nokogiri)
#BuildRequires:	rubygem(ntlm-http)
BuildRequires:	rubygem(webrobots)
BuildRequires:	rubygem(minitest)
# Used in tests
%if 0%{?fedora} >= 34
BuildRequires:	rubygem(webrick)
%endif

Requires:	ruby(release)
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
#Requires:	rubygem(hoe)

# For non-gem support, net-http-persistent (which this package depends on)
# must also create non-gem package. Let's kill it (at least for F-15)
Obsoletes:	ruby-%{gem_name} < 1.0.0-999

BuildArch:	noarch

%description
The Mechanize library is used for automating interaction with websites. 
Mechanize automatically stores and sends cookies, follows redirects, 
can follow links, and submit forms. Form fields can be populated and 
submitted. Mechanize also keeps track of the sites that you have 
visited as a history.

%package	doc
Summary:	Documentation for %{name}
# Directory ownership issue
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(rubygems)

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# Patches
%patch0 -p1 -b .ntlm
%patch1 -p1 -b .ntlmtest

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
# Kill ntlm-http dependency
sed -i -e '\@ntlm-http@d' %{gem_name}.gemspec
%if 0%{?fedora} < 34
# Kill explicit webrick depedency
sed -i -e '\@webrick@d' %{gem_name}.gemspec
%endif


gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
mkdir -p .%{gem_dir}

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

# Clean up
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest \
	.gemtest \
	.gitignore \
	.github/ \
	.travis.yml \
	Gemfile \
	Rakefile \
	*.gemspec \
	test/ \
	%{nil}
popd

%check
pushd ./%{gem_instdir}

# http://pkgs.fedoraproject.org/cgit/openssl.git/tree/openssl-1.0.1e-no-md5-verify.patch
# TODO: need "correct" solution
%if 0%{?fedora} >= 21
export OPENSSL_ENABLE_MD5_VERIFY=yes
%endif

# Workaround. "rake test" invokes test with "ruby -w", i.e. "ruby -W2"
export RUBYLIB=$(pwd)/lib:$(pwd)
ruby -e 'Dir.glob("test/**/test*.rb").each {|f| require f}' || \
	ruby -W2 -e 'Dir.glob("test/**/test*.rb").each {|f| require f}'
popd

%files
%doc	%{gem_instdir}/[A-Z]*.rdoc
%dir	%{gem_instdir}
%{gem_libdir}/
%exclude	%{gem_cache}
%{gem_spec}

%files	doc
%{gem_dir}/doc/%{gem_name}-%{fullver}/
%{gem_instdir}/examples/

%changelog
* Tue Feb  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.7-1
- 2.7.7
  - Including fix for CVE-2021-21289

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 6 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.6-2
- Fix build failure

* Wed Jan  6 14:47:46 CET 2021 Pavel Valena <pvalena@redhat.com> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.6-1
- 2.7.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.5-2
- Backport patch from upstream to fix test failure on ruby 2.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.5-1
- 2.7.5

* Thu Jul 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.4-2
- Support mime-types >= 3 for rails 5 (bug 1356541)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.4-1
- 2.7.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.3-3
- Force to use minitest ver4 for now

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.3-2
- Also modify mime-type dependency on spec (bug 1080855)

* Mon Nov 18 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.3-1
- 2.7.3

* Mon Nov 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.2-1
- 2.7.2

* Thu Oct 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.5.beta.20110107104205.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.1-0.5.beta.20110107104205
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.4.beta.20110107104205.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.4.beta.20110107104205.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.1-0.4.beta.20110107104205
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.3.beta.20110107104205.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.1-0.3.beta.20110107194205
- Allow net-http-persistent 2.x

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.1-0.2.beta.20110107104205
- Bump release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.1.beta.20110107104205.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.1-0.1.beta.20110107104205
- 1.0.1.beta.20110107104205
- Kill non-gem support (at least for F-15)

* Wed Feb 10 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.0-2
- 1.0.0
- Fix permission
- F-11: Kill one failing test due to old (< 1.4.0) nokogiri

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-2
- F-12: Mass rebuild

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-1
- 0.9.3

* Thu Mar 12 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.2-1
- 0.9.2

* Thu Feb 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.1-1
- 0.9.1

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.0-3
- F-11: Mass rebuild

* Tue Jan 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.0-2
- Some cleanup

* Thu Dec 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.0-1
- 0.9.0
- Dependency changed: hpricot -> nokogiri

* Sun Dec 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.5-2
- Switch to Gem

* Wed Nov 26 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.5-1
- 0.8.5

* Wed Oct  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.4-1
- 0.8.4

* Wed Oct  1 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.3-1
- 0.8.3

* Thu Sep 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.0-1
- 0.8.0

* Thu Aug 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.8-1
- 0.7.8

* Thu Jul 31 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.7-1
- 0.7.7

* Thu May 22 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.6-1
- 0.7.6

* Thu Mar 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.5-1
- 0.7.5

* Thu Mar  6 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-1
- 0.7.1

* Thu Jan 17 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.0-1
- 0.7.0

* Thu Dec 13 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.11-1
- 0.6.11

* Fri Nov  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.10-3
- More cleanup

* Sat Nov  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.10-2
- BR: ruby
- Remove unneeded CFLAGS

* Sat Nov  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.10-1
- 0.6.10

* Fri Jun  8 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.8-1
- Initial packaging
