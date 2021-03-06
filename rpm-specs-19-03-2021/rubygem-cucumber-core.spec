# Generated from cucumber-core-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-core

Name: rubygem-%{gem_name}
Version: 3.2.0
Release: 10%{?dist}
Summary: Core library for the Cucumber BDD app
License: MIT
URL: https://cucumber.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/cucumber/cucumber-ruby-core.git && cd cucumber-ruby-core
# git checkout v3.2.0 && tar czvf rubygem-cucumber-core-3.2.0-spec.tar.gz spec/
Source1: %{name}-%{version}-spec.tar.gz
# Fix warnings affecting cucumber-wire test suite.
# https://github.com/cucumber/cucumber-ruby-core/pull/191
Patch0: rubygem-cucumber-core-6.0.0-Remove-unintended-private-call.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(gherkin)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(kramdown-parser-gfm)
BuildRequires: rubygem(cucumber-tag_expressions)
BuildRequires: rubygem(backports)
# BuildRequires: rubygem(unindent)
BuildArch: noarch

%description
Core library for the Cucumber BDD app.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%patch0 -p1

# We do not have gherkin 5 in Fedora yet.
%gemspec_remove_dep -s ../%{gem_name}-%{version}.gemspec -g gherkin '>= 5.0.0'
%gemspec_add_dep -s ../%{gem_name}-%{version}.gemspec -g gherkin '>= 4.1.0'

%gemspec_remove_dep -s ../%{gem_name}-%{version}.gemspec -g cucumber-tag_expressions '~> 1.1.0'
%gemspec_add_dep -s ../%{gem_name}-%{version}.gemspec -g cucumber-tag_expressions '>= 1.1.0'


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec

# unindent is not available in Fedora => avoid the requires.
for file in $(grep -Rl unindent spec); do
  sed -i "/require 'unindent'/ s/^/#/" "${file}"
  sed -i '/^ *expect.*unindent$/ i \pending' "${file}"
done

LANG=C.UTF-8 rspec -rkramdown/parser/gfm spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 V??t Ondruch <vondruch@redhat.com> - 3.2.0-9
- Relax rubygem(cucumber-tag_expressions) dependency.
  Resolves: rhbz#1871619

* Tue Aug 11 2020 V??t Ondruch <vondruch@redhat.com> - 3.2.0-8
- Fix warnings affecting cucumber-wire test suite.
  Resolves: rhbz#1863722

* Tue Aug 11 10:13:05 GMT 2020 V??t Ondruch <vondruch@redhat.com> - 3.2.0-7
- Add `BR: rubygem(kramdown-parser-gfm)` which was extrected into independency
  package.
  Resovles: rhbz#1863721

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 3.2.0-1
- Update to Cucumber-core 3.2.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Jun Aruga <jaruga@redhat.com> - 1.5.0-2
- Improve tests.

* Fri Jan 20 2017 V??t Ondruch <vondruch@redhat.com> - 1.5.0-1
- Update to cucumber-core 1.5.0.

* Tue Apr 05 2016 V??t Ondruch <vondruch@redhat.com> - 1.4.0-1
- Initial package
