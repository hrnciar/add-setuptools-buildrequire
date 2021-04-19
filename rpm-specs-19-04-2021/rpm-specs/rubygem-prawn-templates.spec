%global gem_name prawn-templates

Name: rubygem-%{gem_name}
Version: 0.1.2
Release: 4%{?dist}
Summary: Prawn::Templates allows using PDFs as templates in Prawn
License: Ruby or GPLv2 or GPLv3
URL: https://github.com/prawnpdf/prawn-templates
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/prawnpdf/prawn-templates.git && cd prawn-templates
# git checkout 0.1.2
# tar -czf rubygem-prawn-templates-0.1.2-spec-data.tgz spec/ data/
Source1: %{name}-%{version}-spec-data.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(prawn)
BuildRequires: rubygem-prawn-doc
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(pdf-reader)
BuildRequires: rubygem(pdf-inspector)
BuildArch: noarch

%description
Prawn::Templates allows using PDFs as templates in Prawn.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1
mv %{_builddir}/{spec,data} .
%gemspec_remove_dep -g pdf-reader "~> 2.0"
%gemspec_add_dep -g pdf-reader ">= 2.0"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
sed -i "/require 'bundler'/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler/ s/^/#/" spec/spec_helper.rb
rspec spec

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/prawn-templates.gemspec

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Christopher Brown <chris.brown@redhat.com> - 0.1.2-3
- Enabled test suite

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Christopher Brown <chris.brown@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Christopher Brown <chris.brown@redhat.com> - 0.1.1-1
- Bump to 0.1.1

* Sat Oct 06 2018 Christopher Brown <chris.brown@redhat.com> - 0.0.4-6
- Added patch to workaround strict dependencies

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 17 2016 Fabio Alessandro Locati <me@fale.io> - 0.0.4-1
- Initial package
