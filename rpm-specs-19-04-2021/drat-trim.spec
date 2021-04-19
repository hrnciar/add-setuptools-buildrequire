%global gitdate 20200914
%global commit  d13f761fbdacd052429f14421f95a7e8cd75deb1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           drat-trim
Version:        0
Release:        0.9.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Proof checker for DIMACS proofs

License:        MIT
URL:            https://github.com/marijnheule/drat-trim
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Drat2er wants to use drat-trim as a library, but drat-trim only provides a
# binary.  Modify the sources to provide a library.
Patch0:         %{name}-library.patch
# Drat2er and CVC4 do not want to see commentary.  Apply a patch from the
# drat2er developers to optionally make it shut up.
Patch1:         %{name}-silent.patch

BuildRequires:  gcc
BuildRequires:  help2man

%description
The proof checker DRAT-trim can be used to check whether a
propositional formula in the DIMACS format is unsatisfiable.  Given a
propositional formula and a clausal proof, DRAT-trim validates that the
proof is a certificate of unsatisfiability of the formula.  Clausal
proofs should be in the DRAT format which is used to validate the
results of the SAT competitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers files and library links for developing applications that use
%{name}.

%package        tools
Summary:        Command line interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains a command line interface to %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
# Build the library
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -fPIC -shared -Wl,-h,lib%{name}.so.0 \
  -o lib%{name}.so.0.0.0 %{name}.c
ln -s lib%{name}.so.0.0.0 lib%{name}.so.0
ln -s lib%{name}.so.0 lib%{name}.so

# Build the command line interface
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -o %{name} %{name}-main.c -L. -l%{name}
export LD_LIBRARY_PATH=$PWD

# Build the other tools
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -o lrat-check lrat-check.c
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -o drat-compress compress.c
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -o drat-decompress decompress.c

# Make man page for the command line interface
help2man --version-string=%{gitdate} -N -o %{name}.1 ./%{name}

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a lib%{name}.so* %{buildroot}%{_libdir}

# Install the header file
mkdir -p %{buildroot}%{_includedir}
cp -p %{name}.h %{buildroot}%{_includedir}

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
cp -p drat-compress drat-decompress drat-trim lrat-check %{buildroot}%{_bindir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p drat-trim.1 %{buildroot}%{_mandir}/man1

%check
export LD_LIBRARY_PATH=$PWD
./run-examples

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*

%files          devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files          tools
%doc README.md
%{_bindir}/drat-compress
%{_bindir}/drat-decompress
%{_bindir}/drat-trim
%{_bindir}/lrat-check
%{_mandir}/man1/drat-trim.1*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20200914.d13f761
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Jerry James <loganjerry@gmail.com> - 0-0.8.20200914.d13f761
- Update for proof emission from lrat-check

* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 0-0.7.20200605.9afad0f
- Update for comment support and expandable literal lists

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200125.a89ef60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar  5 2020 Jerry James <loganjerry@gmail.com> - 0-0.5.20200125.a89ef60
- Update to latest git snapshot for derivation fixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20190702.8a7a96b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190702.8a7a96b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Jerry James <loganjerry@gmail.com> - 0-0.2.20190702.8a7a96b
- Bug fix for sortClause

* Thu Jun  6 2019 Jerry James <loganjerry@gmail.com> - 0-0.1.20190516.e6fc615
- Initial RPM
