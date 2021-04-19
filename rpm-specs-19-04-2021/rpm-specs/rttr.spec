Name:           rttr
Version:        0.9.6
Release:        3%{?dist}
Summary:        Run Time Type Reflection

License:        MIT
URL:            https://www.rttr.org
Source0:        %{url}/releases/rttr-%{version}-src.tar.gz
# backport https://github.com/rttrorg/rttr/commit/adeadb7aafe12877f517340145e90de67ab64138
Patch0:         0001-Support-all-LP64-architectures-231.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  cmake3
BuildRequires:  make

BuildRequires:  catch-devel
BuildRequires:  rapidjson-devel


%description
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package -n librttr
Summary:        Run Time Type Reflection for C++
Provides:       bundled(nonius) = 1.1.2

%description -n librttr
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package  -n librttr-devel
Summary:        Header files for the C++ Run Time Type Reflection library
Requires:       librttr%{?_isa} = %{version}-%{release}

%description  -n librttr-devel
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-documentation documentations for %{name}.


%prep
%autosetup -p1
find . -type f -exec chmod -x {} ';'
sed -i 's/PERMISSIONS OWNER_READ//' CMake/*.cmake

# Unbundle
rm -rf 3rd_party/catch-1.12.0 3rd_party/rapidjson-1.1.0

# Fix catch2 include
%if ! 0%{?el7}
find src/unit_tests/ -name *.cpp -exec sed -i -e 's|catch/catch.hpp|catch2/catch.hpp|' {} ';'
%endif

# Disable compiler Werror on src/unit_tests/CMakeLists.txt
# See WIP https://github.com/rttrorg/rttr/pull/260
sed -i -e 's/^set_compiler_warnings/#set_compiler_warnings/' src/unit_tests/CMakeLists.txt


%build
%cmake3 \
  -DCMAKE_INSTALL_CMAKEDIR=cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DBUILD_EXAMPLES=OFF \
  -DBUILD_PACKAGE=OFF \
  -DUSE_PCH=OFF

%cmake3_build


%install
rm -rf __doc
%cmake3_install

# Rework doc
mkdir -p __doc
mv %{buildroot}%{_prefix}/doc/* __doc
find __doc -type f -exec chmod 0644 {} ';'
rm -rf %{buildroot}%{_datadir}/rttr/{LICENSE.txt,README.md}


%check
%ctest3 run_tests


%files -n librttr
%license LICENSE.txt
%doc README.md
%{_libdir}/librttr_core.so.%{version}

%files -n librttr-devel
%{_includedir}/rttr/
%{_libdir}/librttr_core.so
%{_datadir}/rttr/cmake/

%files doc
%doc __doc/*


%changelog
* Thu Feb 25 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-3
- Drop main package
- Split docs

* Wed Feb 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-2
- Backport patch for aarch64

* Mon Feb 08 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-1
- Initial spec file
