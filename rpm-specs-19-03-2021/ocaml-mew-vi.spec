%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Documentation adds a circular dependency, so by
# default we build without.
%bcond_with doc

%global srcname mew-vi
%global upname  mew_vi

Name:           ocaml-%{srcname}
Version:        0.5.0
Release:        8%{?dist}
Summary:        Modal Editing Witch, VI interpreter

License:        MIT
URL:            https://github.com/kandu/mew_vi
Source0:        %{url}/archive/%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 1.1.0
BuildRequires:  ocaml-mew-devel >= 0.1.0
%if %{with doc}
BuildRequires:  ocaml-odoc
%endif
BuildRequires:  ocaml-react-devel

%description
This is a vi-like modal editing engine generator.  Provide `Key`, `Mode`,
and `Concurrent` modules to define the real world environment to get a
handy vi-like modal editing engine.  Feed the the `i` channel user input
and get the vi actions from the `action_output` channel.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-mew-devel%{?_isa}
Requires:       ocaml-react-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%if %{with doc}
%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    docs
Documentation for %{name}.
%endif

%prep
%autosetup -n %{upname}-%{version}

%build
dune build %{?_smp_mflags}
%if %{with doc}
dune build %{?_smp_mflags} @doc
%endif

%install
dune install --destdir=%{buildroot}

%if %{with doc}
# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete
%endif

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod a+x {} \+
%endif

# The tests cannot be run, since Fedora does not yet have ppx_expect.
#
#%%check
#dune runtest

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{upname}/
%{_libdir}/ocaml/%{upname}/%{upname}.cma
%{_libdir}/ocaml/%{upname}/%{upname}*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.a
%{_libdir}/ocaml/%{upname}/%{upname}*.cmx
%{_libdir}/ocaml/%{upname}/%{upname}.cmxa
%endif
%{_libdir}/ocaml/%{upname}/%{upname}*.cmt

%if %{with doc}
%files docs
%doc _build/default/_doc/*
%license LICENSE
%endif

%changelog
* Mon Mar  1 16:58:00 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-8
- OCaml 4.12.0 build
- Make -docs subpackage conditional.

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-7
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.1.0-1
- Initial RPM
