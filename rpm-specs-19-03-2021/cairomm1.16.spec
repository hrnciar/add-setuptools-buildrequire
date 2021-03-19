%global so_version 1
%global apiver 1.16

# “Let mm-common-get copy some files to untracked/”, i.e., replace scripts from
# the tarball with those from mm-common. This is (potentially) required if
# building an autotools-generated tarball with meson, or vice versa.
%bcond_without maintainer_mode

Name:           cairomm%{apiver}
Summary:        C++ API for the cairo graphics library
Version:        1.16.0
Release:        3%{?dist}

URL:            https://www.cairographics.org
License:        LGPLv2+

%global src_base https://www.cairographics.org/releases
Source0:        %{src_base}/cairomm-%{version}.tar.xz
# No keyring with authorized GPG signing keys is published
# (https://gitlab.freedesktop.org/freedesktop/freedesktop/-/issues/331), but we
# are able to verify the signature using the key for Kjell Ahlstedt from
# https://gitlab.freedesktop.org/freedesktop/freedesktop/-/issues/290.
Source1:        %{src_base}/cairomm-%{version}.tar.xz.asc
Source2:        https://gitlab.freedesktop.org/freedesktop/freedesktop/uploads/0ac64e9582659f70a719d59fb02cd037/gpg_key.pub

BuildRequires:  gnupg2

BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(sigc++-3.0)
BuildRequires:  pkgconfig(fontconfig)

# Everything mentioned in data/cairomm*.pc.in, except the Quartz and Win32
# libraries that do not apply to this platform:
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(cairo-xlib-xrender)

%if %{with maintainer_mode}
# mm-common-get
BuildRequires:  mm-common
%endif

BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  doxygen
# dot
BuildRequires:  graphviz
# xsltproc
BuildRequires:  libxslt
BuildRequires:  pkgconfig(mm-common-libstdc++)

# For tests:
BuildRequires:  boost-devel

%description
This library provides a C++ interface to cairo.

The API/ABI version series is %{apiver}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

The API/ABI version series is %{apiver}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       libstdc++-docs
Requires:       libsigc++20-doc

%description    doc
Documentation for %{name} can be viewed either through the devhelp
documentation browser or through a web browser at
%{_datadir}/doc/%{name}-%{apiver}/.

The API/ABI version series is %{apiver}.


%prep
# Import developer’s public GPG key to a keyring that we can use for signature
# verification.
workdir="$(mktemp --directory)"
gpg2 --homedir="${workdir}" --yes --import '%{SOURCE2}'
gpg2 --homedir="${workdir}" --export --export-options export-minimal \
    > %{name}.gpg
rm -rf "${workdir}"

%{gpgverify} \
    --keyring='%{name}.gpg' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n cairomm-%{version}
# We must remove the jQuery/jQueryUI bundle with precompiled/minified/bundled
# JavaScript that is in untracked/docs/reference/html/jquery.js, since such
# sources are banned in Fedora. (Note also that the bundled JavaScript had a
# different license.) We also remove the tag file, which triggers a rebuild of
# the documentation. While we are at it, we might as well rebuild the devhelp
# XML too.
rm -rf untracked/docs/reference/html
rm untracked/docs/reference/cairomm-%{apiver}.tag \
   untracked/docs/reference/cairomm-%{apiver}.devhelp2


%build
%meson \
  -Dmaintainer-mode=%{?with_maintainer_mode:true}%{?!with_maintainer_mode:false} \
  -Dbuild-documentation=true \
  -Dbuild-examples=false \
  -Dbuild-tests=true \
  -Dboost-shared=true \
  -Dwarnings=max
%meson_build


%install
%meson_install
find %{buildroot} -type f -name '*.la' -print -delete

install -t %{buildroot}%{_datadir}/doc/cairomm-%{apiver} -m 0644 -p \
    AUTHORS ChangeLog MAINTAINERS NEWS README
cp -rp examples %{buildroot}%{_datadir}/doc/cairomm-%{apiver}/


%check
%meson_test


%files
%license COPYING
%{_libdir}/libcairomm-%{apiver}.so.%{so_version}
%{_libdir}/libcairomm-%{apiver}.so.%{so_version}.*


%files devel
%{_includedir}/cairomm-%{apiver}
%{_libdir}/libcairomm-%{apiver}.so
%{_libdir}/pkgconfig/cairomm-%{apiver}.pc
%{_libdir}/pkgconfig/cairomm-*-%{apiver}.pc
%{_libdir}/cairomm-%{apiver}


%files doc
%license COPYING
%doc %{_datadir}/doc/cairomm-%{apiver}/
%doc %{_datadir}/devhelp/


%changelog
* Sat Feb 20 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.16.0-3
- Verify source with new strong signatures from upstream

* Wed Feb 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.16.0-2
- Working (but weak, dependent on SHA1) source signature verification
- Tidy up BR’s, including dropping make

* Wed Feb 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.16.0-1
- New multi-version cairomm1.16 package to provide the version 1.16 API/ABI;
  based on the spec file from cairomm-1.14.2-5
