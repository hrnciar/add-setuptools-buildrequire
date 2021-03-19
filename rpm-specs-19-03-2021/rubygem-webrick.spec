# Generated from webrick-1.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name webrick

Name: rubygem-%{gem_name}
Version: 1.7.0
Release: 2%{?dist}
Summary: HTTP server toolkit
License: Ruby and BSD-2-Clause
URL: https://github.com/ruby/webrick
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Test suite is not packaged with the gem, you may check out it like so:
# git clone --no-checkout https://github.com/ruby/webrick
# cd webrick && git archive -v -o webrick-1.7.0-tests.txz v1.7.0 test
Source1: %{gem_name}-%{version}-tests.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3.0
BuildArch: noarch

%description
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server, a
proxy server, and a virtual-host server.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Symlink the test suite.
ln -s %{_builddir}/test .

ruby -Ilib:test:test/lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/webrick.gemspec

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Pavel Valena <pvalena@redhat.com> - 1.7.0-1
- Initial package
