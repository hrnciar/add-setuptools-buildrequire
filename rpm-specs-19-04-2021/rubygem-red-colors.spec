# Generated from red-colors-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name red-colors

Name:		rubygem-%{gem_name}
Version:	0.1.1
Release:	1%{?dist}

Summary:	Red Colors provides a wide array of features for dealing with colors
License:	MIT

URL:		https://github.com/red-data-tools/red-colors
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(test-unit)
BuildArch:	noarch

%description
Red Colors provides a wide array of features for dealing with colors. This
includes conversion between colorspaces, desaturation, and parsing colors.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
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

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}/
rm -rf \
	.yardopts \
	Gemfile \
	Rakefile \
	*.gemspec \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
ruby test/run.rb
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc		%{gem_instdir}/README.md

%{gem_libdir}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Tue Feb 09 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-1
- Initial package
