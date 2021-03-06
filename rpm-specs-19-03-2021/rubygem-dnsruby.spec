# Generated from dnsruby-1.52.gem by gem2rpm -*- rpm-spec -*-
%global gem_name dnsruby


Summary: Ruby DNS(SEC) implementation
Name: rubygem-%{gem_name}
Version: 1.53
Release: 19%{?dist}
License: ASL 2.0
URL: http://rubyforge.org/projects/dnsruby/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Dnsruby is a pure Ruby DNS client library. It provides a complete DNS
client implementation, including DNSSEC. It can also load (BIND) zone
files. Dnsruby has been used in OpenDNSSEC and ISC's DLV service.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
# ri installs bad filenames with macros in it, see rhbz#711893
# Reported to upstream
%gem_install -n %{SOURCE0}

%build

# Requires network traffic, also contains errors and seems to never return
#% check
#pushd .% {gem_instdir}
#RUBYOPT=rubygems testrb test/*.rb
#popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
# fix some DOS formated file
sed -i 's/\r//' %{buildroot}%{gem_instdir}/README
sed -i 's/\r//' %{buildroot}%{gem_instdir}/DNSSEC

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/test
%{gem_instdir}/demo
%{gem_instdir}/Rakefile
%{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/DNSSEC
%doc %{gem_instdir}/EXAMPLES
%doc %{gem_instdir}/README
%doc %{gem_instdir}/EVENTMACHINE


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.53-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.53-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Paul Wouters <paul@xelerance.com> - 1.53-1
- Updated to 1.53

* Fri Oct 14 2011 Paul Wouters <paul@xelerance.com> - 1.52-3
- Initial package
- Re-enabled ri install

* Tue Oct 04 2011 Paul Wouters <paul@xelerance.com> - 1.52-2
- Initial package for review
