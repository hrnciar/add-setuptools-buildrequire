# Enable building and running the tests
# This is disabled by default, because ocaml-lwt requires this package to build.
%bcond_with test

Name:           ocaml-ctypes
Version:        0.18.0
Release:        2%{?dist}
Summary:        Combinators for binding to C libraries without writing any C

License:        MIT
URL:            https://github.com/ocamllabs/ocaml-ctypes
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-bigarray-compat-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-integers-devel >= 0.3.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  pkgconfig(libffi)

%if %{with test}
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  ocaml-bisect-ppx-devel
BuildRequires:  ocaml-lwt-devel >= 3.2.0
BuildRequires:  ocaml-ounit-devel
%endif

%description
Ctypes is a library for binding to C libraries using pure OCaml.  The
primary aim is to make writing C extensions as straightforward as
possible.

The core of ctypes is a set of combinators for describing the structure
of C types -- numeric types, arrays, pointers, structs, unions and
functions.  You can use these combinators to describe the types of the
functions that you want to call, then bind directly to those functions --
all without writing or generating any C!

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-bigarray-compat-devel%{?_isa}
Requires:       ocaml-integers-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains developer documentation for
%{name}.

%prep
%autosetup

# Use Fedora flags
sed -e 's|-fPIC -Wall -g|-fPIC %{build_cflags}|' \
    -e 's|-link -static-libgcc|%{build_ldflags}|' \
    -i Makefile.rules
sed -i 's|=-Wl,--no-as-needed|=%{build_ldflags}|' src/discover/determine_as_needed_flags.sh

# Flags for bigarray-compat are missing
sed -i 's/(OCAMLFIND_BISECT_FLAGS)/& -package bigarray-compat/' Makefile.rules
sed -i 's/^DOCFLAGS=/&-I $(shell ocamlfind query bigarray-compat) /' Makefile

# Don't try to update the system ld.conf
sed -i 's|-add ctypes|& -ldconf %{buildroot}%{_libdir}/ocaml/ld.conf|' Makefile

%build
# FIXME: Infrequent build failures with parallel build
# It looks like the configuration step isn't done before its results are needed
make all XEN=disable
%make_build doc XEN=disable

%install
export DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=$DESTDIR
mkdir -p $DESTDIR/stublibs
touch $DESTDIR/ld.conf
make install XEN=disable
rm $DESTDIR/ld.conf

# We install the documentation elsewhere
rm $DESTDIR/ctypes/*.md

# Install the opam files
mkdir -p $DESTDIR/ctypes-foreign
cp -p ctypes-foreign.opam $DESTDIR/ctypes-foreign/opam
cp -p ctypes.opam $DESTDIR/ctypes/opam

%if %{with test}
%check
make test
%endif

%files
%license LICENSE
%doc CHANGES.md README.md
%dir %{_libdir}/ocaml/ctypes/
%{_libdir}/ocaml/ctypes/META
%{_libdir}/ocaml/ctypes/*.cma
%{_libdir}/ocaml/ctypes/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/ctypes/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllctypes*_stubs.so
%{_libdir}/ocaml/stublibs/dllctypes*_stubs.so.owner

%files devel
%{_libdir}/ocaml/ctypes/opam
%{_libdir}/ocaml/ctypes-foreign/
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/ctypes/*.a
%{_libdir}/ocaml/ctypes/*.cmx
%{_libdir}/ocaml/ctypes/*.cmxa
%endif
%{_libdir}/ocaml/ctypes/*.cmt
%{_libdir}/ocaml/ctypes/*.cmti
%{_libdir}/ocaml/ctypes/*.h
%{_libdir}/ocaml/ctypes/*.mli

%files doc
%doc *.html *.css

%changelog
* Mon Mar  1 13:12:29 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.18.0-2
- OCaml 4.12.0 build

* Tue Feb 09 2021 Jerry James <loganjerry@gmail.com> - 0.18.0-1
- Initial package
