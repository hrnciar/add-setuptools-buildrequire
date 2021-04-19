Name:           xbg
Version:        0.0.2
Release:        1%{?dist}
Summary:        Tiny XCB root window color setter

License:        MIT
URL:            https://github.com/mcpcpc/xbg
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel

%description
xbg is a tiny XCB root window color setter. It changes the root window
background to a specified X11 color name.

%prep
%autosetup

%build
%make_build \
  CC="%{__cc}" \
  CFLAGS="%{optflags}" \
  ALL_LDFLAGS="-lxcb -lxcb-util %{build_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README CHANGELOG
%{_bindir}/xbg

%changelog
* Sun Jan 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.0.2-1
- Initial package
