%global gem_name stringex

Name:           rubygem-%{gem_name}
Summary:        Useful extensions to Ruby's String class
Version:        2.8.5
Release:        5%{?dist}
License:        MIT

URL:            http://github.com/rsl/stringex
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# DEPRECATION WARNING: update_attributes! is deprecated and will be removed
# from Rails 6.1 (please, use update! instead)
Patch1:		rubygem-stringex-2.8.5-rails61-compati.patch

BuildArch:      noarch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby

BuildRequires:  rubygem(activerecord)
BuildRequires:  rubygem(i18n)
BuildRequires:  rubygem(RedCloth)
BuildRequires:  rubygem(sqlite3)
BuildRequires:  rubygem(test-unit)

%description
Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to ASCII transliteration], and
StringExtensions [miscellaneous helper methods for the String class].


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}
%patch1 -p1


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ruby -I'lib:test' -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%license %{gem_instdir}/MIT-LICENSE

%dir %{gem_instdir}
%{gem_instdir}/VERSION
%{gem_instdir}/init.rb
%{gem_instdir}/locales

%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/stringex.gemspec
%{gem_instdir}/test/


%changelog
* Sun Feb 14 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.5-5
- Patch to make test suite compatible with rails 6.1.x

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.5-1
- Initial package

