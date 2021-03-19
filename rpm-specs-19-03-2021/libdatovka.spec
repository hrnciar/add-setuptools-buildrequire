Name: libdatovka
Version: 0.1.1
Release: 1%{?dist}
Summary: Client library for accessing SOAP services of ISDS (Czech Data Boxes)

License: LGPLv3+ and GPLv3+
URL: https://www.datovka.cz/
Source0: https://secure.nic.cz/files/datove_schranky/%{name}/%{name}-%{version}.tar.xz
BuildRequires: dos2unix
BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: coreutils
BuildRequires: docbook-style-xsl
BuildRequires: libxslt-devel
BuildRequires: gettext-devel
BuildRequires: libxml2-devel
BuildRequires: libcurl-devel
BuildRequires: gpgme-devel
BuildRequires: libgcrypt-devel
BuildRequires: expat-devel
BuildRequires: gnupg2-smime
BuildRequires: gnutls-devel

%description
Client library for accessing SOAP services of ISDS (Informační systém
datových schránek / Data Box Information System) as defined in Czech ISDS Act
(300/2008 Coll.) <http://portal.gov.cz/zakon/300/2008> and implied documents.

%package devel
Summary: Development files for libdatovka
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libxml2-devel%{?_isa}
Requires: pkgconfig%{?_isa}

%description devel
Development files for libdatovka.

%package doc
Summary:          Documentation files for libdatovka
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation files for libdatovka.

%prep
%autosetup -p1
dos2unix src/*.{c,h}

%build
autoreconf -fi
%configure \
  --enable-doc \
  --disable-online-test \
  --disable-static \
  --enable-test \
  --with-libcurl

%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name}

%check
make check %{?_smp_mflags}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*

%files doc
%doc client

%changelog
* Tue Feb  2 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-1
- New version

* Mon Feb  1 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.0-2
- Fixed according to the review
  Related: rhbz#1920514

* Thu Jan 28 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.0-1
- Initial release
  Related: rhbz#1920514
