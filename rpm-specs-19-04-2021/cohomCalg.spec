Name:           cohomCalg
Version:        0.32
Release:        8%{?dist}
Summary:        Sheaf cohomologies for line bundles on toric varieties

License:        GPLv3+
URL:            https://github.com/BenjaminJurke/cohomCalg
Source0:        https://github.com/BenjaminJurke/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Test output generated by Jerry James with cohomCalg on the upstream-tested
# architecture (x86_64), to verify that other architectures generate the same
# output.
Source1:        %{name}-test.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(extdash.sty)
BuildRequires:  tex(hyperxmp.sty)

%description
This package computes sheaf cohomologies for line bundles on toric
varieties.

%package doc
Summary:        Manual for %{name}
BuildArch:      noarch

%description doc
User manual for %{name}.

%prep
%autosetup
%setup -q -T -D -a 1

# Remove prebuilt Windows binaries and the prebuilt manual
rm -f bin/*.exe manual.pdf

%build
# Build the binary
%make_build CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"

# Build the manual
cd manual/latex_source
pdflatex manual
bibtex manual
pdflatex manual
pdflatex manual

%install
mkdir -p %{buildroot}%{_bindir}
cp -p bin/cohomcalg %{buildroot}%{_bindir}

%check
# Do not check P31SU8.in; it takes about half a day on a reasonably fast
# computer.
pushd bin
for fil in CP2 P31SU7 Quintic WCP11114 dP1 dP3; do
  ./cohomcalg --integrated $fil.in 2>/dev/null | diff -q out/$fil.out -
done
popd

%files
%license LICENSE
%doc README.md
%{_bindir}/cohomcalg

%files doc
%doc manual/latex_source/manual.pdf

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Jerry James <loganjerry@gmail.com> - 0.32-2
- Move manual to -doc subpackage
- Identify the source of the test output

* Wed Apr 25 2018 Jerry James <loganjerry@gmail.com> - 0.32-1
- Initial RPM
