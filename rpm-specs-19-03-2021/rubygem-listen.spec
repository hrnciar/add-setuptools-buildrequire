# Generated from listen-0.4.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name listen

Name: rubygem-%{gem_name}
Version: 3.4.1
Release: 2%{?dist}
Summary: Listen to file modifications
License: MIT
URL: https://github.com/guard/listen
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/guard/listen.git --no-checkout
# cd listen && git archive -v -o rubygem-listen-3.4.1-spec.txz v3.4.1 spec
Source1: rubygem-listen-%{version}-spec.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rb-inotify)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
The Listen gem listens to file modifications and notifies you about the
changes. Works everywhere!


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
popd

# Remove the hardcoded dependencies. We don't have them in Fedora
# (except rb-inotify), they are platform specifis and not needed.
# https://github.com/guard/listen/pull/54
%gemspec_remove_dep -g rb-fsevent [">= 0.10.3", "~> 0.10"]
sed -i '/def self.usable?$/a         return false' lib/listen/adapter/darwin.rb

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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/spec spec

# We removed dependencies from other platforms so let's remove
# tests as well
mv spec/lib/listen/adapter/darwin_spec.rb{,.disabled}

rspec -rspec_helper spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/listen
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Pavel Valena <pvalena@redhat.com> - 3.4.1-1
- Update to listen 3.4.1.
  Resolves: rhbz#1916416

* Tue Jan 05 2021 Pavel Valena <pavel.valena@email.com> - 3.4.0-1
- Update to listen 3.4.0.
  Resolves: rhbz#1902562

* Thu Nov 12 23:05:28 CET 2020 Pavel Valena <pvalena@redhat.com> - 3.3.0-1
- Update to listen 3.3.0.
  Resolves: rhbz#1896227

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Pavel Valena <pvalena@redhat.com> - 3.2.1-1
- Update to listen 3.2.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Pavel Valena <pvalena@redhat.com> - 3.2.0-1
- Update to listen 3.2.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 V??t Ondruch <vondruch@redhat.com> - 3.1.5-6
- Fix test suite on Ruby 2.6.
- .spec file refresh.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 V??t Ondruch <vondruch@redhat.com> - 3.1.5-1
- Update to Listen 3.1.5.

* Wed Apr 20 2016 Jun Aruga <jaruga@redhat.com> - 3.0.6-1
- Update to 3.0.6.
- Fix test suite for Ruby 2.3 compatibility (rhbz#1308046).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Josef Stribny <jstribny@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 07 2014 Josef Stribny <jstribny@redhat.com> - 2.7.11-1
- Update to listen 2.7.11

* Mon Sep 01 2014 Josef Stribny <jstribny@redhat.com> - 2.7.9-1
- Update to listen 2.7.9.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 V??t Ondruch <vondruch@redhat.com> - 0.4.7-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 V??t Ondruch <vondruch@redhat.com> - 0.4.7-1
- Initial package
