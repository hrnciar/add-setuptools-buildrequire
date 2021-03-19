# Generated from sprockets-2.4.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sprockets

Name: rubygem-%{gem_name}
Version: 4.0.2
Release: 2%{?dist}
Summary: Rack-based asset packaging system
License: MIT
URL: https://github.com/rails/sprockets
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# to get tests:
# git clone https://github.com/rails/sprockets.git && cd sprockets/
# git archive -v -o sprockets-4.0.2-tests.tar.gz v4.0.2 test/
Source1: sprockets-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(coffee-script)
BuildRequires: rubygem(ejs)
BuildRequires: rubygem(execjs)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(sass)
BuildRequires: rubygem(sassc)
BuildRequires: rubygem(timecop)
BuildRequires: rubygem(uglifier)
BuildRequires: %{_bindir}/help2man
BuildRequires: %{_bindir}/node
BuildArch: noarch

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, Sass, and SCSS.


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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Turn `sprockets --help` into man page
export GEM_PATH="%{buildroot}/%{gem_dir}:%{gem_dir}"
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr -N -s1 -o %{buildroot}%{_mandir}/man1/%{gem_name}.1 \
    %{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/bin/%{gem_name}

# Run the test suite
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# We don't have rubygem(babel-transpiler) yet.
mv test/test_babel_processor.rb{,.disabled}
mv lib/sprockets/autoload/babel.rb{,.disabled}
sed -i '/:Babel/ s/^/#/' lib/sprockets/autoload.rb
sed -i '/es6/ s/^/#/' test/test_asset.rb
sed -i '/test "es6 asset" do/,/^  end$/ s/^/#/' test/test_environment.rb
sed -i '/test "compile babel source map" do/,/^  end$/ s/^/#/' test/test_source_maps.rb

# We don't habe rubygem(closure-compiler) anymore.
# https://src.fedoraproject.org/rpms/rubygem-closure-compiler/c/c0d447db3557cba0d0134e9ab21b9e222066df41
mv test/test_closure_compressor.rb{,.disabled}
mv lib/sprockets/autoload/closure.rb{,.disabled}
sed -i '/:Closure/ s/^/#/' lib/sprockets/autoload.rb

# We don't have rubygem(eco) yet.
mv test/test_eco_processor.rb{,.disabled}
mv lib/sprockets/autoload/eco.rb{,.disabled}
sed -i '/:Eco/ s/^/#/' lib/sprockets/autoload.rb
sed -i '/test "eco templates" do/,/^  end/ s/^/#/' test/test_environment.rb

# We don't have rubygem(jsminc) yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=725768
mv test/test_jsminc_compressor.rb{,.disabled}
mv lib/sprockets/autoload/jsminc.rb{,.disabled}
sed -i '/:JSMinC/ s/^/#/' lib/sprockets/autoload.rb

# We don't have rubygem(yui-compressor) yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=725768
mv test/test_yui_compressor.rb{,.disabled}
mv lib/sprockets/autoload/yui.rb{,.disabled}
sed -i '/:YUI/ s/^/#/' lib/sprockets/autoload.rb

# This test fails trying to require `zopfli` which we don't have yet, but
# also trying to load `lib/sprockets/erb_processor.rb`, which is obvious.
# However I really wonder what Bundler does that the test pass upstream.
mv test/test_require.rb{,.disabled}

# Required by TestPathUtils#test_find_upwards test.
touch Gemfile

ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'

# Check content of man page created by help2man.
gunzip -c %{buildroot}%{_mandir}/man1/%{gem_name}.1.gz | \
  grep -q '^Adds the directory to the Sprockets load path'
popd

%files
%dir %{gem_instdir}
%{_bindir}/sprockets
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/%{gem_name}.1*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Vít Ondruch <vondruch@redhat.com> - 4.0.2-1
- Update to Sprockets 4.0.2.
  Resolves: rhbz#1759636

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 pvalena <pvalena@redhat.com> - 3.7.2-1
- Update to sprockets 3.7.2.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Vít Ondruch <vondruch@redhat.com> - 3.7.1-1
- Update to Sprockets 3.7.1.

* Mon Aug 15 2016 Vít Ondruch <vondruch@redhat.com> - 3.7.0-1
- Update to Sprockets 3.7.0.

* Mon Jul 04 2016 Jun Aruga <jaruga@redhat.com> - 3.6.3-1
- Fix a JavaScript runtime issue. (rhbz#1352650)
- Update to Sprockets 3.6.3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Vít Ondruch <vondruch@redhat.com> - 3.2.0-1
- Update to Sprockets 3.2.0.

* Tue Nov 18 2014 Josef Stribny <jstribny@redhat.com> - 2.12.3-1
- Update to 2.12.3

* Mon Aug 18 2014 Josef Strzibny <jstribny@redhat.com> - 2.12.1-3
- Fix FTBFS: ExecJS changed the exception names

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 2.12.1-2
- Filter tilt requires.

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 2.12.1-1
- Update to sprockets 2.12.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 2.8.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Josef Stribny <jstribny@redhat.com> - 2.8.2-1
- Upgraded to version 2.8.2
- Added rubygem-uglifier build dependency

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-1
- Initial package
