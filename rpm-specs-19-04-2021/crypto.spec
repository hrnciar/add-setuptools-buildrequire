%global forgeurl https://github.com/SDL-Hercules-390/crypto
%global commit 837705eff938ca044f2eab5f1ea5cd83b2b0ece7
%forgemeta

# Needed for f32 and epel8
%undefine __cmake_in_source_build
%global _vpath_srcdir %{_builddir}/%{name}-%{version}/%{name}-%{commit}
%global _vpath_builddir %{_builddir}/%{name}-%{version}/%{name}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
Crypto provides a simple implementation of the Rijndael (now AES) and DES
encryption algorithms as well as the SHA1 and SHA2 hashing algorithms. The
library is almost a verbatim copy of the code from OpenBSD and PuTTY.}

Name:           crypto
Version:        1.0.0
Release:        2%{?dist}
Summary:        Simple AES/DES encryption and SHA1/SHA2 hashing library

License:        Public Domain and MIT and BSD
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
%{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# both packages install /usr/include/sha2.h
Conflicts:      sha2-devel

%description    devel
%{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c
tar xzf %{SOURCE0}
pushd %{name}-%{commit}
mv README.md ..
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-devel:g'

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-devel/crypto.LICENSE.txt .

%files devel
%license crypto.LICENSE.txt
%doc README.md
%doc %{_docdir}/%{name}-devel/crypto.README.txt
%{_includedir}/*.h
%{_libdir}/lib%{name}*.a

%changelog
* Tue Mar 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-2.20210321git837705e
- Fix build on f32 and epel8

* Sun Mar 28 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-1.20210321git837705e
- Initial package
