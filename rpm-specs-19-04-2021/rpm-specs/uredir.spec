Name:           uredir
Version:        3.3
Release:        1%{?dist}
Summary:        UDP port redirector

License:        ISC
URL:            https://github.com/troglobit/uredir
Source0:        https://github.com/troglobit/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libuev-devel
BuildRequires:  make

%description
uredir is a small Linux daemon to redirect UDP connections. 
It can be used to forward connections on small and embedded 
systems that do not have (or want to use) iptables or nftables.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%check
make check

%install
%make_install

# remove docs from buildroot
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%license LICENSE
%doc README.md AUTHORS design.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Apr 07 2021 Alessio <alessio@fedoraproject.org> - 3.3-1
- Initial RPM version
