# Generated from between_meals-0.0.12.gem by gem2rpm -*- rpm-spec -*-
%global gem_name between_meals

Name: rubygem-%{gem_name}
Version: 0.0.12
Release: 1%{?dist}
Summary: Between Meals
License: ASL 2.0
URL: https://github.com/facebook/between-meals
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/facebook/between-meals && cd between-meals
# git checkout v0.0.12
# tar -czf rubygem-between_meals-0.0.12-specs.tgz spec/
Source1: rubygem-%{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem-rspec
BuildRequires: rubygem-simplecov
BuildRequires: rubygem-mixlib-shellout
BuildRequires: rubygem-rugged
BuildArch: noarch

%description
Between Meals is the library for calculating what Chef objects were modified
between two revisions in a version control system. It is also the library that
backs Taste Tester and Grocery Delivery. It currently supports SVN, GIT and
HG, but plugins can easily be written for other source control systems. It
also includes some wrappers around knife execution and a few other utility
functions.

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

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jan 26 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.0.12-1
- Initial package
