%global	gem_name	rdtool

%if 0%{?fedora} >= 21
%global	gem_minitest	rubygem(minitest4)
%else
%global	gem_minitest	rubygem(minitest)
%endif

Name:		rubygem-%{gem_name}
Version:	0.6.38
Release:	16%{?dist}

Summary:	Formatter for RD
# From README.rd
# Note that setup.rb is not included in the binary
# rpm
License:	GPLv2+ or Ruby
URL:		https://github.com/uwabami/rdtool
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	%gem_minitest
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(racc)
Requires:	rubygem(racc)
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
RD is multipurpose documentation format created for documentating Ruby and
output of Ruby world. You can embed RD into Ruby script. And RD have neat
syntax which help you to read document in Ruby script. On the other hand, RD
have a feature for class reference.


%package	doc
Summary:	Documentation for %{name}
# utils/rd-mode.el is under GPLv2+
License:	(GPLv2+ or Ruby) and GPLv2+
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# rename rdswap.rb
mv bin/rdswap{.rb,}
sed -i -e "s|rdswap\.rb|rdswap|" %{gem_name}.gemspec

# shebang
sed -i \
	-e '\@/usr/bin/env@d' \
	lib/rd/rd2html-ext-opt.rb
sed -i \
	-e 's|/usr/bin/ruby[^ ][^ ]*|%{_bindir}/ruby|' \
	bin/*

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile Rakefile \
	setup.rb \
	%{gem_name}.gemspec \
	test/

rm -f lib/rd/pre-setup.rb
find lib/rd -type f -print0 | xargs -0 chmod ugo-x
popd

%check
pushd .%{gem_instdir}
ruby -Ilib:test:. -e 'gem "minitest", "<5" ; Dir.glob("test/test-*.rb").each {|f| require f}'
popd

%files
%dir %{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/LGPL-2.1

%{_bindir}/rd2
%{_bindir}/rdswap

%{gem_instdir}/bin
%{gem_libdir}/

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/doc/
%{gem_instdir}/utils/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.38-14
- R,BR rubygem(racc)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.38-6
- BR: rubygem(test-unit)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.38-4
- Force to use minitest ver4 for now

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.38-2
- Incorporate comments on review request (bug 1031316)

* Thu Nov 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.38-1
- Initial package
