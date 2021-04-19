%global octpkg metch

Name:           octave-%{octpkg}
Version:        0.6
Release:        4%{?dist}
Summary:        Mesh/volume registration toolbox
License:        GPLv2+
URL:            http://iso2mesh.sourceforge.net/cgi-bin/index.cgi?metch
Source0:        https://github.com/fangq/%{octpkg}/archive/%{version}/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave
Requires(post): octave
Requires(postun): octave

%description
Matlab/Octave-based mesh/volume registration toolbox. It provides
straightforward functions to register point clouds (or surfaces) to a
triangular/cubic surface mesh by calculating an optimal affine transformation
(in terms of matrix A for scaling and rotation, and b for translation). It
also allows one to project a point cloud onto the surface using surface norms
and guarantee the conformity of the points to the surface. At this point, metch
can only perform rigid-body registration in terms of a linear transformation. 

%prep
%autosetup -n %{octpkg}-%{version}

# Matlab only
rm -vf metchgui*.m

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Matlab/Octave-based mesh/volume registration toolbox. It provides
 straightforward functions to register point clouds (or surfaces) to a
 triangular/cubic surface mesh by calculating an optimal affine transformation
 (in terms of matrix A for scaling and rotation, and b for translation). It
 also allows one to project a point cloud onto the surface using surface norms
 and guarantee the conformity of the points to the surface. At this point, metch
 can only perform rigid-body registration in terms of a linear transformation. 
Categories: Mesh
EOF

cat > INDEX << EOF
metch >> metch
metch
 regpt2surf
 proj2mesh
 affinemap
 dist2surf
 getplanefrom3pt
 linextriangle
 nodesurfnorm
 trisurfnorm
EOF

mkdir -p inst/
mv *.m inst/
chmod -x inst/*

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license COPYING
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Qianqian Fang <fangqq@gmail.com> - 0.6-1
- Update source URL to github
- Fix build error (#1736367)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 0.5.0-9
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 0.5.0-7
- Rebuild for octave 4.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.0-1
- Initial package
