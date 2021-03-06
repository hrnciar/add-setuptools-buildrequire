# Generated from tzinfo-0.3.26.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tzinfo

Name: rubygem-%{gem_name}
Version: 2.0.4
Release: 2%{?dist}
Summary: Daylight savings aware timezone library
License: MIT
URL: http://tzinfo.github.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Gem file does not contain a test suite, you can create it like so:
# git clone https://github.com/tzinfo/tzinfo.git --no-checkout
# cd tzinfo && git archive -v -o tzinfo-2.0.4-tests.txz v2.0.4 test/
Source1: %{gem_name}-%{version}-tests.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(concurrent-ruby)
BuildArch: noarch

%description
TZInfo provides daylight savings aware transformations between times in
different time zones.


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

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# We don't want to use bundler
sed -i "/raise 'Tests must be run with bundler/ s/^/#/" \
  test/test_utils.rb

RUBYOPT="-I.:lib:test" ruby -rtest/ts_all
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Pavel Valena <pavel.valena@email.com> - 2.0.4-1
- Update to tzinfo 2.0.4.
  Resolves: rhbz#1908521

* Fri Nov 13 00:58:17 CET 2020 Pavel Valena <pvalena@redhat.com> - 2.0.3-1
- Update to tzinfo 2.0.3.
  Resolves: rhbz#1895701

* Fri Oct 30 21:10:27 CET 2020 Pavel Valena <pvalena@redhat.com> - 2.0.2-1
- Update to tzinfo 2.0.2.
  Resolves: rhbz#1820389

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Pavel Valena <pvalena@redhat.com> - 2.0.1-1
- Update to tzinfo 2.0.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 V??t Ondruch <vondruch@redhat.com> - 1.2.5-1
- Update to TZInfo 1.2.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Patch tzinfo to use Minitest 5

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 1.1.0-1
- Update to tzinfo 1.1.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Josef Stribny <jstribny@redhat.com> - 0.3.37-1
- Update to tzinfo 0.3.37.

* Mon Feb 25 2013 V??t Ondruch <vondruch@redhat.com> - 0.3.35-1
- Update to tzinfo 0.3.35.

* Mon Feb 25 2013 V??t Ondruch <vondruch@redhat.com> - 0.3.34-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 V??t Ondruch <vondruch@redhat.com> - 0.3.34-1
- Update to tzinfo 0.3.34.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 V??t Ondruch <vondruch@redhat.com> - 0.3.30-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 V??t Ondruch <vondruch@redhat.com> - 0.3.30-1
- Update to tzinfo 0.3.30.

* Sun Apr 10 2011  <Minnikhanov@gmail.com> - 0.3.26-1
- Updated mail to latest upstream release (v.0.3.26 2011-04-01)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011  <Minnikhanov@gmail.com> - 0.3.24-2
- Fix Comment 3 #668098. https://bugzilla.redhat.com/show_bug.cgi?id=668098#c3 

* Tue Jan 18 2011  <Minnikhanov@gmail.com> - 0.3.24-1
- Updated mail to latest upstream release

* Sat Jan 08 2011  <Minnikhanov@gmail.com> - 0.3.23-1
- Initial package

