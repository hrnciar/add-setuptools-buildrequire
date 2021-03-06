# Generated from tins-0.8.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tins

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 15%{?dist}
Summary: Useful tools library in Ruby
License: MIT
URL: http://github.com/flori/tins
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(simplecov)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
All the stuff that isn't good/big enough for a real library.

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

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove uneeded files
rm -rf %{buildroot}%{gem_instdir}/{Gemfile,Rakefile,TODO,VERSION,%{gem_name}.gemspec,.gitignore,.travis.yml}

# Fix shebang
pushd %{buildroot}%{gem_instdir}

for test in mail null_pattern turing; do
  sed -i '1i #!/usr/bin/env ruby' examples/$test.rb
done

popd

%check
pushd .%{gem_instdir}
ruby -rtest-unit -e 'Test::Unit::AutoRunner.run(true)' -Ilib tests/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/COPYING
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/tests/
%{gem_instdir}/examples

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.0-5
- Fix test-unit usage for F22+

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 1.0.0-2
- Fix rpmlint errors/warnings

* Sun Feb 23 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 1.0.0-1
- Bump to 1.0.0
- Do some cleanup

* Mon Jan 27 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 0.13.1-1
- Bump to 0.13.1

* Wed Aug 14 2013 Axilleas Pipinellis <axilleas@fedoraproject.org> - 0.8.4-2
- Add forgotten changelog

* Tue Aug 13 2013 Axilleas Pipinellis <axilleas@fedoraproject.org> - 0.8.4-1
- Version bump

* Tue Aug 13 2013 Axilleas Pipinellis <axilleas@fedoraproject.org> - 0.8.3-1
- Initial package
