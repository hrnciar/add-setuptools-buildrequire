%global forgeurl https://github.com/SDL-Hercules-390/telnet
%global commit 2aca101e06ca84526c1a63c0f65e05fe11522c3b
%forgemeta

# Needed for f32 and epel8
%undefine __cmake_in_source_build
%global _vpath_srcdir %{_builddir}/%{name}-%{version}/telnet-%{commit}
%global _vpath_builddir %{_builddir}/%{name}-%{version}/telnet%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
libtelnet is a library for handling the TELNET protocol. It includes routines
for parsing incoming data from a remote peer as well as formatting data to be
sent to the remote peer.

libtelnet uses a callback-oriented API, allowing application-specific handling
of various events. The callback system is also used for buffering outgoing
protocol data, allowing the application to maintain control of the actual
socket connection.

Features supported include the full TELNET protocol, Q-method option
negotiation, and NEW-ENVIRON.}

Name:           sdl-telnet
Version:        1.0.0
Release:        2%{?dist}
Summary:        Simple RFC-compliant TELNET implementation

License:        Public Domain
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

%description    devel
%{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c
tar xzf %{SOURCE0}
pushd telnet-%{commit}
mv README.md ..
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-devel:g'

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-devel/telnet.LICENSE.txt .

%files devel
%license telnet.LICENSE.txt
%doc README.md
%doc %{_docdir}/%{name}-devel/telnet.README.txt
%{_includedir}/*.h
%{_libdir}/libtelnet*.a

%changelog
* Tue Mar 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-2.20210321git2aca101
- Fix build on f32 and epel8

* Sun Mar 28 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-1.20210321git2aca101
- Initial package
