%global	gem_name	glut

Name:		rubygem-%{gem_name}
Version:	8.3.0
Release:	16%{?dist}

Summary:	Glut bindings for the OpenGL gem
License:	MIT
URL:		https://github.com/larskanis/glut
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	gcc
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	freeglut-devel

%description
Glut bindings for the opengl gem.

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

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd


pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Rakefile \
	ext/ \
popd

# No test suite available

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/History.rdoc
%doc	%{gem_instdir}/Manifest.txt
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/

%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-15
- F-34: rebuild against ruby 3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-12
- F-32: rebuild against ruby27

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 8.3.0-11
- Rebuilt for new freeglut

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-8
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 8.3.0-5
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-4
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun  9 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-1
- 8.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-3
- F-26: rebuild for ruby24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-1
- 8.2.2

* Tue Jan 12 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-5
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-3
- F-22: Rebuild for ruby 2.2

* Sun Jan 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-2
- Some cleanup

* Thu Dec 18 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-1
- Initial package
