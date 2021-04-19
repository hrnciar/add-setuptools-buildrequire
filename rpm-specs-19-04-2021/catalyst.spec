%global commit 2fc94c55ba4eb994f27728141ebcf15c3435f306
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           catalyst
Version:        2.0
Release:        0.2.20201218git%{shortcommit}%{?dist}
Summary:        API specification for simulations to analyze and visualize data in situ

# Conduit is also licensed under the BSD 3-Clause license,
License:        BSD
URL:            https://gitlab.kitware.com/paraview/catalyst
Source0:        https://gitlab.kitware.com/paraview/catalyst/-/archive/%{commit}/catalyst-%{commit}.tar.gz
# Unbundling
Patch0:         catalyst-unbundle.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libb64-devel
BuildRequires:  libyaml-devel
BuildRequires:  rapidjson-devel

# TODO - unbundle
Provides: bundled(conduit)

%description
Catalyst is an API specification developed for simulations (and other
scientific data producers) to analyze and visualize data in situ.

Catalyst has been split out of ParaView. This package includes the definition
together with a lightweight implementation of this Catalyst API.

For details how to use Catalyst for in situ analysis and visualization in
simulations, see https://catalyst-in-situ.readthedocs.io/en/latest/index.html.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit}
rm -r thirdparty/conduit/{libb64,libyaml,rapidjson}


%build
%cmake 
%cmake_build


%install
%cmake_install


%files
%license License.txt 3rdPartyLicenses.txt
%{_libdir}/lib%{name}.so.2*

%files devel
%{_includedir}/%{name}-2.0/
%{_libdir}/cmake/
%{_libdir}/lib%{name}.so
%{_libdir}/lib*.a


%changelog
* Sat Feb 20 2021 Orion Poplawski <orion@nwra.com> - 2.0-0.2.20201218git2fc94c5
- Add %%license, tweak description

* Mon Feb 1 2021 Orion Poplawski <orion@nwra.com> - 2.0-0.1.20201218git2fc94c5
- Initial package
