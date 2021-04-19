%global	gem_name	contracts

Name:		rubygem-%{gem_name}
Version:	0.16.0
Release:	11%{?dist}

Summary:	Contracts for Ruby
License:	BSD
URL:		http://egonschiele.github.io/contracts.ruby/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Upstream patches
Patch1:	rubygem-contracts-0.16.0-0001-Don-t-use-exceptions-for-control-flow.patch
Patch2:	rubygem-contracts-0.16.0-0002-Update-spec-to-specify-error-class-to-suppress-RSpec.patch
Patch3:	rubygem-contracts-0.16.0-0003-Fix-misspellings-in-comments.patch
Patch4:	rubygem-contracts-0.16.0-0004-Wrapping-blocks-only-when-there-is-a-Func-check.-bug.patch
# Ruby 3.0 Trial Upstream patches
# https://github.com/egonSchiele/contracts.ruby/issues/294
# https://github.com/egonSchiele/contracts.ruby/pull/295
Patch5:	rubygem-contracts-0.16.0-0005-Update-implementation-spec-to-be-3.0-compatible.patch

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(rspec) >= 3
BuildArch:		noarch

%description
This library provides contracts for Ruby. Contracts let you clearly express
how your code behaves, and free you from writing tons of boilerplate,
defensive code.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
%patch5 -p1
%endif

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.[^.]* \
	Gemfile \
	Rakefile \
	*gemspec \
	*yml \
	features/ \
	script/ \
	spec/ \
	%{nil}

%check
pushd .%{gem_instdir}
rspec spec/
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE
%doc		%{gem_instdir}/CHANGELOG.markdown
%doc		%{gem_instdir}/README.md
%doc		%{gem_instdir}/TODO.markdown
%doc		%{gem_instdir}/TUTORIAL.md

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
# Keep this
%{gem_instdir}/benchmarks/

%changelog
* Sun Feb 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.16.0-11
- Add conditional for eln

* Sun Jan 31 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.16.0-10
- Backport some patches from the upstream
- Ruby 3.0: apply the upstream WIP patch for keyword separation

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.16.0-1
- 0.16.0

* Fri Mar 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.15.0-1
- 0.15.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.0-2
- Remove features/ directory from packaging

* Thu Aug 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.0-1
- Initial package
