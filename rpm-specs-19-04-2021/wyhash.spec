Name:           wyhash
Summary:        No hash function is perfect, but some are useful
%global forgeurl https://github.com/wangyi-fudan/%{name}
%global tag %{name}_final
%forgemeta
# Upstream has haphazard versioning: after going through “v1”-“v6”, they
# selected a version “final1”, and are now working on “final2”. They also keep
# all old versions in the git repository. We will package only based on the
# “final” version numbers. When “final2” is released, this package will move
# forward to that version, with “final1” offered in a parallel-installable
# compat package,
Version:        final1
# Note that the forgemeta macro prepends commit information to the dist macro.
Release:        1%{?dist}

URL:            %{forgeurl}
Source0:        %{forgesource}
License:        Unlicense

BuildRequires:  gcc-c++
BuildRequires:  make

# We need the delimiter in the “compat” version because the name ends, and the
# version starts, with a letter. See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/#multiple.
%global compat_name %{name}_%{version}

# No compiled code is installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
No hash function is perfect, but some are useful.

wyhash and wyrand are the ideal 64-bit hash function and PRNG respectively:

solid: wyhash passed SMHasher, wyrand passed BigCrush, practrand.

portable: 64-bit/32-bit system, big/little endian.

fastest: Efficient on 64-bit machines, especially for short keys.

simplest: In the sense of code size.}

%description %{common_description}


%package devel
Summary:        %{summary}

# Since this is a header-only library, dependent packages must require one of
# the -static virtual Provides.
Provides:       %{name}-static = %{version}-%{release}

Provides:       %{compat_name}-devel = %{version}-%{release}
Provides:       %{compat_name}-devel%{?_isa} = %{version}-%{release}
Provides:       %{compat_name}-static = %{version}-%{release}

%description devel %{common_description}

Dependent packages that require version %{version} in particular should use the
virtual Provides for %{compat_name}-devel/%{compat_name}-static, and should add
-I%{_includedir}/%{compat_name} to their compiler flags.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc %{common_description}


%prep
%forgeautosetup

# Build the tests with the distribution’s preferred flags
sed -r -i \
    -e 's/ -O3\b//g' \
    -e 's/ -march=native\b/ \$\(CXXFLAGS\) \$\(LDFLAGS\)/g' \
    makefile


%build
%set_build_flags
# We build only the test executable, not the benchmarks.
%make_build test_vector CXX="${CXX-g++}"


%install
# We install only the main wyhash header; others, like wyhash32 and o1hash, are
# not yet properly versioned. We put it in a subdirectory of _includedir for
# parallel-installability; dependent packages requiring particular versions
# will have to adjust their CFLAGS.
install -D -p -m 0644 -t %{buildroot}%{_includedir}/%{compat_name} %{name}.h

# For this package, which tracks the latest version, we also allow the header
# to be used without adding the subdirectory to the CFLAGS.
ln -s %{compat_name}/%{name}.h %{buildroot}%{_includedir}/%{name}.h


%check
./test_vector


%files devel
%license LICENSE

%{_includedir}/%{compat_name}
%{_includedir}/%{name}.h


%files doc
%license LICENSE
%doc README.md
# An academic paper on the algorithm:
%doc *.docx


%changelog
* Sat Mar 06 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.20210306gitfinal
- Initial package
