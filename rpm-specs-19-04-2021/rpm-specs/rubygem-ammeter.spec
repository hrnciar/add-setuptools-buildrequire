# Generated from ammeter-0.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ammeter

Name: rubygem-%{gem_name}
Version: 1.1.4
Release: 8%{?dist}
Summary: Write specs for your Rails 3+ generators
License: MIT
URL: https://github.com/alexrothenberg/%{gem_name}
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Rails 6+ compatibility.
# https://github.com/alexrothenberg/ammeter/pull/62
Patch0: rubygem-ammeter-1.1.4-Pass-source-to-template-separatedly.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(haml)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(rspec-rails) >= 2.2
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
Write specs for your Rails 3+ generators.


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
# Fix test suite for Ruby 2.3 compatibility.
# File#read is re-defined in spec/spec_helpr.rb#stub_file,
# and File#read is also used in 'require': specification.rb#load.
# If the first "require" for on library is called after the stub definition,
# it is failed.
rspec -r haml spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ammeter.gemspec
%{gem_instdir}/features
%{gem_instdir}/spec

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 V??t Ondruch <vondruch@redhat.com> - 1.1.4-7
- Fix Rails 6+ compatibility.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 pvalena <pvalena@redhat.com> - 1.1.4-1
- Update to ammeter 1.1.4.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 29 2016 Jun Aruga <jaruga@redhat.com> - 1.1.3-1
- Update to v1.1.3.
- Fix test suite for Ruby 2.3 compatibility.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 V??t Ondruch <vondruch@redhat.com> - 1.1.2-1
- Update to Ammeter 1.1.2.

* Tue Jun 10 2014 V??t Ondruch <vondruch@redhat.com> - 0.2.9-3
- Fix FTBFS in Rawhide (hrbz#1107063).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Josef Stribny <jstribny@redhat.com> - 0.2.9-1
- Update to 0.2.9
- Rebuilt with Rails 4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 V??t Ondruch <vondruch@redhat.com> - 0.2.8-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.8-1
- Updated to Ammeter 0.2.8.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-2
- Moved features to doc subpackage (not needed for runtime).
- Moved gemspec and Gemfile to doc.
- Patched the dependencies to require rspec-core.

* Thu Feb 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-1
- Initial package
