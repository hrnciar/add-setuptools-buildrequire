# Generated from zeitwerk-2.1.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name zeitwerk

Name: rubygem-%{gem_name}
Version: 2.4.2
Release: 2%{?dist}
Summary: Efficient and thread-safe constant autoloader
License: MIT
URL: https://github.com/fxn/zeitwerk
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Test suite is not included in packaged gem
# git clone https://github.com/fxn/zeitwerk.git --no-checkout
# cd zeitwerk && git archive -v -o zeitwerk-2.4.2-tests.txz v2.4.2 test
Source2: %{gem_name}-%{version}-tests.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-reporters)
BuildArch: noarch

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem
and application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, preloading,
reloading, and eager loading.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b2

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

# focus gem is not needed for tests
sed -i '/require..minitest.focus./ s/^/#/' test/test_helper.rb

ruby -Itest:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 10:16:11 CET 2020 Pavel Valena <pvalena@redhat.com> - 2.4.2-1
- Update to zeitwerk 2.4.2.

* Fri Oct 30 19:47:19 CET 2020 Pavel Valena <pvalena@redhat.com> - 2.4.1-1
- Update to zeitwerk 2.4.1.

* Wed Aug 19 16:28:46 GMT 2020 Pavel Valena <pvalena@redhat.com> - 2.4.0-1
- Update to zeitwerk 2.4.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Pavel Valena <pvalena@redhat.com> - 2.3.0-1
- Update to zeitwerk 2.3.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Pavel Valena <pvalena@redhat.com> - 2.2.1-1
- Update to zeitwerk 2.2.1.

* Tue Sep 24 2019 Pavel Valena <pvalena@redhat.com> - 2.1.10-1
- Initial package
