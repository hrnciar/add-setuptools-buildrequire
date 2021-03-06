%global gem_name thin

Name: rubygem-%{gem_name}
Version: 1.8.0
Release: 1%{?dist}
Summary: A thin and fast web server
# lib/thin/stats.html.erb: BSD
# spec/rails_app/public/javascripts/*.js: MIT
License: (GPLv2+ or Ruby) and BSD and MIT
URL: https://github.com/macournoyer/thin
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/macournoyer/thin.git && cd thin
# git archive -v -o thin-1.8.0-tests.tar.gz v1.8.0 spec/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(eventmachine) >= 1.0.4
BuildRequires: rubygem(daemons) >= 1.0.9
BuildRequires: rubygem(rack) >= 1.0.0

%description
Thin is a Ruby web server that glues together three of the best Ruby
libraries in web history.
The Mongrel parser, the root of Mongrel speed and security,
Event Machine, a network I/O library with extremely high scalability and
Rack, a minimal interface between webservers and Ruby frameworks.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
cp -a %{_builddir}/spec spec

# To prevent timeout error on koji build.
sed -i '/^  def wait_for_server_to_start$/,/^  end$/ s/(10)/(30)/' \
    spec/daemonizing_spec.rb

rspec -I$(dirs +1)%{gem_extdir_mri} spec

popd

%files
%dir %{gem_instdir}
%{_bindir}/thin
%{gem_extdir_mri}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/example/
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Tue Feb 02 2021 V??t Ondruch <vondruch@redhat.com> - 1.8.0-1
- Update to Thin 1.8.0.
  Resolves: rhbz#1897471

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 V??t Ondruch <vondruch@redhat.com> - 1.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Fri Oct 30 2020 Jun Aruga <jaruga@redhat.com> - 1.7.2-15
- Fix to run the tests on RSpec 3.
- Fix outdated URL.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 V??t Ondruch <vondruch@redhat.com> - 1.7.2-12
- Fix FTBFS due maximum_connections changes.

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.2-12
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 V??t Ondruch <vondruch@redhat.com> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Bj??rn Esser <besser82@fedoraproject.org> - 1.7.2-6
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.2-5
- F-28: rebuild for ruby25

* Tue Aug 08 2017 Jun Aruga <jaruga@redhat.com> - 1.7.2-4
- Fix FTBFS.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 V??t Ondruch <vondruch@redhat.com> - 1.7.2-1
- Update to Thin 1.7.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 V??t Ondruch <vondruch@redhat.com> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Fri Jul 29 2016 Jun Aruga <jaruga@redhat.com> - 1.7.0-1
- Update to Thin 1.7.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 V??t Ondruch <vondruch@redhat.com> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Tue Oct 20 2015 V??t Ondruch <vondruch@redhat.com> - 1.6.4-1
- Update to Thin 1.6.4.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.2-4
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Use rspec2 for now

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 V??t Ondruch <vondruch@redhat.com> - 1.6.2-1
- Update to thin 1.6.2.

* Wed Apr 16 2014 Josef Stribny <jstribny@redhat.com> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 V??t Ondruch <vondruch@redhat.com> - 1.5.0-1
- Update to thin 1.5.0.

* Thu Feb 28 2013 V??t Ondruch <vondruch@redhat.com> - 1.3.1-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 V??t Ondruch <vondruch@redhat.com> - 1.3.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 V??t Ondruch <vondruch@redhat.com> - 1.3.1-1
- Update to Thin 1.3.1.

* Tue Sep 06 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-10
- Bump the release so upgrades from F-16 work

* Mon Jul 25 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-3
- Move stats.html.erb to the main package (it is a runtime requirement)

* Fri Jul 22 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-2
- Fix the load path for thin_parser

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.11-1
- Version bump

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-3
- Removed Rake dependency completely

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-2
- Fixed RSpec tests

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-1
- Updated to upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.7-1
- Updated to upstream version

* Thu Feb 04 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-5
- Excluded ppc64 in tests (566401)
- Fixed Licensing

* Wed Feb 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-4
- Added rspec tests
- Fixed unwanted recompilation
- Fixed licensing

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-3
- Fixed description

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-2
- Build fixed
- Licence corrected
- Added missing requires
- Marked relevant files as documentation

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-1
- Initial package


