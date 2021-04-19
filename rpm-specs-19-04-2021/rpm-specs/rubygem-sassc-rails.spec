# Generated from sassc-rails-2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sassc-rails

# Because of circular dependency with sass-rails
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 2.1.2
Release: 2%{?dist}
Summary: Integrate SassC-Ruby into Rails
# SIL license found in
# test/dummy/app/assets/stylesheets/erb_render_with_context.css.erb
# https://github.com/sass/sassc-rails/issues/155
License: MIT and OFL
URL: https://github.com/sass/sassc-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(sass-rails)
BuildRequires: rubygem(sassc)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(tilt)
%endif
BuildArch: noarch

%description
Integrate SassC-Ruby into Rails.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
pushd .%{gem_instdir}

# Copy in .gemspec and use the sass-rails sources
cp %{buildroot}%{gem_spec} sassc-rails.gemspec

# Avoid unnecessary dependency
sed -i -e '/require .pry./ s/^/#/' test/test_helper.rb
sed -i -e '/dependency.*pry./ s/^/#/' \
       -e '/dependency.*rake./ s/^/#/' \
    sassc-rails.gemspec

sed -i -e '/Bundler\.require/ s/^/#/' \
       -e '/require .bundler./ s/^/#/' \
    test/test_helper.rb

ruby -Ilib:test -rsass-rails -rsprockets/railtie \
  -e 'Dir.glob "./test/**/*.rb", &method(:require)'
popd
%endif

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
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/sassc-rails.gemspec
%{gem_instdir}/test
%{gem_instdir}/gemfiles
%doc %{gem_instdir}/CODE_OF_CONDUCT.md

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Pavel Valena <pvalena@redhat.com> - 2.1.2-1
- Initial package.
