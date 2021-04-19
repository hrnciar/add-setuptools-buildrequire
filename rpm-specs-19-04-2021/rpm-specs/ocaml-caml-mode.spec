# Upstream has not tagged any releases
%global srcname caml-mode
%global commit  38ebde12d3d529e6ef8078967997d32226e69e82
%global date    20190413
%global forgeurl https://github.com/ocaml/caml-mode

# This package installs into an arch-specific directory, but contains no
# ELF files.
%global debug_package %{nil}

Name:           ocaml-%{srcname}
Version:        4.06
Release:        1%{?dist}
Summary:        Opam file for caml-mode

%forgemeta

License:        GPLv2+
URL:            %{forgeurl}
Source0:        %{forgesource}
# Update the Emacs interface for Emacs 27.1
Patch0:         %{name}-emacs.patch

BuildRequires:  emacs
BuildRequires:  make

Requires:       emacs-%{srcname} = %{version}-%{release}
Requires:       ocaml(runtime)

%description
This package contains the opam file for emacs-%{srcname}.  Install
this only if you want opam to know that caml-mode is available.
If you just want to use caml-mode, install emacs-%{srcname}.

%package     -n emacs-%{srcname}
Summary:        Emacs mode for editing OCaml source code
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description -n emacs-%{srcname}
This package provides a caml-mode for Emacs, for editing OCaml programs,
as well as an inferior-caml-mode, to run a toplevel.  Caml-mode supports
indentation, compilation and error retrieving, and sending phrases to
the toplevel.  There is also support for hilit, font-lock and imenu.

%prep
%forgesetup
%autopatch -p1

%build
%make_build ocamltags

%install
# Install ocamltags
mkdir -p %{buildroot}%{_bindir}
cp -p ocamltags %{buildroot}%{_bindir}

# Install the opam file
mkdir -p %{buildroot}%{_libdir}/ocaml/%{srcname}
cp -p caml-mode.opam %{buildroot}%{_libdir}/ocaml/%{srcname}/opam

# Install and byte compile the Emacs files
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{srcname}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -m 644 *.el %{buildroot}/%{_emacs_sitelispdir}/%{srcname}
cd %{buildroot}/%{_emacs_sitelispdir}/%{srcname}
mv caml-mode-site-file.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile *.el
cd -

%files
%{_libdir}/ocaml/%{srcname}/

%files -n emacs-%{srcname}
%doc CHANGES.md README.itz README.md
%license COPYING
%{_bindir}/ocamltags
%{_emacs_sitelispdir}/%{srcname}/
%{_emacs_sitestartdir}/caml-mode-site-file.el

%changelog
* Tue Mar  9 2021 Jerry James <loganjerry@gmail.com> - 4.06-1
- Initial RPM
