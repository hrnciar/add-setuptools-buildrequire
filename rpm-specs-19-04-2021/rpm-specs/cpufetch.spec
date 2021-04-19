Name: cpufetch
Summary: Simple tool for determining CPU architecture
License: MIT

Version: 0.94
Release: 2%{?dist}

URL: https://github.com/Dr-Noob/cpufetch
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

# Supports only x86_64 and ARM
ExclusiveArch: %{arm} aarch64 x86_64


%description
%{name} is a simple, yet fancy, CPU architecture fetching tool.
It currently supports x86_64 CPUs (both Intel and AMD) and ARM.


%prep
%setup -q

# Don't override distro CXXFLAGS
sed -e 's|CXXFLAGS=-Wall|CXXFLAGS+=-Wall|g' -i Makefile


%build
%set_build_flags
%make_build


%install
# The upstream Makefile has an "install" target,
# but it does not support DESTDIR nor PREFIX.
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -p %{name} %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_mandir}/man8
install -m 644 -p %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Mon Apr 05 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.94-2
- Preserve timestamps when installing

* Sat Apr 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.94-1
- Initial packaging
