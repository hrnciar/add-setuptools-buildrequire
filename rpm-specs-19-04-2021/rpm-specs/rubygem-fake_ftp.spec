#Generated from fake_ftp-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fake_ftp

Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 8%{?dist}
Summary: Creates a fake FTP server for use in testing
License: MIT
URL: http://rubygems.org/gems/fake_ftp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem-coderay
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Testing FTP? Use this!


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

#remove .files
rm -f .%{gem_instdir}/.gitignore
rm -f .%{gem_instdir}/.rspec
rm -f .%{gem_instdir}/.travis.yml
rm -f .%{gem_instdir}/.simplecov
rm -f .%{gem_instdir}/.codeclimate.yml
rm -f .%{gem_instdir}/.rubocop.yml
rm -f .%{gem_instdir}/.rubocop_todo.yml

%install
mkdir -p %{buildroot}%{gem_dir}

cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

# We are not interested in code coverage.
sed -i "/require 'simplecov'/ s/^/#/" spec/spec_helper.rb

# Increase timeout to make the test suite pass.
sed -i "s/timeout: 5,/timeout: 60,/" spec/spec_helper.rb

FUNCTIONAL_SPECS=1 INTEGRATION_SPECS=1 rspec -rspec_helper spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%doc %{gem_instdir}/README.md


%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%{gem_instdir}/fake_ftp.gemspec
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/LICENSE.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Tomas Hrcka <thrcka@redhat.com> - 0.3.0-6
- Raise timeout in the test suite to pass in koji environment

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 V??t Ondruch <vondruch@redhat.com> - 0.3.0-3
- Enable test suite.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 TOmas Hrcka <thrcka@redhat.com> - 0.3.0-1
- Update to latest upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-2
- Move CONTRIBUTORS.md to doc subpackage
- Fixed description
- Removed trailing whitespace

* Thu Feb 12 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-1
- Initial package

