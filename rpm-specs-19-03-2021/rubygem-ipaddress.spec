%global gem_name ipaddress

Name: rubygem-%{gem_name}
Version: 0.8.3
Release: 9%{?dist}
Summary: IPv4/IPv6 address manipulation library
License: MIT
URL: https://github.com/bluemonk/ipaddress
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
IPAddress is a Ruby library designed to make manipulation
of IPv4 and IPv6 addresses both powerful and simple. It maintains
a layer of compatibility with Ruby's own IPAddr, while 
addressing many of its issues.

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
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}/
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' 
popd

%files
%dir %{gem_instdir}/
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rock.yml
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test/
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%{gem_instdir}/README.rdoc
%{gem_instdir}/CHANGELOG.rdoc

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 08 2017 Franti??ek Dvo????k <valtri@civ.zcu.cz> - 0.8.3-1
- Update to 0.8.3 (#1295974)
- FTBFS fixes (#1308041, #1424324)
- Cleanups and packages changes (new guidelines, gem2rpm)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-8
- Patch tests for Minitest5 and Ruby 2.x (bz#1107145)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-5
- Fix build breakage on >= F19 with new Ruby guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-3
- Correct duplicate LICENSE file

* Thu Dec 27 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-2
- Revised per review in bz#823340

* Mon Apr 30 2012 Jonas Courteau <rpms@courteau.org> - 0.8.0-1
- Initial package
- Submitted https://github.com/bluemonk/ipaddress/issues/23 upstream to remove extra file from gem
