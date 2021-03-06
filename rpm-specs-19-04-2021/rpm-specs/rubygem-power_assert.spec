%global	gem_name	power_assert

# Note: 1.1.7 -> 1.2.0: just the upstream URL changed
Name:		rubygem-%{gem_name}
Version:	1.2.0
Release:	202%{?dist}

Summary:	Power Assert for Ruby
License:	Ruby or BSD
URL:	https://github.com/ruby/power_assert
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-tests-%{version}.tar.gz
# Source1 is created by bash %%{SOURCE2} %%{version}
Source2:	create-power_assert-test-files.sh


BuildRequires:	rubygems-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(byebug)
BuildRequires:	rubygem(pry)

%if 0%{?fedora} < 21
Requires:	ruby(release)
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}
%endif

BuildArch:	noarch

%description
Power Assert for Ruby. Power Assert shows each value of variables and method
calls in the expression. It is useful for testing, providing which value
wasn't correct when the condition is not satisfied.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

tar xf %{SOURCE1}

%build
gem build %{gem_name}.gemspec

%gem_install
cp -a ./test ./%{gem_instdir}/

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# cleanup
pushd %{buildroot}%{gem_instdir}

rm -rf \
	.gitignore .travis.yml \
	Gemfile LEGAL \
	Rakefile \
	*gemspec \
	benchmarks \
	bin/ \
	test/ \
	%{nil}

popd

%check
pushd .%{gem_instdir}
# test-1.1.3/block_test.rb 1.1.3
LANG=C.utf8
ruby -Ilib:. \
	-e \
	'Dir.glob("test/**/*_test.rb").each {|f| require f}'
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/BSDL
%license	%{gem_instdir}/COPYING
%doc	%{gem_instdir}/README.rdoc
%{gem_libdir}
%{gem_spec}

%exclude	%{gem_cache}

%files	doc
%doc	%{gem_docdir}

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-200
- 1.2.0

* Thu Apr 16 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.7-200
- 1.1.7

* Mon Feb 24 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.6-201
- 1.1.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.5-200
- 1.1.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.4-200
- 1.1.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-204
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.3-203
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sun Nov 18 2018 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.3-202
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.3-200
- 1.1.3
- Bump release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov  9 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-100
- 1.1.1

* Thu Sep 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-100
- 1.1.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-100
- 1.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.1-100
- 0.4.1

* Sat Sep 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-100
- 0.3.1

* Wed May  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-100
- 0.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.7-100
- 0.2.7

* Tue Nov 10 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.6-100
- 0.2.6

* Sun Nov  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5-100
- 0.2.5

* Wed Jul 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.4-100
- 0.2.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.3-100
- 0.2.3

* Sun Dec 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-100
- Bump release massively (for ruby srpm)

* Tue Dec  2 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-2
- Misc cleanup

* Thu Nov 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-1
- 0.2.2
- Kill unneeded BR

* Sun Nov 16 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.1-1
- Initial package
