%global pkgname qpa

Name:           gap-pkg-%{pkgname}
Version:        1.32
Release:        1%{?dist}
Summary:        GAP package for quivers and path algebras

License:        GPLv2+
URL:            https://folk.ntnu.no/oyvinso/QPA/
Source0:        https://github.com/gap-packages/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-gbnp
BuildRequires:  tex(beamer.cls)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-gbnp

%description
This package carries out computations for finite dimensional quotients
of path algebras over the fields that are available in GAP.  QPA stands
for "Quivers and Path Algebras".

%package doc
Summary:        QPA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" << EOF
LoadPackage("qpa");
Read("doc/MakeQPADoc.gi");
EOF
rm -fr ../pkg

cd doc/gap-days-lectures
pdflatex lecture1
pdflatex lecture1
pdflatex lecture2
pdflatex lecture2
pdflatex lecture3
pdflatex lecture3
pdflatex lecture4a
pdflatex lecture4a

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{.*.yml,.gitignore,.mailmap,CHANGES,CODE_OF_CONDUCT.md,CONTRIBUTING.md,create-release.sh,LICENSE,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/gap-days-lectures/*.{aux,log,nav,out,snm,toc,vrb}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%changelog
* Thu Mar  4 2021 Jerry James <loganjerry@gmail.com> - 1.32-1
- Version 1.32
- Drop upstreamed -issymmetricalgebra patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Jerry James <loganjerry@gmail.com> - 1.31-1
- Version 1.31
- Drop upstreamed -doc patch
- Add -issymmetricalgebra patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Jerry James <loganjerry@gmail.com> - 1.30-2
- Drop broken "gap-pkg-core" Requires

* Sat Mar 14 2020 Jerry James <loganjerry@gmail.com> - 1.30-1
- Initial RPM
