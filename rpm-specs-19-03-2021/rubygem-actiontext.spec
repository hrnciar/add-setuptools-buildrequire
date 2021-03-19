# Generated from actiontext-6.0.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actiontext

# webdrivers gem is used in tests, but it's not in Fedora yet
%bcond_with webdrivers

Name: rubygem-%{gem_name}
Version: 6.1.3
Release: 1%{?dist}
Summary: Rich text framework
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# Tests are not shipped with the gem
# git clone https://github.com/rails/rails.git --no-checkout
# cd rails/actiontext && git archive -v -o actiontext-6.1.3-tests.txz v6.1.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may get them like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-6.1.3-tools.txz v6.1.3 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(activestorage) = %{version}
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(capybara) >= 3.26
BuildRequires: rubygem(selenium-webdriver)
%if %{with webdrivers}
BuildRequires: rubygem(webdrivers)
%endif
BuildArch: noarch

%description
Edit and display rich text in Rails applications.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/tools ..
mv %{_builddir}/test .

# Remove bundler usage
sed -i '/Bundler.require/ s/^/#/' test/dummy/config/application.rb

# Remove asset pipeline initializer
echo > test/dummy/config/initializers/assets.rb

# We don't have webdrivers
%if %{without webdrivers}
mv test/system/system_test_helper_test.rb{,.disable}
%endif

ruby -rselenium-webdriver -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/package.json
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Feb 18 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3-1
- Update to actiontext 6.1.3.

* Mon Feb 15 2021 Pavel Valena <pvalena@redhat.com> - 6.1.2.1-1
- Update to actiontext 6.1.2.1.

* Wed Jan 27 2021 Pavel Valena <pvalena@redhat.com> - 6.1.1-1
- Update to actiontext 6.1.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 12:04:45 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to actiontext 6.0.3.4.
  Resolves: rhbz#1877508

* Tue Sep 22 01:18:56 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to actiontext 6.0.3.3.
  Resolves: rhbz#1877508

* Mon Aug 17 05:18:06 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to actiontext 6.0.3.2.

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-2
- Initial package Action Text 6.0.3.1.
