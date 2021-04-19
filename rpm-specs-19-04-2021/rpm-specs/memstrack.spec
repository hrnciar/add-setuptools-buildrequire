# vim: syntax=spec
%global gitcommit 183143b73eb7c5b253ecc5b4a84aefaa96f8a682
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global snapshotdate 20210208

Name:           memstrack
Version:        0.2.2
Release:        1%{?dist}
Summary:        A memory allocation tracer, like a hot spot analyzer for memory allocation
License:        GPLv3
URL:            https://github.com/ryncsn/memstrack
VCS:            git+git@github.com:ryncsn/memstrack.git
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

Source:         https://github.com/ryncsn/memstrack/archive/%{gitcommit}/memstrack-%{gitshortcommit}.tar.gz

%description
A memory allocation tracer, like a hot spot analyzer for memory allocation

%prep
%setup -q -n memstrack-%{gitcommit}

%build
%{set_build_flags}
%{make_build}

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 memstrack %{buildroot}/%{_bindir}

%files
%doc README.md
%license LICENSE
%{_bindir}/memstrack

%changelog
* Mon Feb 08 2021 Kairui Song <kasong@redhat.com> - 0.2.2-1
- Update to upstream latest release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Timm Bäder <tbaeder@redhat.com> - 0.1.12-2
- Use %%make_build macro
  https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make

* Sun Aug 30 2020 Kairui Song <kasong@redhat.com> - 0.1.12-1
- Update to upstream latest release

* Thu Jul 30 2020 Kairui Song <kasong@redhat.com> - 0.1.9-1
- Update to upstream latest release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Kairui Song <kasong@redhat.com> - 0.1.8-1
- Update to upstream latest release

* Sat May 30 2020 Kairui Song <ryncsn@gmail.com> - 0.1.5-1
- Update to upstream latest release

* Tue Apr 21 2020 Kairui Song <ryncsn@gmail.com> - 0.1.2-1
- Update to upstream latest release

* Sun Mar 15 2020 Kairui Song <ryncsn@gmail.com> - 0-1.20200310gitee02de2
- First release
