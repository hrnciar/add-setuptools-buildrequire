Name:           xbar
Version:        0.0.1
Release:        1%{?dist}
Summary:        Tiny XCB information bar

License:        MIT
URL:            https://github.com/mcpcpc/xbar
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel

%description
xbar is a tiny XCB status bar. An incredibly lightweight information bar,
designed to print important real-time system metrics. Beyond foreground and
background colors, xbar offers limited customization for a distraction-free
user experience.

%prep
%autosetup

%build
%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README CHANGELOG
%{_bindir}/xbar

%changelog
* Sun Jan 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.0.1-1
- Initial package
