%global pre Final

Name:		postgres-decoderbufs
Version:	1.4.0
Release:	1%{?pre:.%pre}%{?dist}
Summary:	PostgreSQL Protocol Buffers logical decoder plugin

License:	MIT
URL:		https://github.com/debezium/postgres-decoderbufs

%global full_version %{version}.%{?pre:%pre}%{?!pre:Final}

Source0:	https://github.com/debezium/%{name}/archive/v%{full_version}.tar.gz

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	postgresql-devel >= 9.6, postgresql-server-devel >= 9.6
BuildRequires:	protobuf-c-devel
BuildRequires:  llvm, clang

Requires:	protobuf-c
%{?postgresql_module_requires}

%description
A PostgreSQL logical decoder output plugin to deliver data as Protocol Buffers messages.


%package llvmjit
Summary:	Just-in-time compilation support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description llvmjit
Just-in-time compilation support for %{name}.


%prep
%setup -qn postgres-decoderbufs-%{full_version}


%build
%make_build


%install
%make_install


%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/decoderbufs.so
%{_datadir}/pgsql/extension/decoderbufs.control

%files llvmjit
%{_libdir}/pgsql/bitcode/decoderbufs.index.bc
%{_libdir}/pgsql/bitcode/decoderbufs/


%changelog
* Wed Feb  3 2021 Honza Horak <hhorak@redhat.com> - 1.4.0-1.Final
- Update to new release 1.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.6.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 16:42:08 CET 2021 Adrian Reber <adrian@lisas.de> - 1.1.0-0.5.Final
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.1.0-0.4.Final
- Rebuilt for protobuf 3.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.3.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.1.0-0.2.Final
- Rebuilt for protobuf 3.12

* Mon Mar 30 2020 Jiri Pechanec <jpechane@redhat.com> - 1.1.0-0.1.Final
- Update to 1.1.0.Final

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-0.1.Beta3
- Update to 1.0.0-Beta3
- Drop BR: postgis-devel

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 9 2019 - Jiri Pechanec <jpechane@redhat.com> 0.10.0-1
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Tue May 14 2019 - Jiri Pechanec <jpechane@redhat.com> 0.9.5-1
- Initial RPM packaging
