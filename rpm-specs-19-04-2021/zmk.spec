Name:           zmk
Version:        0.5
Release:        1%{?dist}
Summary:        Collection of reusable Makefiles

License:        LGPLv3
URL:            https://github.com/zyga/zmk
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        https://gpg.zygoon.pl/gpgkey-B76CED9B45CAF1557D271A6A2894E93A28C67B47.gpg

BuildArch:      noarch
BuildRequires:  make, gnupg2
Requires:       make, gawk

%description
Collection of make-files implementing a system similar to auto-tools, but
without the generated files that make understanding system behavior harder.

Highlights include:

 - Describe programs, test programs, static libraries, shared libraries,
   development headers, manual pages and more
 - Use familiar targets like "all", "check", "install" and "clean"
 - Works out of the box on popular distributions of Linux and MacOS
 - Friendly to distribution packaging expecting auto-tools
 - Compile with gcc, clang, tcc or the open-watcom compilers
 - Cross compile with gcc and open-watcom
 - Efficient and incremental, including the install target


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
%configure
%make_build


%check
make check


%install
%make_install


%files
%{_includedir}/zmk/
%{_includedir}/z.mk
%{_mandir}/man5/zmk.*.5.*
%{_mandir}/man5/z.mk.5.*
%license LICENSE
%doc NEWS

%changelog
* Wed Feb 03 2021 Zygmunt Krynicki <me@zygoon.pl> - 0.5-1
- New upstream release
- Simplify prep and build steps
* Sun Jan 31 2021 Zygmunt Krynicki <me@zygoon.pl> - 0.4.2-1
- Initial version of the package
